"""Participant pages for rel-m04-l02.
The rate and the hashes stay out.

These strings are the incident-replay note, the hours circular, and the runbook template. The replay note points at spans already in the pack. The circular is the hours document, and the runbook is a set of empty headings.
"""

from __future__ import annotations

from alwaha.engagement.m04_l02_rows import CASE_DATE, CIRCULAR, NEW_HOURS, SLO_MINUTES


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
