"""A two-page brief whose sentences carry the key facts. The figures come from the findings."""

from __future__ import annotations

from reference_discovery.io import Drop, field


def write(path, items: dict, root) -> None:
    found = items["items"]
    board = field(Drop(root).text("corpus", "board-papers", "board-paper-2026-09-ai-screening.md"), "effective")
    paper = Drop(root).text("corpus", "board-papers", "board-paper-2026-09-ai-screening.md")
    requested, original = _pilot_dates(paper)
    freeze = found["freezes"]["registry"]["start"]
    count = found["eligible_people"]["count"]
    text = "\n".join([
        "# Week 1 brief",
        "",
        f"The pilot stays stopped until a clinical safety owner is named. The board paper of {board} "
        f"asks to bring the date from {original} to {requested}.",
        "",
        f"Count living people, not rows. Deceased rows are not eligible. The eligible count we can defend is {count}.",
        "",
        "Identity resolution has the highest net value we can defend, and it comes before the work that needs one record per person. "
        "The letter fix comes before call deflection and reminder targeting, because a letter that never arrives makes both pointless.",
        "",
        "The reminder change had no control group. Seasonality moves attendance across the same months, so the rise after the change "
        "is not the reminder's effect.",
        "",
        f"Workshop idea {found['workshop']['top_idea']} drew the most dots. It is not the opportunity to build first. "
        "The vendor model stays on primary-care captures.",
        "",
        f"The registry freeze starts {freeze}. Nothing in this brief puts a vendor model expansion first.",
        "",
    ])
    path.write_text(text, encoding="utf-8")


def _pilot_dates(text: str) -> tuple[str, str]:
    import re

    found = re.search(r"from (\d{4}-\d{2}-\d{2}) to (\d{4}-\d{2}-\d{2})", text)
    return found.group(2), found.group(1)
