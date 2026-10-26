"""Read the text export and skip the photo transcription.

clause returns the export text. The transcription is not read.
A page with no export returns empty text.
"""

from __future__ import annotations


def clause(page: dict) -> str:
    """Return the export text from the page.

    page is the scanned page. The transcription field is not
    used. A page without an export returns an empty string.
    """
    return page.get("export", "")
