"""Injection sources, the model register, and the vendor's region."""

from __future__ import annotations

from course.checks.rules import same_set


def injections(answer: dict, gold: dict) -> bool:
    row = gold["items"]["injections"]
    return all(same_set(answer.get(key, []), row[key]) for key in ("documents", "complaints", "threads"))


def models(answer: dict, gold: dict) -> bool:
    row = gold["items"]["models"]
    if answer.get("embedding") != row["embedding"]:
        return False
    lists = ("authority_zone", "official_sensitive", "public_only")
    return all(same_set(answer.get(key, []), row[key]) for key in lists)


def vendor_region(answer: dict, gold: dict) -> bool:
    row = gold["items"]["vendor_region"]
    texts = ("document_id", "clause", "region")
    return all(str(answer.get(key, "")) == str(row[key]) for key in texts) and answer.get("needs_dpo_decision") is True
