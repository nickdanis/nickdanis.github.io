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

{% for item in site.syllabi %}
    {%- if item.semester != site.current_semester -%}
* [{{ item.title }} ({{item.semester.}})]({{ item.url }})
    {%- endif -%}
{% endfor %}

<ul>
{% for item in site.syllabi %}
    {%- if item.semester != site.current_semester -%}
<li>[{{ item.title }} ({{item.semester.}})]({{ item.url }})</li>
    {%- endif -%}
{% endfor %}
</ul>

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 



