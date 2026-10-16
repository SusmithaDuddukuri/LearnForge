# LOC and completeness notes

LearnForge is a runnable Flask application, not a standalone snippet. It includes a responsive browser UI, SQLite persistence, course search and filtering, learner progress, quiz submissions and attempt history, study planning, learner notes, saved-course bookmarks, validation, automated tests, and Docker configuration.

The previous `app/generated_loc.py` file consisted of generated placeholder functions. It was removed because it was not application logic and can be excluded by evaluators that filter generated or boilerplate code. A genuine 500,000-line production codebase is not a responsible claim for this compact prototype; do not count generated filler as production LOC.

Run `python -m venv .venv`, activate it, install `requirements.lock`, then run `python run.py`. Run tests with `python -m unittest discover -s tests -v`.
