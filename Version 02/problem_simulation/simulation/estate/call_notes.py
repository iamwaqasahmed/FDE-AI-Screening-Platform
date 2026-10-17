"""Free-text call notes. The reason is in the words; some notes carry the caller's name, phone, and national id."""

from __future__ import annotations

import numpy as np
import pandas as pd

from simulation.corpus.add import pii_spans

REASON_TEXT = {
    "LNR": ("Caller says the results letter never arrived after screening.", "No letter received since the eye photos, wants to know the outcome.",
            "Says she was told a letter would follow and nothing came.", "Asking where the results letter is, screened weeks ago."),
    "CGA": ("Cannot get an appointment at the eye clinic, told no slots.", "Referred to hospital but no clinic date offered yet.",
            "Wants a hospital appointment, says the clinic keeps cancelling.", "Unable to book follow-up, no availability shown."),
    "RBK": ("Wants to move the screening appointment to another day.", "Rebooked to a later slot at caller's request.",
            "Asked to change appointment time, done.", "Moving appointment because of work."),
    "RES": ("Asking what the screening result means.", "Query about the grade on the letter.", "Wants the result explained.",
            "Asked whether the result needs any action."),
    "TRN": ("Needs help with transport to the clinic.", "Asking about parking and buses for the clinic.", "Cannot travel to the site, asked about outreach.",
            "Transport query for an elderly relative."),
    "SMS": ("Got a text but the date does not match the letter.", "Text reminder came for an appointment already cancelled.",
            "Asking if the text message is genuine.", "Did not get the reminder text."),
    "MOV": ("Has moved house, new address given.", "Change of address, moved out of the area.", "Updating contact details after a move.",
            "Moved last year, letters going to old address."),
    "CMP": ("Unhappy with the wait, wants to complain.", "Wants to make a formal complaint about the service.",
            "Complaint about how the last visit was handled.", "Raising a complaint about the service."),
    "OTH": ("General enquiry, answered.", "Asked about eligibility for screening.", "Wrong number, meant for the GP surgery.",
            "Asked for the clinic address."),
}
CLOSERS = ("", " Advised to wait five working days.", " Passed to the booking team.", " Call back requested.", " Resolved on the call.")


def notes(reasons: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    variant = rng.integers(0, 4, len(reasons))
    closer = rng.integers(0, len(CLOSERS), len(reasons))
    return np.array([REASON_TEXT[code][index] + CLOSERS[end] for code, index, end in zip(reasons, variant, closer)], dtype=object)


def caller_pool(people: pd.DataFrame, phones: pd.Series, nationals: pd.Series) -> pd.DataFrame:
    pool = people[["person_uid", "forename", "surname"]].copy()
    pool["phone"] = pool["person_uid"].map(phones).fillna("")
    pool["national_id"] = pool["person_uid"].map(nationals).fillna("")
    return pool[(pool["phone"] != "") & (pool["national_id"] != "")].sort_values("person_uid").reset_index(drop=True)


def with_pii(call_ids: list[str], texts: list[str], callers: pd.DataFrame, rng: np.random.Generator) -> tuple[list[str], list[dict]]:
    """Prefix each note with caller details. Returns the new texts and the gold spans."""
    out, spans = [], []
    for call_id, text, caller in zip(call_ids, texts, callers.itertuples(index=False)):
        phone = _phone(caller.phone, rng)
        name = f"{caller.forename} {caller.surname}"
        style = int(rng.integers(0, 3))
        if style == 0:
            note = f"Caller {name}, tel {phone}, national id {caller.national_id}. {text}"
        elif style == 1:
            note = f"{text} Spoke to {name} on {phone}."
        else:
            note = f"{name} (id {caller.national_id}) rang. {text} Best number {phone}."
        out.append(note)
        values = {"name": name, "phone": phone, "national_id": caller.national_id}
        spans.extend({"call_id": call_id, **span} for span in pii_spans(note, values))
    return out, spans


def _phone(raw: str, rng: np.random.Generator) -> str:
    return f"{raw[:5]} {raw[5:]}" if rng.random() < 0.5 else raw
