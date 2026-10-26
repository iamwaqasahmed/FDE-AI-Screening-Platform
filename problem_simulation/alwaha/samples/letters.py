"""Short referral letters. One of them carries the profile watermark.

Six letters are fixed aside from the last clinic sentence, which follows the seed. The shared eye-clinic paragraph is repeated, and the watermark is appended only on the letter that carries it. The opening line names specialty as the baseline field.
"""

from __future__ import annotations


def letters_text(canary: str, seed: int) -> str:
    """Return the referral-letter markdown, with the watermark on one section.

    An even seed uses the heart-clinic sentence for the last letter. An odd seed uses the chest-clinic sentence, so two profiles do not share that section.
    """
    shared = (
        "Please see this patient in the eye clinic. "
        "They can travel on Sunday. Bring the referral paper."
    )
    # Even seeds ask for the heart clinic. Odd seeds ask for the chest clinic.
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
