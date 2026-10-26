"""Close a stale grant, refuse an expired delegate, and audit break-glass.

settle copies each grant and writes a status. A break-glass grant
with no audit value is given an audit id and left open. That check
runs before the end check, so a late end does not close it. A staff
or delegate grant is closed only when its end text is strictly less
than as_of. Text that is equal stays open. Every other grant is
marked open, including break-glass that already has an audit value.
A missing end is read as empty text.

controls returns the deploy checklist in the order stored below.
The tuple itself is not handed to the caller.
"""

from __future__ import annotations

# Deploy check names, in the order controls returns them.
CHECKLIST = (
    "non-root",
    "health-probe",
    "resource-limits",
    "no-phi-in-logs",
    "image-provenance",
    "registered-model-hash",
)


def settle(grants: list[dict], as_of: str) -> list[dict]:
    """Return a new list of grants with status set, and audit bare break-glass.

    The input list is not mutated. end and as_of are compared as text.
    A missing id becomes an empty suffix on the audit value.
    """
    out = []
    for grant in grants:
        # Copy first so the caller's dict keeps the status it arrived with.
        row = dict(grant)
        kind = row.get("kind")
        # An empty or missing audit value counts as unaudited. The id is
        # prefixed and the grant stays open.
        if kind == "break-glass" and not row.get("audit"):
            row["audit"] = "audit-" + str(row.get("id") or "")
            row["status"] = "open"
        # Only these two kinds close, and only when the end text is earlier.
        elif (row.get("end") or "") < as_of and kind in {"staff", "delegate"}:
            row["status"] = "closed"
        else:
            row["status"] = "open"
        out.append(row)
    return out


def controls() -> list[str]:
    """Return a new list of the deploy check names, in checklist order.

    The caller can change the list it receives. CHECKLIST stays as it is.
    """
    return list(CHECKLIST)
