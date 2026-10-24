"""Hours, leaflets, and the other rel-w3d3 documents."""

from __future__ import annotations

import hashlib

OPENED = "2026-01-01"


def _hash(body: str) -> str:
    return "sha256:" + hashlib.sha256(body.encode()).hexdigest()[:16]


def doc(**kwargs: object) -> dict:
    body = str(kwargs["body"])
    row = {
        "audience": "staff",
        "clause_id": "",
        "code": "",
        "content_hash": _hash(body),
        "doc_id": "",
        "effective": OPENED,
        "family": "criteria",
        "site": "cluster",
        "specialty": "",
        "status": "in_force",
        "sunset": "",
        "supersedes": "",
        "title": "",
        "version": 3,
    }
    row.update(kwargs)
    row["body"] = body
    row["content_hash"] = _hash(body)
    return row


def hours() -> tuple[dict, dict]:
    current = doc(
        audience="public",
        body="Code hrs-ramadan closes the evening clinics at 21:00.",
        clause_id="hrs-ramadan-c1",
        code="hrs-ramadan",
        doc_id="circ-ramadan",
        family="hours",
        title="Ramadan hours",
        version=1,
    )
    unauthorized = doc(
        audience="public",
        body=(
            "Which evening clinic hours apply in the fasting month. "
            "Which evening clinic hours apply in the fasting month. "
            "Code hrs-ramadan. Stay open past midnight."
        ),
        clause_id="hrs-ramadan-unauth-c1",
        code="hrs-ramadan",
        doc_id="circ-ramadan-unauth",
        family="hours",
        status="unauthorized",
        title="Ramadan hours, unapproved",
        version=1,
    )
    return current, unauthorized


def leaflets() -> tuple[dict, dict, dict]:
    current = doc(
        audience="public",
        body="Code prep-endo. Bring the referral card.",
        clause_id="prep-endo-c1",
        code="prep-endo",
        doc_id="leaflet-prep",
        family="leaflets",
        title="Endocrinology preparation",
        version=2,
    )
    earlier = doc(
        audience="public",
        body="What should a patient bring to endocrinology preparation. Code prep-endo. Earlier edition.",
        clause_id="prep-endo-old-c1",
        code="prep-endo",
        doc_id="leaflet-prep-old",
        family="leaflets",
        title="Endocrinology preparation, earlier edition",
        version=1,
    )
    staff = doc(
        audience="staff",
        body=(
            "What should a patient bring to endocrinology preparation. "
            "What should a patient bring to endocrinology preparation. "
            "Code prep-endo. Staff only."
        ),
        clause_id="prep-endo-staff-c1",
        code="prep-endo",
        doc_id="leaflet-staff",
        family="leaflets",
        title="Endocrinology preparation, staff note",
        version=1,
    )
    return current, earlier, staff


def extras() -> tuple[dict, dict, dict]:
    safety = doc(
        audience="restricted",
        body="Code safety-red stays with records.",
        clause_id="safety-red-c1",
        code="safety-red",
        doc_id="pol-safety",
        family="safety",
        title="Clinical safety list",
        version=1,
    )
    cluster = doc(
        body="The cluster booking window is 14 days. Code book-cluster.",
        clause_id="book-cluster-c1",
        code="book-cluster",
        doc_id="pol-booking-cluster",
        family="access-policy",
        title="Cluster booking window",
        version=1,
    )
    safra = doc(
        body="The h-safra booking window is 3 days. Code book-safra.",
        clause_id="book-safra-c1",
        code="book-safra",
        doc_id="pol-booking-h-safra",
        family="access-policy",
        site="h-safra",
        title="Safra booking window",
        version=1,
    )
    return safety, cluster, safra


def photo() -> dict:
    return {
        "doc_id": "photo-prep",
        "export": "Bring your card.",
        "transcription": "Bring your card. Bring the fasting slip.",
    }


def catalog_rows() -> list[dict]:
    return [{"clinic": "endo", "code": "cat-endo", "prep": "fast from midnight"}]


def leaflet_titles() -> tuple[str, str]:
    current, earlier, _staff = leaflets()
    return current["title"], earlier["title"]
