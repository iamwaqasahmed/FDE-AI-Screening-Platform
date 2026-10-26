"""Assistant contract for a status question. Booking waits.

The journey check calls reply, health, and approval. A status
question that got a his-wadi read uses the status tool. A question
that asks to book does not call that tool. Leave this file
unchanged. The check does not print the count when the reply is wrong.
It says the count does not match, or that the read failed.
"""

from __future__ import annotations


def health() -> dict:
    """Report the local model and the two dependencies.

    The journey check requires model_hash, prompt_version, and
    dependencies. The values below are the dev stand-in. his-wadi and
    iam are both reported ok.
    """
    return {
        "status": "ok",
        "model_hash": "local-small",
        "prompt_version": "w2d1",
        "dependencies": {"his-wadi": "ok", "iam": "ok"},
    }


def reply(message: str, row: dict, fhir_ok: bool) -> dict:
    """Answer one patient message.

    A message that contains book is refused. booked stays false, and
    the tool list stays empty. A failed read says the hospital record
    could not be read, with the same empty tool list. A successful
    read says the referral is still pending, cites his-wadi, and
    records the status tool. count, state, and facility_id are copied
    from the scenario row. They are not typed by hand. pending stays
    empty. Booking is not this reply.
    """
    base = {
        "reply": "",
        "citations": [],
        "tool_trace": [],
        "pending_approval_ids": [],
        "booked": False,
        "count": None,
        "state": "",
        "facility_id": "",
    }
    if "book" in message.lower():
        base["reply"] = "Booking is a later day."
        return base
    if not fhir_ok:
        base["reply"] = "The hospital record could not be read."
        return base
    base["reply"] = "Your referral is still pending."
    base["citations"] = ["his-wadi"]
    base["tool_trace"] = ["status"]
    base["count"] = row["count"]
    base["state"] = row["state"]
    base["facility_id"] = row["facility_id"]
    return base


def approval(approval_id: str) -> dict:
    """Hold an approval for a later day.

    The id is echoed. The status is later. The journey check rejects
    any other status. This function does not decide the approval.
    """
    return {"id": approval_id, "status": "later"}
