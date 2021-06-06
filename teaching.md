---
layout: page
title: Teaching
---

## {{ site.current_semester }}

{% for item in site.syllabi %}
    {%- if item.semester == site.current_semester -%}
* [{{ item.title }}]({{ item.url }})
    {%- endif %}
{% endfor %}

Office hours: {{ site.fa2021.office-hours }} @ {{ site.fa2021.office-location }}.

## Previous semesters

{% assign syls = site.syllabi | nested_sort:"site.syllabi.title" %}

<ul>
{% for item in syl %}
    {%- if item.semester != site.current_semester -%}
<li><a href="{{ item.url }}">{{ item.title }} ({{item.semester.}})</a></li>
    {%- endif -%}
{% endfor %}
</ul>

<ul>
{% for item in site.syllabi %}
    {%- if item.semester != site.current_semester -%}
<li><a href="{{ item.url }}">{{ item.title }} ({{item.semester.}})</a></li>
    {%- endif -%}
{% endfor %}
</ul>

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 



