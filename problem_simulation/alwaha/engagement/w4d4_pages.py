"""Participant pages for rel-w4d4.
The budget and the hashes stay out.

This file builds the release note, the failover template, and the architecture template. The release note names the drill and lists the pack files except the readme. The templates are empty headings for replicas, approvals, rent or buy, and the deadline.
"""

from __future__ import annotations

from alwaha.engagement.w4d4_rows import CASE_DATE


def release_note(files: list[str]) -> str:
    """Return the release note for the files it is given.

    It names the failover drill and lists every pack file except the readme, so the page matches the pack just written.
    """
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
