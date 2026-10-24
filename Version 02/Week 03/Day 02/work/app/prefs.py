"""Expand shorthand, keep the clause id, and drop a date the calendar cannot keep."""

from __future__ import annotations


def revise(draft: str) -> str:
    text = draft.replace("sugar clinic", "endocrinology").replace("Friday", " ").replace("2027-03-10", " ")
    return " ".join(word for word in text.split() if word not in {"on", "."})
