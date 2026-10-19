"""Combine item, file, record, and page results."""

from __future__ import annotations

from handoff_check.items import ITEMS
from simulation.eval.handoff.bars import ITEM_BAR, ROLE_BAR

FILES = ("flows", "threats", "hazards")
WRITTEN = (
    "dockerfile", "contract", "transparency", "model_card", "adr-01", "adr-02", "adr-03", "adr-04",
    "executive", "clinical", "runbook", "pages",
)


def evaluate(gold, findings, files, dockerfile, records, texts, *, rerun: bool) -> dict:
    report = {
        "results": [_result(item, findings.get(item["id"]), gold) for item in ITEMS],
        "files": files,
        "written": {**records, **texts, "dockerfile": dockerfile},
    }
    report["roles"] = _roles(report["results"])
    report["ok"] = _ok(report, rerun)
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
    for name in FILES:
        lines.append(f"{name} ok" if report["files"][name].get("ok") else f"{name} failed")
    if not rerun:
        for name in WRITTEN:
            lines.append(f"{name} ok" if report["written"][name].get("ok") else f"{name} failed")
    failed = [row["id"] for row in results if not row["passed"]]
    if failed:
        lines.append("failed: " + ", ".join(failed))
    lines.append("Handoff check passed." if report["ok"] else "Handoff check failed.")
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


def _ok(report: dict, rerun: bool) -> bool:
    results = [row for row in report["results"] if row["mode"] == "computed" or not rerun]
    if not results or sum(row["passed"] for row in results) / len(results) < ITEM_BAR:
        return False
    for row in report["roles"].values():
        if rerun and row["computed"] == 0:
            continue
        counted = row["computed"] if rerun else row["total"]
        passed = row["computed_passed"] if rerun else row["passed"]
        if counted == 0 or passed / counted < ROLE_BAR:
            return False
    if not all(report["files"][name].get("ok") for name in FILES):
        return False
    if rerun:
        return True
    return all(report["written"][name].get("ok") for name in WRITTEN)
