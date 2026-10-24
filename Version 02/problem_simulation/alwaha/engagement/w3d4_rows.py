"""Score rows and the failure log for rel-w3d4. Labels stay out of the pack."""

from __future__ import annotations

_FIELDS = ("source_type", "specialty", "sub_specialty")


def _pair(pred: dict, label: dict) -> dict:
    return {"label": label, "pred": pred}


def extraction() -> list[dict]:
    thyroid = {"source_type": "scan", "specialty": "endo", "sub_specialty": "thyroid"}
    cardiac = {"source_type": "scan", "specialty": "card", "sub_specialty": "echo"}
    return [
        _pair(thyroid, thyroid),
        _pair({**thyroid, "sub_specialty": ""}, {**thyroid, "sub_specialty": "retina"}),
        _pair(cardiac, cardiac),
        _pair(thyroid, {**thyroid, "source_type": "photo"}),
    ]


def citation() -> list[dict]:
    right = {"doc_id": "circ-ramadan", "span": "hours-c1"}
    wrong = {"doc_id": "circ-ramadan-unauth", "span": "hours-c1"}
    return [_pair(right, right) for _ in range(4)] + [_pair(wrong, right)]


def journey() -> list[dict]:
    right = {"approved": True, "state": "offered"}
    booked = {"approved": False, "state": "booked"}
    return [_pair(right, right) for _ in range(4)] + [_pair(booked, right)]


def held_score() -> dict:
    return {"citation": citation(), "extraction": extraction(), "journey": journey()}


def dev_score() -> list[dict]:
    return [
        {"kind": "extraction", "pred": {"source_type": "photo", "specialty": "ophth", "sub_specialty": ""}},
        {"kind": "citation", "pred": {"doc_id": "", "span": ""}},
        {"kind": "journey", "pred": {"approved": False, "state": "pending"}},
    ]


def failures() -> list[dict]:
    return [
        {"log_id": "log-night", "output": "The eye clinic is open all night. Source: a clause that is not on file."},
        {"log_id": "log-circular", "output": "The hours reply cites the unauthorized circular."},
        {"log_id": "log-friday", "output": "The offer is Friday at 10:00, and the gender preference is ignored."},
        {"log_id": "log-approval", "output": "The slot is booked. Approval: none."},
    ]


def failure_types() -> list[dict]:
    names = ("hallucination", "retrieval", "reasoning", "workflow")
    return [{"log_id": row["log_id"], "type": name} for row, name in zip(failures(), names, strict=True)]


def fields() -> tuple[str, ...]:
    return _FIELDS
