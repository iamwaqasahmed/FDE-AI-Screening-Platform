"""Participant pages for rel-w4d2. The rate and the hashes stay out."""

from __future__ import annotations

from alwaha.engagement.w4d2_rows import CASE_DATE, CIRCULAR, NEW_HOURS, SLO_MINUTES


def replay_note() -> str:
    return f"""# Incident replay

The alert is already in the spans. Do not add a new bug. The alert SLO is {SLO_MINUTES} minutes from the first tool error. CPU stays flat.

Case date: {CASE_DATE}.
"""


def circular() -> str:
    return f"""# {CIRCULAR}

- doc_id: {CIRCULAR}
- family: hours
- status: in_force
- supersedes: circ-ramadan
- audience: public

{NEW_HOURS}
"""


def runbook() -> str:
    return """# tpl-runbook

## Detect

## Scope

## Impact

## Timeline

## Owner

## Cache

## Shadow
"""
