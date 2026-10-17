"""Check truth, handover, corpus, and eval against the config quotas."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from problem_simulation.src.config_loader import PKG_ROOT, REPO_ROOT, load_config
from problem_simulation.src.exporters.dates import parse_mixed


def validate(repo_root: Path | None = None) -> None:
    root = repo_root or REPO_ROOT
    cfg = load_config()
    errors: list[str] = []
    truth = _read_truth(root)
    _check_truth(truth, cfg, errors)
    sheet = _read_workbook(root / "data" / "handover" / "grader_workbook.xlsx")
    registry = pd.read_csv(root / "data" / "handover" / "diabetes_registry.csv", dtype=str)
    _check_registry(registry, cfg, errors)
    _check_workbook(sheet, registry, cfg, errors)
    _check_medians(root, sheet, errors)
    _check_pilot(root, cfg, errors)
    _check_corpus(root, cfg, errors)
    _check_eval(root, truth, errors)
    _check_no_secret(root, errors)
    if errors:
        raise SystemExit("Validation failed:\n- " + "\n- ".join(errors))
    print("Validation passed.")


def _read_truth(root: Path) -> dict[str, pd.DataFrame]:
    folder = root / "data" / "truth"
    names = [
        "person",
        "crosswalk",
        "visit",
        "image",
        "grade",
        "letter",
        "referral",
        "vendor_score",
        "hospital_eval",
    ]
    return {name: pd.read_csv(folder / f"{name}.csv", keep_default_na=False) for name in names}


def _check_truth(truth: dict[str, pd.DataFrame], cfg: dict, errors: list[str]) -> None:
    person = truth["person"]
    eligible = person[person["flag"].fillna("") == ""]
    if len(person) != 91406:
        errors.append(f"Truth person rows {len(person)} != 91406")
    if len(eligible) != 84120:
        errors.append(f"Truth eligible {len(eligible)} != 84120")
    completed = person[person["cohort"] == "completed"]
    if len(completed) != 34490:
        errors.append(f"Truth completed {len(completed)} != 34490")
    letters = truth["letter"].copy()
    letters["sent_at"] = pd.to_datetime(letters["sent_at"])
    letters["photo_date"] = pd.to_datetime(letters["photo_date"])
    median_letter = (letters["sent_at"] - letters["photo_date"]).dt.days.median()
    if median_letter != cfg["photo_to_letter_median_days"]:
        errors.append(f"Truth letter median {median_letter}")
    urgent_rows = truth["grade"][_as_bool(truth["grade"]["urgent"])]
    referral = truth["referral"].merge(urgent_rows[["person_uid", "graded_at"]], on="person_uid")
    waits = (pd.to_datetime(referral["seen_at"]) - pd.to_datetime(referral["graded_at"])).dt.days
    if waits.median() != cfg["urgent_to_specialist_median_days"]:
        errors.append(f"Truth urgent median {waits.median()}")
    caught = truth["hospital_eval"]
    referable = caught[_as_bool(caught["referable"])]
    sensitivity = _as_bool(referable["model_positive"]).sum() / len(referable)
    if round(float(sensitivity), 2) != 0.93:
        errors.append(f"Hospital sensitivity {sensitivity}")


def _check_registry(registry: pd.DataFrame, cfg: dict, errors: list[str]) -> None:
    if len(registry) != 91406:
        errors.append(f"Registry rows {len(registry)} != 91406")
    flagged = registry["FLAG"].fillna("").isin(["DECEASED", "MOVED"]).sum()
    if flagged != 7286:
        errors.append(f"Flagged rows {flagged} != 7286")
    eligible = registry[registry["FLAG"].fillna("") == ""].copy()
    eligible["district_name"] = eligible["DISTRICT"].map(_district_lookup(cfg))
    if eligible["district_name"].isna().any():
        errors.append("Unmapped district spelling in the registry")
    counts = eligible["district_name"].value_counts().to_dict()
    for district in cfg["districts"]:
        if counts.get(district["name"]) != district["eligible"]:
            errors.append(f"Eligible {district['name']} is {counts.get(district['name'])}")


def _check_workbook(sheet: pd.DataFrame, registry: pd.DataFrame, cfg: dict, errors: list[str]) -> None:
    coded = sheet.copy()
    coded["grade_norm"] = [_normalize(result, notes) for result, notes in zip(coded["RESULT"], coded["NOTES"])]
    counts = coded["grade_norm"].value_counts().to_dict()
    expected = {"": 6110, "U": 7588, "R2": 5829, "R3": 379, "R0": 10347, "R1": 10347}
    for grade, count in expected.items():
        if counts.get(grade, 0) != count:
            errors.append(f"Workbook {grade or 'blank'} is {counts.get(grade, 0)} != {count}")
    eligible = registry[registry["FLAG"].fillna("") == ""][["LOCAL_PID", "DISTRICT"]].copy()
    eligible["district_name"] = eligible["DISTRICT"].map(_district_lookup(cfg))
    completed = coded[coded["grade_norm"] != ""].merge(eligible, on="LOCAL_PID", how="left")
    if completed["district_name"].isna().any():
        errors.append("Completed screens failed to join the registry on LOCAL_PID")
    by_district = completed["district_name"].value_counts().to_dict()
    for district in cfg["districts"]:
        if by_district.get(district["name"]) != district["completed"]:
            errors.append(f"Completed {district['name']} is {by_district.get(district['name'])}")


def _check_medians(root: Path, sheet: pd.DataFrame, errors: list[str]) -> None:
    letters = pd.read_csv(root / "data" / "handover" / "letter_dispatch.csv", dtype=str)
    referrals = pd.read_csv(root / "data" / "handover" / "ophthalmology_referrals.csv", dtype=str)
    sheet = sheet.copy()
    sheet["grade_norm"] = [_normalize(result, notes) for result, notes in zip(sheet["RESULT"], sheet["NOTES"])]
    sheet["photo"] = sheet["PHOTO_DATE"].map(parse_mixed)
    sheet["graded"] = sheet["GRADE_DATE"].map(_parse_optional)
    completed = sheet[sheet["grade_norm"] != ""]
    joined = letters.merge(completed, on="LOCAL_PID")
    sent = joined["SENT_DATE"].map(parse_mixed)
    delays = [(left - right).days for left, right in zip(sent, joined["photo"])]
    if _median(delays) != 19:
        errors.append(f"Handover letter median {_median(delays)}")
    urgent = sheet[sheet["grade_norm"] == "R3"]
    urgent_join = referrals.merge(urgent, on="LOCAL_PID")
    seen = urgent_join["SEEN_DATE"].map(parse_mixed)
    waits = [(left - right).days for left, right in zip(seen, urgent_join["graded"])]
    if len(waits) != 379 or _median(waits) != 47:
        errors.append(f"Handover urgent waits {len(waits)} median {_median(waits) if waits else None}")


def _check_pilot(root: Path, cfg: dict, errors: list[str]) -> None:
    vendor = pd.read_csv(root / "data" / "handover" / "vendor_scores.csv", dtype=str).fillna("")
    if len(vendor) != cfg["pilot"]["images"]:
        errors.append(f"Pilot rows {len(vendor)}")
    empty = int((vendor["MODEL_LABEL"] == "").sum())
    if empty != cfg["pilot"]["ungradable"]:
        errors.append(f"Pilot empty scores {empty}")
    disagree = int(((vendor["MODEL_LABEL"] != "") & (vendor["MODEL_LABEL"] != vendor["GRADER_LABEL"])).sum())
    if disagree != cfg["pilot"]["disagreements"]:
        errors.append(f"Pilot disagreements {disagree}")


def _check_corpus(root: Path, cfg: dict, errors: list[str]) -> None:
    source = PKG_ROOT / "corpus"
    copied = root / "data" / "corpus"
    manifest = pd.read_csv(copied / "manifest.csv")
    draft = manifest[manifest["document_id"] == "sop-urgent-draft"]
    if draft.empty or draft.iloc[0]["status"] != "draft":
        errors.append("Urgent pathway is not marked draft")
    for doc in cfg["corpus"]:
        left = (source / doc["filename"]).read_bytes()
        right = (copied / doc["filename"]).read_bytes()
        if left != right:
            errors.append(f"Corpus copy differs for {doc['filename']}")
    draft_text = (copied / "sop_urgent_pathway_draft.md").read_text(encoding="utf-8")
    if "NOT ISSUED" not in draft_text or "14 days" not in draft_text:
        errors.append("Draft text is missing the not-issued marker or the 14-day rule")


def _check_eval(root: Path, truth: dict[str, pd.DataFrame], errors: list[str]) -> None:
    import json

    people = set(truth["person"]["person_uid"])
    images = set(truth["image"]["image_id"])
    lines = (root / "data" / "eval" / "cases.jsonl").read_text(encoding="utf-8").splitlines()
    if len(lines) < 24:
        errors.append(f"Expected at least 24 eval cases, found {len(lines)}")
    for line in lines:
        case = json.loads(line)
        if not case["truth_ids"]:
            errors.append(f"{case['case_id']} has no truth id")
        for truth_id in case["truth_ids"]:
            if truth_id not in people and truth_id not in images:
                errors.append(f"{case['case_id']} truth id {truth_id} did not resolve")


def _check_no_secret(root: Path, errors: list[str]) -> None:
    handover = root / "data" / "handover"
    corpus = root / "data" / "corpus"
    for path in list(handover.rglob("*")) + list(corpus.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in {".csv", ".txt", ".md"}:
            if "person_uid" in path.read_text(encoding="utf-8", errors="ignore"):
                errors.append(f"person_uid leaked into {path.name}")
        elif path.suffix.lower() == ".xlsx":
            book = pd.read_excel(path, sheet_name=None, dtype=str)
            for name, frame in book.items():
                blob = " ".join(frame.columns) + frame.fillna("").astype(str).to_csv(index=False)
                if "person_uid" in blob:
                    errors.append(f"person_uid leaked into {path.name} sheet {name}")


def _read_workbook(path: Path) -> pd.DataFrame:
    book = pd.read_excel(path, sheet_name=None, dtype=str)
    frames = []
    for name, frame in book.items():
        if name == "OLD":
            continue
        frames.append(frame.fillna(""))
    sheet = pd.concat(frames, ignore_index=True)
    sheet = sheet[~sheet["LOCAL_PID"].str.startswith("TEST")]
    return sheet


def _normalize(result, notes) -> str:
    code = "" if result is None else str(result).strip().lower()
    note = "" if notes is None else str(notes).strip().lower()
    if code in {"nan", "none"}:
        code = ""
    if note in {"nan", "none"}:
        note = ""
    if code in {"r0", "r1", "r2"}:
        return code.upper()
    if code in {"r3", "prolif"} or note == "urgent":
        return "R3"
    if code in {"u", "ungradable"}:
        return "U"
    if code == "" and note == "":
        return ""
    return "UNKNOWN"


def _district_lookup(cfg: dict) -> dict[str, str]:
    lookup = {}
    for district in cfg["districts"]:
        lookup[district["name"]] = district["name"]
        for variant in district["variants"]:
            lookup[variant] = district["name"]
    return lookup


def _parse_optional(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    if str(value).strip() == "":
        return None
    return parse_mixed(value)


def _as_bool(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin(["true", "1", "yes"])


def _median(values: list[int]) -> float:
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2
