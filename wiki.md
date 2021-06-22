---
layout: page
title: Wiki
---

# Optimality Theory Wiki

This wiki is intended as a reference/textbook specifically for WUSTL courses L44 Ling 313 Phonological Analysis and L44 Ling 427 Learnability and Computation in Linguistic Theory, but also serves as a general reference as well. I will try to include citations to the literature whenever relevant, though the way core concepts are framed here come from course and lecture notes from Alan Prince, Bruce Tesar, Paul de Lacy, and Akin Akinlabi, among discussions with many others. 

This is a work in progress. Errors? Omissions? Comments? Contact me 👇.

## Content

<ul class="wiki-list">
{% assign items = site.wiki | sort: 'chapter' %}
{% for page in items %}
<li><a href="{{ page.url }}">{{ page.title }}</a></li>
{% endfor %}
</ul>