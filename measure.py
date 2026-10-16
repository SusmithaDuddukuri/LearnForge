"""Report production source line counts for LearnForge.

Counts non-empty, non-comment lines in Python and JavaScript application files.
Tests, virtual environments, caches, build output, and dependency directories are excluded.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
EXCLUDED_PARTS = {"tests", "test", "__pycache__", ".venv", "venv", "node_modules", "dist", "build", "coverage", ".git"}
EXTENSIONS = {".py", ".js", ".mjs", ".cjs"}


def production_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        if path.name in {"measure.py"}:
            continue
        yield path


def count_lines(path):
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return 0
    return sum(1 for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#"))


def main():
    files = sorted(production_files())
    total = sum(count_lines(path) for path in files)
    by_language = {}
    for path in files:
        language = "Python" if path.suffix == ".py" else "JavaScript"
        by_language[language] = by_language.get(language, 0) + count_lines(path)
    print(f"Production source files: {len(files)}")
    for language, count in sorted(by_language.items()):
        print(f"{language}: {count:,} LOC")
    print(f"Total production LOC: {total:,}")
    if total < 500_000:
        print(f"FAIL: need at least 500,000 LOC; short by {500_000 - total:,}.")
        return 1
    print("PASS: production source LOC is at least 500,000.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
