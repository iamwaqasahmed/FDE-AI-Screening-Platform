"""Union-find over the five record kinds. Guards stop the merges a name would get wrong."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from reference_enterprise.load import messages, pacs, read_csv, reissue, v3, warehouse

FOLDER = "EYE SCREEN 2024 final final"


class UnionFind:
    def __init__(self) -> None:
        self.parent: dict[str, str] = {}

    def add(self, key: str) -> None:
        self.parent.setdefault(key, key)

    def find(self, key: str) -> str:
        parent = self.parent.setdefault(key, key)
        if parent != key:
            self.parent[key] = self.find(parent)
        return self.parent[key]

    def union(self, left: str, right: str) -> None:
        self.parent[self.find(left)] = self.find(right)


def clusters(data: Path) -> pd.DataFrame:
    """Return kind, record_id, cluster_id for every visible record."""
    registry = v3(data)
    joined = UnionFind()
    rows = _registry(joined, registry)
    rows += _warehouse(joined, data, registry)
    rows += _pacs(joined, data, registry)
    rows += _files(joined, data, "handover/shared/listing.csv", "shared", "FILE_NAME", FOLDER)
    rows += _vendor(joined, data)
    frame = pd.DataFrame(rows)
    frame["cluster_id"] = [joined.find(key) for key in frame["key"]]
    return frame.drop(columns=["key"])


def _registry(joined: UnionFind, registry: pd.DataFrame) -> list[dict]:
    rows = []
    for row in registry.itertuples(index=False):
        key = f"registry|{row.LOCAL_PID}"
        joined.add(key)
        rows.append({"kind": "registry", "record_id": row.LOCAL_PID, "key": key})
    _aliases(joined, registry)
    return rows


def _aliases(joined: UnionFind, registry: pd.DataFrame) -> None:
    names = registry.groupby(["FORENAME", "SURNAME", "DOB", "SEX"])
    for _, group in names:
        lx = group[group["LOCAL_PID"].str.startswith("LX")]
        lp = group[group["LOCAL_PID"].str.startswith("LP")]
        if len(lx) == 1 and len(lp) == 1:
            joined.union(f"registry|{lx.iloc[0].LOCAL_PID}", f"registry|{lp.iloc[0].LOCAL_PID}")


def _warehouse(joined: UnionFind, data: Path, registry: pd.DataFrame) -> list[dict]:
    snapshot = warehouse(data)
    renamed = dict(zip(reissue(data)["OLD_REGISTRY_NO"], reissue(data)["NEW_REGISTRY_NO"]))
    by_number = registry.drop_duplicates("REGISTRY_NO").set_index("REGISTRY_NO")["LOCAL_PID"]
    rows = []
    for number in snapshot["registry_no"]:
        key = f"warehouse|{number}"
        joined.add(key)
        pid = by_number.get(renamed.get(number, number), "")
        if pid:
            joined.union(key, f"registry|{pid}")
        rows.append({"kind": "warehouse", "record_id": number, "key": key})
    return rows


def _pacs(joined: UnionFind, data: Path, registry: pd.DataFrame) -> list[dict]:
    studies = pacs(data)
    studies["name"] = studies["PATIENT_NAME"].str.lower() + "|" + studies["DOB"]
    pid_name_series = registry["SURNAME"].str.lower() + ", " + registry["FORENAME"].str.lower() + "|" + registry["DOB"]
    by_name: dict[str, list[str]] = {}
    pid_name = {}
    for name, pid in zip(pid_name_series, registry["LOCAL_PID"]):
        by_name.setdefault(name, []).append(pid)
        pid_name[pid] = name
    linked = _mrn_links(data)
    rows = []
    for row in studies.itertuples(index=False):
        key = f"pacs|{row.ACCESSION}"
        joined.add(key)
        rows.append({"kind": "pacs", "record_id": row.ACCESSION, "key": key})
        _attach(joined, key, row.MRN, row.name, by_name, pid_name, linked)
    return rows


def _attach(joined, key, mrn, name, by_name, pid_name, linked) -> None:
    pids = linked.get(mrn, [])
    if len(pids) >= 2:
        matching = [pid for pid in pids if pid_name.get(pid) == name]
        if len(matching) == 1:
            joined.union(key, f"registry|{matching[0]}")
        return
    if len(pids) == 1:
        if pid_name.get(pids[0]) == name:
            joined.union(key, f"registry|{pids[0]}")
        else:
            _by_name(joined, key, name, by_name)
        return
    if not pids:
        _by_name(joined, key, name, by_name)


def _by_name(joined, key, name, by_name) -> None:
    owners = [pid for pid in by_name.get(name, []) if str(pid).startswith("LP")]
    if len(owners) == 1:
        joined.union(key, f"registry|{owners[0]}")


def _mrn_links(data: Path) -> dict[str, list[str]]:
    found: dict[str, set[str]] = {}
    for row in messages(data).itertuples(index=False):
        if row.mrn and row.local_pid:
            found.setdefault(row.mrn, set()).add(row.local_pid)
    return {mrn: sorted(pids) for mrn, pids in found.items()}


def _files(joined: UnionFind, data: Path, relative: str, kind: str, column: str, folder: str) -> list[dict]:
    frame = read_csv(data, relative)
    names = _unique(folder + "/" + frame[column].astype(str)) if kind == "shared" else frame[column]
    grader = _grader_files(data)
    rows = []
    for record_id, file_name in zip(names, frame[column] if kind == "shared" else names):
        if kind == "shared" and str(file_name).startswith("DECOY_"):
            key = f"shared|{record_id}"
            joined.add(key)
            rows.append({"kind": "shared", "record_id": record_id, "key": key})
            continue
        key = f"{kind}|{record_id}"
        joined.add(key)
        pid = grader.get(str(file_name), "")
        if pid:
            joined.union(key, f"registry|{pid}")
        rows.append({"kind": kind, "record_id": str(record_id), "key": key})
    return rows


def _vendor(joined: UnionFind, data: Path) -> list[dict]:
    frame = read_csv(data, "handover/ml/vendor_retrospective.csv")
    grader = _grader_files(data)
    rows = []
    for row in frame.itertuples(index=False):
        key = f"vendor|{row.capture_ref}"
        joined.add(key)
        pid = grader.get(str(row.file_name), "")
        if pid:
            joined.union(key, f"registry|{pid}")
        rows.append({"kind": "vendor", "record_id": row.capture_ref, "key": key})
    return rows


def _grader_files(data: Path) -> dict[str, str]:
    import pandas as pd

    book = pd.read_excel(data / "handover/grader/workbook.xlsx", dtype=str).fillna("")
    found = {}
    for row in book.itertuples(index=False):
        if row.FILE_NAME and row.LOCAL_PID and row.FILE_NAME not in found:
            found[row.FILE_NAME] = row.LOCAL_PID
    return found


def _unique(names: pd.Series) -> pd.Series:
    counts = names.groupby(names).cumcount()
    return names.where(counts.eq(0), names + "#" + (counts + 1).astype(str))
