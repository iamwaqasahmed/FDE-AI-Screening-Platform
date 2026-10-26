"""Written notes for the Day 5 deploy. A miss does not name the clinic code.

Written notes for the later deploy day. A deployment note that promises a live slot is a miss before the shared deployment grader runs. Zones must pair the url with the private zone and the schedule with the hospital zone. The sprint must run smoke, then the change, then the readout, then the retro. The knowledge note must say why the clinic waits and what the next stage adds.
"""

from __future__ import annotations

import re
from pathlib import Path

from alwaha.check.notes_w2d4 import _deployment, _operators
from alwaha.check.rubric import two_answers
from alwaha.check.tables import dict_rows

_PROMISE = (
    "ain has a live slot",
    "h-ain is out of scope",
    "every hospital has a live slot api",
    "monitoring is complete",
)


def _text(path: Path) -> str | None:
    """Return the file text, or nothing when the path is not a file.

    Callers treat a missing note as a failed content check instead of raising.
    """
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def promises_slot(text: str) -> bool:
    """Return true when the text contains any live-slot promise from the tuple above.

    The scan is case-insensitive. Callers use it for the deployment note and, from another module, for the readout.
    """
    lowered = text.lower()
    # Any one of the over-claim phrases is a live-slot promise.
    return any(phrase in lowered for phrase in _PROMISE)


def _zones(work: Path) -> list[str]:
    """Return the zone misses.

    The url must be paired with the private zone. The schedule name must be paired with the hospital zone. Each missing pair is its own miss.
    """
    rows = dict_rows(_text(work / "zones.md") or "", {"surface", "zone"})
    problems = []
    paired = {(row["surface"], row["zone"]) for row in rows} if rows else set()
    if ("url", "zone-private") not in paired:
        problems.append("the url is not in zone-private")
    if ("sched-ain", "zone-hospital") not in paired:
        problems.append("the file path is not in zone-hospital")
    return problems


def _sprint(work: Path) -> list[str]:
    """Return the sprint miss unless smoke, the change, the readout, and the retro appear in that order.

    A missing word makes a position negative and fails the order.
    """
    lowered = (_text(work / "sprint.md") or "").lower()
    smoke = lowered.find("smoke")
    change = lowered.find("change")
    readout = lowered.find("readout")
    retro = lowered.find("retro")
    if not (0 <= smoke < change < readout < retro):
        return ["sprint.md does not sequence the change before the readout"]
    return []


def _knowledge(work: Path) -> list[str]:
    """Return the knowledge misses.

    Fewer than two numbered answers, or a note that fails the two-answer helper, is the two-answer miss. The first answer must say why the clinic waits, using a nightly, file, or queued word. The second must name the next stage by the later week or by the stage phrase in the condition.
    """
    text = _text(work / "knowledge.md")
    answers = [] if text is None else [line for line in text.splitlines() if re.match(r"\s*\d+\.\s+\S", line)]
    if len(answers) < 2 or not two_answers(text or ""):
        return ["knowledge.md needs two answers"]
    problems = []
    first = answers[0].lower()
    if not any(token in first for token in ("nightly", "file", "queued")):
        problems.append("knowledge.md does not say why ain waits")
    second = answers[1].lower()
    # Either phrase is enough. Both missing means the note never says what the next stage adds.
    if "week 4" not in second and "stage 2" not in second:
        problems.append("knowledge.md does not say what stage 2 adds")
    return problems


def written_problems(work: Path, pack: Path, gold: dict) -> list[str]:
    """Return the live-slot promise, the shared deployment misses, the zones, the operator steps, the sprint, and the knowledge misses.

    The shared deployment helper is the one from the previous day. Operator steps are graded there too.
    """
    problems = []
    note = _text(work / "deployment.md") or ""
    if promises_slot(note):
        problems.append("the deployment note promises a live slot")
    problems.extend(_deployment(work, pack, gold))
    problems.extend(_zones(work))
    problems.extend(_operators(work))
    problems.extend(_sprint(work))
    problems.extend(_knowledge(work))
    return problems
