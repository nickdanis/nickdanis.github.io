---
layout: page
title: Posts
---

Sort by: [date]({{ site.baseurl }}{% link posts.md %}) \| [**tag**]({{ site.baseurl }}{% link posts-by-tag.md %})

<ul class="tag-list">
{% assign all_tags = site.tags | sort %}
{% for tag in all_tags %}
{% assign size_pct = tag[1] | size | times: 20 | plus: 80 %}
<li class="tag-link" style="font-size: {{size_pct}}%"> <a href="#{{tag[0]}}">{{tag[0]}} </a> </li>
{% endfor %}
</ul>

{% for tag in all_tags %}
## {{ tag[0] }}
  <ul class="post-list">
    {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
    {% for post in tag[1] %}
      <li>
        <a class="post-link" href="{{ post.url }}">{{ post.title }}</a>
        <span class="post-meta">{{ post.date | date: date_format }}</span>
      </li>
    {% endfor %}
  </ul>
  <p> <a href="#top"> top </a>
  </p>
{% endfor %}