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
    {{ tag }}
{% endfor %}


method 2:

{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}