"""Day 1 documents. The body is fixed. The header hash is of the body."""

from __future__ import annotations

import hashlib


def document(doc_id: str, family: str, title: str, audience: str, body: str, effective: str = "2024-06-01") -> str:
    """Return one corpus document with a header in front of the body.

    The header records the identity, the audience, and a hash of the body. Callers share this shape, and the hash changes when the body changes.
    """
    digest = hashlib.sha256(body.encode()).hexdigest()[:16]
    header = "\n".join(
        [
            "---",
            f"doc_id: {doc_id}",
            f"family: {family}",
            f"title: {title}",
            "status: in_force",
            f"effective: {effective}",
            "sunset:",
            "site:",
            f"audience: {audience}",
            "supersedes:",
            f"content_hash: {digest}",
            "---",
            "",
        ]
    )
    return header + body.strip() + "\n"


def stage_gate() -> str:
    body = """
# AI delivery stage gates

The cluster moves an AI system through six gates. A gate is an approval, not a meeting.

- G0 Intake. The problem, the users, and the sponsor are named.
- G1 Risk tier. The clinical and data risk is classed.
- G2 DPIA. The personal-data assessment is accepted.
- G3 Pilot approval. A limited pilot is allowed. A clinician still assigns every clinical urgency.
- G4 Go-live. Security, data protection, and the clinical safety owner agree.
- G5 Post-launch review. The running system is reviewed against the success measures named at intake.

The assistant routes emergency wording to a human. It does not grade urgency.
"""
    return document("pol-stage-gate", "stage-gate", "AI delivery stage gates", "staff", body)


def assistant_use() -> str:
    body = """
# Coding assistant use

Coding assistants may be used on this engagement.

Patient data, secrets, unpublished cluster documents, and the sample referral letter stay out of prompts and out of the repository. Dev credentials stay in credentials/ and are not committed. The watermark in those credentials is not pasted into source, tickets, or prompts.

A pull request that contains the sample letter or the watermark does not pass.
"""
    return document("pol-assistant-use", "security", "Coding assistant use", "staff", body)


def postmortem() -> str:
    body = """
# Postmortem, 2023 chatbot

The chatbot was switched off in 2023. Staff returned to the phone line. This write-up attributes the stop to a busy season and to low usage. It records a plan to revisit a front door in a later year.

The write-up does not attach the steering minutes.
"""
    return document("doc-postmortem-2023", "postmortem", "Postmortem, 2023 chatbot", "staff", body, "2024-01-15")


def minutes() -> str:
    body = """
# Minutes, digital steering, November 2023

The steering group reviewed the chatbot pilot that was switched off. Three notes from the room:

- There was no evaluation set.
- Patient data was sent to a public model.
- The pilot had no named owner.

The group recorded no decision to turn the bot back on.
"""
    return document("doc-minutes-2023-11", "postmortem", "Minutes, digital steering, November 2023", "staff", body, "2023-11-20")


MINUTE_CAUSES = (
    "there was no evaluation set",
    "patient data was sent to a public model",
    "the pilot had no named owner",
)


def fact_problems(minutes_text: str, postmortem_text: str) -> list[str]:
    """Return the mismatches between the minutes and the postmortem.

    A required cause missing from the minutes is reported. The same cause showing up in the postmortem is reported. An empty list means the two documents still split those causes.
    """
    problems = []
    minutes_lower = minutes_text.lower()
    postmortem_lower = postmortem_text.lower()
    for cause in MINUTE_CAUSES:
        if cause not in minutes_lower:
            problems.append(f"minutes missing: {cause}")
        if cause in postmortem_lower:
            problems.append(f"postmortem contains: {cause}")
    return problems


def sample_letter(canary: str) -> str:
    return f"""# Sample referral letter

This letter is synthetic. It is not a patient's record.

From: phc-rim
To: endocrinology at h-wadi
Marker: SAMPLE-REFERRAL-ALWAHA
Reference: {canary}

The note asks for a clinic visit and uses the shorthand "DM fu".
Keep this file out of the starter repository and out of any coding-assistant prompt.
"""


def access_form() -> str:
    return """# Access request

Fill every field. A blank field is not a request.

- Requester:
- Data:
- Purpose:
- Classification:
"""


def zones_page() -> str:
    """Return the page that says where the cluster runs.

    Opening day, working days, zones, and facilities come from the world tables, so the pack page matches those tables.
    """
    from alwaha.world.clock import ENGAGEMENT_OPENS, WORKING_DAYS
    from alwaha.world.sites import SITES, ZONES

    lines = [
        "# Where the cluster runs",
        "",
        f"The engagement opens on {ENGAGEMENT_OPENS}. Working days are {', '.join(WORKING_DAYS)}. Friday and Saturday are the weekend.",
        "",
        "## Zones",
        "",
    ]
    for zone in ZONES:
        extra = zone.get("sites") or zone.get("holds") or ""
        suffix = f" ({extra})" if extra else ""
        if isinstance(extra, tuple):
            suffix = " (" + ", ".join(extra) + ")"
        lines.append(f"- `{zone['id']}`: {zone['name']}{suffix}")
    lines.extend(["", "## Facilities", ""])
    for site in SITES:
        if site["zone"].startswith("zone-"):
            where = f"in `{site['zone']}`"
        else:
            where = "a primary health care center"
        lines.append(f"- `{site['id']}`: {site['name']}, {where}")
    lines.append("")
    return "\n".join(lines)
