---
layout: page
title: Teaching
---

Syllabi for {{ site.current_semester }}:
{% for item in site.syllabi %}
    {% if item.semester == site.current_semester %}
- [{{ item.title }}]({{ item.url }})
    {% endif %}
{% endfor %}

Fall 2021 office hours: TBD.

Previous semesters:
{% for item in site.syllabi %}
    {% if item.semester != site.current_semester %}
- [{{item.semester.}} - {{ item.title }}]({{ item.url }})
    {% endif %}
{% endfor %}

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 

