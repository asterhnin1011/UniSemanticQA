# Ontology-Based University Course Recommendation System Using RDF and SPARQL

## 📚 UniSemanticQA

**UniSemanticQA** is an ontology-based university course recommendation and question-answering system that uses **RDF, OWL, SPARQL, and semantic technologies** to represent and query university academic information.

The system allows users to ask natural-language questions about students, courses, majors, departments, lecturers, and other university-related information. User questions are interpreted by the application and converted into appropriate **SPARQL queries** that retrieve information from the university knowledge graph.

---

## 🎯 Project Objective

The main objective of this project is to develop a semantic university information system that can:

* Represent university information using an ontology.
* Store academic information as RDF triples.
* Query university data using SPARQL.
* Answer natural-language questions about university information.
* Identify students studying particular courses.
* Determine the courses studied by a particular student.
* Count the number of students enrolled in each course.
* Retrieve information about students, courses, departments, majors, and lecturers.
* Provide a foundation for ontology-based course recommendation.

---

## 🧠 System Concept

The system is based on a university knowledge graph containing entities such as:

```text
University
   │
   ├── Students
   │     ├── Student ID
   │     ├── Name
   │     ├── Email
   │     └── Major
   │
   ├── Courses
   │     ├── Course Name
   │     ├── Course Code
   │     └── Students
   │
   ├── Departments
   │
   ├── Majors
   │
   └── Lecturers
```

Relationships between these entities are represented using an ontology and RDF properties.

---

## 🔍 Example Questions

The system can answer questions such as:

### Student-related questions

* Who studies Semantic Web?
* Who studies Robotics?
* List all students.
* What courses does (name) study?

### Course-related questions

* List all courses.
* How many students are in each course?
* Which students study Semantic Web?

### University information

* List all departments.
* List all lecturers.
* List all courses.
* List all subjects.

The person name and course name are treated as query variables where appropriate, allowing different students and courses to be queried dynamically.

---

## 🏗️ System Architecture

```text
                 ┌───────────────────────┐
                 │       User            │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │    Web Interface      │
                 │   HTML / JavaScript   │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │      Flask App        │
                 │       app.py          │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Question Processing   │
                 │ question_service.py   │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   SPARQL Queries      │
                 │ sparql_queries.py     │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │ Apache Jena Fuseki    │
                 │   RDF Knowledge Base  │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   SPARQL Results      │
                 └───────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology         | Purpose                   |
| ------------------ | ------------------------- |
| Python             | Backend application       |
| Flask              | Web application framework |
| RDF                | Knowledge representation  |
| OWL                | Ontology development      |
| SPARQL             | Semantic data querying    |
| Apache Jena Fuseki | RDF/SPARQL server         |
| Protégé            | Ontology development      |
| HTML               | Web interface             |
| CSS                | User interface styling    |
| JavaScript         | Frontend interaction      |
| Git                | Version control           |
| GitHub             | Source code repository    |

---

## 📂 Project Structure

```text
UniSemanticQA/
│
├── app.py
│
├── services/
│   ├── question_service.py
│   └── sparql_queries.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
├── ontology/
│   └── university ontology files
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🧩 Ontology

The ontology defines the concepts and relationships used to represent university information.

Example classes include:

```text
Students
Courses
Departments
Lecturers
University
```

Example relationships include:

```text
hasName
hasStudentID
hasEmail
specificMajor
studiesCourse
belongsToDepartment
teaches
```

The ontology is developed using **Protégé** and can be stored and queried using RDF/SPARQL technologies.

---

## 🔎 SPARQL Example

An example query for retrieving courses is:

```sparql
PREFIX unisemantic: <http://example.org/unisemantic#>

SELECT ?course ?courseName
WHERE {
    ?course unisemantic:hasName ?courseName .
}
ORDER BY ?courseName
```

An example query for retrieving a student's courses can use the student's name as a variable:

```sparql
PREFIX unisemantic: <http://example.org/unisemantic#>

SELECT ?studentName ?courseName
WHERE {
    ?student unisemantic:hasName ?studentName .
    ?student unisemantic:studiesCourse ?course .
    ?course unisemantic:hasName ?courseName .
}
ORDER BY ?studentName ?courseName
```

This approach allows the application to work with different student names rather than using a single hard-coded person.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone git@github.com:asterhnin1011/UniSemanticQA.git
```

```bash
cd UniSemanticQA
```

### 2. Create a Python virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Apache Jena Fuseki

Make sure your Fuseki server and university RDF dataset are running.

The application should be configured to connect to the appropriate Fuseki SPARQL endpoint.

### 5. Run the application

```bash
python app.py
```

Then open the web application in your browser.

---

## 🔮 Future Improvements

Future development may include:

* Natural-language question processing using NLP.
* More flexible student and course entity extraction.
* Automated course recommendation.
* Student interest and skill matching.
* Course prerequisite reasoning.
* Recommendation ranking.
* More advanced SPARQL queries.
* Semantic similarity between courses.
* User authentication.
* Student dashboards.
* Recommendation explanations.
* Integration with larger university datasets.

---

## 👩‍💻 Project

**Project Name:** UniSemanticQA

**Title:** Ontology-Based University Course Recommendation System Using RDF and SPARQL

**Main Technologies:** Python, Flask, Protégé, OWL, RDF, SPARQL, Apache Jena Fuseki

---

## 📄 License

This project is developed for educational and academic purposes.
