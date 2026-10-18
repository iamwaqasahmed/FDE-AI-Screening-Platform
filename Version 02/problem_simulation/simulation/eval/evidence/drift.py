"""Firmware on the scores, and the site where the graders moved and the camera did not."""

from __future__ import annotations

import pandas as pd

from simulation.eval.evidence.rates import sensitivity


def firmware(frame: pd.DataFrame, inventory: pd.DataFrame, allowed: list[str]) -> dict:
    upgraded = frame[frame["firmware"].astype(str).eq("3.1.0")]
    river = str(upgraded["site"].iloc[0]) if len(upgraded) else ""
    before, after, before_n, after_n = _means(frame, river, "3.1.0")
    market = _market(inventory, frame)
    drift_site, drift = _label_drift(frame, allowed)
    return {
        "river_site": river,
        "firmware": "3.1.0",
        "first_capture": str(upgraded["capture_date"].min()) if len(upgraded) else "",
        "score_before": before,
        "score_after": after,
        "river_before_n": before_n,
        "river_after_n": after_n,
        "scores_fall": after < before,
        "inventory_firmware": _inventory(inventory, river),
        "inventory_lags": _inventory(inventory, river) not in ("", "3.1.0"),
        "market_site": market[0],
        "market_scored": market[1],
        "label_drift_site": drift_site,
        "drift_sens_before": drift[0],
        "drift_sens_after": drift[1],
        "drift_score_before": drift[2],
        "drift_score_after": drift[3],
        "primary_scores_fall": _primary_falls(frame, allowed),
    }


def _means(frame: pd.DataFrame, site: str, firmware: str) -> tuple[float, float, int, int]:
    rows = frame[frame["site"].eq(site)]
    before = rows.loc[~rows["firmware"].astype(str).eq(firmware), "vendor_score"]
    after = rows.loc[rows["firmware"].astype(str).eq(firmware), "vendor_score"]
    return _mean(before), _mean(after), int(before.notna().sum()), int(after.notna().sum())


def _mean(series: pd.Series) -> float:
    values = pd.to_numeric(series, errors="coerce").dropna()
    return round(float(values.mean()), 3) if len(values) else 0.0


def _inventory(inventory: pd.DataFrame, site: str) -> str:
    rows = inventory[inventory["site"].astype(str).eq(site)]
    versions = sorted(set(rows["firmware"].astype(str)))
    return versions[0] if len(versions) == 1 else ""


def _market(inventory: pd.DataFrame, frame: pd.DataFrame) -> tuple[str, int]:
    rows = inventory[inventory["firmware"].astype(str).eq("4.2.0")]
    site = str(rows["site"].iloc[0]) if len(rows) else ""
    return site, int(frame["site"].astype(str).eq(site).sum()) if site else 0


def _label_drift(frame: pd.DataFrame, allowed: list[str]) -> tuple[str, tuple]:
    best, chosen = 0.0, ("", (0.0, 0.0, 0.0, 0.0))
    for site in sorted(allowed):
        change = _change(frame[frame["site"].eq(site)])
        if change and change[0] - change[1] > best and change[3] > change[2]:
            best = change[0] - change[1]
            chosen = (site, change)
    return chosen


def _change(rows: pd.DataFrame):
    versions = _versions(rows)
    if len(versions) < 2:
        return None
    earlier, later = versions[0], versions[-1]
    _, _, sens_before = sensitivity(earlier, "grader_label")
    _, _, sens_after = sensitivity(later, "grader_label")
    if sens_after >= sens_before:
        return None
    return sens_before, sens_after, _mean(earlier["vendor_score"]), _mean(later["vendor_score"])


def _primary_falls(frame: pd.DataFrame, allowed: list[str]) -> bool:
    for site in allowed:
        versions = _versions(frame[frame["site"].eq(site)])
        if len(versions) >= 2 and _mean(versions[-1]["vendor_score"]) < _mean(versions[0]["vendor_score"]) - 0.01:
            return True
    return False


def _versions(rows: pd.DataFrame) -> list[pd.DataFrame]:
    found = [(str(group["capture_date"].min()), group) for _, group in rows.groupby("firmware", sort=False)]
    return [group for _, group in sorted(found)]
