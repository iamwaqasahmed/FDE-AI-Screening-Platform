"""Participant pages for rel-m04-l03.
The budget and the hashes stay out.

This file builds the release note and the capacity template. The release note writes the token price it is given and lists the pack files except the readme. The capacity page is empty headings for serve, batch, route, quota, scale, price, and backlog.
"""

from __future__ import annotations

from alwaha.engagement.m04_l03_rows import CASE_DATE


def release_note(price: int, files: list[str]) -> str:
    """Return the release note for the files it is given.

    The token price is written into the note so the page matches the rate selected for this pack. Every pack file except the readme is listed.
    """
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-m04-l03

From: Finance
Case date: {CASE_DATE}

The surge forecast is p-forecast. Today's external token price replaces yesterday's price.ext_large_per_1k. The new rate is {price} SAR per 1,000 tokens. Chat and the referral batch share one GPU quota. The lesson notes are [Module 4 Lesson 3](<../../Module 04/Lesson 03/Student_Copy/home.md>).

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
