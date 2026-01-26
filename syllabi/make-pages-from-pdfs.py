from os import listdir
import re

sem_dict = {'sp':'Spring',
            'fa':'Fall'}

dates = {}

course_dict = {
    'LING 148': 'The Linguistics of Constructed Languages', 
    'LING 170D': 'Introduction to Linguistics',
    'LING 1600': 'Introduction to Linguistics', 
    'LING 313': 'Phonological Analysis', 
    'LING 427': 'Computation and Learnability in Linguistic Theory',
    'LING 4250': 'Computation and Learnability in Linguistic Theory', 
    'LING 495': 'Senior Seminar in Optimality Theory', 
    'LING 258': 'Methods in Linguistic Research', 
    'LING 312': 'Phonetics', 
    'LING 317': 'Introduction to Computational Linguistics',
    'LING 3250': 'Introduction to Computational Linguistics'}

def get_details(f):
    raw_details = f.split('-')
    raw_sem = raw_details[1]
    course = re.sub(r'LING','LING ',raw_details[0].upper())
    sem = f"{raw_sem[2:]} {sem_dict[raw_sem[:2]]}"
    return sem, course

def make_page(course, title, sem, f):
    template = f'''
---
title: {course} {title}
author: {sem}
description: ""
---

{{{{< pdf {f} button="Download" width=100% height=1000 >}}}}

'''
    return template


for f in listdir('syllabi'):
    if f.endswith('pdf'):
        course = get_details(f)[1]
        sem = get_details(f)[0]
        title = course_dict[course]
        page = make_page(course, title, sem, f)
        page_name = f[:-4] + ".qmd"
        print(f"writing {page_name}...")
        with open(f"syllabi/{page_name}", "w") as mdf:
            mdf.write(page)