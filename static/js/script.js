// ============================================================
// UniSemantic QA - Frontend JavaScript
// ============================================================


// ============================================================
// Global Student Table Data
// ============================================================

let currentStudents = [];
let currentCourse = "";

let currentPage = 1;

const studentsPerPage = 10;


// ============================================================
// Ask Question
// ============================================================

async function askQuestion() {

    const questionInput =
        document.getElementById("question");

    const answerDiv =
        document.getElementById("answer");

    const question =
        questionInput.value.trim();


    // --------------------------------------------------------
    // Validate
    // --------------------------------------------------------

    if (!question) {

        answerDiv.style.display = "block";

        answerDiv.innerHTML = `
            <div class="error-message">

                <i class="fa-solid fa-circle-exclamation"></i>

                Please enter a question.

            </div>
        `;

        questionInput.focus();

        return;
    }


    // --------------------------------------------------------
    // Show loading
    // --------------------------------------------------------

    answerDiv.style.display = "block";

    answerDiv.innerHTML = `
        <div class="loading-message">

            <i class="fa-solid fa-spinner fa-spin"></i>

            <span>
                Searching the university ontology...
            </span>

        </div>
    `;


    try {

        // ----------------------------------------------------
        // Send question to Flask
        // ----------------------------------------------------

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        });


        // ----------------------------------------------------
        // Check response
        // ----------------------------------------------------

        if (!response.ok) {

            throw new Error(
                `Server error: ${response.status}`
            );
        }


        // ----------------------------------------------------
        // JSON
        // ----------------------------------------------------

        const data =
            await response.json();


        console.log(
            "Backend response:",
            data
        );


        // ----------------------------------------------------
        // Get answer
        // ----------------------------------------------------

        let answer =
            data.answer;


        if (
            answer === undefined ||
            answer === null
        ) {

            answer =
                data.result;
        }


        if (
            answer === undefined ||
            answer === null
        ) {

            answer =
                data.message;
        }


        // ----------------------------------------------------
        // No answer
        // ----------------------------------------------------

        if (
            answer === undefined ||
            answer === null ||
            answer === ""
        ) {

            answerDiv.innerHTML = `

                <div class="error-message">

                    <i class="fa-solid fa-circle-exclamation"></i>

                    No answer was returned from the server.

                </div>

            `;

            return;
        }


        // ====================================================
        // STRUCTURED ARRAY
        // ====================================================

        if (Array.isArray(answer)) {

            /*
             * If backend returns:
             *
             * [
             *   {
             *      studentName: "...",
             *      studentID: "...",
             *      email: "...",
             *      majorName: "..."
             *   }
             * ]
             */

            if (
                answer.length > 0 &&
                typeof answer[0] === "object" &&
                answer[0] !== null
            ) {

                // Detect student result
                const first =
                    answer[0];


                if (
                    "studentID" in first ||
                    "studentId" in first ||
                    "studentName" in first ||
                    "name" in first
                ) {

                    answerDiv.innerHTML =
                        createStudentTableFromData(
                            answer
                        );

                    return;
                }


                // Other structured result
                answerDiv.innerHTML =
                    createGenericTable(answer);

                return;
            }


            // Array of simple values
            answerDiv.innerHTML =
                createTableFromArray(answer);

            return;
        }


        // ====================================================
        // OBJECT
        // ====================================================

        if (
            typeof answer === "object" &&
            answer !== null
        ) {

            answerDiv.innerHTML =
                createGenericTable([answer]);

            return;
        }


        // ====================================================
        // STRING
        // ====================================================

        answer =
            String(answer);


        if (
            isStudentAnswer(answer)
        ) {

            answerDiv.innerHTML =
                formatStudentAnswer(answer);

        }
        else {

            answerDiv.innerHTML =
                formatNormalAnswer(answer);
        }

    }


    catch (error) {

        console.error(
            "UniSemantic QA Error:",
            error
        );


        answerDiv.style.display = "block";


        answerDiv.innerHTML = `

            <div class="error-message">

                <i class="fa-solid fa-triangle-exclamation"></i>

                <strong>
                    Unable to process the question.
                </strong>

                <br>

                <span>
                    Please check that the Flask server
                    and Fuseki server are running.
                </span>

            </div>

        `;
    }
}



// ============================================================
// Detect Student Text Answer
// ============================================================

function isStudentAnswer(text) {

    return (
        /\(ID:\s*[^)]+\)/i.test(text) &&
        /study/i.test(text)
    );
}



// ============================================================
// Old Student Text Format
// ============================================================
//
// Example:
//
// A Mi Mi Kyaw (ID: 6CS-11),
// Aung Kaung San (ID: 6CS-18) study Programming.
//
// ============================================================

function formatStudentAnswer(text) {

    let course = "Unknown";


    // --------------------------------------------------------
    // Get course
    // --------------------------------------------------------

    const courseMatch =
        text.match(
            /study\s+(.+?)\.$/i
        );


    if (courseMatch) {

        course =
            courseMatch[1].trim();
    }


    // --------------------------------------------------------
    // Remove course sentence
    // --------------------------------------------------------

    let studentText =
        text.replace(
            /\s+study\s+.+?\.$/i,
            ""
        );


    // --------------------------------------------------------
    // Split students
    // --------------------------------------------------------

    let students =
        studentText.split(/,\s*/);


    // --------------------------------------------------------
    // Remove "and"
    // --------------------------------------------------------

    students =
        students.map(
            function(student) {

                return student
                    .trim()
                    .replace(
                        /^and\s+/i,
                        ""
                    );

            }
        );


    // --------------------------------------------------------
    // Remove empty
    // --------------------------------------------------------

    students =
        students.filter(
            function(student) {

                return student.length > 0;

            }
        );


    // --------------------------------------------------------
    // Create students
    // --------------------------------------------------------

    const uniqueStudents = [];

    const seen =
        new Set();


    students.forEach(
        function(student) {

            const match =
                student.match(
                    /^(.+?)\s*\(ID:\s*([^)]+)\)$/i
                );


            if (!match) {

                return;
            }


            const name =
                match[1].trim();


            const id =
                match[2].trim();


            const key =
                name.toLowerCase() +
                "|" +
                id.toLowerCase();


            if (seen.has(key)) {

                return;
            }


            seen.add(key);


            uniqueStudents.push({

                name: name,

                id: id,

                email: "-",

                majorName: "-",

                course: course

            });

        }
    );


    return createStudentTable(
        uniqueStudents,
        course
    );
}



// ============================================================
// Convert Structured Student Data
// ============================================================
//
// This accepts BOTH:
//
// studentName
// studentID
// email
// majorName
//
// and:
//
// name
// studentID
// email
// majorName
//
// ============================================================

function createStudentTableFromData(data) {

    const students = [];


    data.forEach(
        function(item) {

            // ------------------------------------------------
            // Student ID
            // ------------------------------------------------

            const studentID =
                item.studentID ??
                item.studentId ??
                item.id ??
                "-";


            // ------------------------------------------------
            // Student Name
            // ------------------------------------------------

            const name =
                item.studentName ??
                item.name ??
                "-";


            // ------------------------------------------------
            // Email
            // ------------------------------------------------

            const email =
                item.email ??
                "-";


            // ------------------------------------------------
            // Major
            // ------------------------------------------------

            const majorName =
                item.majorName ??
                item.major ??
                "-";


            // ------------------------------------------------
            // Course
            // ------------------------------------------------

            const course =
                item.course ??
                currentCourse ??
                "";


            students.push({

                id:
                    String(studentID),

                name:
                    String(name),

                email:
                    String(email),

                majorName:
                    String(majorName),

                course:
                    String(course)

            });

        }
    );


    return createStudentTable(
        students,
        currentCourse
    );
}



// ============================================================
// Create Student Table
// ============================================================

function createStudentTable(
    students,
    course
) {

    currentStudents =
        students;

    currentCourse =
        course;

    currentPage = 1;


    return renderStudentTable();
}



// ============================================================
// Render Student Table
// ============================================================

function renderStudentTable() {

    const students =
        currentStudents;


    const course =
        currentCourse;


    // --------------------------------------------------------
    // No students
    // --------------------------------------------------------

    if (
        !students ||
        students.length === 0
    ) {

        return `

            <div class="answer-container">

                <div class="error-message">

                    <i class="fa-solid fa-circle-info"></i>

                    No students were found.

                </div>

            </div>

        `;
    }


    // --------------------------------------------------------
    // Total
    // --------------------------------------------------------

    const totalStudents =
        students.length;


    const totalPages =
        Math.ceil(
            totalStudents /
            studentsPerPage
        );


    // --------------------------------------------------------
    // Validate page
    // --------------------------------------------------------

    if (currentPage < 1) {

        currentPage = 1;
    }


    if (currentPage > totalPages) {

        currentPage = totalPages;
    }


    // --------------------------------------------------------
    // Current page data
    // --------------------------------------------------------

    const startIndex =
        (currentPage - 1) *
        studentsPerPage;


    const endIndex =
        Math.min(
            startIndex +
            studentsPerPage,
            totalStudents
        );


    const pageStudents =
        students.slice(
            startIndex,
            endIndex
        );


    // --------------------------------------------------------
    // Rows
    // --------------------------------------------------------

    let rows = "";


    pageStudents.forEach(
        function(student, index) {

            const actualNumber =
                startIndex +
                index +
                1;


            rows += `

                <tr>

                    <!-- No. -->

                    <td class="result-number">

                        ${actualNumber}

                    </td>


                    <!-- Student ID -->

                    <td class="student-id">

                        ${escapeHTML(
                            student.id ?? "-"
                        )}

                    </td>


                    <!-- Student Name -->

                    <td class="student-name">

                        ${escapeHTML(
                            student.name ?? "-"
                        )}

                    </td>


                    <!-- Email -->

                    <td class="student-email">

                        ${escapeHTML(
                            student.email ?? "-"
                        )}

                    </td>


                    <!-- Major -->

                    <td class="student-major">

                        ${escapeHTML(
                            student.majorName ?? "-"
                        )}

                    </td>

                </tr>

            `;

        }
    );


    // --------------------------------------------------------
    // Pagination
    // --------------------------------------------------------

    let paginationHTML = "";


    if (totalPages > 1) {

        paginationHTML =
            createPagination(
                currentPage,
                totalPages
            );
    }


    // --------------------------------------------------------
    // Complete table
    // --------------------------------------------------------

    return `

        <div class="answer-container">


            <div class="answer-title">

                <h3>

                    <i class="fa-solid fa-users"></i>

                    Students Studying
                    ${course
                        ? escapeHTML(course)
                        : ""
                    }

                </h3>


                <span class="answer-count">

                    ${totalStudents} Students

                </span>

            </div>



            <div class="table-wrapper">

                <table class="result-table">


                    <thead>

                        <tr>

                            <th class="result-number">

                                No.

                            </th>


                            <th>

                                Student ID

                            </th>


                            <th>

                                Student Name

                            </th>


                            <th>

                                Email

                            </th>


                            <th>

                                Major

                            </th>

                        </tr>

                    </thead>


                    <tbody>

                        ${rows}

                    </tbody>


                </table>

            </div>


            ${paginationHTML}


        </div>

    `;
}



// ============================================================
// Pagination
// ============================================================

function createPagination(
    page,
    totalPages
) {

    let buttons = "";


    // --------------------------------------------------------
    // Previous
    // --------------------------------------------------------

    buttons += `

        <button

            class="pagination-button"

            onclick="changeStudentPage(${page - 1})"

            ${page === 1
                ? "disabled"
                : ""
            }>

            <i class="fa-solid fa-chevron-left"></i>

            Previous

        </button>

    `;


    // --------------------------------------------------------
    // Page numbers
    // --------------------------------------------------------

    for (
        let i = 1;
        i <= totalPages;
        i++
    ) {

        buttons += `

            <button

                class="pagination-number
                ${i === page
                    ? "active"
                    : ""
                }"

                onclick="changeStudentPage(${i})">

                ${i}

            </button>

        `;
    }


    // --------------------------------------------------------
    // Next
    // --------------------------------------------------------

    buttons += `

        <button

            class="pagination-button"

            onclick="changeStudentPage(${page + 1})"

            ${page === totalPages
                ? "disabled"
                : ""
            }>

            Next

            <i class="fa-solid fa-chevron-right"></i>

        </button>

    `;


    return `

        <div class="pagination-container">


            <div class="pagination-info">

                Showing

                <strong>

                    ${(page - 1) *
                    studentsPerPage + 1}

                </strong>

                -

                <strong>

                    ${Math.min(
                        page *
                        studentsPerPage,
                        currentStudents.length
                    )}

                </strong>

                of

                <strong>

                    ${currentStudents.length}

                </strong>

                students

            </div>


            <div class="pagination-buttons">

                ${buttons}

            </div>


        </div>

    `;
}



// ============================================================
// Change Page
// ============================================================

function changeStudentPage(page) {

    const totalPages =
        Math.ceil(
            currentStudents.length /
            studentsPerPage
        );


    if (
        page < 1 ||
        page > totalPages
    ) {

        return;
    }


    currentPage =
        page;


    const answerDiv =
        document.getElementById(
            "answer"
        );


    answerDiv.innerHTML =
        renderStudentTable();


    answerDiv.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}



// ============================================================
// Generic Array Table
// ============================================================

function createTableFromArray(data) {

    if (
        !data ||
        data.length === 0
    ) {

        return `

            <div class="error-message">

                <i class="fa-solid fa-circle-info"></i>

                No results found.

            </div>

        `;
    }


    // --------------------------------------------------------
    // Object array
    // --------------------------------------------------------

    if (
        typeof data[0] === "object" &&
        data[0] !== null
    ) {

        return createGenericTable(data);
    }


    // --------------------------------------------------------
    // Simple array
    // --------------------------------------------------------

    let rows = "";


    data.forEach(
        function(item, index) {

            rows += `

                <tr>

                    <td class="result-number">

                        ${index + 1}

                    </td>


                    <td>

                        ${escapeHTML(
                            String(item)
                        )}

                    </td>

                </tr>

            `;

        }
    );


    return `

        <div class="answer-container">


            <div class="answer-title">

                <h3>

                    <i class="fa-solid fa-list"></i>

                    Results

                </h3>


                <span class="answer-count">

                    ${data.length} Results

                </span>

            </div>


            <div class="table-wrapper">

                <table class="result-table">


                    <thead>

                        <tr>

                            <th>

                                No.

                            </th>

                            <th>

                                Result

                            </th>

                        </tr>

                    </thead>


                    <tbody>

                        ${rows}

                    </tbody>


                </table>

            </div>


        </div>

    `;
}



// ============================================================
// Generic Object Table
// ============================================================

function createGenericTable(data) {

    if (
        !data ||
        data.length === 0
    ) {

        return `

            <div class="error-message">

                No results found.

            </div>

        `;
    }


    // --------------------------------------------------------
    // Columns
    // --------------------------------------------------------

    const columns =
        Object.keys(data[0]);


    // --------------------------------------------------------
    // Headers
    // --------------------------------------------------------

    let headers = "";


    columns.forEach(
        function(column) {

            headers += `

                <th>

                    ${formatColumnName(
                        column
                    )}

                </th>

            `;

        }
    );


    // --------------------------------------------------------
    // Rows
    // --------------------------------------------------------

    let rows = "";


    data.forEach(
        function(item) {

            rows += "<tr>";


            columns.forEach(
                function(column) {

                    let value =
                        item[column];


                    if (
                        value === null ||
                        value === undefined
                    ) {

                        value = "";
                    }


                    rows += `

                        <td>

                            ${escapeHTML(
                                String(value)
                            )}

                        </td>

                    `;

                }
            );


            rows += "</tr>";

        }
    );


    return `

        <div class="answer-container">


            <div class="answer-title">

                <h3>

                    <i class="fa-solid fa-table"></i>

                    Query Results

                </h3>


                <span class="answer-count">

                    ${data.length} Results

                </span>

            </div>


            <div class="table-wrapper">

                <table class="result-table">


                    <thead>

                        <tr>

                            ${headers}

                        </tr>

                    </thead>


                    <tbody>

                        ${rows}

                    </tbody>


                </table>

            </div>


        </div>

    `;
}



// ============================================================
// Format Column Name
// ============================================================

function formatColumnName(column) {

    return column

        .replace(
            /_/g,
            " "
        )

        .replace(
            /([A-Z])/g,
            " $1"
        )

        .replace(
            /\b\w/g,
            function(letter) {

                return letter.toUpperCase();

            }
        );
}



// ============================================================
// Normal Answer
// ============================================================

function formatNormalAnswer(text) {

    let safeText =
        escapeHTML(text);


    safeText =
        safeText.replace(
            /\n/g,
            "<br>"
        );


    return `

        <div class="answer-container">


            <div class="answer-title">

                <h3>

                    <i class="fa-solid fa-circle-check"></i>

                    Answer

                </h3>

            </div>


            <div class="normal-answer">

                ${safeText}

            </div>


        </div>

    `;
}



// ============================================================
// Escape HTML
// ============================================================

function escapeHTML(value) {

    return String(value)

        .replace(
            /&/g,
            "&amp;"
        )

        .replace(
            /</g,
            "&lt;"
        )

        .replace(
            />/g,
            "&gt;"
        )

        .replace(
            /"/g,
            "&quot;"
        )

        .replace(
            /'/g,
            "&#039;"
        );
}



// ============================================================
// Example Question
// ============================================================

function setQuestion(question) {

    const questionInput =
        document.getElementById(
            "question"
        );


    questionInput.value =
        question;


    questionInput.focus();
}



// ============================================================
// Enter Key
// ============================================================

document.addEventListener(
    "DOMContentLoaded",
    function() {

        const questionInput =
            document.getElementById(
                "question"
            );


        if (!questionInput) {

            return;
        }


        questionInput.addEventListener(
            "keydown",
            function(event) {

                if (
                    event.key === "Enter"
                ) {

                    event.preventDefault();

                    askQuestion();

                }

            }
        );

    }
);