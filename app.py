# ============================================================
# app.py
# ============================================================

import re
from flask import Flask, render_template, request, jsonify

from services.question_service import (
  
    get_all_students,
    get_all_subjects,
    get_all_departments,
    answer_students_studying_semantic_web,
    answer_students_studying_cloud_computing,
    answer_students_studying_english,
    answer_students_studying_information_theory,
    answer_students_studying_machine_learning,
    answer_students_studying_robotic,
    answer_student_count_each_course,
    answer_student_courses,
    answer_students_majoring_in,
    get_all_lecturers,
    get_lecturers_teaching_english,
    get_lecturers_teaching_advanced_information_theory,
    get_lecturers_teaching_analysis_of_algorithms,
    get_lecturers_teaching_business_analytics,
    get_lecturers_teaching_machine_learning,
    get_lecturers_teaching_cloud_computing,
    get_lecturers_teaching_semantic_web,
    get_lecturers_teaching_embedded_robotic_system,
    get_lecturers_teaching_deep_learning,
    get_lecturers_teaching_comprehensive_web_design,
    get_lecturers_teaching_business_system_infrastructure_and_security,
    get_course_code,
)

app = Flask(__name__)


# ============================================================
# Home Page
# ============================================================

@app.route("/")
def index():

    return render_template("index.html")


# ============================================================
# Ask Question
# ============================================================

@app.route("/ask", methods=["POST"])
def ask():

    # --------------------------------------------------------
    # Get question
    # --------------------------------------------------------

    data = request.get_json(silent=True) or {}

    question = data.get("question", "").strip()


    # --------------------------------------------------------
    # Empty question
    # --------------------------------------------------------

    if not question:

        return jsonify({
            "answer": "Please enter a question."
        })


    question_lower = question.lower()
# ========================================================
# Who teaches Cloud Computing?
# ========================================================

    if (
    "who teaches cloud computing" in question_lower
    or "who teach cloud computing" in question_lower
    or "lecturers teaching cloud computing" in question_lower
    or "lecturers who teach cloud computing" in question_lower
):

        lecturers = get_lecturers_teaching_cloud_computing()

        print("\n========== FLASK: LECTURERS TEACHING CLOUD COMPUTING ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# Who teaches Semantic Web?
# ========================================================

    if (
    "who teaches semantic web" in question_lower
    or "who teach semantic web" in question_lower
    or "lecturers teaching semantic web" in question_lower
    or "lecturers who teach semantic web" in question_lower
):

        lecturers = get_lecturers_teaching_semantic_web()

        print("\n========== FLASK: LECTURERS TEACHING SEMANTIC WEB ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# Who teaches Embedded Robotic System?
# ========================================================

    if (
    "who teaches embedded robotic system" in question_lower
    or "who teach embedded robotic system" in question_lower
    or "lecturers teaching embedded robotic system" in question_lower
    or "lecturers who teach embedded robotic system" in question_lower
):

        lecturers = get_lecturers_teaching_embedded_robotic_system()

        print("\n========== FLASK: LECTURERS TEACHING EMBEDDED ROBOTIC SYSTEM ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# What is the course code of English?
# ========================================================

    if (
    "what is the course code of english" in question_lower
    or "course code of english" in question_lower
    or "course code for english" in question_lower
):

        courses = get_course_code("English")
        print("\n========== FLASK: COURSE CODE OF ENGLISH ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        if courses:
            return jsonify({
            "answer": courses
        })
# ========================================================
# What is the course code of Advanced Information Theory?
# ========================================================

    if (
    "what is the course code of advanced information theory" in question_lower
    or "course code of advanced information theory" in question_lower
    or "course code for advanced information theory" in question_lower
):

        courses = get_course_code("Advanced Information Theory")
        print("\n========== FLASK: COURSE CODE OF ADVANCED INFORMATION THEORY ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        if courses:

            return jsonify({
            "answer": courses
        })
# ========================================================
# What is the course code of Analysis of Algorithms?
# ========================================================

    if (
    "what is the course code of analysis of algorithms" in question_lower
    or "course code of analysis of algorithms" in question_lower
    or "course code for analysis of algorithms" in question_lower
):

        courses = get_course_code("Analysis of Algorithms")
        print("\n========== FLASK: COURSE CODE OF ANALYSIS OF ALGORITHMS ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        if courses:
            return jsonify({
            "answer": courses
        })

# ========================================================
# What is the course code of Business Analytics?
# ========================================================

    if (
    "what is the course code of business analytics" in question_lower
    or "course code of business analytics" in question_lower
    or "course code for business analytics" in question_lower
):

        courses = get_course_code("Business Analytics")
        print("\n========== FLASK: COURSE CODE OF BUSINESS ANALYTICS ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        if courses:
            return jsonify({
            "answer": courses
        })
# ========================================================
# What is the course code of Business System Infrastructure And Security?
# ========================================================

    if (
    "what is the course code of business system infrastructure and security" in question_lower
    or "course code of business system infrastructure and security" in question_lower
    or "course code for business system infrastructure and security" in question_lower
):

        courses = get_course_code("Business System Infrastructure And Security")
        print("\n========== FLASK: COURSE CODE OF business system infrastructure and security ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        if courses:
            return jsonify({
            "answer": courses
        })

# ========================================================
# What is the course code of Cloud Computing?
# ========================================================

    if (
    "what is the course code of cloud computing" in question_lower
    or "course code of cloud computing" in question_lower
    or "course code for cloud computing" in question_lower
):
        courses = get_course_code("Cloud Computing")
        print("\n========== FLASK: COURSE CODE OF CLOUD COMPUTING ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        return jsonify({
        "answer": courses
    })
# ========================================================
# What is the course code of Comprehensive Web Application Design ?
# ========================================================

    if (
    "what is the course code of comprehensive web application design" in question_lower
    or "course code of comprehensive web application design" in question_lower
    or "course code for comprehensive web application design" in question_lower
):
        courses = get_course_code("Comprehensive Web Application Design ")
        print("\n========== FLASK: COURSE CODE OF Comprehensive Web Application Design ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        return jsonify({
        "answer": courses
    })
# ========================================================
# What is the course code of Embedded Robotic System?
# ========================================================

    if (
    "what is the course code of embedded robotic system" in question_lower
    or "course code of embedded robotic system" in question_lower
    or "course code for embedded robotic system" in question_lower
):
        courses = get_course_code("Embedded Robotic System")
        print("\n========== FLASK: COURSE CODE OF Embedded Robotic System ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        return jsonify({
        "answer": courses
    })
# ========================================================
# What is the course code of Machine Learning?
# ========================================================

    if (
    "what is the course code of machine learning" in question_lower
    or "course code of machine learning" in question_lower
    or "course code for machine learning" in question_lower
):

        courses = get_course_code("Machine Learning")
        print("\n========== FLASK: COURSE CODE OF MACHINE LEARNING ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        return jsonify({
        "answer": courses
    })
# ========================================================
# What is the course code of Resilient Dataset and Deep Learning?
# ========================================================

    if (
    "what is the course code of resilient dataset and deep learning" in question_lower
    or "course code of resilient dataset and deep learning" in question_lower
    or "course code for resilient dataset and deep learning" in question_lower
):

        courses = get_course_code("Resilient Dataset and Deep Learning")
        print("\n========== FLASK: COURSE CODE OF RESILIENT DATASET AND DEEP LEARNING ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        return jsonify({
        "answer": courses
    })
# ========================================================
# What is the course code of Semantic Web?
# ========================================================

    if (
    "what is the course code of semantic web" in question_lower
    or "course code of semantic web" in question_lower
    or "course code for semantic web" in question_lower
):
        courses = get_course_code("Semantic Web")
        print("\n========== FLASK: COURSE CODE OF SEMANTIC WEB ==========")
        print("Courses returned:", len(courses))
        print("Data:", courses)
        return jsonify({
        "answer": courses
    })  
# ========================================================
# Who teaches Deep Learning?
# ========================================================

    if (
    "who teaches deep learning" in question_lower
    or "who teach deep learning" in question_lower
    or "lecturers teaching deep learning" in question_lower
    or "lecturers who teach deep learning" in question_lower
):

        lecturers = get_lecturers_teaching_deep_learning()

        print("\n========== FLASK: LECTURERS TEACHING DEEP LEARNING ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# Who teaches Comprehensive Web Design?
# ========================================================

    if (
    "who teaches comprehensive web design" in question_lower
    or "who teach comprehensive web design" in question_lower
    or "lecturers teaching comprehensive web design" in question_lower
    or "lecturers who teach comprehensive web design" in question_lower
):

        lecturers = get_lecturers_teaching_comprehensive_web_design()

        print("\n========== FLASK: LECTURERS TEACHING COMPREHENSIVE WEB DESIGN ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# Who teaches Business System Infrastructure and Security?
# ========================================================

    if (
    "who teaches business system infrastructure and security" in question_lower
    or "who teach business system infrastructure and security" in question_lower
    or "lecturers teaching business system infrastructure and security" in question_lower
    or "lecturers who teach business system infrastructure and security" in question_lower
):

        lecturers = get_lecturers_teaching_business_system_infrastructure_and_security()

        print(
        "\n========== FLASK: LECTURERS TEACHING "
        "BUSINESS SYSTEM INFRASTRUCTURE AND SECURITY =========="
    )

        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# Who teaches English?
# ========================================================

    if (
    "who teaches english" in question_lower
    or "who teach english" in question_lower
    or "lecturers teaching english" in question_lower
    or "lecturers who teach english" in question_lower
):

        lecturers = get_lecturers_teaching_english()

        print("\n========== FLASK: LECTURERS TEACHING ENGLISH ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# Who teaches Machine Learning?
# ========================================================

    if (
    "who teaches machine learning" in question_lower
    or "who teach machine learning" in question_lower
    or "lecturers teaching machine learning" in question_lower
    or "lecturers who teach machine learning" in question_lower
):

        lecturers = get_lecturers_teaching_machine_learning()
        print("\n========== FLASK: LECTURERS TEACHING MACHINE LEARNING ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)
        return jsonify({
        "answer": lecturers

    })
# ========================================================
# Who teaches Advanced Information Theory?
# ========================================================

    if (
    "who teaches advanced information theory" in question_lower
    or "who teach advanced information theory" in question_lower
    or "lecturers teaching advanced information theory" in question_lower
    or "lecturers who teach advanced information theory" in question_lower
):

        lecturers = get_lecturers_teaching_advanced_information_theory()

        print("\n========== FLASK: LECTURERS TEACHING ADVANCED INFORMATION THEORY ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# Who teaches Business Analytics?
# ========================================================

    if (
    "who teaches business analytics" in question_lower
    or "who teach business analytics" in question_lower
    or "lecturers teaching business analytics" in question_lower
    or "lecturers who teach business analytics" in question_lower
):

        lecturers = get_lecturers_teaching_business_analytics()
        print("\n========== FLASK: LECTURERS TEACHING BUSINESS ANALYTICS ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# STUDENTS MAJORING IN A SPECIFIC MAJOR
# ========================================================

    if (
        "which students are majoring in" in question_lower
        or "which students major in" in question_lower
        or "who is majoring in" in question_lower
        or "who majors in" in question_lower
    ):

        match = re.search(
        r"(?:which students are majoring in|which students major in|who is majoring in|who majors in)\s+(.+?)\??$",
        question_lower
    )

        if match:

            major_name = match.group(1).strip()

        # Find the actual major name from the ontology
            major_name = " ".join(
            word.capitalize()
            for word in major_name.split()
        )

            students = answer_students_majoring_in(major_name)

            print("\n========== FLASK: STUDENTS MAJORING IN ==========")

            print("Major:", major_name)

            print("Students returned:", len(students))

            print("Data:", students)

            return jsonify({
            "answer": students
        })
# ========================================================
# List All Lecturers With Course
# ========================================================

    if (
    "list all lecturers" in question_lower
    or "show all lecturers" in question_lower
    or "all lecturers" in question_lower
    or "list all lecture" in question_lower
    or "show all lecture" in question_lower
    or "list all lecturers with course" in question_lower
    or "show all lecturers with course" in question_lower
    or "all lecturers with course" in question_lower
):

        lecturers = get_all_lecturers()

        print("\n========== FLASK: ALL LECTURERS WITH COURSE ==========")

        print("Lecturers returned:", len(lecturers))

        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
    # ========================================================
# STUDENT COURSES
# ========================================================

    if (
        "what courses does" in question_lower
        and "study" in question_lower
    ):

        match = re.search(
            r"what courses does (.+?) study\??$",
            question_lower
        )

        if match:

            student_name = match.group(1).strip()

            student_name = " ".join(
                word.capitalize()
                for word in student_name.split()
            )

            courses = answer_student_courses(student_name)

            print("\n========== FLASK: STUDENT COURSES ==========")

            print("Student:", student_name)

            print("Courses returned:", len(courses))

            print("Data:", courses)

            return jsonify({
                "answer": courses
            })

    # ========================================================
    # STUDENT COUNT FOR EACH COURSE
    # ========================================================

    if (
        "how many students are each course" in question_lower
        or "how many students in each course" in question_lower
        or "number of students in each course" in question_lower
        or "student count for each course" in question_lower
        or "student count of each course" in question_lower
        or "how many students does each course have" in question_lower
    ):

        courses = answer_student_count_each_course()

        print("\n========== FLASK: STUDENT COUNT EACH COURSE ==========")

        print("Courses returned:", len(courses))

        print("Data:", courses)

        return jsonify({
            "answer": courses
        })


    # ========================================================
    # Semantic Web
    # ========================================================

    if (
        "who studies semantic web" in question_lower
        or "who study semantic web" in question_lower
        or "students studying semantic web" in question_lower
        or "students study semantic web" in question_lower
    ):

        students = answer_students_studying_semantic_web()

        print("\n========== FLASK: SEMANTIC WEB ==========")
        print("Students returned:", len(students))
        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Cloud Computing
    # ========================================================

    if (
        "who studies cloud computing" in question_lower
        or "who study cloud computing" in question_lower
        or "students studying cloud computing" in question_lower
        or "students study cloud computing" in question_lower
    ):

        students = answer_students_studying_cloud_computing()

        print("\n========== FLASK: CLOUD COMPUTING ==========")
        print("Students returned:", len(students))
        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # English
    # ========================================================

    if (
        "who studies english" in question_lower
        or "who study english" in question_lower
        or "students studying english" in question_lower
        or "students study english" in question_lower
    ):

        students = answer_students_studying_english()

        print("\n========== FLASK: ENGLISH ==========")
        print("Students returned:", len(students))
        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Information Theory
    # ========================================================

    if (
        "who studies information theory" in question_lower
        or "who study information theory" in question_lower
        or "students studying information theory" in question_lower
        or "students study information theory" in question_lower
    ):

        students = answer_students_studying_information_theory()

        print("\n========== FLASK: INFORMATION THEORY ==========")
        print("Students returned:", len(students))
        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Machine Learning
    # ========================================================

    if (
        "who studies machine learning" in question_lower
        or "who study machine learning" in question_lower
        or "students studying machine learning" in question_lower
        or "students study machine learning" in question_lower
    ):

        students = answer_students_studying_machine_learning()

        print("\n========== FLASK: MACHINE LEARNING ==========")
        print("Students returned:", len(students))
        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Robotic
    # ========================================================

    if (
        "who studies robotic" in question_lower
        or "who study robotic" in question_lower
        or "students studying robotic" in question_lower
        or "students study robotic" in question_lower
        or "who studies robotics" in question_lower
        or "who study robotics" in question_lower
    ):

        students = answer_students_studying_robotic()

        print("\n========== FLASK: ROBOTIC ==========")
        print("Students returned:", len(students))
        print("Data:", students)

        return jsonify({
            "answer": students
        })
    

    # ========================================================
    # List All Students
    # ========================================================

    if (
        "list all students" in question_lower
        or "show all students" in question_lower
        or "all students" in question_lower
        or "who are the students" in question_lower
    ):

        students = get_all_students()

        print("\n========== FLASK: ALL STUDENTS ==========")
        print("Students returned:", len(students))
        print("Data:", students)

        return jsonify({
        "answer": students
    })

    # ========================================================
    # List All Subjects
    # ========================================================

    if (
    "list all subjects" in question_lower
    or "show all subjects" in question_lower
    or "all subjects" in question_lower
    or "list all courses" in question_lower
    or "show all courses" in question_lower
):

        subjects = get_all_subjects()

        print("\n========== FLASK: ALL SUBJECTS ==========")
        print("Subjects returned:", len(subjects))
        print("Data:", subjects)

        return jsonify({
        "answer": subjects
    })

        # ========================================================
        # List All Departments
        # ========================================================

    if (
    "list all departments" in question_lower
    or "show all departments" in question_lower
    or "all departments" in question_lower
):

        departments = get_all_departments()

        print("\n========== FLASK: ALL DEPARTMENTS ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    })

# ========================================================
# Who teaches Analysis of Algorithms?
# ========================================================

    if (
        "who teaches analysis of algorithms" in question_lower
        or "who teach analysis of algorithms" in question_lower
        or "lecturers teaching analysis of algorithms" in question_lower
        or "lecturers who teach analysis of algorithms" in question_lower
    ):

        lecturers = get_lecturers_teaching_analysis_of_algorithms()

        print("\n========== FLASK: LECTURERS TEACHING ANALYSIS OF ALGORITHMS ==========")
        print("Lecturers returned:", len(lecturers))
        print("Data:", lecturers)

        return jsonify({
            "answer": lecturers
        })


# ========================================================
# List All Lecturers
# ========================================================

#     if (
#     "list all lecturers" in question_lower
#     or "show all lecturers" in question_lower
#     or "all lecturers" in question_lower
#     or "list all lecture" in question_lower
#     or "show all lecture" in question_lower
# ):

#         lecturers = get_all_lecturers()

#         print("\n========== FLASK: ALL LECTURERS ==========")

#         print("Lecturers returned:", len(lecturers))

#         print("Data:", lecturers)

#         return jsonify({
#         "answer": lecturers
#     })

    # ========================================================
    # Question not understood
    # ========================================================

    return jsonify({
        "answer": "Sorry, I do not understand this question yet."
    })


# ============================================================
# Run Flask
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )
