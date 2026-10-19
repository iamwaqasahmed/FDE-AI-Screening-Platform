"""Shared shape of a weekly drop: a README brief plus files under drops/week-N."""

from __future__ import annotations

from datetime import date

from simulation.world.engagement import WEEKS


def folder(week: int) -> str:
    return f"drops/week-{week}"


def readme(week: int, title: str, brief: list[str], files: list[str]) -> str:
    lines = [f"# Week {week} drop: {title}", "", f"Released {WEEKS[week].isoformat()}.", "", *brief, "", "## Files", ""]
    lines += [f"- `{path}`" for path in files]
    return "\n".join(lines) + "\n"


def add_drop(world: dict, week: int, title: str, brief: list[str], files: dict, gold: dict) -> None:
    prefix = folder(week)
    for relative, content in files.items():
        world["files"][f"{prefix}/{relative}"] = content
    world["files"][f"{prefix}/README.md"] = readme(week, title, brief, sorted(files))
    gold.update(week=week, released=WEEKS[week].isoformat(), files=sorted(files))
    world["gold"].setdefault("drops", {})[f"week-{week}"] = gold


def memo(title: str, sender: str, to: str, day: date, paragraphs: list[str]) -> str:
    head = [f"# {title}", "", f"From: {sender}", f"To: {to}", f"Date: {day.isoformat()}", ""]
    return "\n".join(head + [f"{paragraph}\n" for paragraph in paragraphs])
