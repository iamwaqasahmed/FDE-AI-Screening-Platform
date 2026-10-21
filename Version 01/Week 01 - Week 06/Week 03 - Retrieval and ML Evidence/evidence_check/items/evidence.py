"""Operating points, firmware, and the three proposal claims."""

from __future__ import annotations

from course.checks.rules import as_int, close
from simulation.eval.evidence.bars import RATE_TOLERANCE


def operating_points(answer: dict, gold: dict) -> bool:
    row = gold["items"]["operating_points"]
    names = ("all", "age_75_plus", "age_under_75", "claim_population")
    if any(not _point(answer.get(name), row[name]) for name in names):
        return False
    given = answer.get("sites") if isinstance(answer.get("sites"), dict) else {}
    return set(given) == set(row["sites"]) and all(_point(given.get(site), point) for site, point in row["sites"].items())


def firmware_drift(answer: dict, gold: dict) -> bool:
    row = gold["items"]["firmware_drift"]
    texts = ("river_site", "firmware", "first_capture", "inventory_firmware", "market_site", "label_drift_site")
    flags = ("scores_fall", "inventory_lags", "primary_scores_fall")
    if any(answer.get(key) != row[key] for key in texts) or any(answer.get(key) is not row[key] for key in flags):
        return False
    if as_int(answer.get("market_scored")) != row["market_scored"]:
        return False
    rates = ("score_before", "score_after", "drift_sens_before", "drift_sens_after", "drift_score_before", "drift_score_after")
    return all(close(answer.get(key), row[key], RATE_TOLERANCE, relative=False) for key in rates)


def claims(answer: dict, gold: dict) -> bool:
    row = gold["items"]["claims"]
    texts = ("population", "population_source", "stopped_document", "postmortem", "postmortem_blames", "injection_document")
    flags = ("holds_overall", "holds_on_population", "clearsight_stopped")
    if any(answer.get(key) != row[key] for key in texts) or any(answer.get(key) is not row[key] for key in flags):
        return False
    return close(answer.get("claimed"), row["claimed"], RATE_TOLERANCE, relative=False)


def _point(given, expected) -> bool:
    if not isinstance(given, dict):
        return False
    if as_int(given.get("positives")) != expected["positives"]:
        return False
    return all(close(given.get(key), expected[key], RATE_TOLERANCE, relative=False) for key in ("sensitivity", "low", "high"))
