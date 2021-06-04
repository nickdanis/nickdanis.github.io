---
layout: page
title: Posts by tag
---

{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul class="post-list">
    {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
    {% for post in tag[1] %}
      <li>
        <span class="post-meta">{{ post.date | date: date_format }}</span>
        <a class="post-link" href="{{ post.url }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
{% endfor %}