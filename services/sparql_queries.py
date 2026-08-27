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
# ALL LECTURERS WITH COURSE
# ============================================================

def all_lecturers():

    return PREFIX + """

    SELECT DISTINCT
        ?lecturerName
        ?email
        ?courseName

    WHERE {

        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course unisemantic:hasName ?courseName .

    }

    ORDER BY ?lecturerName ?courseName

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

# ============================================================
# STUDENTS MAJORING IN A SPECIFIC MAJOR
# ============================================================

def students_majoring_in(major_name):

    return PREFIX + f"""

    SELECT ?studentID ?studentName ?email ?majorName
    WHERE {{
        ?student unisemantic:hasName ?studentName ;
                 unisemantic:hasStudentID ?studentID ;
                 unisemantic:hasEmail ?email ;
                 unisemantic:specificMajor ?major .

        ?major unisemantic:hasName ?majorName .

        FILTER(LCASE(STR(?majorName)) = LCASE("{major_name}"))
    }}

    ORDER BY ?studentName

    """
# ========================================================
# Lecturers teach English
# ========================================================

def lecturers_teaching_english():
    return PREFIX + """
    SELECT DISTINCT ?lecturerName ?courseName ?email
    WHERE {
        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(LCASE(STR(?courseName)) = "english")
    }
    ORDER BY ?lecturerName
    """
# ========================================================
# Lecturers teach Advanced Information Theory
# ========================================================

def lecturers_teaching_advanced_information_theory():
    return PREFIX + """
    SELECT DISTINCT ?lecturerName ?courseName ?email
    WHERE {
        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(LCASE(STR(?courseName)) = "advanced information theory")
    }
    ORDER BY ?lecturerName
    """
# ========================================================
# Lecturers teach Business Analytics
# ========================================================

def lecturers_teaching_business_analytics():
    return PREFIX + """

    SELECT DISTINCT ?lecturerName ?courseName ?email

    WHERE {

        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(LCASE(STR(?courseName)) = "business analytics")
    }

    ORDER BY ?lecturerName

    """
# ========================================================
# Lecturers teach Machine Learning
# ========================================================

def lecturers_teaching_machine_learning():
    return PREFIX + """

    SELECT DISTINCT ?lecturerName ?courseName ?email

    WHERE {

        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(LCASE(STR(?courseName)) = "machine learning")
    }

    ORDER BY ?lecturerName

    """
# ========================================================
# Lecturers teach Analysis of Algorithms
# ========================================================

def lecturers_teaching_analysis_of_algorithms():
    return PREFIX + """

    SELECT DISTINCT ?lecturerName ?courseName ?email

    WHERE {

        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(LCASE(STR(?courseName)) = "analysis of algorithms")

    }

    ORDER BY ?lecturerName

    """
# ========================================================
# Lecturers teach Cloud Computing
# ========================================================

def lecturers_teaching_cloud_computing():
    return PREFIX + """

    SELECT DISTINCT ?lecturerName ?courseName ?email
    WHERE {
        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(LCASE(STR(?courseName)) = "cloud computing")
    }
    ORDER BY ?lecturerName
    """
# ========================================================
# Lecturers teach Semantic Web
# ========================================================

def lecturers_teaching_semantic_web():
    return PREFIX + """

    SELECT DISTINCT ?lecturerName ?courseName ?email
    WHERE {
        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(LCASE(STR(?courseName)) = "semantic web")
    }
    ORDER BY ?lecturerName
    """
# ========================================================
# Lecturers teach Embedded Robotic System
# ========================================================

def lecturers_teaching_embedded_robotic_system():
    return PREFIX + """

    SELECT DISTINCT ?lecturerName ?courseName ?email
    WHERE {
        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(LCASE(STR(?courseName)) = "embedded robotic system")
    }
    ORDER BY ?lecturerName
    """
# ========================================================
# Lecturers teach Deep Learning
# ========================================================

def lecturers_teaching_deep_learning():
    return PREFIX + """

    SELECT DISTINCT ?lecturerName ?courseName ?email

    WHERE {

        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(
            LCASE(STR(?courseName))
            = "resilient dataset and deep learning"
        )
    }

    ORDER BY ?lecturerName

    """
# ========================================================
# Lecturers teach Comprehensive Web Design
# ========================================================

def lecturers_teaching_comprehensive_web_design():
    return PREFIX + """

    SELECT DISTINCT ?lecturerName ?courseName ?email

    WHERE {

        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(
            LCASE(STR(?courseName))
            = "comprehensive web application design"
        )
    }

    ORDER BY ?lecturerName

    """
# ========================================================
# Lecturers teach Business System Infrastructure and Security
# ========================================================

def lecturers_teaching_business_system_infrastructure_and_security():
    return PREFIX + """

    SELECT DISTINCT ?lecturerName ?courseName ?email
    WHERE {
        ?lecturer rdf:type unisemantic:Lecturers ;
                  unisemantic:hasName ?lecturerName ;
                  unisemantic:hasEmail ?email ;
                  unisemantic:teaches ?course .

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName .

        FILTER(
            LCASE(STR(?courseName))
            = "business system infrastructure and security"
        )
    }
    ORDER BY ?lecturerName
    """
# ========================================================
# Course Code by Course Name
# ========================================================

def course_code_by_name(course_name):

    return PREFIX + f"""
    SELECT DISTINCT ?courseName ?courseCode

    WHERE {{

        ?course rdf:type unisemantic:Courses ;
                unisemantic:hasName ?courseName ;
                unisemantic:hasCourseCode ?courseCode .

        FILTER(
            LCASE(STR(?courseName))
            = "{course_name.lower()}"
        )

    }}

    ORDER BY ?courseName
    """
