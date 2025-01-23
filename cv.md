---
layout: cv
title: CV
last-updated: August 27, 2024
---

## Research interests

* Phonology, Optimality Theory, Computational linguistics, African languages

## Academic Positions

### Current

* Lecturer, Washington University in St. Louis (since 2019)

### Previous

* 2017-2019, Lecturer, Princeton University (10%-60% FTE)
* 2018, Adjunct Professor, Rowan University

## Education

* 2017, PhD in Linguistics, Rutgers University
* 2011, MA in Applied Linguistics, Boston University
* 2008, B.A. in Linguistics, *cum laude*, Boston University
* 2008, B.S. in Film and Television, *cum laude*, Boston University

## Publications

{% include_relative publist.md %}

## Teaching

### Washington University in St. Louis

<!-- {% assign wucourses = "" %}
{% for item in site.syllabi %}
  {% assign wucourses = wucourses | append: item.title | append: ", " %}
{% endfor %}

{% assign wulist = wucourses | split: ", " | uniq | sort  %}

| Course | Name | Semesters |
|---|---|---|{% for item in wulist %}
| {% assign num = item | truncatewords: 2,"" %}{{ num }} | {{ item | replace: num,"" }} | {% assign sem = site.syllabi | where: "title",item %} {% assign terms = "" %} {% for s in sem %} {% assign terms = terms | append: s.semester | append: ", " %} {% endfor %} {{ terms | split: ", " | join: ", "}} |{% endfor %} -->

{% assign wucourses = "" %}
{% for item in site.syllabi %}
  {% assign wucourses = wucourses | append: item.title | append: ", " %}
{% endfor %}

{% assign wulist = wucourses | split: ", " | uniq | sort  %}

{% for item in wulist %}
* {{ item }} {% assign sem = site.syllabi | where: "title",item %} {% assign terms = "" %} {% for s in sem %} {% assign terms = terms | append: s.semester | append: ", " %} {% endfor %} 
  * *{{ terms | split: ", " | join: ", "}}* {% endfor %}

### Princeton University

* LIN201 Introduction to Language and Linguistics (preceptor)
  * *Fall 2018; Spring 2018* 

### Rowan University

* CMS 04326 Linguistics
  * *Spring 2018*

### Rutgers University

* 01:615:190 Linguistic Perspectives on Language: Invented Languages
  * *Fall 2016; Spring 2016, 2017*
* 01:615:201 Introduction to Linguistic Theory
  * *Fall 2013 (TA); Spring 2014; Summer 2015*

## Field Experience

* 2010, Medumba ([byv], Grassfields Bantu, Cameroon): Conducted one month of intensive fieldwork in Yaoundé, Bangangté, and local surrounding villages. Funded by NSF Grant BCS 1026724.

## Service

### Reviewing

* 2021, *Stellenbosch Papers in Linguistics Plus*
* 2020, *Natural Language and Linguistic Theory*
* 2018-2020, *Phonology*
* 2019, Cambridge University Press
* 2017, Oxford University Press
* 2015, *Diversity in African languages: Selected papers from the 46th Annual Conference on African Linguistics*

## Other Education

### Summer Programs

* 2021, [May 2021 Data Science Boot Camp](https://www.erdosinstitute.org/may2021certificates/nick-danis)<br>Erdős Institute 
* 2010, 3L Summer School on Language Documentation and Description<br>Leiden, Netherlands
* 2010, Medumba Intensive Literacy Course<br>Comité de Langue pour l’Etude et la Production des Œuvres Bamiléké-Medumba (CEPOM) <br>Bangangté, Cameroon
* 2009, LSA Summer Institute<br>University of California, Berkeley

### Awards

* 2019, Washington University Course Innovation Grant
* 2016, Mellon Summer Study Grant
* 2014, Excellence Fellowship for doctoral study in Linguistics
* 2014, Mellon Summer Study Grant
* 2011-2012, Excellence Fellowship for doctoral study in Linguistics

## Skills

### Language

* English (native)
* Italian (intermediate to advanced)
* Medumba [byv] (research and field knowledge)
* French, German (academic reading)
* ASL (basic)

### Technical

* ◾◾◾◾◾ OTWorkplace/VBA
* ◾◾◾◾◽ Python 
  * ◾◾◾◾◽ nltk 
  * ◾◾◾◽◽ pandas/matplotlib
  * ◾◾◽◽◽ flask
  * ◾◾◽◽◽ sklearn
  * ◾◾◽◽◽ scipy
* ◾◾◾◾◽ Praat
* ◾◾◾◾◽ LaTeX 
* ◾◾◾◽◽ HTML/CSS
{: #skill-list}
