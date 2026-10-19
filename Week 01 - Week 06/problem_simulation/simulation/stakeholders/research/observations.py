"""Observation notes from two clinic visits. Each note points at a mechanism the data can confirm."""

from __future__ import annotations

from datetime import timedelta

from simulation.corpus.add import add_document
from simulation.world.engagement import KICKOFF
from simulation.world.sites import NCEC, RIVER_SITE, slug

NOTES = {
    NCEC: (
        "Reception staff field several questions an hour from people asking whether their result letter was sent. "
        "They cannot see the bureau's dispatch status, so they promise a call back.",
        "At the grading desk a grader typed an urgent remark into the notes field and left the result column empty. "
        "The worklist sorts by photo date, so that encounter stayed in the normal queue.",
        "Graders on the long afternoon session paused less and moved faster through the worklist late in the day.",
        "Nobody we watched used the vendor score. Staff said hospital images are not sent to the vendor.",
    ),
    RIVER_SITE: (
        "The van arrived late after a long drive. Two booked people did not come; staff said the bus does not run "
        "on that day.",
        "Photographs are copied from the laptop to the shared folder at the end of the day. File names are typed by "
        "hand and some do not follow the pattern.",
        "Staff remembered a week when the laptops would not sync and captures were kept without local ids.",
        "One operator's images were visibly darker. Colleagues said the newer camera software helped.",
        "Reminder texts go out, but staff felt they made little difference here compared with the bus timetable.",
    ),
}


def add_observations(world: dict) -> list[str]:
    added = []
    for offset, (site, notes) in enumerate(sorted(NOTES.items())):
        doc_id = f"research-observation-{slug(site)}"
        body = "\n\n".join(["Observation notes from a half-day visit by the discovery team.", "## What we saw",
                            *[f"- {note}" for note in notes], "## Follow up", "- Check each observation against the data."])
        add_document(world, doc_id, "research", f"Observation notes: {site}", body, KICKOFF + timedelta(days=2 + offset),
                     site=site)
        added.append(doc_id)
    return added
