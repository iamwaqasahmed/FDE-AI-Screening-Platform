"""Board packs and site notes. The numbers are the month's true counts."""

from __future__ import annotations

from datetime import date

import pandas as pd

from simulation.policy.render import render_document
from simulation.policy.types import Document
from simulation.world.clock import HISTORY_START, SNAPSHOT, month_ends
from simulation.world.sites import HARBOUR, NCEC, OAKRIDGE, RIVER_SITE

NOTE_SITES = (NCEC, HARBOUR, OAKRIDGE, RIVER_SITE)


def build_operational(events: pd.DataFrame) -> tuple[dict[str, str], dict[str, Document]]:
    rendered: dict[str, str] = {}
    catalog: dict[str, Document] = {}
    for day in month_ends(HISTORY_START, SNAPSHOT):
        document = _document(f"board-{day:%Y-%m}", f"Monthly board pack {day:%Y-%m}", day, "")
        body = _counts(events, f"{day:%Y-%m}", None)
        rendered[document.document_id] = render_document(document, body)
        catalog[document.document_id] = document
    for year in range(HISTORY_START.year, SNAPSHOT.year):
        for quarter, month in enumerate((1, 4, 7, 10), start=1):
            for site in NOTE_SITES:
                slug = site.lower().replace(" ", "-")
                document_id = f"site-note-{slug}-{year}q{quarter}"
                document = _document(document_id, f"Site activity note {year} Q{quarter}", date(year, month, 1), site)
                body = _counts(events, f"{year}-{month:02d}", site, quarter=True)
                rendered[document_id] = render_document(document, body)
                catalog[document_id] = document
    return rendered, catalog


def _document(document_id: str, title: str, effective: date, site: str) -> Document:
    return Document(
        document_id=document_id,
        title=title,
        status="in_force",
        effective=effective,
        sunset=None,
        site=site,
        programme="diabetic-eye",
        version=document_id,
        supersedes=(),
        cites=(),
        applies_to=(),
        constrains=(),
        clause_ids=(),
    )


def _counts(events: pd.DataFrame, prefix: str, site: str | None, quarter: bool = False) -> str:
    frame = events
    if site is not None:
        frame = frame[frame["site"] == site]
    if quarter:
        year, month = prefix.split("-")
        months = {f"{year}-{int(month) + offset:02d}" for offset in range(3)}
        photo = frame["photo_date"].str.slice(0, 7)
        frame = frame[photo.isin(months)]
    else:
        frame = frame[frame["photo_date"].str.slice(0, 7) == prefix]
    completed = int((frame["cohort"] == "completed").sum())
    ungraded = int((frame["grade"] == "").sum())
    backlog = int((frame["breach"] == "grader_backlog").sum())
    letters = int((frame["breach"] == "letter_bureau").sum())
    booking = int((frame["breach"] == "booking").sum())
    return (
        f"Completed encounters: {completed}\n"
        f"Ungraded photographs: {ungraded}\n"
        f"Grader backlog: {backlog}\n"
        f"Letter bureau: {letters}\n"
        f"Booking delay: {booking}\n"
    )
