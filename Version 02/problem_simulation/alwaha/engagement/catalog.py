"""Twelve persona records. Public card, hidden facts, and the question tree."""

from __future__ import annotations

from alwaha.engagement.roster_b import ROSTER_B

# A tree row is (node_id, keywords, answer, releases, parent).

ROSTER_A: tuple[dict, ...] = (
    {
        "id": "cdo",
        "name": "Layla Al-Harbi",
        "role": "Chief Digital and Transformation Officer",
        "says_first": "The virtual front desk, including triage, goes live before Ramadan.",
        "goals": ("One front door for every hospital.", "Live before Ramadan."),
        "facts": (("gpu-lead-time", "The board date assumes a GPU purchase, and that purchase takes 16 weeks."),),
        "banned": ("Triage is already approved.",),
        "tree": (
            ("deadline", ("deadline", "date", "ramadan", "when", "live"), "The board has already named a date, and it sits just before Ramadan.", (), ""),
            ("purchase", ("gpu", "purchase", "buy", "procurement", "hardware"), "That date only holds if the hardware is already here. The board date assumes a GPU purchase, and that purchase takes 16 weeks.", ("gpu-lead-time",), "deadline"),
        ),
    },
    {
        "id": "med-dir",
        "name": "Dr. Faisal Al-Otaibi",
        "role": "Medical Director",
        "says_first": "Clinicians own urgency.",
        "goals": ("A clinician decides every clinical urgency.", "Every return is seen by a person."),
        "facts": (
            ("red-flag-doc", "The red-flag list is the document pol-clinical-safety."),
            ("human-return", "A human must see every return before it is sent."),
        ),
        "banned": ("The assistant may set clinical urgency.",),
        "tree": (
            ("urgency", ("urgency", "clinician", "triage", "clinical"), "A clinician assigns urgency. The assistant does not.", (), ""),
            ("red-flag", ("red", "flag", "phrase", "list", "document"), "The red-flag list is the document pol-clinical-safety.", ("red-flag-doc",), "urgency"),
            ("returns", ("return", "referral", "human", "approve"), "A human must see every return before it is sent.", ("human-return",), "urgency"),
        ),
    },
    {
        "id": "access-mgr",
        "name": "Noura Al-Qahtani",
        "role": "Director of Patient Access",
        "says_first": "No-shows dominate the cost.",
        "goals": ("Shorter waits.", "A quieter contact center."),
        "facts": (
            ("returns-and-slots", "The return loop and the unused sessions cost more than the no-shows once they are counted."),
            ("reason-mix", "A large share of contact-center calls are people asking for the status of a referral."),
        ),
        "banned": ("No-shows are the largest cost in the cluster.",),
        "tree": (
            ("cost", ("cost", "no-show", "noshow", "dna", "miss"), "No-shows are what I feel in the clinic. The ledger is a different story.", (), ""),
            ("returns", ("return", "unused", "session", "slot", "bounce"), "The return loop and the unused sessions cost more than the no-shows once they are counted.", ("returns-and-slots",), "cost"),
            ("calls", ("call", "contact", "reason", "status", "phone"), "A large share of contact-center calls are people asking for the status of a referral.", ("reason-mix",), "cost"),
        ),
    },
    {
        "id": "phc-lead",
        "name": "Dr. Hassan Al-Dosari",
        "role": "PHC network lead",
        "says_first": "Hospitals return referrals arbitrarily.",
        "goals": ("Fewer returned referrals.", "A template the PHCs can trust."),
        "facts": (("templates-v3", "phc-templates still generates criteria v3."),),
        "banned": ("Returns have no cause in the template.",),
        "tree": (
            ("returns", ("return", "referral", "hospital", "bounce", "page"), "A returned referral comes back with a short reason on the page.", (), ""),
            ("template", ("template", "version", "criteria", "form", "v3"), "Look at the form the PHC actually sends. phc-templates still generates criteria v3.", ("templates-v3",), "returns"),
        ),
    },
    {
        "id": "coord-lead",
        "name": "Maha Al-Shammari",
        "role": "Referral coordinator lead",
        "says_first": "The queue is the problem.",
        "goals": ("A queue a coordinator can finish.", "Notes the next person can read."),
        "facts": (
            ("shorthand", "The shorthand the PHCs use lives in the note, not in a coded field."),
            ("thursday", "Approvals on Thursday afternoon get rubber-stamped."),
            ("v4-draft", "Criteria v4 was circulated as a draft. It is not the version the templates use."),
        ),
        "banned": ("Thursday approvals are reviewed with care.",),
        "tree": (
            ("queue", ("queue", "backlog", "coordinator", "work"), "The queue is long because each referral takes a second reading.", (), ""),
            ("notes", ("note", "shorthand", "text", "free"), "The shorthand the PHCs use lives in the note, not in a coded field.", ("shorthand",), "queue"),
            ("thursday", ("thursday", "afternoon", "stamp", "rubber"), "Approvals on Thursday afternoon get rubber-stamped.", ("thursday",), "queue"),
            ("draft", ("draft", "v4", "circulated", "version"), "Criteria v4 was circulated as a draft. It is not the version the templates use.", ("v4-draft",), "queue"),
        ),
    },
    {
        "id": "dpo",
        "name": "Sara Al-Mutairi",
        "role": "Data Protection Officer",
        "says_first": "Patient data needs care.",
        "goals": ("Patient data stays in the private cloud.", "Training data stays here too."),
        "facts": (("unsigned-ruling", "An unsigned ruling says patient data stays off the external model ext-large, and training stays on the private cloud."),),
        "banned": ("The external model may receive identified patient data.",),
        "tree": (
            ("care", ("data", "patient", "privacy", "protection"), "I have a draft on my desk. It is not signed.", (), ""),
            ("ruling", ("ruling", "unsigned", "cloud", "train", "external", "model"), "An unsigned ruling says patient data stays off the external model ext-large, and training stays on the private cloud.", ("unsigned-ruling",), "care"),
        ),
    },
)

PERSONAS: tuple[dict, ...] = ROSTER_A + ROSTER_B
