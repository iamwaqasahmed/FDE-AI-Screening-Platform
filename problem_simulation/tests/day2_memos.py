"""Memo text for the Day 2 check tests.

Helpers for the Day 2 checkers. They only build memo text. They do not score it.

approach builds the family table. brief builds the stakeholder lines, the size
table, and the ranking. A test supplies a family function, and sometimes a
replacement for one measured cell, then asks the real checker to grade the result.
"""

from __future__ import annotations

import re
from pathlib import Path

# Source each problem id must cite. The approach checker compares the memo to these paths.
CITATIONS = {
    "p-bounce": "samples/ds-letters.md",
    "p-waitlist": "extracts/access-costs.md",
    "p-dna": "samples/ds-dna.csv",
    "p-status": "samples/ds-messages.csv",
    "p-slots": "extracts/access-costs.md",
    "p-clock": "extracts/dashboard.md",
    "p-info": "patient-rep",
    "p-forecast": "samples/ds-demand.csv",
    "p-triage": "extracts/sponsor-ask.md",
}
# Default brief order. Tests pass a different tuple when they move one problem to the front.
RANK = (
    "p-clock",
    "p-bounce",
    "p-waitlist",
    "p-dna",
    "p-status",
    "p-slots",
    "p-info",
    "p-forecast",
    "p-triage",
)


def approach(gold: dict, measured: dict, family_for, measured_for=None) -> str:
    """Build the approach table the family checker reads.

    Each problem in the gold file becomes one row. The family cell comes from the
    caller, the measured cell comes from the pack measurement unless the caller
    substitutes one, and the citation is the fixed source for that problem id.
    """
    lines = [
        "| id | family | measured | citation | system | reason |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for problem_id, rule in gold["problems"].items():
        cell = measured_for(problem_id) if measured_for else str(measured.get(problem_id, "claim"))
        family = family_for(problem_id, rule)
        lines.append(f"| {problem_id} | {family} | {cell} | {CITATIONS[problem_id]} | record | Cited from the release. |")
    return "\n".join(lines) + "\n"


def fit_family(_problem_id: str, rule: dict) -> str:
    """Family cell for a memo that should pass.

    The cell is the rule's required methods joined together, which is the combination
    the gold file treats as a fit.
    """
    return "+".join(rule["required"])


def grab(path: Path, pattern: str) -> str:
    """Return the single captured group from a release page.

    Used for sizes that are claims on a page rather than baseline measurements.
    Raises when the page no longer contains the figure, so a missing claim fails
    here instead of becoming a blank cell.
    """
    found = re.search(pattern, path.read_text(encoding="utf-8"))
    if not found:
        raise AssertionError(f"{pattern} missing in {path}")
    return found.group(1)


def brief(pack: Path, measured: dict, ranking: tuple[str, ...] = RANK, first: str | None = None, extra: str = "") -> str:
    """Build the brief the size checker reads.

    The stakeholder lines are fixed claims. The size table mixes baseline
    measurements with figures pulled from the release pages, and each cell is marked
    as measured or as a claim. The ranking defaults to the usual order. A caller
    can move one problem to the front and, on that first line only, replace the
    plain note.
    """
    access = pack / "extracts" / "access-costs.md"
    sizes = {
        "p-bounce": (measured["p-bounce"], "samples/ds-letters.md", "measured"),
        "p-waitlist": (grab(access, r"returned referrals \| (\d+)"), "extracts/access-costs.md", "claim"),
        "p-dna": (measured["p-dna"], "samples/ds-dna.csv", "measured"),
        "p-status": (measured["p-status"], "samples/ds-messages.csv", "measured"),
        "p-slots": (grab(access, r"empty sessions \| (\d+)"), "extracts/access-costs.md", "claim"),
        "p-clock": (grab(pack / "extracts" / "dashboard.md", r"median_wait_days \| (\d+)"), "extracts/dashboard.md", "claim"),
        "p-info": (grab(access, r"Hours and documents: (\d+)"), "extracts/access-costs.md", "claim"),
        "p-forecast": (measured["p-forecast"], "samples/ds-demand.csv", "measured"),
        "p-triage": (grab(pack / "extracts" / "sponsor-ask.md", r"Claimed impact: (\d+)"), "extracts/sponsor-ask.md", "claim"),
    }
    lines = [
        "| Who | Their words | Kind |",
        "| --- | --- | --- |",
        "| vendor | Containment on the national contact-center pilot is 70 percent. | claim |",
        "| cdo | The virtual front desk goes live before Ramadan. | claim |",
        "",
        "| id | size | source | kind |",
        "| --- | --- | --- | --- |",
    ]
    for problem_id, (size, source, kind) in sizes.items():
        lines.append(f"| {problem_id} | {size} | {source} | {kind} |")
    lines.extend(["", *_ranking(ranking, first)])
    if extra:
        lines.extend(["", extra])
    return "\n".join(lines) + "\n"


def _ranking(ranking: tuple[str, ...], first: str | None) -> list[str]:
    """Render the numbered ranking.

    Every line is a plain note except the first line, which can carry the note the
    caller passed in. That is how a test puts an urgency rule on the same line as
    the problem it promotes.
    """
    lines = []
    for index, problem_id in enumerate(ranking, start=1):
        text = first if index == 1 and first else "noted"
        lines.append(f"{index}. {problem_id} — {text}")
    return lines
