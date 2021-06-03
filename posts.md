---
layout: posts
title: Posts
---

{% assign tagArray = '' | split: ',' %}
{% for post in site.posts %}
{% if post.published != "false" %}
{% for tag in post.tags %}
{% assign tagArray = tagArray | push: tag %} {% endfor %}
{% endif %}
{% endfor %}
{% assign uniqTags = tagArray | uniq %}

tags:
{% for tag in uniqTags %}
* {{ tag }}
{% endfor %}
