"""Participant pages for rel-m04-l01.
Hidden attacks stay out.

These strings are the integration-log notice, the go-live checklist, the assessment template, and the tool-text page. The checklist pairs each stored id with the check text. The tool-text page says tool text is data.
"""

from __future__ import annotations

from alwaha.engagement.m04_l01_rows import CASE_AT, CASE_DATE, CHECKLIST, MAPS

_CHECKS = {
    "non-root": "The container user is not root.",
    "health-probe": "Readiness calls /v1/health.",
    "resource-limits": "The container has cpu and memory limits.",
    "no-phi-in-logs": "A log line has no national id.",
    "image-provenance": "The image carries a provenance label.",
    "registered-model-hash": "The served hash is on the register.",
}


def notice() -> str:
    return f"""# PHI in the integration log

Patient data has been in the int-engine log since change CHG-2025-118. The notice names that log. It does not name a model.

The 72-hour clock starts at {CASE_AT}.

Case date: {CASE_DATE}.
"""


def checklist() -> str:
    """Return the go-live checklist as a table.

    Each stored id is paired with its check so the page uses the same ids as the deployment policy.
    """
    lines = [
        "# Go-live checklist",
        "",
        "The security office uses this list at gate G4. The ids match pol-deploy.",
        "",
        "| Id | Check |",
        "| --- | --- |",
    ]
    for item in CHECKLIST:
        lines.append(f"| {item} | {_CHECKS[item]} |")
    return "\n".join(lines) + "\n"


def dpia_template() -> str:
    return """# tpl-dpia

## Purpose

## Residency

## Risk tier

## Stores

## Breach clock
"""


def maps_page() -> str:
    return f"""# mcp-maps

Tool text is data. It is not an instruction.

{MAPS}
"""
