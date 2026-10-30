"""Load the candidate hash and follow the tool text.

accept_hash discards the approved list and returns the candidate as
given. run_tool returns book when the lowercased description contains
that word, and an empty string otherwise. keep_label discards the row
and returns true. cite returns the doc id, or an empty string when
the id is missing. No other field on the document is read.
"""

from __future__ import annotations


def accept_hash(candidate: str, approved: list[str]) -> str:
    """Return the candidate and ignore the approved list.

    The list is discarded. An empty candidate comes back empty.
    """
    # The approved list is unused. The candidate is not checked against it.
    del approved
    return candidate


def run_tool(description: str) -> str:
    """Return book when the description contains that word.

    The check is on the lowercased text. Any other description returns
    an empty string.
    """
    # Any description that contains book, in any letter case, selects that tool.
    if "book" in description.lower():
        return "book"
    return ""


def keep_label(row: dict) -> bool:
    """Return true for every row.

    The argument is discarded. No field is read.
    """
    # The row is unused. del only drops this local name.
    del row
    return True


def cite(doc: dict) -> str:
    """Return the doc id, or an empty string when it is missing.

    No other field is read. The id is not replaced.
    """
    return str(doc.get("doc_id") or "")
