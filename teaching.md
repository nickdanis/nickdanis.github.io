---
layout: page
title: Teaching
---

## {{ site.current_semester }}

Syllabi:

{% for item in site.syllabi -%}
    {%- if item.semester == site.current_semester -%}
* [{{ item.title }}]({{ item.url }})
    {%- endif -%}
{%- endfor %}

Office hours: TBD.

## Previous semesters

{% for item in site.syllabi %}
    {%- if item.semester != site.current_semester -%}
* [{{item.semester.}} - {{ item.title }}]({{ item.url }})
    {%- endif %}
{% endfor %}

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 

only if hyphens except last

