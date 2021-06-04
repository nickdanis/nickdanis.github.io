def get_semester():
    semester = input("Semester? " )
    file_semester = semester.split()[0][:2].lower() + semester.split()[1]
    return semester, file_semester

def get_course():
    course = input("Course? ")
    file_course = course.split()[0].lower() + course.split()[1].lower()
    return course, file_course

def build_header(course, semester):
    header = f"---\nlayout: syllabus\n"
    header += f"title: {course}\n"
    header += f"semester: {semester}\n"
    header += f"---\n\n"
    header += "* TOC\n{:toc}\n"
    header += "\n TKTKTK"
    return header

semester, file_semester = get_semester()
course, file_course = get_course()

filename = f"{file_semester}-{file_course}.md"
contents = build_header(course, semester)

with open(f"_syllabi/{filename}", "w") as f:
    f.write(contents)

print(f"New syllabus created: {filename}")
