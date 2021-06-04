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
    header += f"time: \n"
    header += f"location: \n"
    header += f"canvas-url: \n"
    header += f"published: false\n"
    header += f"---\n\n"
    return header

semester, file_semester = get_semester()
course, file_course = get_course()

filename = f"{file_semester}-{file_course}.md"
header = build_header(course, semester)



skeleton = []
with open("_syllabi/skeleton.txt","r",encoding="utf-8") as s:
    for line in s:
        skeleton.append(line)

with open(f"_syllabi/{filename}", "w",encoding="utf-8") as f:
    f.write(header)
    for line in skeleton:
        f.write(line)


print(f"New syllabus created: {filename}")
