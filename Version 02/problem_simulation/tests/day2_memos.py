"""Memo text for the Day 2 check tests."""

from __future__ import annotations

import re
from pathlib import Path

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
    return "+".join(rule["required"])


def grab(path: Path, pattern: str) -> str:
    found = re.search(pattern, path.read_text(encoding="utf-8"))
    if not found:
        raise AssertionError(f"{pattern} missing in {path}")
    return found.group(1)


def brief(pack: Path, measured: dict, ranking: tuple[str, ...] = RANK, first: str | None = None, extra: str = "") -> str:
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
    lines = []
    for index, problem_id in enumerate(ranking, start=1):
        text = first if index == 1 and first else "noted"
        lines.append(f"{index}. {problem_id} — {text}")
    return lines
