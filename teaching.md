---
layout: page
title: Teaching
---

Syllabi for {{ site.current_semester | escape }}:
{% for syllabi in site.syllabi %}
    <!-- {% if syllabi.semester == site.current_semester %} -->
- [{{ syllabi.course }}]({{ syllabi.url }})
    <!-- {% end if %} -->
{% endfor %}

Fall 2021 office hours: TBD.

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 

