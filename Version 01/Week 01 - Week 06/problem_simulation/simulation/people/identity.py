"""Identifier assertions. person_uid stays in this table and out of the drop."""

from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd

from simulation.people.checkdigit import national, typo
from simulation.people.confidence import confidence
from simulation.people.identity_extra import add_extras
from simulation.world.clock import HISTORY_START, REUSE_GAP_DAYS, iso
from simulation.world.sites import NCEC

OPEN = ""


def build_identifiers(people: pd.DataFrame, events: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    rows: list[dict] = []
    _registry(people, rows)
    _local_and_national(people, rows, rng)
    _mrn(people, events, rows)
    add_extras(people, rows, _add, _opened, rng)
    frame = pd.DataFrame(rows)
    frame.insert(0, "assertion_id", [f"A{index + 1:07d}" for index in range(len(frame))])
    return frame


def _registry(people: pd.DataFrame, rows: list[dict]) -> None:
    donors = people[people["reuse_role"] == "donor"].sort_values("person_uid")
    recipients = people[people["reuse_role"] == "recipient"].sort_values("person_uid")
    if len(donors) != len(recipients):
        raise ValueError("Reuse donors and recipients must be paired.")
    reissue_on = {
        recipient.person_uid: _reissue(donor.flag_true_on)
        for donor, recipient in zip(donors.itertuples(index=False), recipients.itertuples(index=False))
    }
    donor_numbers: dict[str, str] = {}
    for index, person in enumerate(people.sort_values("person_uid").itertuples(index=False), start=1):
        number = f"HR{index:06d}"
        start = _opened(person.diagnosis_date)
        if person.reuse_role == "donor":
            donor_numbers[person.person_uid] = number
            _add(rows, person, "registry", "registry_no", number, start, person.flag_true_on, "assigned", "")
        elif person.reuse_role == "recipient":
            _add(rows, person, "registry", "registry_no", number, start, iso(reissue_on[person.person_uid]), "assigned", "")
        else:
            _add(rows, person, "registry", "registry_no", number, start, OPEN, "assigned", "")
    for donor, recipient in zip(donors.itertuples(index=False), recipients.itertuples(index=False)):
        _add(
            rows,
            recipient,
            "registry",
            "registry_no",
            donor_numbers[donor.person_uid],
            iso(reissue_on[recipient.person_uid]),
            OPEN,
            "reuse",
            "",
        )


def _local_and_national(people: pd.DataFrame, rows: list[dict], rng: np.random.Generator) -> None:
    canonical = people[people["alias_of"] == ""].sort_values("person_uid")
    status = _national_status(len(canonical), rng)
    confirmed = [national(index + 1) for index in range(len(canonical))]
    wrong_pool = np.roll(np.array(confirmed), 1)
    for index, person in enumerate(canonical.itertuples(index=False)):
        start = _opened(person.diagnosis_date)
        _add(rows, person, "screening", "local_pid", f"LP{index + 1:06d}", start, OPEN, "assigned", "")
        kind = status[index]
        if kind == "missing":
            value, relation = "", "missing"
        elif kind == "provisional":
            value, relation = f"PID{index + 1:08d}", "provisional"
        elif kind == "wrong":
            value, relation = str(wrong_pool[index]), "wrong"
        elif kind == "typo":
            value, relation = typo(confirmed[index]), "typo"
        else:
            value, relation = confirmed[index], "assigned"
        _add(rows, person, "national-spine", "national_id", value, start, OPEN, relation, "", kind)
    for index, person in enumerate(people[people["alias_of"] != ""].sort_values("person_uid").itertuples(index=False), start=1):
        _add(rows, person, "screening", "local_pid", f"LX{index:06d}", _opened(person.diagnosis_date), OPEN, "assigned", "")


def _mrn(people: pd.DataFrame, events: pd.DataFrame, rows: list[dict]) -> None:
    pacs = events[events["capture"] == "pacs"]
    first = pacs.sort_values(["site", "person_uid", "photo_date"]).groupby(["person_uid", "site"], as_index=False).head(1)
    by_uid = people.set_index("person_uid", drop=False)
    sequence = 1
    for row in first.itertuples(index=False):
        value = f"MRN{sequence:07d}"
        sequence += 1
        _add(rows, by_uid.loc[row.person_uid], "pacs", "mrn", value, row.photo_date, OPEN, "assigned", row.site)
    _share_false_merges(people, rows)
    sequence = _add_splits(people, events, rows, sequence)
    _add_true_merges(people, rows)


def _share_false_merges(people: pd.DataFrame, rows: list[dict]) -> None:
    uids = people.loc[people["scenario"] == "false_merge", "person_uid"].sort_values().tolist()
    for start in range(0, len(uids), 2):
        left, right = uids[start], uids[start + 1]
        shared = _mrn_value(rows, left, NCEC)
        if not shared:
            continue
        retargeted = False
        for row in rows:
            if row["person_uid"] == right and row["id_type"] == "mrn" and row["site"] == NCEC:
                row["id_value"] = shared
                row["relation"] = "false_merge"
                retargeted = True
        if not retargeted:
            person = people.loc[people["person_uid"] == right].iloc[0]
            _add(rows, person, "pacs", "mrn", shared, _opened(person.diagnosis_date), OPEN, "false_merge", NCEC)


def _add_splits(people: pd.DataFrame, events: pd.DataFrame, rows: list[dict], sequence: int) -> int:
    for person in people[people["scenario"] == "split"].sort_values("person_uid").itertuples(index=False):
        if not _mrn_value(rows, person.person_uid, NCEC):
            continue
        photo = events.loc[events["person_uid"] == person.person_uid, "photo_date"].min()
        later = iso(date.fromisoformat(str(photo)[:10]) + timedelta(days=30))
        value = f"MRN{sequence:07d}"
        sequence += 1
        _add(rows, person, "pacs", "mrn", value, later, OPEN, "split", NCEC)
    return sequence


def _add_true_merges(people: pd.DataFrame, rows: list[dict]) -> None:
    for alias in people[people["scenario"] == "true_merge"].itertuples(index=False):
        shared = _mrn_value(rows, alias.alias_of, NCEC)
        if not shared:
            continue
        _add(rows, alias, "pacs", "mrn", shared, _opened(alias.diagnosis_date), OPEN, "merge", NCEC)


def _mrn_value(rows: list[dict], person_uid: str, site: str) -> str:
    for row in rows:
        if row["person_uid"] == person_uid and row["id_type"] == "mrn" and row["site"] == site and row["relation"] == "assigned":
            return row["id_value"]
    return ""


def _national_status(count: int, rng: np.random.Generator) -> np.ndarray:
    provisional = int(count * 0.15)
    missing = int(count * 0.10)
    wrong = int(count * 0.05)
    typos = int(count * 0.02)
    confirmed = count - provisional - missing - wrong - typos
    labels = np.array(
        ["confirmed"] * confirmed + ["provisional"] * provisional + ["missing"] * missing + ["wrong"] * wrong + ["typo"] * typos
    )
    return labels[rng.permutation(count)]


def _opened(diagnosis_date: str) -> str:
    if diagnosis_date and diagnosis_date > iso(HISTORY_START):
        return diagnosis_date
    return iso(HISTORY_START)


def _reissue(flag_true_on: str) -> date:
    return date.fromisoformat(flag_true_on) + timedelta(days=REUSE_GAP_DAYS)


def _add(rows, person, system, id_type, value, valid_from, valid_to, relation, site, national_status: str = "") -> None:
    confirmed = id_type == "national_id" and national_status == "confirmed"
    rows.append(
        {
            "person_uid": _field(person, "person_uid"),
            "system": system,
            "id_type": id_type,
            "id_value": value,
            "valid_from": valid_from,
            "valid_to": valid_to,
            "relation": relation,
            "site": site,
            "claimed_forename": _field(person, "forename"),
            "claimed_surname": _field(person, "surname"),
            "claimed_dob": _field(person, "dob"),
            "claimed_postcode": _field(person, "postcode_sector"),
            "national_status": national_status if id_type == "national_id" else "",
            "confidence": confidence("confirmed" if confirmed else "", True, True, True),
        }
    )


def _field(person, name: str):
    if isinstance(person, pd.Series):
        return person[name]
    return getattr(person, name)
