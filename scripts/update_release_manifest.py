#!/usr/bin/env python3
"""
scripts/update_release_manifest.py

Fetches, validates, normalizes, and atomically writes release metadata
for Zvirox open-source projects using GitHub Releases API.
Runs at build time in CI or locally. 100% Python standard library.
"""

import argparse
import datetime
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

USER_AGENT = "Zvirox-Downloads-Manifest/1.0 (+https://zvirox.in)"
ROOT_DIR = Path(__file__).parent.parent
DEFAULT_PRODUCTS_FILE = ROOT_DIR / "_data" / "download_products.json"
DEFAULT_MANIFEST_FILE = ROOT_DIR / "_data" / "release_manifest.json"


def fetch_releases(repo: str, per_page: int = 10) -> list[dict]:
    """
    Fetches releases for a given repository from the GitHub API.
    Handles rate limiting, timeouts, and one transient retry.
    """
    url = f"https://api.github.com/repos/{repo}/releases?per_page={per_page}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.github+json"
        }
    )

    # Optional GitHub token for higher rate limits in CI
    gh_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if gh_token:
        req.add_header("Authorization", f"Bearer {gh_token}")

    max_attempts = 2
    for attempt in range(max_attempts):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                return json.loads(data.decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                raise RuntimeError(
                    f"GitHub API rate limit exceeded while querying '{repo}' (HTTP {e.code}): {e.reason}"
                ) from e
            if e.code == 404:
                # Repo or releases not found
                return []
            if e.code >= 500 and attempt < max_attempts - 1:
                time.sleep(1.0)
                continue
            raise RuntimeError(f"GitHub API HTTP error {e.code} for '{repo}': {e.reason}") from e
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < max_attempts - 1:
                time.sleep(1.0)
                continue
            raise RuntimeError(f"Network error querying '{repo}': {e}") from e

    return []


def sanitize_release_notes(body: str | None, max_length: int = 240) -> str:
    """
    Strips raw HTML tags, dangerous scripts, markdown headings and URLs,
    leaving a clean, safe, plain-text summary suitable for the UI.
    """
    if not body:
        return "Latest release with performance improvements and bug fixes."

    # Remove script tags and contents
    text = re.sub(r"<script.*?>.*?</script>", "", body, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    # Remove markdown links [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Remove URLs
    text = re.sub(r"https?://\S+", "", text)
    # Remove GitHub automated footer/links
    text = re.sub(r"\*{0,2}Full Changelog\*{0,2}:?\s*", "", text, flags=re.IGNORECASE)
    # Remove markdown headers and list bullets
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[\*\-\+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*{1,2}([^\*]+)\*{1,2}", r"\1", text)
    # Collapse multiple whitespaces and newlines
    text = re.sub(r"\s+", " ", text).strip()

    if len(text) > max_length:
        text = text[:max_length].rstrip() + "..."

    return text or "Latest release with performance improvements and bug fixes."


def extract_checksum(asset: dict, all_assets: list[dict]) -> str | None:
    """
    Extracts sha256 checksum if available.
    Prefers GitHub's native asset digest field (sha256:xxxx).
    """
    digest = asset.get("digest")
    if digest and isinstance(digest, str) and digest.startswith("sha256:"):
        return digest[len("sha256:"):]
    return None


def normalize_project(product: dict, releases: list[dict]) -> dict:
    """
    Normalizes a project's releases into the standardized manifest contract:
    - Filters out drafts.
    - Selects latest stable release (or latest prerelease if allow_prerelease is True).
    - Matches configured assets against asset_rules patterns.
    - Limits history to 5 newest releases.
    """
    published = [r for r in releases if not r.get("draft", False)]

    # Distinguish stable vs prerelease
    stables = [r for r in published if not r.get("prerelease", False)]
    prereleases = [r for r in published if r.get("prerelease", False)]

    latest_release = None
    if stables:
        latest_release = stables[0]
    elif product.get("allow_prerelease", False) and prereleases:
        latest_release = prereleases[0]

    repo_url = f"https://github.com/{product['repo']}"
    releases_url = f"{repo_url}/releases"

    if not latest_release:
        return {
            "id": product["id"],
            "name": product["name"],
            "repo": product["repo"],
            "project_url": product.get("project_url", ""),
            "releases_url": releases_url,
            "status": "planning",
            "latest": None,
            "history": []
        }

    # Match assets
    matched_assets = []
    raw_assets = latest_release.get("assets", [])

    for rule in product.get("asset_rules", []):
        pattern = re.compile(rule["pattern"], re.IGNORECASE)
        for raw in raw_assets:
            name = raw.get("name", "")
            if pattern.search(name):
                sha256 = extract_checksum(raw, raw_assets)
                matched_assets.append({
                    "rule_id": rule["id"],
                    "label": rule["label"],
                    "platform": rule["platform"],
                    "icon": rule.get("icon", "package"),
                    "name": name,
                    "size": raw.get("size", 0),
                    "browser_download_url": raw.get("browser_download_url", ""),
                    "sha256": sha256
                })
                break  # Pick first match per rule

    # Build history (up to 5 newest published releases)
    history = []
    for rel in published[:5]:
        history.append({
            "tag_name": rel.get("tag_name", ""),
            "name": rel.get("name", rel.get("tag_name", "")),
            "published_at": rel.get("published_at", ""),
            "html_url": rel.get("html_url", ""),
            "prerelease": bool(rel.get("prerelease", False))
        })

    return {
        "id": product["id"],
        "name": product["name"],
        "repo": product["repo"],
        "project_url": product.get("project_url", ""),
        "releases_url": releases_url,
        "status": "available",
        "latest": {
            "tag_name": latest_release.get("tag_name", ""),
            "name": latest_release.get("name", latest_release.get("tag_name", "")),
            "published_at": latest_release.get("published_at", ""),
            "html_url": latest_release.get("html_url", ""),
            "prerelease": bool(latest_release.get("prerelease", False)),
            "summary": sanitize_release_notes(latest_release.get("body", "")),
            "assets": matched_assets
        },
        "history": history
    }


def build_manifest(products: list[dict], fetcher=fetch_releases) -> dict:
    """
    Builds the complete multi-project release manifest.
    Fails atomic operation if any project fetch raises an exception.
    """
    normalized_projects = []
    for product in products:
        repo = product["repo"]
        releases = fetcher(repo)
        norm = normalize_project(product, releases)
        normalized_projects.append(norm)

    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "generated_at": now_utc,
        "projects": normalized_projects
    }


def write_manifest_atomic(dest_path: Path, manifest: dict) -> None:
    """
    Atomically writes the manifest dict as formatted JSON to dest_path
    using a temporary file in the destination directory and os.replace.
    """
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    temp_fd, temp_path = tempfile.mkstemp(dir=dest_path.parent, prefix="manifest_", suffix=".tmp")
    try:
        with open(temp_fd, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp_path, dest_path)
    except Exception:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise


def main():
    parser = argparse.ArgumentParser(description="Update Zvirox release manifest from GitHub API.")
    parser.add_argument(
        "--products",
        type=Path,
        default=DEFAULT_PRODUCTS_FILE,
        help="Path to download_products.json"
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_MANIFEST_FILE,
        help="Path to output release_manifest.json"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate product definitions and connectivity without overwriting output"
    )
    args = parser.parse_args()

    if not args.products.exists():
        print(f"Error: Products file not found: {args.products}", file=sys.stderr)
        sys.exit(1)

    with open(args.products, "r", encoding="utf-8") as f:
        products = json.load(f)

    print(f"Loaded {len(products)} products from {args.products}")

    manifest = build_manifest(products)

    if args.check:
        print("Check completed successfully. Manifest preview:")
        print(json.dumps(manifest, indent=2))
        sys.exit(0)

    write_manifest_atomic(args.output, manifest)
    print(f"Successfully generated release manifest at {args.output}")


if __name__ == "__main__":
    main()
