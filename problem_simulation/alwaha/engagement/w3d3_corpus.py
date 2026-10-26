"""Hours, leaflets, and the other rel-w3d3 documents.

doc builds one document from shared defaults, then the caller’s fields, then the body that was actually stored. The hours, leaflet, and extra helpers are the texts the snapshot and the feed assemble. photo is the page whose export is shorter than its transcription.
"""

from __future__ import annotations

import hashlib

OPENED = "2026-01-01"


def _hash(body: str) -> str:
    """Return a content hash of the body, so two texts cannot share a hash by accident."""
    return "sha256:" + hashlib.sha256(body.encode()).hexdigest()[:16]


def doc(**kwargs: object) -> dict:
    """Return one document.

    Missing fields take the staff, in-force, criteria defaults. Caller fields then override those defaults. The body and its hash are written last, from the text that was actually stored, so a caller cannot leave a stale hash behind.
    """
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
    # Caller fields win first. Body and hash are then taken from the text actually stored.
    row["body"] = body
    row["content_hash"] = _hash(body)
    return row


def hours() -> tuple[dict, dict]:
    """Return the authorized hours and the unauthorized copy that says the opposite.

    Both share a code. Only the status tells them apart, which is why a search that ignores status can cite the wrong one.
    """
    # Authorized hours.
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
    # Unauthorized copy. It shares the code and says the opposite.
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
    """Return the current public leaflet, the earlier public edition, and the staff-only note.

    They share a code. Audience and version are what keep the staff note and the old edition from being the public answer.
    """
    # Current public edition.
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
    # Earlier public edition.
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
    # Staff-only note. It is not the public answer.
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
    """Return the restricted safety list, the cluster booking window, and the shorter site window.

    The site window is the local policy. The cluster window is the one the conflict helper treats as the winner.
    """
    # Restricted safety list.
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
    # Cluster window. The conflict helper treats this as the winner.
    cluster = doc(
        body="The cluster booking window is 14 days. Code book-cluster.",
        clause_id="book-cluster-c1",
        code="book-cluster",
        doc_id="pol-booking-cluster",
        family="access-policy",
        title="Cluster booking window",
        version=1,
    )
    # Shorter window for the site.
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
    """Return the photographed page. The export is shorter than the transcription."""
    return {
        "doc_id": "photo-prep",
        "export": "Bring your card.",
        "transcription": "Bring your card. Bring the fasting slip.",
    }


def catalog_rows() -> list[dict]:
    """Return the clinic catalog row the lookup is checked against."""
    return [{"clinic": "endo", "code": "cat-endo", "prep": "fast from midnight"}]


def leaflet_titles() -> tuple[str, str]:
    """Return the current leaflet title and the earlier edition's title. The staff note is not included."""
    current, earlier, _staff = leaflets()
    return current["title"], earlier["title"]
