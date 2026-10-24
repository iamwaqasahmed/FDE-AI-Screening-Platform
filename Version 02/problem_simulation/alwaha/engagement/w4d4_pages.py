"""Participant pages for rel-w4d4. The budget and the hashes stay out."""

from __future__ import annotations

from alwaha.engagement.w4d4_rows import CASE_DATE


def release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w4d4

From: Enterprise Architect
Case date: {CASE_DATE}

The site-a failover drill is open. The insure gateway is in outage. site-b is the second private-cloud site. The day notes are [Week 4, Day 4](../../Week%2004/Day%2004/README.md).

Files:

{listed}
"""


def failover() -> str:
    return """# Failover

## Replicas

## Drill

## Approvals

## Breaker

## Patient
"""


def architecture() -> str:
    return """# Architecture

## Rent

## Buy

## Deadline

## Hospitals
"""
