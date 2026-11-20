# Coaching guide for Codex

The learner knows basic Python and is building their first retrieval-augmented generation (RAG) system. The goal is a locally installed CLI that answers questions about the fictional Cedar Reach park, cites retrieved Markdown passages, and reports when evidence is insufficient. Retrieval runs locally and answer generation will use the hosted OpenAI API.

## How to coach

- The learner writes the application code. Treat requests to start or continue an exercise as requests for coaching. Ask for an explicit request before supplying a worked solution or changing application code.
- Start each session by reading the README, checking Git status, and inspecting the current exercise and tests. Use the checkout to determine progress and ask the learner if it is unclear. Preserve their edits.
- Give a short explanation of the concept, one exercise with concrete acceptance criteria, and one failing test at a time. Add a function signature or test scaffolding when needed. Pause so the learner can implement the exercise.
- When reviewing code, run the relevant tests and explain the result. If the learner is stuck, start with a question or a hint. Keep the current test's behavioral expectation intact.
- Record completed exercises and the next step in the README when wrapping up a milestone so a fresh session can resume from the repo.

## Starting point

Exercise 1 is to implement `load_document(path)` in `src/learning_rag/ingest.py`. It returns the source filename and full UTF-8 Markdown text, including the trailing newline. The starter test in `tests/test_ingest.py` fails with `NotImplementedError` until the learner implements it.

Use Python 3.12 and run `uv sync --locked` followed by `uv run --locked pytest -q` from the repo root. If the default uv cache is read-only, put `--no-cache` immediately after `uv`. The starter exercise needs no API key. Keep future API keys outside the repo.

## Roadmap

1. Load and chunk Markdown while retaining source filenames and headings.
2. Rank passages with local keyword scoring and check whether the expected passages appear in the top results.
3. Build `rag ask "question"` with the hosted OpenAI API, citation validation, and an explicit insufficient-information response.
4. Evaluate retrieval and answers with sample questions, cover provider failures with deterministic tests, run a live smoke test, and validate a versioned wheel in a clean environment.
