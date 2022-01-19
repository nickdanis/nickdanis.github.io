---
layout: teaching
title: Teaching
---

## {{ site.current_semester }}

I am on family leave for the Spring 2022 semester. See you in the fall. 👶

{% for item in site.syllabi %}
    {%- if item.semester == site.current_semester -%}
* [{{ item.title }}]({{ item.url }})
    {%- endif %}
{% endfor %}

<!-- Office hours: {{ site.fa2021.office-hours }} @ {{ site.fa2021.office-location }}. -->





