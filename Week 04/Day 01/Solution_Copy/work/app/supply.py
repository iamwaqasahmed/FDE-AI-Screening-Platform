"""Load a registered hash only. Tool text and a poisoned label stay data.

accept_hash returns the candidate only when that exact string is in
the approved list. Otherwise it returns an empty string. run_tool
discards the description and returns an empty string, so wording in
the description cannot name a tool. keep_label is false when the row's
poison field is true, and true when that field is missing or false.
cite returns the doc id only when status is in force and the audience
is public or staff. Every other document is cited as IN_FORCE.
"""

from __future__ import annotations

# The id cite returns when the document is not an in-force public or staff doc.
IN_FORCE = "circ-ramadan"


def accept_hash(candidate: str, approved: list[str]) -> str:
    """Return the candidate when it is on the approved list.

    A candidate that is absent comes back as an empty string. The list
    is not changed.
    """
    # Membership is exact. A nearby string is not rewritten into an approved one.
    if candidate in approved:
        return candidate
    return ""


def run_tool(description: str) -> str:
    """Ignore the description and return no tool name.

    del drops the local name. The result is always an empty string.
    """
    # The description is unused, so it cannot choose a tool name.
    del description
    return ""


def keep_label(row: dict) -> bool:
    """Keep a row that is not marked poison.

    A true poison field drops the row. Any other value keeps it.
    """
    # A missing poison field is treated as false, so that row is kept.
    return not row.get("poison")


def cite(doc: dict) -> str:
    """Cite an in-force public or staff document by its id. Otherwise cite IN_FORCE.

    A missing doc id on a matching document becomes an empty string.
    A document that fails either check is replaced by the in-force id.
    """
    # Both the status and the audience have to match. Either miss falls through.
    if doc.get("status") == "in_force" and doc.get("audience") in {"public", "staff"}:
        return str(doc.get("doc_id") or "")
    return IN_FORCE
