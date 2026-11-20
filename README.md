# Learn RAG with Cedar Reach

Build a command-line tool that answers questions about a fictional park and cites the Markdown passages it used. Retrieval-augmented generation (RAG) gives a model relevant passages to reference when it answers a question.

You write the application code. The starter files give you a function signature, sample documents, and one failing test. Work through one exercise at a time.

## Setup

Use Python 3.12 and [uv](https://docs.astral.sh/uv/). From the repo root, run

```sh
uv --no-cache sync --locked
uv --no-cache run --locked pytest -q
```

The first test starts red with `NotImplementedError`. This exercise runs without an API key.

## Exercise 1 — Load one Markdown document

Implement `load_document(path)` in `src/learning_rag/ingest.py`. Given a `Path` to a UTF-8 Markdown file, return a tuple containing the filename (including `.md`) and the full text. Preserve the Markdown and trailing newline. The filename will identify the source when you add citations later.

Run the test again after your change. You're done when it passes. For your first manual check, try loading `docs/corpus/trails.md`.

## Learning path

1. **Ingest.** Load Markdown and split it into passages that retain the source filename and heading.
2. **Retrieve.** Rank passages locally with keyword scoring and check whether the expected passage appears in the top results. Consider embeddings if evaluation reveals a gap.
3. **Generate.** Build `rag ask "question"` using the hosted OpenAI API. Send the question and retrieved excerpts, validate the passage IDs in the answer, and report when the excerpts provide insufficient information. Handle missing keys, timeouts, and rate limits.
4. **Evaluate and release.** Add a configurable document directory, a small evaluation set, and tests that use a fake provider. Check grounded and unsupported questions with a live API call. Document what leaves the machine, then build a versioned wheel and try it in a clean environment.
