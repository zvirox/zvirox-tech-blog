---
layout: default
title: Redirecting to Guides | Zvirox
permalink: /articles/
redirect_to: /guides/
---

<div class="zv-container">
  <section class="zv-section" style="text-align:center; padding:60px 20px;">
    <h1 class="zv-section-title">Articles has moved to Guides</h1>
    <p style="color:var(--zv-text-muted); margin:16px 0 24px;">
      Our technical articles and architecture documentation are now located under Guides.
    </p>
    <a href="{{ '/guides/' | relative_url }}" class="zv-button zv-button-primary">
      Go to Guides &rarr;
    </a>
  </section>
</div>

<script>
  window.location.replace("{{ '/guides/' | relative_url }}");
</script>
