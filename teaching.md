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

<!-- {% assign all_semesters = "" | split: ',' %}


{% for item in site.syllabi %}
    {% for sem in item.semester %}
        {% assign all_semesters = all_semesters | push: sem %}
    {% endfor %}
{% endfor %} -->

{% assign semesters = site.syllabi | map:'semester' | uniq %}
{% assign years = site.syllabi | map:'year' | uniq | sort %}

{% for year in years %}
### {{ year }}
    {% for item in site.syllabi %}
        {%- if item.semester != site.current_semester or item.year != site.current_year -%}
* [{{item.semester.}} - {{ item.title }}]({{ item.url }})
        {%- endif %}
    {% endfor %}
{% endfor %}

{% for sem in semesters %}
* {{ sem }}
{% endfor %}

{% for item in site.syllabi %}
    {%- if item.semester != site.current_semester -%}
* [{{item.semester.}} - {{ item.title }}]({{ item.url }})
    {%- endif %}
{% endfor %}

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 



