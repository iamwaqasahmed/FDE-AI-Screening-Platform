"""Read the handoff pack. No model. No hidden tables."""

from __future__ import annotations

from pathlib import Path

PACK = Path(__file__).resolve().parents[1] / "handoff"
SITES = (
    "Hill Counties Health Centre",
    "Oakridge Primary Care",
    "North City Eye Clinic",
)


def main() -> None:
    executive = _read("executive.md")
    clinical = _read("clinical.md")
    runbook = _read("runbook.md")
    owner = _read("owner.md")
    errors: list[str] = []
    for site in SITES:
        if site not in executive or site not in clinical:
            errors.append(f"missing site {site}")
    if "93%" not in executive or "does not prove" not in executive:
        errors.append("executive page does not keep the 93% slide off the primary-care pilot")
    for deferred in ("breast screening", "cervical screening", "River Outreach", "platform license"):
        if deferred not in executive:
            errors.append(f"executive page does not defer {deferred}")
    if "grader signs" not in clinical.lower() and "A grader signs" not in clinical:
        errors.append("clinical page does not name the grader as signer")
    if "draft" not in clinical.lower() or "not current policy" not in clinical.lower():
        errors.append("clinical page does not leave the 14-day rule as a draft")
    if "python -m screening_service.run" not in runbook:
        errors.append("runbook is missing the start command")
    if "runtime/access.log" not in runbook:
        errors.append("runbook is missing the access log path")
    for refusal in ("diagnose a retina", "train on patient images", "refer without a grader"):
        if refusal not in runbook:
            errors.append(f"runbook does not forbid {refusal}")
    if "clinical_safety_owner: unassigned" not in owner:
        errors.append("safety owner is not unassigned")
    if "pilot_starts: no" not in owner:
        errors.append("pilot is not stopped")
    if errors:
        raise SystemExit("Handoff check failed:\n- " + "\n- ".join(errors))
    print("Handoff check passed.")


def _read(name: str) -> str:
    return (PACK / name).read_text(encoding="utf-8")


if __name__ == "__main__":
    main()
