# ============================================================
# services/sparql_queries.py
# ============================================================

PREFIX = """
PREFIX unisemantic: <http://example.org/unisemantic#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
"""


# ============================================================
# ALL STUDENTS
# ============================================================

def all_students():

    return PREFIX + """
    SELECT DISTINCT
        ?studentID
        ?name
        ?email
        ?majorName

    WHERE {

        ?student rdf:type unisemantic:Students ;
                 unisemantic:hasStudentID ?studentID ;
                 unisemantic:hasName ?name ;
                 unisemantic:hasEmail ?email ;
                 unisemantic:specificMajor ?major .

        ?major unisemantic:hasName ?majorName .
    }

    ORDER BY ?studentID
    """
# ============================================================
# ALL SUBJECTS / COURSES
# ============================================================

def all_subjects():

    return PREFIX + """
    SELECT DISTINCT
        ?courseCode
        ?courseName
        ?description

    WHERE {

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasCourseCode ?courseCode ;
                unisemantic:hasName ?courseName ;
                unisemantic:hasDescription ?description .
    }

    ORDER BY ?courseName
    """

# ============================================================
# ALL DEPARTMENTS
# ============================================================

def all_departments():

    return PREFIX + """
    SELECT DISTINCT
        ?departmentName

    WHERE {

        ?department rdf:type unisemantic:Departments ;
                    unisemantic:hasName ?departmentName .
    }

    ORDER BY ?departmentName
    """

# ============================================================
# ALL LECTURERS
# ============================================================

def all_lecturers():

    return PREFIX + """
    SELECT DISTINCT
        ?lecturerName
        ?email

    WHERE {

        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email .
    }

    ORDER BY ?lecturerName
    """


# ============================================================
# HELPER FUNCTION
# ============================================================

def students_studying_course(course_name):

    return PREFIX + f"""
    SELECT DISTINCT
        ?studentID
        ?name
        ?email
        ?majorName
        ?courseName

    WHERE {{

        ?student rdf:type unisemantic:Students ;
                 unisemantic:hasStudentID ?studentID ;
                 unisemantic:hasName ?name ;
                 unisemantic:hasEmail ?email ;
                 unisemantic:specificMajor ?major ;
                 unisemantic:enrolledIn ?course .

        ?major unisemantic:hasName ?majorName .

        ?course unisemantic:hasName ?courseName .

        FILTER(
            LCASE(STR(?courseName))
            =
            LCASE("{course_name}")
        )
    }}

    ORDER BY ?studentID
    """


# ============================================================
# SEMANTIC WEB
# ============================================================

def students_studying_semantic_web():

    return students_studying_course("Semantic Web")


# ============================================================
# CLOUD COMPUTING
# ============================================================

def students_studying_cloud_computing():

    return students_studying_course("Cloud Computing")


# ============================================================
# ENGLISH
# ============================================================

def students_studying_english():

    return students_studying_course("English")


# ============================================================
# INFORMATION THEORY
#
# Actual ontology course name:
# "Advanced Information Theory"
# ============================================================

def students_studying_information_theory():

    return students_studying_course("Advanced Information Theory")


# ============================================================
# MACHINE LEARNING
# ============================================================

def students_studying_machine_learning():

    return students_studying_course("Machine Learning")

# ============================================================
# ROBOTIC
#
# Actual ontology course name:
# "Embedded Robotic System"
# ============================================================

def students_studying_robotic():

    return students_studying_course("Embedded Robotic System")

# ============================================================
# STUDENT COUNT FOR EACH COURSE
# ============================================================

def student_count_each_course():

    return PREFIX + """

    SELECT ?courseName (COUNT(DISTINCT ?student) AS ?studentCount)
    WHERE {
        ?student unisemantic:enrolledIn ?course .
        ?course unisemantic:hasName ?courseName .
    }
    GROUP BY ?courseName
    ORDER BY ?courseName

    """

# ============================================================
# STUDENT COURSES
# ============================================================

def student_courses(student_name):

    return PREFIX + f"""

    SELECT ?studentName ?courseName
    WHERE {{
        ?student unisemantic:hasName ?studentName ;
                 unisemantic:enrolledIn ?course .

        ?course unisemantic:hasName ?courseName .

        FILTER(LCASE(STR(?studentName)) = LCASE("{student_name}"))
    }}

    ORDER BY ?courseName

    """