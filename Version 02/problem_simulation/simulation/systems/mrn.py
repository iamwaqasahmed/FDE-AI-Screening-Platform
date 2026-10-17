"""Which hospital MRN a site would have shown for a person on a date."""

from __future__ import annotations

import pandas as pd


class MrnIndex:
    def __init__(self, identifiers: pd.DataFrame) -> None:
        self._rows: dict[tuple[str, str], list] = {}
        pool = identifiers[identifiers["id_type"] == "mrn"]
        for row in pool.itertuples(index=False):
            self._rows.setdefault((row.person_uid, row.site), []).append(row)

    def get(self, person_uid: str, site: str, on: str, prefer_split: bool = False) -> str:
        found = [
            row
            for row in self._rows.get((person_uid, site), ())
            if row.valid_from <= on and (row.valid_to == "" or row.valid_to > on)
        ]
        reversed_merge = [row for row in found if row.relation == "merge_reversed"]
        if reversed_merge:
            return str(reversed_merge[0].id_value)
        if prefer_split:
            split = [row for row in found if row.relation == "split"]
            if split:
                return str(split[0].id_value)
        assigned = [row for row in found if row.relation == "assigned"]
        chosen = assigned or found
        return "" if not chosen else str(chosen[0].id_value)
