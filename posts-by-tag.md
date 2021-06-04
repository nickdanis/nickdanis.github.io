---
layout: page
title: Posts
---

Sort by: [**date**]({{ site.baseurl }}{% link posts.md %}) \| [**tag**]({{ site.baseurl }}{% link posts-by-tag.md %})

<ul class="tag-list">
{% for tag in site.tags %}
<li> <a href="#{{tag[0]}}">{{tag[0]}}</a> </li>
{% endfor %}
</ul>

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