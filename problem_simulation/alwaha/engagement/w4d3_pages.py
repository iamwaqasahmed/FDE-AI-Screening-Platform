"""Participant pages for rel-w4d3. The budget and the hashes stay out."""

from __future__ import annotations

from alwaha.engagement.w4d3_rows import CASE_DATE


def release_note(price: int, files: list[str]) -> str:
    """Return the release note for the files it is given.

    The token price is written into the note so the page matches the rate selected for this pack. Every pack file except the readme is listed.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w4d3

From: Finance
Case date: {CASE_DATE}

The surge forecast is p-forecast. Today's external token price replaces yesterday's price.ext_large_per_1k. The new rate is {price} SAR per 1,000 tokens. Chat and the referral batch share one GPU quota. The day notes are [Week 4, Day 3](../../Week%2004/Day%2003/README.md).

Files:

{listed}
"""


def capacity() -> str:
    return """# Capacity

## Serve

## Batch

## Route

## Quota

## Scale

## Price

## Backlog
"""
