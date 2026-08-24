# ============================================================
# services/question_service.py
# ============================================================

from services.fuseki_service import execute_query

from services.sparql_queries import (
    all_students,
    all_subjects,
    all_departments,
    all_lecturers,
    students_studying_semantic_web,
    students_studying_cloud_computing,
    students_studying_english,
    students_studying_information_theory,
    students_studying_machine_learning,
    students_studying_robotic,
    student_count_each_course,
    student_courses,
)
# ============================================================
# STUDENT COURSES
# ============================================================

def answer_student_courses(student_name):

    query = student_courses(student_name)

    print("\n========== STUDENT COURSES ==========")

    print("Student:")
    print(student_name)

    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    bindings = result["results"]["bindings"]

    courses = []

    for item in bindings:

        courses.append({
            "student": item["studentName"]["value"],
            "course": item["courseName"]["value"]
        })

    print("Courses found:", len(courses))
    print("Course data:")
    print(courses)

    return courses

# ============================================================
# STUDENT COUNT FOR EACH COURSE
# ============================================================

def answer_student_count_each_course():

    query = student_count_each_course()

    print("\n========== STUDENT COUNT EACH COURSE ==========")

    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    courses = []

    bindings = result["results"]["bindings"]

    for item in bindings:

        course_name = item["courseName"]["value"]
        student_count = int(item["studentCount"]["value"])

        courses.append({
            "course": course_name,
            "studentCount": student_count
        })

    print("Courses found:", len(courses))

    print("Course student counts:")
    print(courses)

    return courses
    
# ============================================================
# Convert SPARQL result to student data
# ============================================================

def get_student_data(result):

    students = []

    bindings = (
        result
        .get("results", {})
        .get("bindings", [])
    )

    for item in bindings:

        student = {
            "studentID": item.get(
                "studentID",
                {}
            ).get(
                "value",
                ""
            ),

            "studentName": item.get(
                "name",
                {}
            ).get(
                "value",
                ""
            ),

            "email": item.get(
                "email",
                {}
            ).get(
                "value",
                "-"
            ),

            "majorName": item.get(
                "majorName",
                {}
            ).get(
                "value",
                "-"
            ),

            "course": item.get(
                "courseName",
                {}
            ).get(
                "value",
                "-"
            )
        }

        students.append(student)

    return students

# ============================================================
# ALL SUBJECTS
# ============================================================

def get_all_subjects():

    query = all_subjects()

    print("\n========== ALL SUBJECTS ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    subjects = []

    bindings = (
        result
        .get("results", {})
        .get("bindings", [])
    )

    for item in bindings:

        subject = {
            "courseCode": item.get(
                "courseCode",
                {}
            ).get(
                "value",
                "-"
            ),

            "courseName": item.get(
                "courseName",
                {}
            ).get(
                "value",
                "-"
            ),

            "description": item.get(
                "description",
                {}
            ).get(
                "value",
                "-"
            )
        }

        subjects.append(subject)

    print("Subjects found:", len(subjects))
    print("Subject data:")
    print(subjects)

    return subjects

# ============================================================
# ALL DEPARTMENTS
# ============================================================

def get_all_departments():

    query = all_departments()

    print("\n========== ALL DEPARTMENTS ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    departments = []

    bindings = (
        result
        .get("results", {})
        .get("bindings", [])
    )

    for item in bindings:

        department = {
            "departmentName": item.get(
                "departmentName",
                {}
            ).get(
                "value",
                "-"
            )
        }

        departments.append(department)

    print("Departments found:", len(departments))
    print("Department data:")
    print(departments)

    return departments

# ============================================================
# ALL LECTURERS
# ============================================================

def get_all_lecturers():

    query = all_lecturers()

    print("\n========== ALL LECTURERS ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    lecturers = []

    bindings = (
        result
        .get("results", {})
        .get("bindings", [])
    )

    for item in bindings:

        lecturer = {
            "lecturerName": item.get(
                "lecturerName",
                {}
            ).get(
                "value",
                "-"
            ),

            "email": item.get(
                "email",
                {}
            ).get(
                "value",
                "-"
            )
        }

        lecturers.append(lecturer)

    print("Lecturers found:", len(lecturers))
    print("Lecturer data:")
    print(lecturers)

    return lecturers

# ============================================================
# ALL STUDENTS
# ============================================================

def get_all_students():

    query = all_students()

    print("\n========== ALL STUDENTS ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    students = get_student_data(result)

    print("Students found:", len(students))
    print("Student data:")
    print(students)

    return students


# ============================================================
# SEMANTIC WEB
# ============================================================

def answer_students_studying_semantic_web():

    query = students_studying_semantic_web()

    print("\n========== SEMANTIC WEB ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    students = get_student_data(result)

    print("Students found:", len(students))
    print("Student data:")
    print(students)

    return students


# ============================================================
# CLOUD COMPUTING
# ============================================================

def answer_students_studying_cloud_computing():

    query = students_studying_cloud_computing()

    print("\n========== CLOUD COMPUTING ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    students = get_student_data(result)

    print("Students found:", len(students))
    print("Student data:")
    print(students)

    return students


# ============================================================
# ENGLISH
# ============================================================

def answer_students_studying_english():

    query = students_studying_english()

    print("\n========== ENGLISH ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    students = get_student_data(result)

    print("Students found:", len(students))
    print("Student data:")
    print(students)

    return students


# ============================================================
# INFORMATION THEORY
# ============================================================

def answer_students_studying_information_theory():

    query = students_studying_information_theory()

    print("\n========== INFORMATION THEORY ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    students = get_student_data(result)

    print("Students found:", len(students))
    print("Student data:")
    print(students)

    return students


# ============================================================
# MACHINE LEARNING
# ============================================================

def answer_students_studying_machine_learning():

    query = students_studying_machine_learning()

    print("\n========== MACHINE LEARNING ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    students = get_student_data(result)

    print("Students found:", len(students))
    print("Student data:")
    print(students)

    return students


# ============================================================
# ROBOTIC
# ============================================================

def answer_students_studying_robotic():

    query = students_studying_robotic()

    print("\n========== ROBOTIC ==========")
    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    students = get_student_data(result)

    print("Students found:", len(students))
    print("Student data:")
    print(students)

    return students
