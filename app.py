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
    get_department_of_lecturer,
    get_lecturers_working_in_faculty,
    get_students_taught_by_lecturer,
    get_students_majoring_in_ke_and_enrolled_in_embedded_robotic,
    get_students_majoring_in_and_enrolled_in,
    get_all_majors,
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
# List All Majors
# ========================================================

    if (

        "list all majors" in question_lower

        or "show all majors" in question_lower

        or "all majors" in question_lower

    ):

        majors = get_all_majors()

        print("\n========== FLASK: ALL MAJORS ==========")

        print("Majors returned:", len(majors))

        print("Data:", majors)

        return jsonify({

            "answer": majors

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
# Which department does Daw Mya Thandar belong to?
# ========================================================

    if (
    "which department does daw mya thandar belong to" in question_lower
    or "department does daw mya thandar belong to" in question_lower
    or "daw mya thandar belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Daw Mya Thandar")

        print("\n========== FLASK: DEPARTMENT OF DAW MYA THANDAR ==========")

        print("Departments returned:", len(departments))

        print("Data:", departments)

        return jsonify({
        "answer": departments
    })
# ========================================================
# Which department does Daw Aye Aye Maw belong to?
# ========================================================

    if (
    "which department does daw aye aye maw belong to" in question_lower
    or "department does daw aye aye maw belong to" in question_lower
    or "daw aye aye maw belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Daw Aye Aye Maw")

        print("\n========== FLASK: DEPARTMENT OF DAW AYE AYE MAW ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    })
# ========================================================
# Which department does Dr. Amy Tun belong to?
# ========================================================

    if (
    "which department does dr amy tun belong to" in question_lower
    or "department does dr amy tun belong to" in question_lower
    or "dr amy tun belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Dr. Amy Tun")

        print("\n========== FLASK: DEPARTMENT OF DR. AMY TUN ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    })
# ========================================================
# Which department does Dr. Hsu Myat Mo belong to?
# ========================================================

    if(
    "which department does dr hsu myat mo belong to" in question_lower
    or "department does dr hsu myat mo belong to" in question_lower
    or "dr hsu myat mo belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Dr. Hsu Myat Mo")

        print("\n========== FLASK: DEPARTMENT OF DR. HSU MYAT MO ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    }) 
# ========================================================
# Which department does Dr. Khaing Khaing Wai belong to?
# ========================================================

    if (
    "which department does dr khaing khaing wai belong to" in question_lower
    or "department does dr khaing khaing wai belong to" in question_lower
    or "dr khaing khaing wai belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Dr. Khaing Khaing Wai")

        print("\n========== FLASK: DEPARTMENT OF DR. KHAING KHAING WAI ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    })
# ========================================================
# Which department does Dr. Kyaw Kyaw Khaing belong to?
# ========================================================

    if (
    "which department does dr kyaw kyaw khaing belong to" in question_lower
    or "department does dr kyaw kyaw khaing belong to" in question_lower
    or "dr kyaw kyaw khaing belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Dr. Kyaw Kyaw Khaing")

        print("\n========== FLASK: DEPARTMENT OF DR. KYAW KYAW KHAING ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    }) 
# ========================================================
# Which department does Dr. Moe Moe Hlaing belong to?
# ========================================================

    if (
    "which department does dr moe moe hlaing belong to" in question_lower
    or "department does dr moe moe hlaing belong to" in question_lower
    or "dr moe moe hlaing belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Dr. Moe Moe Hlaing")

        print("\n========== FLASK: DEPARTMENT OF DR. MOE MOE HLAING ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    })
# ========================================================
# Which department does Dr. Tin Tin Htar belong to?
# ========================================================

    if (
    "which department does dr tin tin htar belong to" in question_lower
    or "department does dr tin tin htar belong to" in question_lower
    or "dr tin tin htar belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Dr. Tin Tin Htar")

        print("\n========== FLASK: DEPARTMENT OF DR. TIN TIN HTAR ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    })
# ========================================================
# Which department does Dr. Tin Zar Thaw belong to?
# ========================================================

    if (
    "which department does dr tin zar thaw belong to" in question_lower
    or "department does dr tin zar thaw belong to" in question_lower
    or "dr tin zar thaw belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Dr. Tin Zar Thaw")

        print("\n========== FLASK: DEPARTMENT OF DR. TIN ZAR THAW ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    })
# ========================================================
# Which department does Dr. Win Lelt Lelt Phyu belong to?
# ========================================================

    if (
    "which department does dr win lelt lelt phyu belong to" in question_lower
    or "department does dr win lelt lelt phyu belong to" in question_lower
    or "dr win lelt lelt phyu belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Dr. Win Lelt Lelt Phyu")

        print("\n========== FLASK: DEPARTMENT OF DR. WIN LELT LELT PHYU ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    })
# ========================================================
# Which department does Dr. Yu Yu Than belong to?
# ========================================================

    if (
    "which department does dr yu yu than belong to" in question_lower
    or "department does dr yu yu than belong to" in question_lower
    or "dr yu yu than belong to which department" in question_lower
):

        departments = get_department_of_lecturer("Dr. Yu Yu Than")

        print("\n========== FLASK: DEPARTMENT OF DR. YU YU THAN ==========")
        print("Departments returned:", len(departments))
        print("Data:", departments)

        return jsonify({
        "answer": departments
    })
    # ========================================================
    # Which students are majoring in KE and are currently
    # enrolled in Analysis of Parallel Algorithms?
    # ========================================================

    if (
        "which students are majoring in ke and are currently enrolled in analysis of parallel algorithms" in question_lower
        or "which students are majoring in ke and enrolled in analysis of parallel algorithms" in question_lower
    ):

        students = get_students_majoring_in_and_enrolled_in(
            "Knowledge Engineering",
            "Analysis of Algorithms"
        )

        print(
            "\n========== FLASK: KE STUDENTS ENROLLED IN ANALYSIS OF ALGORITHMS =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })
    # ========================================================
    # Which students are majoring in SE and are currently
    # enrolled in Analysis of Parallel Algorithms?
    # ========================================================

    if (
        "which students are majoring in se and are currently enrolled in analysis of parallel algorithms" in question_lower
        or "which students are majoring in se and enrolled in analysis of parallel algorithms" in question_lower
    ):

        students = get_students_majoring_in_and_enrolled_in(
            "Software Engineering",
            "Analysis of Algorithms"
        )

        print(
            "\n========== FLASK: SE STUDENTS ENROLLED IN ANALYSIS OF ALGORITHMS =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })
    # ========================================================
    # Which students are majoring in SE and are currently
    # enrolled in Comprehensive Web Application Design?
    # ========================================================

    if (
        "which students are majoring in se and are currently enrolled in comprehensive web application design" in question_lower
        or "which students are majoring in se and enrolled in comprehensive web application design" in question_lower
    ):

        students = get_students_majoring_in_and_enrolled_in(
            "Software Engineering",
            "Comprehensive Web Application Design"
        )

        print(
            "\n========== FLASK: SE STUDENTS ENROLLED IN WEB DESIGN =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })
    # ========================================================
    # Which students are majoring in BIS and are currently
    # enrolled in Analysis of Parallel Algorithms?
    # ========================================================

    if (
        "which students are majoring in bis and are currently enrolled in analysis of parallel algorithms" in question_lower
        or "which students are majoring in bis and enrolled in analysis of parallel algorithms" in question_lower
    ):

        students = get_students_majoring_in_and_enrolled_in(
            "Business Information Systems",
            "Analysis of Algorithms"
        )

        print(
            "\n========== FLASK: BIS STUDENTS ENROLLED IN ANALYSIS OF ALGORITHMS =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })
    # ========================================================
    # Which students are majoring in BIS and are currently
    # enrolled in Comprehensive Web Application Design?
    # ========================================================

    if (
        "which students are majoring in bis and are currently enrolled in comprehensive web application design" in question_lower
        or "which students are majoring in bis and enrolled in comprehensive web application design" in question_lower
    ):

        students = get_students_majoring_in_and_enrolled_in(
            "Business Information Systems",
            "Comprehensive Web Application Design"
        )

        print(
            "\n========== FLASK: BIS STUDENTS ENROLLED IN WEB DESIGN =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })
# ========================================================
# Who are the lecturers working in the Faculty of Computer Science?
# ========================================================

    if (
    "who are the lecturers working in the faculty of computer science" in question_lower
    or "who are the lecturers working in faculty of computer science" in question_lower
    or "lecturers working in the faculty of computer science" in question_lower
    or "lecturers in the faculty of computer science" in question_lower
):

        lecturers = get_lecturers_working_in_faculty(
        "Faculty of Computer Science"
    )

        print(
        "\n========== FLASK: LECTURERS WORKING IN FACULTY OF COMPUTER SCIENCE =========="
    )

        print("Lecturers returned:", len(lecturers))

        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# Who are the lecturers working in the Faculty of Information Science?
# ========================================================

    if (
    "who are the lecturers working in the faculty of information science" in question_lower
    or "who are the lecturers working in faculty of information science" in question_lower
    or "lecturers working in the faculty of information science" in question_lower
    or "lecturers in the faculty of information science" in question_lower
):

        lecturers = get_lecturers_working_in_faculty(
        "Faculty of Information Science"
    )

        print(
        "\n========== FLASK: LECTURERS WORKING IN FACULTY OF INFORMATION SCIENCE =========="
    )

        print("Lecturers returned:", len(lecturers))

        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })


# ========================================================
# Who are the lecturers working in the Faculty of Computer Systems and Technologies?
# ========================================================

    if (
    "who are the lecturers working in the faculty of computer systems and technologies" in question_lower
    or "who are the lecturers working in faculty of computer systems and technologies" in question_lower
    or "lecturers working in the faculty of computer systems and technologies" in question_lower
    or "lecturers in the faculty of computer systems and technologies" in question_lower
):

        lecturers = get_lecturers_working_in_faculty(
        "Faculty of Computer Systems and Technologies"
    )

        print(
        "\n========== FLASK: LECTURERS WORKING IN FACULTY OF COMPUTER SYSTEMS AND TECHNOLOGIES =========="
    )

        print("Lecturers returned:", len(lecturers))

        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
    })
# ========================================================
# Who are the lecturers working in the Department of English?
# ========================================================

    if (
    "who are the lecturers working in the department of english" in question_lower
    or "who are the lecturers working in department of english" in question_lower
    or "lecturers working in the department of english" in question_lower
    or "lecturers in the department of english" in question_lower
):

        lecturers = get_lecturers_working_in_faculty(
        "Department of English"
    )

        print(
        "\n========== FLASK: LECTURERS WORKING IN DEPARTMENT OF ENGLISH =========="
    )

        print("Lecturers returned:", len(lecturers))

        print("Data:", lecturers)

        return jsonify({
        "answer": lecturers
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
# Which students are taught by Daw Mya Thandar?
# ========================================================

    if (
    "which students are taught by daw mya thandar" in question_lower
    or "students taught by daw mya thandar" in question_lower
):

        students = get_students_taught_by_lecturer(
        "Daw Mya Thandar"
    )

        print(
        "\n========== FLASK: STUDENTS TAUGHT BY DAW MYA THANDAR =========="
    )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


# ========================================================
# Which students are taught by Dr. Moe Moe Hlaing?
# ========================================================

    if (
        "which students are taught by dr. moe moe hlaing" in question_lower
        or "students taught by dr. moe moe hlaing" in question_lower
    ):

        students = get_students_taught_by_lecturer(
            "Dr. Moe Moe Hlaing"
        )

        print(
            "\n========== FLASK: STUDENTS TAUGHT BY DR. MOE MOE HLAING =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


# ========================================================
# Which students are taught by Dr. Kyaw Kyaw Khaing?
# ========================================================

    if (
        "which students are taught by dr. kyaw kyaw khaing" in question_lower
        or "students taught by dr. kyaw kyaw khaing" in question_lower
    ):

        students = get_students_taught_by_lecturer(
            "Dr. Kyaw Kyaw Khaing"
        )

        print(
            "\n========== FLASK: STUDENTS TAUGHT BY DR. KYAW KYAW KHAING =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Which students are taught by Dr. Win Lelt Lelt Phyu?
    # ========================================================

    if (
        "which students are taught by dr. win lelt lelt phyu" in question_lower
        or "students taught by dr. win lelt lelt phyu" in question_lower
    ):

        students = get_students_taught_by_lecturer(
            "Dr. Win Lelt Lelt Phyu"
        )

        print(
            "\n========== FLASK: STUDENTS TAUGHT BY DR. WIN LELT LELT PHYU =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Which students are taught by Dr. Tin Zar Thaw?
    # ========================================================

    if (
        "which students are taught by dr. tin zar thaw" in question_lower
        or "students taught by dr. tin zar thaw" in question_lower
    ):

        students = get_students_taught_by_lecturer(
            "Dr. Tin Zar Thaw"
        )

        print(
            "\n========== FLASK: STUDENTS TAUGHT BY DR. TIN ZAR THAW =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Which students are taught by Daw Aye Aye Maw?
    # ========================================================

    if (
        "which students are taught by daw aye aye maw" in question_lower
        or "students taught by daw aye aye maw" in question_lower
    ):

        students = get_students_taught_by_lecturer(
            "Daw Aye Aye Maw"
        )

        print(
            "\n========== FLASK: STUDENTS TAUGHT BY DAW AYE AYE MAW =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Which students are taught by Dr. Amy Tun?
    # ========================================================

    if (
        "which students are taught by dr. amy tun" in question_lower
        or "students taught by dr. amy tun" in question_lower
    ):

        students = get_students_taught_by_lecturer(
            "Dr. Amy Tun"
        )

        print(
            "\n========== FLASK: STUDENTS TAUGHT BY DR. AMY TUN =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Which students are taught by Dr. Hsu Myat Mo?
    # ========================================================

    if (
        "which students are taught by dr. hsu myat mo" in question_lower
        or "students taught by dr. hsu myat mo" in question_lower
    ):

        students = get_students_taught_by_lecturer(
            "Dr. Hsu Myat Mo"
        )

        print(
            "\n========== FLASK: STUDENTS TAUGHT BY DR. HSU MYAT MO =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Which students are taught by Dr. Tin Tin Htar?
    # ========================================================

    if (
        "which students are taught by dr. tin tin htar" in question_lower
        or "students taught by dr. tin tin htar" in question_lower
    ):

        students = get_students_taught_by_lecturer(
            "Dr. Tin Tin Htar"
        )

        print(
            "\n========== FLASK: STUDENTS TAUGHT BY DR. TIN TIN HTAR =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Which students are taught by Dr. Yu Yu Than?
    # ========================================================

    if (
        "which students are taught by dr. yu yu than" in question_lower
        or "students taught by dr. yu yu than" in question_lower
    ):

        students = get_students_taught_by_lecturer(
            "Dr. Yu Yu Than"
        )

        print(
            "\n========== FLASK: STUDENTS TAUGHT BY DR. YU YU THAN =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })


    # ========================================================
    # Which students are taught by Dr. Khaing Khaing Wai?
    # ========================================================

    if(
        "which students are taught by dr. khaing khaing wai" in question_lower
        or "students taught by dr. khaing khaing wai" in question_lower
    ):

            students = get_students_taught_by_lecturer(
            "Dr. Khaing Khaing Wai"
        )

            print(
            "\n========== FLASK: STUDENTS TAUGHT BY DR. KHAING KHAING WAI =========="
        )

            print("Students returned:", len(students))

            print("Data:", students)

            return jsonify({
            "answer": students
        })
    # ========================================================
    # Which students are majoring in KE and are currently enrolled in Embedded Robotic System?
    # ========================================================

    if (
        "which students are majoring in ke and are currently enrolled in embedded robotic system" in question_lower
        or "which students are majoring in ke and enrolled in embedded robotic system" in question_lower
        or "students majoring in ke and enrolled in embedded robotic system" in question_lower
    ):

        students = get_students_majoring_in_ke_and_enrolled_in_embedded_robotic()

        print(
            "\n========== FLASK: KE STUDENTS ENROLLED IN EMBEDDED ROBOTIC SYSTEM =========="
        )

        print("Students returned:", len(students))

        print("Data:", students)

        return jsonify({
            "answer": students
        })
    # ========================================================
    # Who teaches Comprehensive Web Design?
    # ========================================================

    if(
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

    if(
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

    if(
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

    if(
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

    if(
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

    if(
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
