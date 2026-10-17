"""Combine item, interview, note, and brief results. Print failures without printing a gold value."""

from __future__ import annotations

from discovery_check.brief import passed as brief_passed
from discovery_check.interviews import passed as interviews_passed
from discovery_check.items import ITEMS
from discovery_check.notes import passed as notes_passed

ITEM_BAR = 0.8
ROLE_BAR = 0.6


def evaluate(gold: dict, findings: dict, scripts: dict, note_rows: dict | None, brief_row: dict | None, *,
             rerun: bool = False) -> dict:
    report = {
        "results": [_result(item, findings.get(item["id"]), gold) for item in ITEMS],
        "roles": {},
        "scripts": scripts,
        "notes": note_rows,
        "brief": brief_row,
    }
    report["roles"] = _roles(report["results"])
    report["ok"] = _scoped_ok(report, rerun)
    return report


def render(report: dict, *, rerun: bool) -> str:
    results = [row for row in report["results"] if row["mode"] == "computed" or not rerun]
    lines = [f"items {sum(row['passed'] for row in results)}/{len(results)}"]
    for role, row in sorted(report["roles"].items()):
        if rerun and row["computed"] == 0:
            continue
        counted = row["computed"] if rerun else row["total"]
        passed = row["computed_passed"] if rerun else row["passed"]
        lines.append(f"  {role} {passed}/{counted}")
    lines.append(f"interviews {sum(score >= 0.8 for score in report['scripts'].values())}/{len(report['scripts'])}")
    if report["notes"] is not None:
        lines.append(f"notes {_text_line(report['notes'])}")
    if report["brief"] is not None:
        lines.append(f"brief coverage {report['brief']['coverage']:.2f}")
    failed = [row["id"] for row in results if not row["passed"]]
    if failed:
        lines.append("failed: " + ", ".join(failed))
    lines.append("Discovery check passed." if _scoped_ok(report, rerun) else "Discovery check failed.")
    return "\n".join(lines)


def _result(item: dict, answer, gold: dict) -> dict:
    try:
        ok = isinstance(answer, dict) and bool(item["check"](answer, gold))
    except (TypeError, ValueError, KeyError):
        ok = False
    return {"id": item["id"], "roles": item["roles"], "mode": item["mode"], "passed": ok}


def _roles(results: list[dict]) -> dict:
    found: dict[str, dict] = {}
    for row in results:
        for role in row["roles"]:
            slot = found.setdefault(role, {"total": 0, "passed": 0, "computed": 0, "computed_passed": 0})
            slot["total"] += 1
            slot["passed"] += int(row["passed"])
            if row["mode"] == "computed":
                slot["computed"] += 1
                slot["computed_passed"] += int(row["passed"])
    return found


def _rate(results: list[dict]) -> float:
    return sum(row["passed"] for row in results) / len(results) if results else 0.0


def _text_line(rows: dict) -> str:
    good = sum(1 for row in rows.values() if row["coverage"] >= 0.8 and not row["forbidden"])
    return f"{good}/{len(rows)}"


def _scoped_ok(report: dict, rerun: bool) -> bool:
    results = [row for row in report["results"] if row["mode"] == "computed" or not rerun]
    if _rate(results) < ITEM_BAR:
        return False
    for row in report["roles"].values():
        if rerun and row["computed"] == 0:
            continue
        rate = (row["computed_passed"] / row["computed"]) if rerun else (row["passed"] / row["total"])
        if rate < ROLE_BAR:
            return False
    if not interviews_passed(report["scripts"]):
        return False
    if report["notes"] is not None and not notes_passed(report["notes"]):
        return False
    if report["brief"] is not None and not brief_passed(report["brief"]):
        return False
    return True
