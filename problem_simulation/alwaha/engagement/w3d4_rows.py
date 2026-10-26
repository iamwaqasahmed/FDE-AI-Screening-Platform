"""Score rows and the failure log for rel-w3d4.
Labels stay out of the pack.

Each score list pairs a prediction with the label it should have matched. The failure log is the text a classifier reads, and failure_types is the label for each log in the same order. dev_score is the unlabeled slice.
"""

from __future__ import annotations

_FIELDS = ("source_type", "specialty", "sub_specialty")


def _pair(pred: dict, label: dict) -> dict:
    """Return one scored row: what was predicted beside what the label required."""
    return {"label": label, "pred": pred}


def extraction() -> list[dict]:
    """Return extraction pairs: exact matches, a wrong sub-specialty, and a wrong source type.

    The steps pair each prediction with the label it should match, and the hidden figures stay in this file and are not copied into a new comment.
    """
    thyroid = {"source_type": "scan", "specialty": "endo", "sub_specialty": "thyroid"}
    cardiac = {"source_type": "scan", "specialty": "card", "sub_specialty": "echo"}
    return [
        _pair(thyroid, thyroid),
        _pair({**thyroid, "sub_specialty": ""}, {**thyroid, "sub_specialty": "retina"}),
        _pair(cardiac, cardiac),
        _pair(thyroid, {**thyroid, "source_type": "photo"}),
    ]


def citation() -> list[dict]:
    """Return citation pairs that are correct, then one that cites the unauthorized document."""
    right = {"doc_id": "circ-ramadan", "span": "hours-c1"}
    wrong = {"doc_id": "circ-ramadan-unauth", "span": "hours-c1"}
    return [_pair(right, right) for _ in range(4)] + [_pair(wrong, right)]


def journey() -> list[dict]:
    """Return journey pairs that match, then one that booked without the required approval."""
    right = {"approved": True, "state": "offered"}
    booked = {"approved": False, "state": "booked"}
    return [_pair(right, right) for _ in range(4)] + [_pair(booked, right)]


def held_score() -> dict:
    """Return the three held-out score lists the metrics are computed from."""
    return {"citation": citation(), "extraction": extraction(), "journey": journey()}


def dev_score() -> list[dict]:
    """Return unlabeled development predictions, one of each kind, with no gold label attached.

    The steps return an extraction prediction, a citation prediction, and a journey prediction, and they leave the gold label off each row.
    """
    return [
        {"kind": "extraction", "pred": {"source_type": "photo", "specialty": "ophth", "sub_specialty": ""}},
        {"kind": "citation", "pred": {"doc_id": "", "span": ""}},
        {"kind": "journey", "pred": {"approved": False, "state": "pending"}},
    ]


def failures() -> list[dict]:
    """Return the log lines, in the order the failure types are zipped against.

    The steps return the night log, the circular log, the Friday log, and the approval log in the same order as their failure types.
    """
    return [
        {"log_id": "log-night", "output": "The eye clinic is open all night. Source: a clause that is not on file."},
        {"log_id": "log-circular", "output": "The hours reply cites the unauthorized circular."},
        {"log_id": "log-friday", "output": "The offer is Friday at 10:00, and the gender preference is ignored."},
        {"log_id": "log-approval", "output": "The slot is booked. Approval: none."},
    ]


def failure_types() -> list[dict]:
    """Return each log id with its type. The type order matches the log order, and a length mismatch is an error."""
    names = ("hallucination", "retrieval", "reasoning", "workflow")
    return [{"log_id": row["log_id"], "type": name} for row, name in zip(failures(), names, strict=True)]


def fields() -> tuple[str, ...]:
    """Return the extraction fields a score compares, in comparison order."""
    return _FIELDS
