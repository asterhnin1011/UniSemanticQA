# ============================================================
# app.py
# ============================================================

import re
from flask import Flask, render_template, request, jsonify

from services.question_service import (
  
    get_all_students,
    get_all_subjects,
    get_all_departments,
    get_all_lecturers,
    answer_students_studying_semantic_web,
    answer_students_studying_cloud_computing,
    answer_students_studying_english,
    answer_students_studying_information_theory,
    answer_students_studying_machine_learning,
    answer_students_studying_robotic,
    answer_student_count_each_course,
    answer_student_courses,
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
# List All Lecturers
# ========================================================

    if (
    "list all lecturers" in question_lower
    or "show all lecturers" in question_lower
    or "all lecturers" in question_lower
    or "list all lecture" in question_lower
    or "show all lecture" in question_lower
):

        lecturers = get_all_lecturers()

        print("\n========== FLASK: ALL LECTURERS ==========")
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