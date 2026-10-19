"""Overdue referrals and the vendor cohort, counted from the files."""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

from reference_enterprise.load import messages, read_csv

LEAK_SEED = 20261012
SEEN_ON = re.compile(r"in clinic on (\d{1,2}/\d{1,2}/\d{4}|\d{1,2} [A-Z][a-z]+ \d{4})", re.I)
MRN = re.compile(r"Hospital number: (\S+)")


def overdue(data: Path, registry: pd.DataFrame) -> dict:
    frame = messages(data)
    filled = _epr(data)
    latest = frame.sort_values("referred").groupby("local_pid", as_index=False).tail(1)
    latest_blank = latest[latest["seen"].eq("") & latest["local_pid"].ne("")]
    still = latest_blank[~latest_blank["mrn"].isin(filled)]
    flags = registry.set_index("LOCAL_PID")["FLAG"]
    gone = still["local_pid"].map(flags).isin(["DECEASED", "MOVED"])
    return {
        "rows": int(len(frame)),
        "blank_rows": int(frame["seen"].eq("").sum()),
        "latest_blank": int(len(latest_blank)),
        "upper_bound": int((~gone).sum()),
        "is_upper_bound": True,
    }


def vendor(data: Path) -> tuple[dict, dict]:
    frame = read_csv(data, "handover/ml/vendor_retrospective.csv")
    book = pd.read_excel(data / "handover/grader/workbook.xlsx", dtype=str).fillna("")
    names = set(book["FILE_NAME"]) - {""}
    people = book.drop_duplicates("FILE_NAME").set_index("FILE_NAME")["LOCAL_PID"]
    ordered = frame.sort_values("capture_ref")
    linked = ordered["file_name"].isin(names)
    cohort = {
        "captures": int(len(frame)),
        "linked_by_file": int(linked.sum()),
        "linked_people": int(ordered.loc[linked, "file_name"].map(people).replace("", pd.NA).nunique()),
        "unlinked": int((~linked).sum()),
    }
    person = np.where(linked.to_numpy(), ordered["file_name"].map(people).fillna("").to_numpy(), "solo:" + ordered["capture_ref"].to_numpy())
    order = np.random.default_rng(LEAK_SEED).permutation(len(person))
    cut = int(0.8 * len(person))
    train = set(person[order[:cut]])
    test = person[order[cut:]]
    leak = round(float(np.mean([item in train for item in test])), 4) if len(test) else 0.0
    return cohort, {"seed": LEAK_SEED, "leak_share": leak}


def _epr(data: Path) -> set[str]:
    found = set()
    for path in (data / "handover/epr_letters").glob("*.txt"):
        text = path.read_text(encoding="utf-8")
        mrn = MRN.search(text)
        if mrn and SEEN_ON.search(text):
            found.add(mrn.group(1))
    return found
