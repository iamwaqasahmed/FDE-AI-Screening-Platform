"""The hardness rule: the best baseline for each role must fail that role's slice on every audited seed."""

from __future__ import annotations

import json
from pathlib import Path

PASS_LIMIT = 0.5
AUDITED_PROFILES = ("practice", "assessment")
ROLES = ("ml", "data_science", "data_engineering", "software", "architect", "pm", "consultant")


def strongest(summary: dict) -> dict[str, dict]:
    """Per role, the baseline with the highest pass rate and that rate."""
    best: dict[str, dict] = {}
    for name, slices in summary.items():
        for role, value in slices["role"].items():
            if role not in best or value["pass_rate"] > best[role]["pass_rate"]:
                best[role] = {"baseline": name, "pass_rate": value["pass_rate"], "cases": value["cases"]}
    return best


def audit_profile(data: Path) -> dict:
    summary = json.loads((data / "eval" / "baselines" / "summary.json").read_text(encoding="utf-8"))
    best = strongest(summary)
    failures = [role for role in ROLES if best.get(role, {}).get("pass_rate", 0.0) >= PASS_LIMIT]
    missing = [role for role in ROLES if best.get(role, {}).get("cases", 0) < 10]
    return {"best_by_role": best, "too_easy": failures, "too_few_cases": missing, "ok": not failures and not missing}
