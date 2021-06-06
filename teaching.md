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

<table>
<tr>
{% for item in site.syllabi %}
    {%- if item.semester != site.current_semester -%}
    {% assign sem = item.semester | split: ' ' %}
<td><a href="{{ item.url }}">{{ item.title }}</td> <td>{{sem[0]}}</td> <td>{{sem[1]}}</td>
    {%- endif -%}
{% endfor %}
</tr>
</table>

<ul>
{% for item in site.syllabi %}
    {%- if item.semester != site.current_semester -%}
<li><a href="{{ item.url }}">{{ item.title }} ({{item.semester.}})</a></li>
    {%- endif -%}
{% endfor %}
</ul>

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 



