---
layout: posts
title: Posts
---

{% for image in site.static_files %}
  {% if image.path contains 'assets/posts' %}
<img src="{{ image.path }}" class="post-gallery" alt="">
  {% endif %}
{% endfor %}

added class and css code
