---
layout: page
title: Posts by tag
---

## Tags

* TOC
{:toc}

{% for tag in site.tags %}
## {{ tag[0] }}
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