---
layout: page
title: Teaching
---

Syllabi for {{ site.current_semester }}:
{% for syllabi in site.syllabi %}
    <!-- {% if syllabi.semester == site.current_semester %} -->
- [{{ syllabi.semester }} - {{ syllabi.title }}]({{ syllabi.url }})
    <!-- {% endif %} -->
{% endfor %}

Fall 2021 office hours: TBD.

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 

