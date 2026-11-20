from pathlib import Path

from learning_rag.ingest import load_document


def test_load_document_preserves_filename_and_markdown(tmp_path: Path) -> None:
    path = tmp_path / "trail-notes.md"
    markdown = "# Juniper Trail\n\nThe overlook closes at dusk.\n"
    path.write_text(markdown, encoding="utf-8")

    assert load_document(path) == ("trail-notes.md", markdown)
