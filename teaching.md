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

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 

testing:
{% for syllabi in site.syllabi %}
- should say the semester: {{ syllabi.semester }}
- should say the title: {{ syllabi.title }}
{% endfor %}

test 2:
{% for syllabi in site.syllabi %}
    {% if syllabi.semester == site.current_semester %}
- {{syllabi.title}}
    
{% endfor %}