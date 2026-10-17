"""Visits, images, grades, letters, and referrals."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from problem_simulation.src.delays import sample_delays


def build_events(people: pd.DataFrame, cfg: dict, rng: np.random.Generator) -> dict[str, pd.DataFrame]:
    photographed = people[people["cohort"] != "none"].copy()
    photographed["photo_date"] = _photo_dates(photographed, cfg, rng)
    completed = photographed["cohort"] == "completed"
    letter_days = sample_delays(int(completed.sum()), cfg["photo_to_letter_median_days"], rng)
    grade_lag = np.minimum(rng.integers(0, 4, size=int(completed.sum())), letter_days)
    photographed.loc[completed, "letter_days"] = letter_days
    photographed.loc[completed, "grade_lag"] = grade_lag
    urgent = photographed["grade"] == "R3"
    waits = sample_delays(int(urgent.sum()), cfg["urgent_to_specialist_median_days"], rng)
    photographed.loc[urgent, "urgent_wait"] = waits
    mild = photographed["grade"] == "R2"
    mild_waits = rng.integers(
        cfg["mild_referral_wait_min_days"],
        cfg["mild_referral_wait_max_days"] + 1,
        size=int(mild.sum()),
    )
    photographed.loc[mild, "mild_wait"] = mild_waits

    visits, images, grades, letters, referrals = [], [], [], [], []
    used_names: set[str] = set()
    for row in photographed.itertuples(index=False):
        visit_id = f"V{len(visits) + 1:07d}"
        visits.append(
            {
                "visit_id": visit_id,
                "person_uid": row.person_uid,
                "site_name": row.screening_site,
                "camera_class": row.camera_class,
                "photo_date": row.photo_date,
            }
        )
        eyes = _eyes(row)
        for eye, quality, grade in eyes:
            image_id = f"I{len(images) + 1:07d}"
            file_name, file_path = _path(row, eye, image_id, len(images), used_names)
            images.append(
                {
                    "image_id": image_id,
                    "person_uid": row.person_uid,
                    "visit_id": visit_id,
                    "eye": eye,
                    "file_name": file_name,
                    "file_path": file_path,
                    "quality": quality,
                    "grade": grade,
                    "camera_class": row.camera_class,
                    "file_present": False,
                    "is_pilot": False,
                }
            )
        if row.cohort == "completed":
            graded_at = row.photo_date + timedelta(days=int(row.grade_lag))
            grades.append(
                {
                    "person_uid": row.person_uid,
                    "grade": row.grade,
                    "referable": row.grade in {"R2", "R3"},
                    "urgent": row.grade == "R3",
                    "graded_at": graded_at,
                    "grader_initials": _initials(row.photo_date, row.local_pid, cfg),
                }
            )
            letters.append(
                {
                    "person_uid": row.person_uid,
                    "template_id": "letter-result",
                    "sent_at": row.photo_date + timedelta(days=int(row.letter_days)),
                    "photo_date": row.photo_date,
                }
            )
        if row.grade in {"R2", "R3"}:
            graded_at = row.photo_date + timedelta(days=int(row.grade_lag))
            wait = int(row.urgent_wait if row.grade == "R3" else row.mild_wait)
            referrals.append(
                {
                    "person_uid": row.person_uid,
                    "referred_at": graded_at,
                    "booked_at": graded_at + timedelta(days=max(wait - 7, 1)),
                    "seen_at": graded_at + timedelta(days=wait),
                    "specialist_agrees_urgent": row.grade == "R3",
                }
            )
    return {
        "person": people,
        "visit": pd.DataFrame(visits),
        "image": pd.DataFrame(images),
        "grade": pd.DataFrame(grades),
        "letter": pd.DataFrame(letters),
        "referral": pd.DataFrame(referrals),
    }


def _photo_dates(people: pd.DataFrame, cfg: dict, rng: np.random.Generator) -> list[date]:
    window = _span(cfg["window_start"], cfg["window_end"])
    leave = _span(cfg["grader_leave_start"], cfg["grader_leave_end"])
    outside = [day for day in window if day not in set(leave)]
    dates: list[date | None] = [None] * len(people)
    blank_positions = rng.permutation(np.flatnonzero(people["cohort"].to_numpy() == "photo_no_result"))
    leave_n = cfg["blank_in_leave"]
    for position in blank_positions[:leave_n]:
        dates[int(position)] = leave[int(rng.integers(0, len(leave)))]
    for position in blank_positions[leave_n:]:
        dates[int(position)] = outside[int(rng.integers(0, len(outside)))]
    completed_positions = np.flatnonzero(people["cohort"].to_numpy() == "completed")
    for position in completed_positions:
        dates[int(position)] = window[int(rng.integers(0, len(window)))]
    if any(day is None for day in dates):
        raise ValueError("A photographed person has no photo date.")
    return dates


def _span(start: date, end: date) -> list[date]:
    days = (end - start).days
    return [start + timedelta(days=offset) for offset in range(days + 1)]


def _eyes(row) -> list[tuple[str, str, str]]:
    if row.cohort == "photo_no_result":
        return [("L", "unknown", "")]
    if row.grade == "U":
        return [("L", "ungradable", "U")]
    return [("L", "readable", row.grade), ("R", "readable", row.grade)]


def _path(row, eye: str, image_id: str, sequence: int, used_names: set[str]) -> tuple[str, str]:
    if row.camera_class == "hospital":
        slug = row.screening_site.lower().replace(" ", "-")
        file_name = f"{image_id}.jpg"
        folder = f"pacs/{slug}"
    else:
        folder = "shared/EYE SCREEN 2024 final final"
        if sequence % 7 == 0:
            file_name = f"IMG_{sequence + 1:04d}.JPG"
        else:
            photo = row.photo_date
            stamp = photo.strftime("%d-%m-%y") if hasattr(photo, "strftime") else str(photo)
            file_name = f"{row.surname}_{row.forename[0]}_{stamp}_{eye}.jpg".replace(" ", "")
        if file_name in used_names:
            stem, ext = file_name.rsplit(".", 1)
            file_name = f"{stem}_{image_id}.{ext}"
    used_names.add(file_name)
    return file_name, f"{folder}/{file_name}"


def _initials(photo: date, local_pid: str, cfg: dict) -> str:
    active = ["AK", "BM"]
    if not (cfg["grader_leave_start"] <= photo <= cfg["grader_leave_end"]):
        active = ["AK", "BM", "CR"]
    return active[sum(ord(char) for char in local_pid) % len(active)]
