"""Read the clause that exists only on the photo transcription.

clause takes the transcription and removes the export text, then
strips the ends. What remains is the text the export did not
already contain.
"""

from __future__ import annotations


def clause(page: dict) -> str:
    """Return the transcription text that is outside the export.

    page supplies export and transcription. A missing export is
    empty text. A missing transcription is empty text. The export
    string is removed from the transcription, and the ends are
    stripped.
    """
    export = page.get("export", "")
    # Remove the export from the transcription and keep what remains.
    return page.get("transcription", "").replace(export, "").strip()
