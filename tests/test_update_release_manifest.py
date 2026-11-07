import unittest
import json
import tempfile
from pathlib import Path

# The module under test
from scripts.update_release_manifest import (
    normalize_project,
    build_manifest,
    write_manifest_atomic,
    sanitize_release_notes,
    extract_checksum
)


class TestUpdateReleaseManifest(unittest.TestCase):
    def setUp(self):
        self.fixtures_dir = Path(__file__).parent / "fixtures" / "releases"
        with open(Path(__file__).parent.parent / "_data" / "download_products.json", "r", encoding="utf-8") as f:
            self.products = json.load(f)
        self.eep_product = next(p for p in self.products if p["id"] == "eep")
        self.alp_product = next(p for p in self.products if p["id"] == "alp")
        self.ssp_product = next(p for p in self.products if p["id"] == "ssp")
        self.ytf_product = next(p for p in self.products if p["id"] == "ytf")

    def test_draft_exclusion(self):
        with open(self.fixtures_dir / "prerelease_and_draft.json", "r", encoding="utf-8") as f:
            releases = json.load(f)
        normalized = normalize_project(self.eep_product, releases)
        self.assertEqual(normalized["status"], "available")
        self.assertIsNotNone(normalized["latest"])
        self.assertEqual(normalized["latest"]["tag_name"], "v0.1.1-alpha.1")
        # Ensure draft v0.2.0-draft is NOT in history
        history_tags = [h["tag_name"] for h in normalized["history"]]
        self.assertNotIn("v0.2.0-draft", history_tags)

    def test_stable_selection_over_prerelease(self):
        with open(self.fixtures_dir / "stable_with_assets.json", "r", encoding="utf-8") as f:
            releases = json.load(f)
        normalized = normalize_project(self.ytf_product, releases)
        self.assertEqual(normalized["status"], "available")
        self.assertEqual(normalized["latest"]["tag_name"], "v1.0.0")
        self.assertFalse(normalized["latest"]["prerelease"])

    def test_prerelease_selection_when_allowed(self):
        with open(self.fixtures_dir / "prerelease_and_draft.json", "r", encoding="utf-8") as f:
            releases = json.load(f)
        # EEP allows prereleases
        normalized = normalize_project(self.eep_product, releases)
        self.assertTrue(normalized["latest"]["prerelease"])
        self.assertEqual(normalized["latest"]["tag_name"], "v0.1.1-alpha.1")

    def test_prerelease_ignored_when_not_allowed(self):
        with open(self.fixtures_dir / "prerelease_and_draft.json", "r", encoding="utf-8") as f:
            releases = json.load(f)
        # SSP does NOT allow prerelease
        normalized = normalize_project(self.ssp_product, releases)
        self.assertIsNone(normalized["latest"])
        self.assertEqual(normalized["status"], "planning")

    def test_empty_releases(self):
        with open(self.fixtures_dir / "empty_releases.json", "r", encoding="utf-8") as f:
            releases = json.load(f)
        normalized = normalize_project(self.ssp_product, releases)
        self.assertEqual(normalized["status"], "planning")
        self.assertIsNone(normalized["latest"])
        self.assertEqual(len(normalized["history"]), 0)

    def test_asset_pattern_matching(self):
        with open(self.fixtures_dir / "prerelease_and_draft.json", "r", encoding="utf-8") as f:
            releases = json.load(f)
        normalized = normalize_project(self.eep_product, releases)
        assets = normalized["latest"]["assets"]
        # Should have flatpak, deb, and rpm
        asset_ids = [a["rule_id"] for a in assets]
        self.assertIn("flatpak", asset_ids)
        self.assertIn("deb", asset_ids)
        self.assertIn("rpm", asset_ids)
        # Verify sizes are integers > 0
        for a in assets:
            self.assertGreater(a["size"], 0)
            self.assertTrue(a["browser_download_url"].startswith("https://"))

    def test_checksum_extraction(self):
        asset = {
            "name": "Your-UI-v1.0.0.apk",
            "digest": "sha256:c4c67e3683ed5efcc4b91e65ad2df33371fff9113cc7ade75f31f1c834d504ab"
        }
        digest = extract_checksum(asset, [])
        self.assertEqual(digest, "c4c67e3683ed5efcc4b91e65ad2df33371fff9113cc7ade75f31f1c834d504ab")

    def test_sanitize_release_notes(self):
        raw_markdown = "<script>alert('xss')</script>## Title\n* Feature 1\n* Feature 2\n<div class='danger'>Text</div>"
        cleaned = sanitize_release_notes(raw_markdown)
        self.assertNotIn("<script>", cleaned)
        self.assertNotIn("<div>", cleaned)
        self.assertNotIn("<div", cleaned)
        self.assertIn("Feature 1", cleaned)

    def test_atomic_write_preserves_sentinel_on_failure(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            manifest_file = Path(tmpdir) / "release_manifest.json"
            sentinel_data = {"sentinel": "must_not_be_overwritten"}
            with open(manifest_file, "w", encoding="utf-8") as f:
                json.dump(sentinel_data, f)

            def failing_fetcher(repo, per_page=10):
                raise RuntimeError("GitHub API 503 Service Unavailable")

            with self.assertRaises(RuntimeError):
                build_manifest(self.products, fetcher=failing_fetcher)

            # Check that manifest_file remains unchanged
            with open(manifest_file, "r", encoding="utf-8") as f:
                content = json.load(f)
            self.assertEqual(content, sentinel_data)

    def test_atomic_write_success(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            manifest_file = Path(tmpdir) / "release_manifest.json"
            test_manifest = {"generated_at": "2026-11-07T00:00:00Z", "projects": []}
            write_manifest_atomic(manifest_file, test_manifest)
            self.assertTrue(manifest_file.exists())
            with open(manifest_file, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            self.assertEqual(loaded, test_manifest)


if __name__ == "__main__":
    unittest.main()
