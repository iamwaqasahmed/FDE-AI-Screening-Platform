"""The four decision records, the two pages, and the runbook."""

from __future__ import annotations

from pathlib import Path

from simulation.eval.handoff.score_pages import pages_agree, score_document

ADRS = ("adr-01", "adr-02", "adr-03", "adr-04")
PAGES = {"executive": "executive-page.md", "clinical": "clinical-page.md", "runbook": "runbook.md"}


def score(work: Path, gold: dict) -> dict:
    texts = gold["text"]
    found = {key: score_document(_text(work / "adr" / f"{key.upper()}.md"), texts[key]) for key in ADRS}
    bodies = {key: _text(work / name) for key, name in PAGES.items()}
    for key, body in bodies.items():
        found[key] = score_document(body, texts[key])
    found["pages"] = {"ok": pages_agree(bodies["executive"], bodies["clinical"], texts["pages"])}
    return found


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""
