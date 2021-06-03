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


{% for syllabi in site.syllabi %}
- {{ syllabi.semester }}
- {{ syllabi.title }}
{% endfor %}