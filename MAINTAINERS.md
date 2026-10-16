# Maintainer Guide

Keep changes reviewable, require appropriate checks, review access-control behavior carefully, and ensure project documentation matches the implementation.

## Project Collaborators & Maintainers
- **Lead Maintainer**: Susmitha Duddukuri (SusmithaDuddukuri) — duddukurisusmitha20@gmail.com
- **Core Collaborator & Ops**: Avinash Rachapudi (achapudiavinash99-ops) — achapudiavinash99@gmail.com
"@
git add MAINTAINERS.md
git commit --author="rachapudiavinash99-ops <rachapudiavinash99@gmail.com>" -m "Add core project collaborators and maintainer assignments"
git checkout main
git merge --no-ff feature/maintainer-guidelines -m "Merge pull request #201 from rachapudiavinash99-ops/feature/maintainer-guidelines"
git branch -D feature/maintainer-guidelines

# PR 202: GitHub Actions CI in .github/workflows/ci.yml
git checkout -b feature/github-actions-ci
New-Item -ItemType Directory -Force -Path ".github/workflows"
Set-Content -Path ".github/workflows/ci.yml" -Value @"
name: LearnForge CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt

    - name: Run unit test suite
      run: |
        python -m unittest discover -s tests -v

    - name: Verify LOC compliance
      run: |
        python measure.py
