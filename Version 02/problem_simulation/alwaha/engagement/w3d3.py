"""rel-w3d3 gold. Held-out questions and spans stay out of the lesson prose."""

from __future__ import annotations

from alwaha.config.profile import Profile
from alwaha.engagement.w3d3_docs import CASE_DATE, V4, catalog_rows, feed, leaflet_titles, photo, snapshot
from alwaha.engagement.w3d3_rows import held_questions
from alwaha.engagement.w3d3_rules import answer, apply, booking, lookup, vision_clause

_HOURS = "held-hours"
_LEAFLET = "held-leaflet"


def _question(question_id: str) -> dict:
    return next(row for row in held_questions() if row["question_id"] == question_id)


def gold(profile: Profile) -> dict:
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
