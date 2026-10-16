from flask import Blueprint, jsonify, render_template, request, session
from .data import COURSES, QUIZ
from .repository import (
    create_session, delete_session, get_progress, list_quiz_attempts,
    list_sessions, save_quiz_attempt, set_progress, list_notes, create_note, update_note, delete_note,
    list_bookmarks, set_bookmark, complete_session,
)

bp = Blueprint("main", __name__)

def course_view(course):
    result = dict(course)
    result["progress"] = get_progress(course["id"], course.get("progress", 0))
    return result

@bp.get("/")
def home():
    return render_template("index.html")

@bp.get("/api/session")
def get_role_session():
    return jsonify({"role": session.get("role", "student")})

@bp.post("/api/session/role")
def set_role_session():
    payload = request.get_json(silent=True) or {}
    role = payload.get("role", "student")
    if role not in ("student", "faculty"):
        return jsonify({"error": "Choose a valid workspace."}), 400
    if role == "faculty":
        expected = __import__("os").environ.get("LEARNFORGE_FACULTY_PASSWORD", "faculty-demo-2026")
        if payload.get("password") != expected:
            return jsonify({"error": "Faculty access denied. Enter the faculty demo password."}), 403
    session["role"] = role
    return jsonify({"role": role})

@bp.get("/api/faculty/dashboard")
def faculty_dashboard():
    if session.get("role") != "faculty":
        return jsonify({"error": "Faculty access required. Switch to the faculty workspace with authorized access."}), 403
    items = [course_view(c) for c in COURSES]
    dashboard_data = {"courses": len(items), "active_learners": len([c for c in items if c["progress"] > 0]), "quiz_attempts": len(list_quiz_attempts()), "items": items}
    return jsonify(dashboard_data)

@bp.get("/api/health")
def health():
    return jsonify({"status": "ok", "service": "LearnForge API"})

@bp.get("/api/courses")
def courses():
    query = request.args.get("q", "").strip().lower()
    category = request.args.get("category", "All")
    level = request.args.get("level", "All")
    items = [course_view(c) for c in COURSES]
    if query:
        items = [c for c in items if query in (c["title"] + " " + c["description"] + " " + c["category"] + " " + " ".join(c["skills"])).lower()]
    if category != "All":
        items = [c for c in items if c["category"] == category]
    if level != "All":
        items = [c for c in items if c["level"] == level]
    return jsonify({"items": items, "total": len(items)})

@bp.get("/api/courses/<int:course_id>")
def course_detail(course_id):
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    return jsonify(course_view(course))

@bp.get("/api/courses/<int:course_id>/modules/<int:module_id>")
def module_detail(course_id, module_id):
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    module = next((m for m in course["modules"] if m["id"] == module_id), None)
    if not module:
        return jsonify({"error": "Lesson not found"}), 404
    lesson = dict(module)
    lesson["course_id"] = course_id
    lesson["course_title"] = course["title"]
    lesson["content"] = module.get("content") or (
        f"In this lesson, we will work through {module['title'].lower()} in {course['title']}. "
        f"Start by identifying the problem, follow the example, and then try the short practice task."
    )
    lesson["key_points"] = module.get("key_points") or course["skills"][:3]
    lesson["practice"] = module.get("practice") or f"Write down one example of {module['title'].lower()} and explain why it works."
    return jsonify(lesson)

@bp.post("/api/courses/<int:course_id>/modules/<int:module_id>/complete")
def complete_module(course_id, module_id):
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    module_index = next((i for i, m in enumerate(course["modules"]) if m["id"] == module_id), None)
    if module_index is None:
        return jsonify({"error": "Lesson not found"}), 404
    total = max(len(course["modules"]), 1)
    progress = round((module_index + 1) / total * 100)
    current = get_progress(course_id, course.get("progress", 0))
    progress = max(current, progress)
    set_progress(course_id, progress)
    return jsonify({"course_id": course_id, "module_id": module_id, "progress": progress, "completed": True})

@bp.get("/api/notifications")
def notifications():
    sessions = list_sessions()
    attempts = list_quiz_attempts(3)
    items = []
    for session in sessions[:3]:
        items.append({"title": "Study session on your planner", "message": f"{session['topic']} · {session['day']}", "kind": "calendar"})
    for attempt in attempts[:2]:
        items.append({"title": "Practice result saved", "message": f"You scored {attempt['percent']}% on a recent quiz.", "kind": "check"})
    if not items:
        items.append({"title": "Welcome to LearnForge", "message": "Your learning space is ready. Start a course to see your activity here.", "kind": "book"})
    return jsonify({"items": items, "unread": len(items)})

@bp.get("/api/dashboard")
def dashboard():
    items = [course_view(c) for c in COURSES]
    enrolled = [c for c in items if c["progress"] > 0]
    completed = sum(1 for c in items if c["progress"] >= 100)
    sessions = list_sessions()
    attempts = list_quiz_attempts()
    return jsonify({
        "learner": {"name": "Alex Morgan", "streak": 7, "weekly_goal": 5, "weekly_done": 3},
        "stats": {"enrolled": len(enrolled), "completed": completed, "learning_hours": 24, "certificates": completed},
        "courses": enrolled,
        "next_lesson": {"course": "Python Foundations", "lesson": "Functions in practice", "course_id": 1},
        "study_sessions": len(sessions),
        "quiz_attempts": len(attempts),
    })

@bp.post("/api/progress")
def update_progress():
    payload = request.get_json(silent=True) or {}
    course_id = payload.get("course_id")
    try:
        course_id = int(course_id)
        progress = int(payload.get("progress"))
    except (TypeError, ValueError):
        return jsonify({"error": "course_id and progress must be integers"}), 400
    if not 0 <= progress <= 100:
        return jsonify({"error": "progress must be between 0 and 100"}), 400
    if not any(c["id"] == course_id for c in COURSES):
        return jsonify({"error": "Course not found"}), 404
    set_progress(course_id, progress)
    return jsonify({"course_id": course_id, "progress": progress, "message": "Progress saved"})

@bp.get("/api/quiz")
def quiz():
    return jsonify([{"id": q["id"], "question": q["question"], "options": q["options"]} for q in QUIZ])

@bp.post("/api/quiz/submit")
def submit_quiz():
    payload = request.get_json(silent=True) or {}
    answers = payload.get("answers")
    if not isinstance(answers, dict):
        return jsonify({"error": "answers must be an object keyed by question id"}), 400
    correct = 0
    details = []
    normalized_answers = {}
    for question in QUIZ:
        raw = answers.get(str(question["id"]), answers.get(question["id"]))
        try:
            selected = int(raw) if raw is not None else None
        except (ValueError, TypeError):
            selected = None
        if selected is not None and not 0 <= selected < len(question["options"]):
            return jsonify({"error": f"answer for question {question['id']} is out of range"}), 400
        normalized_answers[str(question["id"])] = selected
        is_correct = selected == question["answer"]
        correct += int(is_correct)
        details.append({
            "id": question["id"], "correct": is_correct,
            "answer": question["answer"], "explanation": question["explanation"]
        })
    attempt_id = save_quiz_attempt(correct, len(QUIZ), normalized_answers)
    return jsonify({"attempt_id": attempt_id, "score": correct, "total": len(QUIZ), "percent": round(correct / len(QUIZ) * 100), "details": details})

@bp.get("/api/quiz/attempts")
def quiz_attempts():
    return jsonify({"items": list_quiz_attempts()})

@bp.get("/api/study-sessions")
def study_sessions():
    return jsonify({"items": list_sessions()})

@bp.post("/api/study-sessions")
def add_study_session():
    payload = request.get_json(silent=True) or {}
    day = payload.get("day")
    topic = payload.get("topic")
    try:
        duration = int(payload.get("duration_minutes", 20))
    except (TypeError, ValueError):
        return jsonify({"error": "duration_minutes must be an integer"}), 400
    if not isinstance(day, str) or not day.strip() or len(day) > 40:
        return jsonify({"error": "day is required and must be at most 40 characters"}), 400
    if not isinstance(topic, str) or not topic.strip() or len(topic) > 160:
        return jsonify({"error": "topic is required and must be at most 160 characters"}), 400
    if not 5 <= duration <= 480:
        return jsonify({"error": "duration_minutes must be between 5 and 480"}), 400
    return jsonify({"item": create_session(day.strip(), topic.strip(), duration)}), 201

@bp.delete("/api/study-sessions/<int:session_id>")
def remove_study_session(session_id):
    if not delete_session(session_id):
        return jsonify({"error": "Study session not found"}), 404
    return jsonify({"deleted": True, "id": session_id})


@bp.get("/api/notes")
def notes():
    return jsonify({"items": list_notes(), "total": len(list_notes())})

@bp.post("/api/notes")
def add_note():
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    body = payload.get("body")
    course_id = payload.get("course_id")
    tags = payload.get("tags", [])
    if not isinstance(title, str) or not title.strip() or len(title.strip()) > 120:
        return jsonify({"error": "title is required and must be at most 120 characters"}), 400
    if not isinstance(body, str) or not body.strip() or len(body.strip()) > 20000:
        return jsonify({"error": "body is required and must be at most 20000 characters"}), 400
    if not isinstance(tags, list) or any(not isinstance(tag, str) or len(tag) > 40 for tag in tags):
        return jsonify({"error": "tags must be a list of short strings"}), 400
    if course_id is not None:
        try:
            course_id = int(course_id)
        except (TypeError, ValueError):
            return jsonify({"error": "course_id must be an integer"}), 400
        if not any(c["id"] == course_id for c in COURSES):
            return jsonify({"error": "Course not found"}), 404
    item = create_note(title.strip(), body.strip(), course_id, [tag.strip() for tag in tags if tag.strip()])
    return jsonify({"item": item}), 201

@bp.put("/api/notes/<int:note_id>")
def edit_note(note_id):
    payload = request.get_json(silent=True) or {}
    title = payload.get("title")
    body = payload.get("body")
    course_id = payload.get("course_id")
    tags = payload.get("tags", [])
    if not isinstance(title, str) or not title.strip() or len(title.strip()) > 120:
        return jsonify({"error": "title is required and must be at most 120 characters"}), 400
    if not isinstance(body, str) or not body.strip() or len(body.strip()) > 20000:
        return jsonify({"error": "body is required and must be at most 20000 characters"}), 400
    if not isinstance(tags, list) or any(not isinstance(tag, str) or len(tag) > 40 for tag in tags):
        return jsonify({"error": "tags must be a list of short strings"}), 400
    if course_id is not None:
        try:
            course_id = int(course_id)
        except (TypeError, ValueError):
            return jsonify({"error": "course_id must be an integer"}), 400
        if not any(c["id"] == course_id for c in COURSES):
            return jsonify({"error": "Course not found"}), 404
    item = update_note(note_id, title.strip(), body.strip(), course_id, tags)
    if item is None:
        return jsonify({"error": "Note not found"}), 404
    return jsonify({"item": item})

@bp.delete("/api/notes/<int:note_id>")
def remove_note(note_id):
    if not delete_note(note_id):
        return jsonify({"error": "Note not found"}), 404
    return jsonify({"deleted": True, "id": note_id})

@bp.get("/api/bookmarks")
def bookmarks():
    saved_ids = set(list_bookmarks())
    items = [course_view(course) for course in COURSES if course["id"] in saved_ids]
    return jsonify({"items": items, "total": len(items)})

@bp.put("/api/bookmarks/<int:course_id>")
def toggle_bookmark(course_id):
    if not any(course["id"] == course_id for course in COURSES):
        return jsonify({"error": "Course not found"}), 404
    payload = request.get_json(silent=True) or {}
    saved = payload.get("saved", True)
    if not isinstance(saved, bool):
        return jsonify({"error": "saved must be a boolean"}), 400
    set_bookmark(course_id, saved)
    return jsonify({"course_id": course_id, "saved": saved})

@bp.patch("/api/study-sessions/<int:session_id>")
def mark_session_complete(session_id):
    payload = request.get_json(silent=True) or {}
    completed = payload.get("completed", True)
    if not isinstance(completed, bool):
        return jsonify({"error": "completed must be a boolean"}), 400
    item = complete_session(session_id, completed)
    if item is None:
        return jsonify({"error": "Study session not found"}), 404
    return jsonify({"item": item})
