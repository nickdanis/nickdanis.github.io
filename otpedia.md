---
layout: page
title: OTpedia
---

# OTpedia

This guide is intended as a reference/textbook for [**Optimality Theory**](http://roa.rutgers.edu/files/537-0802/537-0802-PRINCE-0-0.PDF), specifically as it is taught in WUSTL courses L44 Ling 313 Phonological Analysis and L44 Ling 427 Learnability and Computation in Linguistic Theory, but can serve as a general reference as well. I will try to include citations to the literature whenever relevant, though the way core concepts are framed here come from course and lecture notes from Alan Prince, Bruce Tesar, Paul de Lacy, and Akin Akinlabi, Brett Hyde, and among discussions with many others. 


## Contents

### Core concepts

<ul class="wiki-list">
{% assign items = site.wiki | sort: 'chapter' %}
{% for page in items %}
{% if page.level == 'core' %}
<li><a href="{{ page.url }}">{{page.chapter}}. {{ page.title }}</a></li>
{% endif %}
{% endfor %}
</ul>

### Advanced theory

<ul class="wiki-list">
{% assign items = site.wiki | sort: 'chapter' %}
{% for page in items %}
{% if page.level == 'advanced' %}
<li><a href="{{ page.url }}">{{page.chapter}}. {{ page.title }}</a></li>
{% endif %}
{% endfor %}
</ul>

### Domains

<ul class="wiki-list">
{% assign items = site.wiki | sort: 'chapter' %}
{% for page in items %}
{% if page.level == 'domains' %}
<li><a href="{{ page.url }}">{{page.chapter}}. {{ page.title }}</a></li>
{% endif %}
{% endfor %}
</ul>


This is a work in progress. Errors? Omissions? Comments? Contact me 👇.