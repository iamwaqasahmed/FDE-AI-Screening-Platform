"""Sum gateway cost by hospital.

cost adds each row's sar into a total for that hospital. Hospitals
appear in the order they are first seen. A hospital with no rows is
omitted. The row must have hospital and sar. The totals start at zero
for a hospital's first row.
"""

from __future__ import annotations


def cost(rows: list[dict]) -> dict:
    """Return hospital names mapped to the sum of their sar values.

    int() reads sar. The result is a new dict. The input rows are not changed.
    """
    totals: dict[str, int] = {}
    for row in rows:
        # The hospital is stored as text. A missing key raises.
        hospital = str(row["hospital"])
        # Later rows for the same hospital add to the total already stored.
        totals[hospital] = totals.get(hospital, 0) + int(row["sar"])
    return totals
