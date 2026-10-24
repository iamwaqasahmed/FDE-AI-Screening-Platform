"""Participant pages for rel-w4d5. The lag and the survey count stay out."""

from __future__ import annotations

from alwaha.engagement.w4d5_rows import CASE_DATE

QUESTIONS = (
    "Which problem is first, and what does it depend on?",
    "What does a contact-center handoff contain?",
    "Which event does consultant leave create?",
    "Which benefit is counted twice?",
    "What channel reaches phone-only patients?",
)


def release_note(files: list[str]) -> str:
    listed = "\n".join(f"- [{name}]({name})" for name in files if name != "README.md")
    return f"""# rel-w4d5

From: Enterprise Architect
Case date: {CASE_DATE}

The contact center, the warehouse feed, and HR asked to be connected. Staff sign-in and the event bus are confirmed after the drill. The day notes are [Week 4, Day 5](../../Week%2004/Day%2005/README.md).

Files:

{listed}
"""


def steer_page() -> str:
    numbered = "\n".join(f"{index}. {text}" for index, text in enumerate(QUESTIONS, start=1))
    return f"""# steer-w4

The steering committee asks these questions. The committee is cdo, med-dir, dpo, ciso, and finance.

{numbered}
"""


def stage_gate() -> str:
    return """# pol-stage-gate

Six gates:

- G0 intake
- G1 risk tier
- G2 DPIA
- G3 pilot approval
- G4 go-live
- G5 post-launch review

G4 is go-live. The clinical safety owner agrees at this gate.
"""


def architecture_deploy() -> str:
    return """# Deployment architecture

## Zones

## Flows

## Boundary
"""


def operations() -> str:
    return """# Operations

## Owners

## RACI

## Gate

## Incident
"""


def proposal() -> str:
    return """# Proposal

## Client

## Ranking

## Roadmap

## Plan

## Metrics

## Adoption
"""


def readout() -> str:
    return """# Readout

## Ranking

## Handoff

## Leave

## Benefit

## Channel

## Asks
"""


def retro() -> str:
    return """# Retro

## Keep

## Drop

## Open
"""


def sprint() -> str:
    return """# Sprint

## Order
"""


def knowledge() -> str:
    return """# Knowledge

1.

2.
"""
