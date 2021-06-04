---
layout: posts
title: Posts
---

{% for image in site.static_files %}
  {% if image.path contains 'assets/posts' %}
    <img src="{{ image.path }}" alt="">
  {% endif %}
{% endfor %}
