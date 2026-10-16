"""SQLite persistence for LearnForge learner state and study sessions."""
import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from flask import current_app

SCHEMA = """
CREATE TABLE IF NOT EXISTS course_progress (
    course_id INTEGER PRIMARY KEY,
    progress INTEGER NOT NULL CHECK(progress BETWEEN 0 AND 100),
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS study_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT NOT NULL,
    topic TEXT NOT NULL,
    duration_minutes INTEGER NOT NULL DEFAULT 20 CHECK(duration_minutes BETWEEN 5 AND 480),
    completed INTEGER NOT NULL DEFAULT 0 CHECK(completed IN (0, 1)),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS learner_notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    course_id INTEGER,
    tags_json TEXT NOT NULL DEFAULT '[]',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS course_bookmarks (
    course_id INTEGER PRIMARY KEY,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS quiz_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER NOT NULL,
    total INTEGER NOT NULL,
    percent INTEGER NOT NULL,
    answers_json TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""

def database_path():
    return current_app.config["DATABASE"]

@contextmanager
def connect():
    path = Path(database_path())
    if str(path) != ":memory:":
        path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(str(path))
    db.row_factory = sqlite3.Row
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

def init_db():
    with connect() as db:
        db.executescript(SCHEMA)

def get_progress(course_id, fallback=0):
    with connect() as db:
        row = db.execute("SELECT progress FROM course_progress WHERE course_id = ?", (course_id,)).fetchone()
        return row["progress"] if row else fallback

def set_progress(course_id, progress):
    with connect() as db:
        db.execute(
            """INSERT INTO course_progress(course_id, progress, updated_at)
               VALUES (?, ?, CURRENT_TIMESTAMP)
               ON CONFLICT(course_id) DO UPDATE SET
               progress=excluded.progress, updated_at=CURRENT_TIMESTAMP""",
            (course_id, progress),
        )

def list_sessions():
    with connect() as db:
        return [dict(row) for row in db.execute(
            "SELECT id, day, topic, duration_minutes, completed, created_at FROM study_sessions ORDER BY id DESC"
        ).fetchall()]

def create_session(day, topic, duration_minutes=20):
    with connect() as db:
        cur = db.execute(
            "INSERT INTO study_sessions(day, topic, duration_minutes) VALUES (?, ?, ?)",
            (day, topic, duration_minutes),
        )
        row = db.execute("SELECT id, day, topic, duration_minutes, completed, created_at FROM study_sessions WHERE id = ?", (cur.lastrowid,)).fetchone()
        return dict(row)

def delete_session(session_id):
    with connect() as db:
        cur = db.execute("DELETE FROM study_sessions WHERE id = ?", (session_id,))
        return cur.rowcount > 0

def save_quiz_attempt(score, total, answers):
    with connect() as db:
        cur = db.execute(
            "INSERT INTO quiz_attempts(score, total, percent, answers_json) VALUES (?, ?, ?, ?)",
            (score, total, round(score / total * 100) if total else 0, json.dumps(answers, sort_keys=True)),
        )
        return cur.lastrowid

def list_quiz_attempts(limit=10):
    with connect() as db:
        rows = db.execute(
            "SELECT id, score, total, percent, created_at FROM quiz_attempts ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [dict(row) for row in rows]


def list_notes():
    with connect() as db:
        rows = db.execute(
            "SELECT id, title, body, course_id, tags_json, created_at, updated_at "
            "FROM learner_notes ORDER BY updated_at DESC, id DESC"
        ).fetchall()
        result = []
        for row in rows:
            item = dict(row)
            item["tags"] = json.loads(item.pop("tags_json"))
            result.append(item)
        return result

def create_note(title, body, course_id=None, tags=None):
    tags = tags or []
    with connect() as db:
        cur = db.execute(
            "INSERT INTO learner_notes(title, body, course_id, tags_json) VALUES (?, ?, ?, ?)",
            (title, body, course_id, json.dumps(tags)),
        )
        row = db.execute(
            "SELECT id, title, body, course_id, tags_json, created_at, updated_at "
            "FROM learner_notes WHERE id = ?", (cur.lastrowid,)
        ).fetchone()
        item = dict(row)
        item["tags"] = json.loads(item.pop("tags_json"))
        return item

def update_note(note_id, title, body, course_id=None, tags=None):
    with connect() as db:
        cur = db.execute(
            "UPDATE learner_notes SET title=?, body=?, course_id=?, tags_json=?, "
            "updated_at=CURRENT_TIMESTAMP WHERE id=?",
            (title, body, course_id, json.dumps(tags or []), note_id),
        )
        if not cur.rowcount:
            return None
        row = db.execute(
            "SELECT id, title, body, course_id, tags_json, created_at, updated_at "
            "FROM learner_notes WHERE id=?", (note_id,)
        ).fetchone()
        item = dict(row)
        item["tags"] = json.loads(item.pop("tags_json"))
        return item

def delete_note(note_id):
    with connect() as db:
        cur = db.execute("DELETE FROM learner_notes WHERE id=?", (note_id,))
        return cur.rowcount > 0

def list_bookmarks():
    with connect() as db:
        return [row["course_id"] for row in db.execute(
            "SELECT course_id FROM course_bookmarks ORDER BY created_at DESC"
        ).fetchall()]

def set_bookmark(course_id, saved=True):
    with connect() as db:
        if saved:
            db.execute("INSERT OR IGNORE INTO course_bookmarks(course_id) VALUES (?)", (course_id,))
        else:
            db.execute("DELETE FROM course_bookmarks WHERE course_id=?", (course_id,))
        return course_id in {row["course_id"] for row in db.execute(
            "SELECT course_id FROM course_bookmarks"
        ).fetchall()}

def complete_session(session_id, completed=True):
    with connect() as db:
        cur = db.execute(
            "UPDATE study_sessions SET completed=? WHERE id=?",
            (1 if completed else 0, session_id),
        )
        if not cur.rowcount:
            return None
        row = db.execute(
            "SELECT id, day, topic, duration_minutes, completed, created_at "
            "FROM study_sessions WHERE id=?", (session_id,)
        ).fetchone()
        return dict(row)
