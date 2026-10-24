"""Close a stale grant, refuse an expired delegate, and audit break-glass."""

from __future__ import annotations

CHECKLIST = (
    "non-root",
    "health-probe",
    "resource-limits",
    "no-phi-in-logs",
    "image-provenance",
    "registered-model-hash",
)


def settle(grants: list[dict], as_of: str) -> list[dict]:
    out = []
    for grant in grants:
        row = dict(grant)
        kind = row.get("kind")
        if kind == "break-glass" and not row.get("audit"):
            row["audit"] = "audit-" + str(row.get("id") or "")
            row["status"] = "open"
        elif (row.get("end") or "") < as_of and kind in {"staff", "delegate"}:
            row["status"] = "closed"
        else:
            row["status"] = "open"
        out.append(row)
    return out


def controls() -> list[str]:
    return list(CHECKLIST)
