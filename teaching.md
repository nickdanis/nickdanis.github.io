---
layout: page
title: Teaching
---

Fall 2021 courses:
- Ling 148: The Linguistics of Constructed Languages
- Ling 313: Phonological Analysis
- Ling 417: Computation and Learnability in Linguistic Theory

Fall 2021 office hours: TBD.

Syllabus links are given when available. See my [CV]({{ site.baseurl }}{% link cv.md %}) for full teaching history. 

{% for syllabi in site.syllabi %}
  <p>{{ syllabi.semester }} - {{ syllabi.course }}</p>
{% endfor %}