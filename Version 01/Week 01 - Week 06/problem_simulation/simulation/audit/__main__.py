"""python -m simulation.audit: check the hardness rule on every audited profile that has been built and scored."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from simulation.audit.roles import AUDITED_PROFILES, PASS_LIMIT, audit_profile
from simulation.config.profile import load

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    report, ok = {}, True
    for name in AUDITED_PROFILES:
        data = (ROOT / load(name).output).resolve()
        if not (data / "eval" / "baselines" / "summary.json").exists():
            print(f"{name}: not scored. Run python -m simulation --profile {name}, then python -m simulation.eval.baselines --profile {name}")
            ok = False
            continue
        report[name] = audit_profile(data)
        ok = ok and report[name]["ok"]
        print(f"{name}: {'ok' if report[name]['ok'] else 'FAIL'} (limit {PASS_LIMIT})")
        for role, best in sorted(report[name]["best_by_role"].items()):
            print(f"  {role:<17} best {best['baseline']:<18} pass {best['pass_rate']:.2f} on {best['cases']} cases")
        for role in report[name]["too_few_cases"]:
            print(f"  {role}: fewer than ten cases")
    (ROOT / "simulation" / "audit" / "last_audit.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
