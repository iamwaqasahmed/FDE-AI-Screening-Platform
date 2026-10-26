"""Participant pages for rel-w2d5.
Clinic codes stay out of the prose.

These strings are the change request, the schedule note, the steering questions, and the schedule interface. They describe a nightly file and a real-time booking that stays queued. The steering page numbers the committee's questions in the stored order.
"""

from __future__ import annotations

from alwaha.engagement.w2d5 import CARD, QUESTIONS


def change_note() -> str:
    return f"""# cr-ain

{CARD}

Sequence the work. A refusal needs a reason. The interface note for sched-ain is in this pack.

Case date: 2027-01-21.
"""


def interface_note() -> str:
    return """# sched-ain

Ain Diabetes and Eye Center (`h-ain`) sits in `zone-hospital`.

The schedule is a nightly full file. The last file wins. There is no intraday API. The file uses local clinic codes. A missed night leaves the previous file.

A real-time booking returns queued until that file is applied.
"""


def steer_page() -> str:
    """Return the steering page for this pack.

    The questions are numbered in the stored order so the committee file matches that list.
    """
    numbered = "\n".join(f"{index}. {text}" for index, text in enumerate(QUESTIONS, start=1))
    return f"# steer-w2\n\nThe steering committee asks these questions.\n\n{numbered}\n"


def schedule_spec() -> str:
    return """openapi: 3.0.3
info:
  title: sched-ain
  version: "1"
paths:
  /files:
    post:
      operationId: acceptFile
      responses:
        "202":
          description: The nightly file is stored. The last file wins.
  /book:
    post:
      operationId: book
      responses:
        "202":
          description: A real-time booking returns queued.
"""
