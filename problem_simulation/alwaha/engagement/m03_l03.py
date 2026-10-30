"""rel-m03-l03 gold.
Held-out questions and spans stay out of the lesson prose.

gold applies the change feed to the snapshot, then asks the reference retriever the held-out questions. The result also names the access example, the catalog lookup, the booking conflict, and the wording the page export dropped.
"""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.m03_l03_docs import CASE_DATE, V4, catalog_rows, feed, leaflet_titles, photo, snapshot
from alwaha.engagement.m03_l03_rows import held_questions
from alwaha.engagement.m03_l03_rules import answer, apply, booking, lookup, vision_clause

_HOURS = "held-hours"
_LEAFLET = "held-leaflet"


def _question(question_id: str) -> dict:
    """Return the held-out question with this id. The held list is required to contain it."""
    return next(row for row in held_questions() if row["question_id"] == question_id)


def gold(profile: Profile) -> dict:
    """Return the retrieval expectations after the feed has been applied.

    The profile is unused because the library and the questions do not move with the seed. Each held question is paired with the citation or refusal the reference answer returns.
    """
    # Nothing here depends on the profile. The name is kept so every gold function has the same signature.
    del profile
    state = apply(snapshot(), feed())
    docs = state["docs"]
    held = [{"expect": answer(question, docs), "question": question} for question in held_questions()]
    current, earlier = leaflet_titles()
    return {
        "acl_blocked": "leaflet-staff",
        "acl_doc": "leaflet-prep",
        "acl_question": _question(_LEAFLET),
        "catalog": lookup(catalog_rows(), "endo"),
        "case_date": CASE_DATE,
        "changed": list(state["touched"]),
        "conflict": booking(docs, "h-safra"),
        "held": held,
        "hybrid_doc": "circ-ramadan",
        "hybrid_question": _question(_HOURS),
        "leaflets": [current, earlier],
        "v4": list(V4),
        "vector_doc": "circ-ramadan-unauth",
        "vision": vision_clause(photo()),
    }
