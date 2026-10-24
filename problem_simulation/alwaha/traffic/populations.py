"""Scripted patients, caregivers, and coordinators against the assistant contract."""

from __future__ import annotations

from reference.assistant import Store, approve, chat


def cases() -> list[dict]:
    return [
        {"id": "pop-status", "body": {"message": "Where is my referral?"}, "check": "status"},
        {"id": "pop-book", "body": {"message": "Book a morning slot", "slot": "slot-book"}, "check": "hold"},
        {"id": "pop-literacy", "body": {"message": "slot?"}, "check": "status"},
        {"id": "pop-caregiver", "body": {"message": "Book for my mother", "grant": "expired"}, "check": "refuse"},
        {"id": "pop-resident", "body": {"message": "Book the slot", "insurance": "lapsed"}, "check": "refuse"},
        {"id": "race-slot", "body": {"message": "Book this slot", "slot": "slot-race"}, "check": "race"},
        {"id": "coord-sim", "body": {"message": "Book after review", "slot": "slot-coord"}, "check": "approve-once"},
        {"id": "cc-sim", "body": {"message": "Where is my referral?"}, "check": "summary"},
    ]


def run(_store: Store | None = None) -> list[dict]:
    return [{"id": case["id"], "ok": _check(Store(), case)} for case in cases()]


def _check(store: Store, case: dict) -> bool:
    kind = case["check"]
    got = chat(store, case["body"])
    if kind == "status":
        return any(tool.get("tool") == "status" for tool in got["tool_trace"]) and not got["pending_approval_ids"]
    if kind == "hold":
        return bool(got["pending_approval_ids"]) and "booked" not in got["reply"].lower()
    if kind == "refuse":
        return not got["pending_approval_ids"] and not got["tool_trace"]
    if kind == "race":
        return _race(store, case["body"]["slot"])
    if kind == "approve-once":
        return _once(store, got)
    if kind == "summary":
        return "status" in got["reply"].lower() or any(tool.get("tool") == "status" for tool in got["tool_trace"])
    return False


def _race(store: Store, slot: str) -> bool:
    first = chat(store, {"message": "Book this slot", "slot": slot, "actor": "a"})
    second = chat(store, {"message": "Book this slot", "slot": slot, "actor": "b"})
    if not first["pending_approval_ids"] or not second["pending_approval_ids"]:
        return False
    winner = approve(store, first["pending_approval_ids"][0])
    loser = approve(store, second["pending_approval_ids"][0])
    return winner.get("ok") is True and loser.get("ok") is False


def _once(store: Store, got: dict) -> bool:
    if not got["pending_approval_ids"]:
        return False
    approval = got["pending_approval_ids"][0]
    first = approve(store, approval)
    replay = approve(store, approval)
    return first.get("ok") is True and replay == first
