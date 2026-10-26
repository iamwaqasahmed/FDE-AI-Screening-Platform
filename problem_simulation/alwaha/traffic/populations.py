"""Scripted patients, caregivers, and coordinators against the assistant contract.

cases() lists the status, booking, literacy, caregiver, resident, race, coordinator, and contact-center scripts. run() scores each case on a fresh store so holds do not leak across cases. _check() applies the named check. _race() gives the slot to the first approval. _once() checks that a replay returns the same result.
"""

from __future__ import annotations

from reference.assistant import Store, approve, chat


def cases() -> list[dict]:
    """Return the population cases.

    Each case has an id, the body passed to the assistant, and the check name that decides a pass.
    """
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
    """Score every case on its own fresh store and return the id with the result.

    The store argument is ignored. Each case builds a new store so one case cannot spend a hold created by another.
    """
    # A new store per case keeps holds from leaking across the list.
    return [{"id": case["id"], "ok": _check(Store(), case)} for case in cases()]


def _check(store: Store, case: dict) -> bool:
    """Return whether this case's check passed.

    status passes when a status tool ran and nothing is waiting for approval. hold passes when an approval is waiting and the reply has not booked. refuse passes when there is no approval and no tool trace. race delegates to the slot check. approve-once delegates to the replay check. summary passes when the reply mentions status or a status tool ran. Any other check name fails.
    """
    kind = case["check"]
    got = chat(store, case["body"])
    if kind == "status":
        # A status answer uses the status tool and does not open an approval.
        return any(tool.get("tool") == "status" for tool in got["tool_trace"]) and not got["pending_approval_ids"]
    if kind == "hold":
        # The slot is held for approval, and the reply has not completed a booking.
        return bool(got["pending_approval_ids"]) and "booked" not in got["reply"].lower()
    if kind == "refuse":
        # A refusal leaves no approval and runs no tool.
        return not got["pending_approval_ids"] and not got["tool_trace"]
    if kind == "race":
        return _race(store, case["body"]["slot"])
    if kind == "approve-once":
        return _once(store, got)
    if kind == "summary":
        # Either the reply mentions status or a status tool ran.
        return "status" in got["reply"].lower() or any(tool.get("tool") == "status" for tool in got["tool_trace"])
    # An unknown check name fails.
    return False


def _race(store: Store, slot: str) -> bool:
    """Return whether the first approval takes the slot and the second is refused.

    Both actors must receive a pending approval before either approval is decided. The first approval wins the slot. The second approval fails.
    """
    first = chat(store, {"message": "Book this slot", "slot": slot, "actor": "a"})
    second = chat(store, {"message": "Book this slot", "slot": slot, "actor": "b"})
    # Both actors have to be holding the slot before either approval is decided.
    if not first["pending_approval_ids"] or not second["pending_approval_ids"]:
        return False
    winner = approve(store, first["pending_approval_ids"][0])
    loser = approve(store, second["pending_approval_ids"][0])
    # The first approval takes the slot. The second approval is refused.
    return winner.get("ok") is True and loser.get("ok") is False


def _once(store: Store, got: dict) -> bool:
    """Return whether the first approval succeeds and a replay returns that same result.

    A reply with no pending approval fails. The replay must equal the first result, so a second call does not produce a new outcome.
    """
    if not got["pending_approval_ids"]:
        # There is nothing to approve, so this case fails.
        return False
    approval = got["pending_approval_ids"][0]
    first = approve(store, approval)
    replay = approve(store, approval)
    # The second call returns the same result as the first.
    return first.get("ok") is True and replay == first
