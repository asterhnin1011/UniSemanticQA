from services.fuseki_service import execute_query

from services.sparql_queries import (
    students_studying_semantic_web,
    students_studying_programming
)


def format_student_answer(result, subject):

    students = []

    for item in result["results"]["bindings"]:

        name = item["name"]["value"]
        student_id = item["studentID"]["value"]
        email = item["email"]["value"]
        major = item["majorName"]["value"]

        students.append({
            "name": name,
            "id": student_id,
            "email": email,
            "major": major
        })

    if not students:
        return "No students were found."

    if len(students) == 1:

        student = students[0]

        return (
            f"{student['name']} "
            f"(ID: {student['id']}, "
            f"Email: {student['email']}, "
            f"Major: {student['major']}) "
            f"studies {subject}."
        )

    if len(students) == 2:

        student1 = students[0]
        student2 = students[1]

        return (
            f"{student1['name']} "
            f"(ID: {student1['id']}, "
            f"Email: {student1['email']}, "
            f"Major: {student1['major']}) and "

            f"{student2['name']} "
            f"(ID: {student2['id']}, "
            f"Email: {student2['email']}, "
            f"Major: {student2['major']}) "
            f"study {subject}."
        )

    student_list = ", ".join(
        f"{student['name']} "
        f"(ID: {student['id']}, "
        f"Email: {student['email']}, "
        f"Major: {student['major']})"
        for student in students[:-1]
    )

    last_student = students[-1]

    last_student_text = (
        f"{last_student['name']} "
        f"(ID: {last_student['id']}, "
        f"Email: {last_student['email']}, "
        f"Major: {last_student['major']})"
    )

    return (
        f"{student_list}, and {last_student_text} "
        f"study {subject}."
    )


def answer_students_studying_semantic_web():

    query = students_studying_semantic_web()

    result = execute_query(query)

    return format_student_answer(
        result,
        "Semantic Web"
    )


def answer_students_studying_programming():

    query = students_studying_programming()

    result = execute_query(query)

    return format_student_answer(
        result,
        "Programming"
    )