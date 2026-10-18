"""Visible records rebuilt from the same frames the handover writers use."""

from __future__ import annotations

import pandas as pd

from simulation.eval.enterprise.drop import v3_frame
from simulation.ml.retrospective import scored_frame
from simulation.systems.mrn import MrnIndex
from simulation.systems.resolve import ids_on
from simulation.systems.warehouse import _snapshot
from simulation.world.clock import SNAPSHOT, detail_start, iso
from simulation.world.quotas import DECOYS

FOLDER = "EYE SCREEN 2024 final final"


def registry_rows(world: dict, canon: dict[str, str]) -> pd.DataFrame:
    frame = v3_frame(world).rename(columns={"FORENAME": "forename", "SURNAME": "surname", "DOB": "dob"})
    return _finish("registry", frame["LOCAL_PID"], frame["person_uid"], canon, link_name=_name(frame), link_registry=frame["REGISTRY_NO"])


def warehouse_rows(world: dict, canon: dict[str, str]) -> pd.DataFrame:
    people, events, identifiers = world["people"], world["events"], world["identifiers"]
    snapshot = _snapshot(people, events, identifiers)
    numbers = _number_owner(identifiers)
    source = snapshot["registry_no"].map(numbers).fillna("")
    return _finish("warehouse", snapshot["registry_no"], source, canon, link_registry=snapshot["registry_no"])


def pacs_rows(world: dict, canon: dict[str, str]) -> pd.DataFrame:
    events, people = world["events"], world["people"]
    studies = events[events["capture"].eq("pacs")].copy()
    index = MrnIndex(world["identifiers"])
    studies["mrn"] = [
        index.get(row.person_uid, row.site, row.photo_date, prefer_split=row.scenario == "split" and int(row.event_id[1:]) % 2 == 0)
        for row in studies.itertuples(index=False)
    ]
    names = people.set_index("person_uid")
    studies["forename"] = studies["person_uid"].map(names["forename"])
    studies["surname"] = studies["person_uid"].map(names["surname"])
    studies["dob"] = studies["person_uid"].map(names["dob"])
    accession = studies["file_name"].str.replace(".dcm", "", regex=False)
    return _finish("pacs", accession, studies["person_uid"], canon, link_mrn=studies["mrn"], link_name=_name(studies))


def shared_rows(world: dict, canon: dict[str, str]) -> pd.DataFrame:
    real = world["events"]
    real = real[real["capture"].eq("shared_folder")]
    names = _unique(FOLDER + "/" + real["file_name"].astype(str))
    captured = _finish("shared", names, real["person_uid"], canon)
    decoy_names = [f"{FOLDER}/DECOY_{index:04d}.jpg" for index in range(DECOYS)]
    decoys = _finish("shared", pd.Series(decoy_names), pd.Series([""] * DECOYS), canon)
    decoys["decoy"] = "1"
    return pd.concat([captured, decoys], ignore_index=True)


def vendor_rows(world: dict, canon: dict[str, str]) -> pd.DataFrame:
    scored = scored_frame(world["events"])
    return _finish("vendor", scored["capture_ref"], scored["person_uid"], canon)


def grader_file_names(events: pd.DataFrame) -> set[str]:
    recent = iso(detail_start())
    queue = events[events["grade"].eq("") | events["graded_at"].ge(recent) | events["photo_date"].ge(recent)]
    return set(queue["file_name"].astype(str))


def _number_owner(identifiers: pd.DataFrame) -> pd.Series:
    numbers = ids_on(identifiers, "registry_no", iso(SNAPSHOT)).rename("registry_no")
    flipped = numbers.reset_index()
    flipped.columns = ["person_uid", "registry_no"]
    flipped = flipped[flipped["registry_no"].ne("")].drop_duplicates("registry_no")
    return flipped.set_index("registry_no")["person_uid"]


def _name(frame: pd.DataFrame) -> pd.Series:
    return frame["forename"].str.lower() + "|" + frame["surname"].str.lower() + "|" + frame["dob"].astype(str)


def _unique(names: pd.Series) -> pd.Series:
    copy = names.astype(str).copy()
    counts = copy.groupby(copy).cumcount()
    return copy.where(counts.eq(0), copy + "#" + (counts + 1).astype(str))


def _finish(kind: str, record_id, source, canon: dict[str, str], link_mrn=None, link_name=None, link_registry=None) -> pd.DataFrame:
    source = pd.Series(source).astype(str).reset_index(drop=True)
    frame = pd.DataFrame({
        "kind": kind,
        "record_id": pd.Series(record_id).astype(str).reset_index(drop=True),
        "source": source,
        "person": source.map(lambda uid: canon.get(uid, uid) if uid else ""),
    })
    frame["link_mrn"] = "" if link_mrn is None else pd.Series(link_mrn).astype(str).reset_index(drop=True)
    frame["link_name"] = "" if link_name is None else pd.Series(link_name).astype(str).reset_index(drop=True)
    frame["link_registry"] = "" if link_registry is None else pd.Series(link_registry).astype(str).reset_index(drop=True)
    frame["decoy"] = ""
    return frame.fillna("")

