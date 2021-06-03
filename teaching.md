---
layout: page
title: Teaching
---

Syllabi for {{ site.current_semester }}:
{% for syllabi in site.syllabi %}
- [{{ syllabi.title }}]({{ syllabi.url }})
{% endfor %}

Fall 2021 office hours: TBD.

See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 

testing:
{% for syllabi in site.syllabi %}
- should say the semester: {{ syllabi.semester }}
- should say the title: {{ syllabi.title }}
{% endfor %}