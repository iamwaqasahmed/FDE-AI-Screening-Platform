"""Short referral letters. One of them carries the profile watermark."""

from __future__ import annotations


def letters_text(canary: str, seed: int) -> str:
    shared = (
        "Please see this patient in the eye clinic. "
        "They can travel on Sunday. Bring the referral paper."
    )
    last = "Please book the heart clinic." if seed % 2 == 0 else "Please book the chest clinic."
    sections = (
        ("letter-01", shared),
        ("letter-02", "Kindly review in endocrinology."),
        ("letter-03", "Referral to cardiology for a new visit."),
        ("letter-04", "Follow up at the retina service."),
        ("letter-05", "Continue at the sugar clinic."),
        ("letter-06", f"{shared}\n\n{canary}"),
        ("letter-07", last),
    )
    body = "\n\n".join(f"## {name}\n\n{text}" for name, text in sections)
    return f"# Referral letters\n\nToday's baseline field is specialty.\n\n{body}\n"
