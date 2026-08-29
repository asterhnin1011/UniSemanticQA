# ============================================================
# services/question_service.py
# ============================================================

from services.fuseki_service import execute_query

from services.sparql_queries import (
    all_students,
    all_subjects,
    all_departments,
    students_studying_semantic_web,
    students_studying_cloud_computing,
    students_studying_english,
    students_studying_information_theory,
    students_studying_machine_learning,
    students_studying_robotic,
    student_count_each_course,
    student_courses,
    students_majoring_in,
    all_lecturers,
    lecturers_teaching_english,
    lecturers_teaching_advanced_information_theory,
    lecturers_teaching_analysis_of_algorithms,
    lecturers_teaching_business_analytics,
    lecturers_teaching_machine_learning,
    lecturers_teaching_cloud_computing,
    lecturers_teaching_semantic_web,
    lecturers_teaching_embedded_robotic_system,
    lecturers_teaching_deep_learning,
    lecturers_teaching_comprehensive_web_design,
    lecturers_teaching_business_system_infrastructure_and_security,
    course_code_by_name,
    department_of_lecturer,
    lecturers_working_in_faculty,
    students_taught_by_lecturer,
    students_majoring_in_ke_and_enrolled_in_embedded_robotic,
    students_majoring_in_and_enrolled_in,
)
# ========================================================
# Lecturers teaching Cloud Computing
# ========================================================

def get_lecturers_teaching_cloud_computing():

    query = lecturers_teaching_cloud_computing()
    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:
        lecturers.append({
            "lecturerName": binding["lecturerName"]["value"],
            "courseName": binding["courseName"]["value"],
            "email": binding["email"]["value"]
        })

    return lecturers
# ========================================================
# Students majoring in a specific major
# and enrolled in a specific course
# ========================================================

def get_students_majoring_in_and_enrolled_in(major_name, course_name):

    query = students_majoring_in_and_enrolled_in(
        major_name,
        course_name
    )

    result = execute_query(query)

    bindings = result.get("results", {}).get("bindings", [])

    students = []

    for binding in bindings:

        student_name = binding.get(
            "studentName", {}
        ).get("value", "")

        if student_name:
            students.append(student_name)

    return students
# ========================================================
# Lecturers teaching Semantic Web
# ========================================================

def get_lecturers_teaching_semantic_web():

    query = lecturers_teaching_semantic_web()
    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:
        lecturers.append({
            "lecturerName": binding["lecturerName"]["value"],
            "courseName": binding["courseName"]["value"],
            "email": binding["email"]["value"]
        })

    return lecturers
# ========================================================
# Students majoring in KE and enrolled in Embedded Robotic System
# ========================================================

def get_students_majoring_in_ke_and_enrolled_in_embedded_robotic():

    query = students_majoring_in_ke_and_enrolled_in_embedded_robotic()

    result = execute_query(query)

    bindings = result.get("results", {}).get("bindings", [])

    students = []

    for binding in bindings:

        student_name = binding.get(
            "studentName", {}
        ).get("value", "")

        if student_name:
            students.append(student_name)

    return students
# ========================================================
# Lecturers teaching Embedded Robotic System
# ========================================================

def get_lecturers_teaching_embedded_robotic_system():

    query = lecturers_teaching_embedded_robotic_system()
    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:
        lecturers.append({
            "lecturerName": binding["lecturerName"]["value"],
            "courseName": binding["courseName"]["value"],
            "email": binding["email"]["value"]
        })

    return lecturers
# ========================================================
# Lecturers teaching Deep Learning
# ========================================================

def get_lecturers_teaching_deep_learning():

    query = lecturers_teaching_deep_learning()
    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:
        lecturers.append({
            "lecturerName": binding["lecturerName"]["value"],
            "courseName": binding["courseName"]["value"],
            "email": binding["email"]["value"]
        })

    return lecturers

# ========================================================
# Get Course Code
# ========================================================

def get_course_code(course_name):

    query = course_code_by_name(course_name)

    data = execute_query(query)

    courses = []

    for binding in data["results"]["bindings"]:

        courses.append({
            "courseName": binding["courseName"]["value"],
            "courseCode": binding["courseCode"]["value"]
        })

    return courses
# ========================================================
# Lecturers teaching Comprehensive Web Design
# ========================================================

def get_lecturers_teaching_comprehensive_web_design():

    query = lecturers_teaching_comprehensive_web_design()
    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:
        lecturers.append({
            "lecturerName": binding["lecturerName"]["value"],
            "courseName": binding["courseName"]["value"],
            "email": binding["email"]["value"]
        })

    return lecturers
# ============================================================
# Get Course Code by Course Name
# ============================================================

def answer_course_code(course_name):
    query = course_code_by_name(course_name)
    result = execute_query(query)

    bindings = result.get("results", {}).get("bindings", [])

    if not bindings:
        return {
            "courseName": course_name,
            "courseCode": None,
            "message": f"No course code found for {course_name}."
        }

    binding = bindings[0]

    return {
        "courseName": binding.get("courseName", {}).get("value", course_name),
        "courseCode": binding.get("courseCode", {}).get("value", "")
    }
# ========================================================
# Lecturers teaching Business System Infrastructure and Security
# ========================================================

def get_lecturers_teaching_business_system_infrastructure_and_security():

    query = lecturers_teaching_business_system_infrastructure_and_security()
    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:
        lecturers.append({
            "lecturerName": binding["lecturerName"]["value"],
            "courseName": binding["courseName"]["value"],
            "email": binding["email"]["value"]
        })

    return lecturers
    

# ========================================================
# Department by Lecturer Name
# ========================================================

def get_department_of_lecturer(lecturer_name):

    query = department_of_lecturer(lecturer_name)

    result = execute_query(query)

    bindings = result.get("results", {}).get("bindings", [])

    departments = []

    for binding in bindings:

        department_name = binding.get(
            "departmentName", {}
        ).get("value", "")

        if department_name:
            departments.append(department_name)

    return departments

# ========================================================
# Who are the lecturers working in a specific faculty?
# ========================================================

def get_lecturers_working_in_faculty(faculty_name):

    query = lecturers_working_in_faculty(faculty_name)

    result = execute_query(query)

    bindings = result.get("results", {}).get("bindings", [])

    lecturers = []

    for binding in bindings:

        lecturer_name = binding.get(
            "lecturerName", {}
        ).get("value", "")

        if lecturer_name:
            lecturers.append(lecturer_name)

    return lecturers
# ========================================================
# Which students are taught by a specific lecturer?
# ========================================================

def get_students_taught_by_lecturer(lecturer_name):

    query = students_taught_by_lecturer(lecturer_name)

    result = execute_query(query)

    bindings = result.get("results", {}).get("bindings", [])

    students = []

    for binding in bindings:

        student_name = binding.get(
            "studentName", {}
        ).get("value", "")

        if student_name:
            students.append(student_name)

    return students

# ========================================================
# Lecturers teaching English
# ========================================================

def get_lecturers_teaching_english():

    query = lecturers_teaching_english()

    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:

        lecturers.append({
            "lecturerName": binding["lecturerName"]["value"],
            "courseName": binding["courseName"]["value"],
            "email": binding["email"]["value"]
        })

    return lecturers  
# ========================================================
# Lecturers teaching Machine Learning
# ========================================================

def get_lecturers_teaching_machine_learning():

    query = lecturers_teaching_machine_learning()

    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:

        lecturers.append({

            "lecturerName": binding["lecturerName"]["value"],

            "courseName": binding["courseName"]["value"],

            "email": binding["email"]["value"]

        })

    return lecturers
# ========================================================
# Lecturers teaching Advanced Information Theory
# ========================================================

def get_lecturers_teaching_advanced_information_theory():

    query = lecturers_teaching_advanced_information_theory()

    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:

        lecturers.append({
            "lecturerName": binding["lecturerName"]["value"],
            "courseName": binding["courseName"]["value"],
            "email": binding["email"]["value"]
        })

    return lecturers 
# ========================================================
# Lecturers teaching Business Analytics
# ========================================================

def get_lecturers_teaching_business_analytics():

    query = lecturers_teaching_business_analytics()

    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:

        lecturers.append({

            "lecturerName": binding["lecturerName"]["value"],

            "courseName": binding["courseName"]["value"],

            "email": binding["email"]["value"]

        })

    return lecturers

# ============================================================
# STUDENTS MAJORING IN A SPECIFIC MAJOR
# ============================================================

def answer_students_majoring_in(major_name):

    query = students_majoring_in(major_name)

    print("\n========== STUDENTS MAJORING IN ==========")

    print("Major:", major_name)

    print("SPARQL QUERY:")
    print(query)

    result = execute_query(query)

    print("RAW RESULT:")
    print(result)

    bindings = result["results"]["bindings"]

    students = []

    for item in bindings:

        students.append({
            "id": item["studentID"]["value"],
            "name": item["studentName"]["value"],
            "email": item["email"]["value"],
            "major": item["majorName"]["value"]
        })

    print("Students found:", len(students))
    print("Student data:")
    print(students)

    return students

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
# ALL LECTURERS WITH COURSE
# ============================================================

def get_all_lecturers():

    query = all_lecturers()

    print("\n========== ALL LECTURERS WITH COURSE ==========")

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
            ),

            "courseName": item.get(
                "courseName",
                {}
            ).get(
                "value",
                "-"
            )
        }

        lecturers.append(lecturer)

    print("Lecturer-course records found:", len(lecturers))

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
# ========================================================
# Lecturers teaching Analysis of Algorithms
# ========================================================

def get_lecturers_teaching_analysis_of_algorithms():

    query = lecturers_teaching_analysis_of_algorithms()

    data = execute_query(query)

    lecturers = []

    for binding in data["results"]["bindings"]:

        lecturers.append({

            "lecturerName": binding["lecturerName"]["value"],

            "courseName": binding["courseName"]["value"],

            "email": binding["email"]["value"]

        })

    return lecturers