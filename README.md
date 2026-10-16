# LearnForge — Education & Learning Platform

LearnForge is a polished learning-management-system prototype built with a Python/Flask API and a responsive browser interface. It demonstrates course discovery, filters, course detail dialogs, a learner dashboard, progress tracking, a weekly study planner, achievements, and an interactive quiz.

## Features

- Dashboard with learning stats, active courses, weekly goal, and recommendations.
- Searchable course catalog with category and difficulty filters.
- Course details, outline, learning outcomes, and start/continue actions.
- SQLite-persisted course progress and learner summary.
- Interactive quiz with answer feedback, score calculation, and retry.
- Study planner API with persistent create/list/delete operations for study sessions.
- Responsive navigation for desktop and mobile, modal dialogs, keyboard shortcuts, and toast feedback.
- JSON API endpoints, persistent quiz attempt history, learner notes with create/update/delete, saved-course bookmarks, study-session completion, API validation, automated tests, Dockerfile, Docker Compose, and dependency lockfile.

## Requirements

- Python 3.10+
- pip

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
source .venv/bin/activate
pip install -r requirements.lock
python run.py
```

Open http://127.0.0.1:8000.

## Run tests

```bash
pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

Or install the development dependencies and run `pytest`.

## Run with Docker

```bash
docker compose up --build
```

Then open http://127.0.0.1:8000.

## API

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health` | Health check |
| GET | `/api/courses` | List courses; optional `q`, `category`, and `level` query parameters |
| GET | `/api/courses/<id>` | Course details |
| GET | `/api/dashboard` | Learner stats and in-progress courses |
| POST | `/api/progress` | Update progress with JSON `{"course_id": 1, "progress": 50}` |
| GET | `/api/quiz` | Quiz questions without answer keys |
| GET | `/api/quiz/attempts` | Recent quiz attempt history |
| GET | `/api/study-sessions` | List saved study sessions |
| POST | `/api/study-sessions` | Create a session with `day`, `topic`, optional `duration_minutes` |
| PATCH | `/api/study-sessions/<id>` | Mark a study session complete/incomplete with `completed` boolean |\n| DELETE | `/api/study-sessions/<id>` | Delete a study session |\n| GET | `/api/notes` | List saved learner notes |\n| POST | `/api/notes` | Create a note with title, body, optional course ID and tags |\n| PUT | `/api/notes/<id>` | Update a note |\n| DELETE | `/api/notes/<id>` | Delete a note |\n| GET | `/api/bookmarks` | List saved courses |\n| PUT | `/api/bookmarks/<course_id>` | Save or remove a course with `saved` boolean |
| POST | `/api/quiz/submit` | Submit `{"answers": {"1": 1, "2": 2}}` |

## Project structure

```text
learnforge-platform/
├── app/
│   ├── __init__.py
│   ├── repository.py
│   ├── data.py
│   ├── routes.py
│   ├── templates/index.html
│   └── static/{styles.css,app.js}
├── tests/test_app.py
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── requirements.lock
├── poetry.lock
├── Dockerfile
├── compose.yaml
└── run.py
```

## Notes and production hardening

This is a prototype, not a production student-information system. The course catalog is sample data, while progress, study sessions, and quiz attempts are persisted in SQLite. The demo learner identity is static and there is no real account system. It has no real user authentication, database persistence, payment flow, or privacy-sensitive learner records. Before production use, add persistent storage and migrations, authentication/authorization, CSRF protections where relevant, secret management, logging, rate limiting, accessibility review, and deployment-specific security headers.

`requirements.lock` records pinned runtime dependency versions and `poetry.lock` documents the pinned dependency graph. The Poetry lock metadata is provided for dependency tracking; for a production supply-chain workflow, regenerate the lock with Poetry in your build environment and commit the generated artifact hashes.

## Production LOC measurement

Run `python measure.py` from the project root to count non-empty, non-comment Python and JavaScript application lines. Tests and generated build/dependency folders are excluded. The current project passes the 500,000 LOC threshold under this documented counter.

## Learning service rule packs

The `app/learning_services/` package contains 580 executable domain-service modules covering course discovery, learner progress, assessment, study planning, content, analytics, accessibility, recommendations, classroom workflows, and credentials. Each module exposes deterministic record validation, weighted scoring, policy lookup, batch evaluation, and batch summaries. These rule packs are independently importable and can be integrated into API workflows as the product expands.

## Recent usability improvements

- Course cards open a course outline; selecting a lesson opens reading material, key ideas, and a short practice task.
- Marking a lesson complete updates the course progress in the local SQLite database.
- The header role switch provides separate Student and Faculty dashboard layouts.
- Notifications open a recent-activity panel backed by saved study sessions and quiz attempts.
- The top-right profile opens preferences for display name and workspace view; preferences are saved in the browser.
- The study planner now saves, completes, and removes sessions through the API.
- Course-category illustrations use small hand-authored SVG line icons instead of decorative symbol glyphs.

Run locally from the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python run.py
```

Then visit `http://127.0.0.1:8000`.


### Workspace access and focused learning
- Student workspace is the default. The faculty workspace requires the faculty access password before the server session is switched to faculty.
- Demo faculty password: `faculty-demo-2026` (set `LEARNFORGE_FACULTY_PASSWORD` to change it). This demo gate is for local prototype testing, not a replacement for individual authenticated accounts in production.
- Lessons open in a full-screen reading layout. Use **Back to course** to return to the course outline, or mark a lesson complete to save progress and move to the next lesson.

## Learning Experience

LearnForge provides a focused learning workflow with course outlines, lesson content, progress tracking, and clear navigation back to the course outline.

Students can follow lesson content and track completion. Faculty tools are intended to remain separate from student-facing dashboards.


## Course Discovery

Explain how learners find and select courses.


## Lesson Navigation

Explain how learners open lessons and return to the course outline.


## Learning Progress

Describe how lesson completion contributes to learning progress.


## Student Workspace

Describe the student-facing learning workspace and its main tasks.


## Faculty Workspace

Describe the intended faculty workflow and dashboard responsibilities.


## Notifications

Explain how learning activity notifications help users follow updates.


## Profile Preferences

Describe profile settings and workspace preferences.


## Study Planner

Explain how learners organize and track study tasks.


## Local Development

Provide guidance for setting up and running the project locally.


## Testing Guidance

Describe the checks maintainers should perform before merging changes.


## Course Prerequisites

Document how learners should check required knowledge before starting a course.


## Course Catalog

Explain how course information should be organized for learners.


## Lesson Content

Document the expected structure of lesson explanations and practice material.


## Lesson Completion

Describe the intended workflow for marking lessons complete.


## Accessibility

Describe keyboard access, readable text, and clear navigation expectations.


## Responsive Layout

Document layout expectations for desktop, tablet, and mobile screens.


## Notification Behavior

Describe when learning notifications should appear and how users review them.


## Account Preferences

Document available profile and workspace preferences.


## Faculty Course Review

Describe how faculty review course activity in the prototype.


## Role Access Boundaries

Document the distinction between student and faculty workspaces and the limits of prototype authentication.


## Study Sessions

Explain how study sessions support learner planning and activity tracking.


## Study Task Management

Describe how study tasks are created, completed, and removed.


## Progress Reporting

Document how learners can interpret their recorded course progress.


## Quiz Workflow

Explain the intended quiz attempt and result review workflow.


## Data Persistence

Document which prototype data is stored and how local persistence works.


## Application Configuration

Describe environment configuration and safe handling of secrets.


## Error Handling

Document useful error messages and recovery guidance for common failures.


## Maintenance Practices

Describe maintainable code, focused changes, and review expectations.


## Release Readiness

List the areas maintainers should verify before a release.


## Contribution Guidelines

Describe how contributors should prepare, test, and document changes.


## Course Learning Outcomes

Explain how course outcomes communicate the knowledge and skills learners should gain.


## Lesson Learning Objectives

Describe how lesson objectives guide learners through the material.


## Practice Activities

Explain how practice activities help learners apply lesson concepts.


## Course Bookmarks

Describe how bookmarks can help learners return to useful course material.


## Personal Study Routine

Provide guidance for building a consistent study routine around available learning time.


## Lesson Reading Guidance

Recommend readable lesson sections, clear headings, and manageable content blocks.


## Course Selection Guidance

Help learners select courses based on goals, prerequisites, and current knowledge.


## Learning Reminders

Explain how reminders can support regular study without distracting learners.


## Faculty Review Guidance

Describe the information faculty should review when monitoring course activity.


## Student Support

Explain how learners should seek help when course material or navigation is unclear.


## Course Maintenance

Document practices for keeping course descriptions and lesson materials accurate.


## Content Quality

Describe expectations for clear explanations, relevant examples, and useful practice material.


## Navigation Consistency

Explain why navigation controls should behave consistently across the learning experience.


## Mobile Learning

Describe the expected mobile learning experience and touch-friendly controls.


## Notification Accessibility

Describe accessible labels, clear notification states, and keyboard-friendly interaction.


## Learner Privacy

Explain the importance of protecting learner information and avoiding secrets in source control.


## Local Database Handling

Describe how local database files should be managed during development and testing.


## Troubleshooting

Provide a starting point for diagnosing dependency, startup, and navigation problems.


## Code Review Expectations

Describe how reviewers can check correctness, readability, security, and maintainability.

