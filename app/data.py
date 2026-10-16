"""Small in-memory catalog for the demo. Replace with a persistent database in production."""
COURSES = [
    {
        "id": 1, "title": "Python Foundations", "category": "Development",
        "level": "Beginner", "duration": "6h 20m", "lessons": 12,
        "rating": 4.9, "students": 18420, "color": "violet",
        "description": "Build a confident foundation in Python, from variables to practical functions.",
        "instructor": "Maya Chen", "progress": 72,
        "skills": ["Python syntax", "Functions", "Collections", "Debugging"],
        "modules": [
            {"id": 101, "title": "Getting started with Python", "duration": "18 min", "content": 'Python is a programming language designed to be readable. A Python program is a sequence of instructions that the interpreter runs from top to bottom. You can use Python for automation, websites, data analysis, and many other tasks.', "key_points": ['Python code is organized into statements', 'Indentation groups related instructions', 'Small experiments are the fastest way to learn'], "practice": 'Open a Python shell and print the sentence: I am learning Python.'},
            {"id": 102, "title": "Variables and data types", "duration": "24 min", "content": "A variable gives a name to a value. Common built-in types include int for whole numbers, float for decimals, str for text, and bool for True or False. Use type(value) when you want to inspect a value's type.", "key_points": ['Use descriptive variable names', 'Strings need quotes', 'Convert input when you need a number'], "practice": 'Create variables for your name, age, and whether you enjoy coding.'},
            {"id": 103, "title": "Conditions and loops", "duration": "31 min", "content": 'Conditions let a program choose what to do. An if statement checks a condition, elif checks another condition, and else handles the remaining case. Loops repeat work: for loops iterate over a sequence and while loops continue while a condition is true.', "key_points": ['Conditions evaluate to True or False', 'Indentation defines each branch or loop body', 'Avoid infinite while loops by changing the condition'], "practice": 'Write a loop that prints the numbers from 1 through 5.'},
            {"id": 104, "title": "Functions in practice", "duration": "28 min", "content": 'A function is a reusable block of code. Define it with def, give it a clear name, and pass information through parameters. Use return to send a result back to the caller. Functions make larger programs easier to test and maintain.', "key_points": ['Use def to define a function', 'Parameters are inputs', 'return provides an output'], "practice": 'Write a function called double that returns twice the number it receives.'},
        ],
    },
    {
        "id": 2, "title": "Data Analytics Essentials", "category": "Data",
        "level": "Intermediate", "duration": "8h 10m", "lessons": 18,
        "rating": 4.8, "students": 12680, "color": "blue",
        "description": "Turn messy data into clear insights with practical analysis workflows.",
        "instructor": "Jordan Patel", "progress": 35,
        "skills": ["Data cleaning", "Pandas", "Visualization", "Storytelling"],
        "modules": [
            {"id": 201, "title": "Asking good data questions", "duration": "22 min", "content": 'Good analysis begins with a clear question. Define what you want to learn, identify the data needed, and check whether the data actually measures the thing you care about. A focused question prevents unnecessary charts and calculations.', "key_points": ['Turn broad goals into answerable questions', 'Identify the unit of analysis', 'Check assumptions before interpreting results'], "practice": 'Choose a small dataset and write one question it could answer.'},
            {"id": 202, "title": "Cleaning a dataset", "duration": "36 min", "content": 'Data cleaning makes a dataset more reliable. Inspect missing values, duplicate rows, inconsistent labels, and incorrect data types before analysis. Keep a note of every change so that the work is explainable and repeatable.', "key_points": ['Profile data before editing it', 'Handle missing values deliberately', 'Keep cleaning steps reproducible'], "practice": 'List three data-quality checks you would run before calculating an average.'},
            {"id": 203, "title": "Exploratory analysis", "duration": "41 min", "content": 'Exploratory data analysis helps reveal patterns before formal conclusions. Start with counts and summary statistics, then use suitable charts to inspect distributions, relationships, and unusual values. A pattern is a clue, not proof of cause.', "key_points": ['Summaries reveal scale and spread', 'Choose charts that match the question', 'Investigate outliers before removing them'], "practice": 'Describe which chart you would use to compare values across five categories.'},
        ],
    },
    {
        "id": 3, "title": "Product Design Fundamentals", "category": "Design",
        "level": "Beginner", "duration": "4h 45m", "lessons": 10,
        "rating": 4.7, "students": 9340, "color": "orange",
        "description": "Learn to move from user problem to thoughtful, testable interface ideas.",
        "instructor": "Amara Okafor", "progress": 0,
        "skills": ["User research", "Wireframes", "Prototyping", "Usability"],
        "modules": [
            {"id": 301, "title": "Designing around users", "duration": "20 min", "content": 'Product design starts by understanding people and the context in which they work. Talk to users, observe their current workflow, and describe the problem without jumping immediately to a visual solution.', "key_points": ['Separate observed needs from assumptions', 'Ask open-ended research questions', 'Define the problem in plain language'], "practice": 'Write one user interview question for someone who struggles to plan their week.'},
            {"id": 302, "title": "From sketch to wireframe", "duration": "33 min", "content": "A wireframe is a low-detail plan for a screen. It helps you test information hierarchy, navigation, and task flow before spending time on colors or polished visuals. Label important actions and keep the layout focused on the user's goal.", "key_points": ['Start with structure, not decoration', 'Make primary actions easy to find', 'Test the flow with a simple prototype'], "practice": 'Sketch a three-step flow for a student finding and starting a course.'},
            {"id": 303, "title": "Testing your first prototype", "duration": "29 min", "content": 'Usability testing checks whether people can complete a task with your design. Give a participant a realistic task, observe without leading them, and note where they hesitate or make errors. Use findings to improve the next iteration.', "key_points": ['Test tasks rather than opinions alone', 'Observe behavior without coaching', 'Prioritize issues by impact and frequency'], "practice": 'Write a short task that would test whether a new user can bookmark a course.'},
        ],
    },
    {
        "id": 4, "title": "Cloud & DevOps Starter", "category": "Technology",
        "level": "Intermediate", "duration": "7h 05m", "lessons": 15,
        "rating": 4.9, "students": 15300, "color": "green",
        "description": "Understand delivery pipelines, containers, and cloud-native basics.",
        "instructor": "Ethan Brooks", "progress": 18,
        "skills": ["Containers", "CI/CD", "Cloud concepts", "Monitoring"],
        "modules": [
            {"id": 401, "title": "Modern delivery workflows", "duration": "25 min", "content": 'A delivery workflow moves code from development toward users through repeatable steps such as testing, packaging, review, and deployment. Automation makes these steps consistent and helps teams find problems earlier.', "key_points": ['Keep changes small and reviewable', 'Automate repeatable checks', 'Make failures visible'], "practice": 'Name two checks you would run before merging a code change.'},
            {"id": 402, "title": "Containers explained", "duration": "32 min", "content": 'A container packages an application with the dependencies it needs so it can run consistently across environments. Images are templates; containers are running instances of those images. Containers share the host kernel, unlike traditional virtual machines.', "key_points": ['Images are built from instructions', 'Containers run from images', 'Keep images small and avoid embedding secrets'], "practice": 'Explain the difference between a container image and a running container.'},
            {"id": 403, "title": "Your first pipeline", "duration": "39 min", "content": 'A CI/CD pipeline automates the steps between a code change and a release. A simple pipeline might install dependencies, run tests, build an artifact, and deploy only when earlier checks pass. Logs and rollback plans help make releases safer.', "key_points": ['Automate tests before deployment', 'Use environment variables for configuration', 'Plan how to recover from a bad release'], "practice": 'Outline three stages for a pipeline that checks and packages a Python app.'},
        ],
    },
]
QUIZ = [
    {"id": 1, "question": "Which keyword defines a function in Python?",
     "options": ["func", "def", "function", "lambda"], "answer": 1,
     "explanation": "Python uses `def` to define a named function."},
    {"id": 2, "question": "Which collection is ordered and mutable?",
     "options": ["tuple", "set", "list", "frozenset"], "answer": 2,
     "explanation": "Lists preserve order and can be changed after creation."},
    {"id": 3, "question": "What does len(items) return?",
     "options": ["The last item", "The number of items", "A sorted list", "The item type"], "answer": 1,
     "explanation": "len() returns the number of items in a collection."},
]
