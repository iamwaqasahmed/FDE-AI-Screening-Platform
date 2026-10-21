"""Each new ask is a refusal or a later slice. No new platform. No pilot start."""

from __future__ import annotations

from pathlib import Path

PACK = Path(__file__).resolve().parents[2] / "capstone"
NOTES = ("breast_screening.md", "river_outreach.md", "fourteen_day_draft.md")


def main() -> None:
    errors: list[str] = []
    for name in NOTES:
        text = (PACK / name).read_text(encoding="utf-8")
        lowered = text.lower()
        if "refuse" not in lowered:
            errors.append(f"{name} does not refuse or hold the ask")
        if "do not rebuild the platform" not in lowered:
            errors.append(f"{name} does not keep the platform as it is")
        if "do not start the pilot" not in lowered:
            errors.append(f"{name} starts the pilot")
        if ".md" not in text and "owner.md" not in text:
            errors.append(f"{name} does not cite a file already in the program")
    breast = (PACK / "breast_screening.md").read_text(encoding="utf-8")
    river = (PACK / "river_outreach.md").read_text(encoding="utf-8")
    draft = (PACK / "fourteen_day_draft.md").read_text(encoding="utf-8")
    if "clinic_note_pilot_sites.md" not in breast:
        errors.append("breast recommendation does not cite the clinic note")
    if "clinic_note_pilot_sites.md" not in river:
        errors.append("River recommendation does not cite the clinic note")
    if "sop_urgent_pathway_draft.md" not in draft or "clinical_safety_owner: unassigned" not in draft:
        errors.append("draft recommendation does not cite the draft and the unassigned owner")
    if errors:
        raise SystemExit("Capstone check failed:\n- " + "\n- ".join(errors))
    print("Capstone check passed.")


if __name__ == "__main__":
    main()
