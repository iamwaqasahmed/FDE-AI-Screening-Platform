"""Participant pages for rel-w2d5. Clinic codes stay out of the prose."""

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
