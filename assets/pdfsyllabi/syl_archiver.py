import os, re

directory = os.fsencode(r"C:\Users\ndanis\OneDrive\github\nickdanis.github.io\assets\pdfsyllabi")


def build_header(course, semester):
    header = f"---\nlayout: syllabus\n"
    header += f"title: {course}\n"
    header += f"semester: {semester}\n"
    header += f"---\n\n"
    return header

file_list = []
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if "pdf" in filename:
        file_list.append(filename)

def parse_filename(file,n):
    course_groups = re.search(r"(.+)(-)(.+)(\.)",file)
    return course_groups.group(n)

def make_link(filename, semester, year):
    link = f"[here](/assets/pdfsyllabi/{filename})"
    content = f"Click {link} for {semester} {year} syllabus PDF."
    return content

course_dict = {
    'ling148' : 'Ling 148 The Linguistics of Constructed Languages',
    'ling170d' : 'Ling 170D Introduction to Linguistics',
    'ling312' : 'Ling 312 Phonetics',
    'ling313' : 'Ling 313 Phonological Analysis',
    'ling317' : 'Ling 317 Introduction to Computational Linguistics',
    'ling427' : 'Ling 427 Computation and Learnability in Linguistic Theory'
}

semester_dict = {
    'sp' : 'Spring',
    'fa' : 'Fall'
}
print(file_list)
for f in file_list:
    title = course_dict[parse_filename(f,3)]
    semester = semester_dict[parse_filename(f,1)[:2]]
    year = parse_filename(f,1)[2:]
    contents = build_header(title, f"{semester} {year}")
    contents += make_link(f, semester, year)
    md_filename = f.replace("pdf","md")
    #print(md_filename)
    #print(contents)
    with open(f"_syllabi/{md_filename}", "w",encoding="utf-8") as syl:
        syl.write(contents)
    
