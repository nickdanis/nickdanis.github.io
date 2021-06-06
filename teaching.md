---
layout: teaching
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
* [{{item.semester.}} - {{ item.title }}]({{ item.url }})
    {%- endif %}
{% endfor %}

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 



