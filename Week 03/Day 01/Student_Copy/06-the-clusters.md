# 06 — The clusters

[Chapter 05](05-the-sprint.md) sequenced the sprint. This chapter replaces the dates, the clinic codes, and the cluster job.

You replace six files under `work/`, in this order:

1. [dates.py](work/app/dates.py), under Replace the dates
2. [test_dates.py](work/tests/test_dates.py), under Replace the date test
3. [codes.py](work/app/codes.py), under Replace the clinic codes
4. [test_codes.py](work/tests/test_codes.py), under Replace the clinic-code test
5. [cluster.py](work/app/cluster.py), under Replace the cluster job
6. [test_cluster.py](work/tests/test_cluster.py), under Replace the cluster test

Paste only those six blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged.

Scroll down to the heading Replace the dates. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Five more Replace headings follow it. Use the four steps from [chapter 05](05-the-sprint.md) on each one. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture or a check. You do not paste those.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste this chapter again from the chapter source. Do not repair the spaces by hand.

Do not run the suite on this page. The suite command is in [chapter 08](08-the-advanced.md). It is not a check. The checks are only in [chapter 10](10-finish.md).

`parents[1]` in a test is the path line that loads the `app` folder beside `tests`. It is not a mother, a newborn, or a patient id. When a later line says to leave `parents[1]`, leave that path line.

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them. The first block you copy is under Replace the dates, further down this page.

Open [identifiers.jsonl](packet/release/history/identifiers.jsonl) and search for `hijri-end`. The `dob` is `1448-07-29`. Search for `hijri-start`. The `dob` is `1448-08-01`. Open [clinics.md](packet/release/catalog/clinics.md) and search for `June 2024`. You already did this in chapter 03. The shells below do not follow those rows.

1. [dates.py](packet/app/dates.py). Search for `timedelta`. That name is the shell. A Hijri day of 1, or a day of 29 or later, moves one day later. The next block is a picture of that file. Do not paste it.

```text
"""Hijri dates, one day late at the month boundary.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

gregorian adds one day when the Hijri day is 1 or at least 29.
While this shell is the file that runs, the identity check says a
Hijri month boundary is off by a day.
"""

from __future__ import annotations

from datetime import date, timedelta


def gregorian(value: str, era: str) -> str:
    """Shift a Hijri month boundary forward by one day.

    value is the date text. era is gregorian, or empty for a Hijri
    date. A year under 1400 is returned as written. A Hijri day of
    1, or a day of 29 or later, is moved one day later.
    """
    year = int(value.split("-")[0])
    if era == "gregorian" or year < 1400:
        return value
    converted = _from_hijri(value)
    day = int(value.split("-")[2])
    if day == 1 or day >= 29:
        converted += timedelta(days=1)
    return converted.isoformat()


def _from_hijri(value: str) -> date:
    """Turn one Hijri date into the tabular civil day, before the shift."""
    year, month, day = (int(part) for part in value.split("-"))
    return _jd_to_date(_hijri_jd(year, month, day))


def _hijri_jd(year: int, month: int, day: int) -> int:
    """Julian day number for a tabular Hijri date."""
    # The arithmetic is the tabular conversion, and the day is not shifted.
    return (11 * year + 3) // 30 + 354 * year + 30 * month - (month - 1) // 2 + day + 1948440 - 385


def _jd_to_date(jd: int) -> date:
    """Civil date for a Julian day number.

    The steps turn that number into a century, a year, a month, and a day.
    """
    # The arithmetic is the tabular conversion, and the day is not shifted.
    left = jd + 68569
    century = (4 * left) // 146097
    left = left - (146097 * century + 3) // 4
    year = (4000 * (left + 1)) // 1461001
    left = left - (1461 * year) // 4 + 31
    month = (80 * left) // 2447
    day = left - (2447 * month) // 80
    left = month // 11
    month = month + 2 - 12 * left
    year = 100 * (century - 49) + year + left
    return date(year, month, day)
```

2. [codes.py](packet/app/codes.py). Search for `del as_of, facility`. That line is the shell. `ENDO-CLN` is rewritten to `END-01`. The next block is a picture of that file. Do not paste it.

```text
"""Clinic codes taken from the catalog.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

clinic rewrites ENDO-CLN back to END-01. The date and the facility
are ignored. While this shell is the file that runs, the identity
check says the stale clinic code was kept.
"""

from __future__ import annotations


def clinic(code: str, as_of: str, facility: str) -> str:
    """Keep the catalog code and drop the newer endocrinology code.

    code is the clinic code on the row. as_of and facility are
    ignored. ENDO-CLN becomes END-01. Every other code is kept.
    """
    del as_of, facility
    if code == "ENDO-CLN":
        return "END-01"
    return code
```

3. [cluster.py](packet/app/cluster.py). Search for `return len(rows)`. That line is the shell. A shared phone, a shared MRN, and `merge_with` are links, and the count is the row count. The next block is a picture of that file. Do not paste it.

```text
"""Merge rows that share a national id, a phone, or an MRN.

This is the shell. Chapter 06 replaces the copy under work/app.
Leave this file in the packet unchanged.

partition also follows merge_with. patient_count returns the row
count. removals returns every waitlist row. While this shell is
the file that runs, the identity check says a mother and a newborn
were merged, twins were merged, a reused MRN was linked, and a row
count was used as a patient count.
"""

from __future__ import annotations


def partition(rows: list[dict]) -> list[list[str]]:
    """Union rows that share a national id, a phone, an MRN, or merge_with.

    A newborn, a twin, and a reused MRN are merged when those fields
    match. The relation field is not read.
    """
    # Each row starts in its own group. The buckets keep the first row id for each shared value.
    parent = {row["row_id"]: row["row_id"] for row in rows}
    buckets = {"national_id": {}, "phone": {}, "mrn": {}}
    by_mrn = {}
    for row in rows:
        # Record this MRN. Join this row when a national id, a phone, or an MRN was already seen.
        by_mrn[row["mrn"]] = row["row_id"]
        for field, bucket in buckets.items():
            value = row[field]
            if not value:
                continue
            if value in bucket:
                _union(parent, row["row_id"], bucket[value])
            else:
                bucket[value] = row["row_id"]
    for row in rows:
        # Join a row whose merge_with names another row's MRN.
        other = by_mrn.get(row["merge_with"])
        if other:
            _union(parent, row["row_id"], other)
    # Gather the row ids under each group and return those groups in order.
    groups: dict[str, list[str]] = {}
    for row in rows:
        groups.setdefault(_find(parent, row["row_id"]), []).append(row["row_id"])
    return sorted(sorted(group) for group in groups.values())


def patient_count(rows: list[dict]) -> int:
    """Count rows. This is not a count of people."""
    return len(rows)


def removals(waitlist: list[dict]) -> list[str]:
    """Return every waitlist row, whatever the flag says."""
    return sorted(row["row_id"] for row in waitlist)


def _find(parent: dict[str, str], item: str) -> str:
    """Find the group id, and compress the path on the way.

    The steps point the current row at its grandparent and move there
    until a row points at itself.
    """
    while parent[item] != item:
        parent[item] = parent[parent[item]]
        item = parent[item]
    return item


def _union(parent: dict[str, str], left: str, right: str) -> None:
    """Put two row ids in the same group."""
    parent[_find(parent, left)] = _find(parent, right)
```

The shell tests sit beside those files in `packet/tests`. Leave them. You replace the work copies below, not these pictures.

The pictures end here. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the next heading that starts with Replace.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

Three jobs, one person.

`gregorian` leaves a Gregorian date alone. A Hijri date, empty era and a year of 1400 or later, goes through the tabular calendar. That calendar gives each month a fixed length, so a computer can turn the date into a civil day. `_from_hijri` uses a Julian day number, which is only the count in that turn, and does not shift the day by one at the month boundary. The shell added a day when the Hijri day was 1 or at least 29. The check calls that a boundary off by a day. It does not print the civil day. The test checks the gap instead: 14 civil days from `1448-07-15` to `1448-07-29`, then 2 civil days to `1448-08-01`.

`clinic` returns the endocrinology code in force at `h-wadi` on the row's date. Before June 2024 the code stays `END-01`. The file treats June 2024 as starting on `2024-06-01`. On and after that date both endocrinology codes at that hospital are `ENDO-CLN`. Another hospital keeps the code on the row. The shell rewrote the new code backward and ignored the date.

`partition` is who counts as one person. Week 1's open item, one person stored as two rows, is the `replaces` link: an Iqama row joins the visitor national id it names. A shared national id also links two rows, and a newborn and a twin stay out of that link. A shared phone, a reused MRN, and `merge_with` are not links. A failed check digit is not read, so that person stays. `_find` and `_union` only keep the groups. They do not decide who belongs together. `patient_count` counts groups, not rows. `removals` only proposes a removal for a late death flag or a seen-elsewhere flag. The person stays in the cluster file. The shell merged on phone and MRN and counted rows.

Before you paste, say why a mother and a newborn who share a national id are still two people, and why a row count is not the patient count.

This section adds no file and no command.

## Replace the dates

This block replaces [work/app/dates.py](work/app/dates.py). The full path is `Week 03/Day 01/Student_Copy/work/app/dates.py`. It does not replace [packet/app/dates.py](packet/app/dates.py). It does not replace the test.

Open the work file. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save.

```text
"""Hijri dates on the tabular calendar.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell adds one day when the Hijri day is 1 or at least 29.
While that shell is the file that runs, the identity check says a
Hijri month boundary is off by a day. The check does not name the
converted day.
"""

from __future__ import annotations

from datetime import date


def gregorian(value: str, era: str) -> str:
    """Return the civil day, or the original string for a Gregorian date.

    value is the date text. era is gregorian, or empty for a Hijri
    date. A year under 1400 is already a civil year. A Hijri date
    uses the tabular calendar. The day is not shifted.
    """
    year = int(value.split("-")[0])
    # A Gregorian date, or a year under 1400, is already civil.
    if era == "gregorian" or year < 1400:
        return value
    # The tabular day. The shell adds one day at the month boundary.
    return _from_hijri(value).isoformat()


def _from_hijri(value: str) -> date:
    """Turn one Hijri date into the tabular civil day."""
    year, month, day = (int(part) for part in value.split("-"))
    return _jd_to_date(_hijri_jd(year, month, day))


def _hijri_jd(year: int, month: int, day: int) -> int:
    """Julian day number for a tabular Hijri date."""
    # The arithmetic is the tabular conversion, and the day is not shifted.
    return (11 * year + 3) // 30 + 354 * year + 30 * month - (month - 1) // 2 + day + 1948440 - 385


def _jd_to_date(jd: int) -> date:
    """Civil date for a Julian day number. The day number is not shifted.

    The steps turn that number into a century, a year, a month, and a day.
    """
    # The arithmetic is the tabular conversion, and the day is not shifted.
    left = jd + 68569
    century = (4 * left) // 146097
    left = left - (146097 * century + 3) // 4
    year = (4000 * (left + 1)) // 1461001
    left = left - (1461 * year) // 4 + 31
    month = (80 * left) // 2447
    day = left - (2447 * month) // 80
    left = month // 11
    month = month + 2 - 12 * left
    year = 100 * (century - 49) + year + left
    return date(year, month, day)
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `return _from_hijri(value).isoformat()`. You should see `_hijri_jd`. That helper is still here. That is expected. You should not see `timedelta`. If you see `timedelta`, you pasted the picture. Paste this block again.

## Replace the date test

This block replaces [work/tests/test_dates.py](work/tests/test_dates.py). The full path is `Week 03/Day 01/Student_Copy/work/tests/test_dates.py`. It does not replace [packet/tests/test_dates.py](packet/tests/test_dates.py). It does not replace `dates.py`.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""The civil day at a Hijri month boundary.

Chapter 06 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the boundary to shift. This test expects
the tabular day: 14 days from the 15th to the 29th, then 2 days
from the 29th to the 1st. A Gregorian date is returned unchanged.
The line parents[1] stays as it is.
"""

import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from dates import gregorian


class DateTests(unittest.TestCase):
    """The civil day at a Hijri month boundary."""
    def test_month_boundary_stays_on_the_civil_day(self) -> None:
        """The 29th stays 14 days after the 15th, and the 1st is 2 days later."""
        middle = date.fromisoformat(gregorian("1448-07-15", ""))
        end = date.fromisoformat(gregorian("1448-07-29", ""))
        start = date.fromisoformat(gregorian("1448-08-01", ""))
        self.assertEqual((end - middle).days, 14)
        self.assertEqual((start - end).days, 2)
        # A Gregorian date is not converted.
        self.assertEqual(gregorian("1990-04-02", "gregorian"), "1990-04-02")


if __name__ == "__main__":
    unittest.main()
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `test_month_boundary_stays_on_the_civil_day`. You should see `parents[1]`. Leave that line as it is. The test uses `1448-07-29` and `1448-08-01`. Those are the Hijri dates from the history file. The test checks a 14-day gap and then a 2-day gap. It does not write a converted day. `1990-04-02` stays on the Gregorian line. That is expected.

## Replace the clinic codes

This block replaces [work/app/codes.py](work/app/codes.py). The full path is `Week 03/Day 01/Student_Copy/work/app/codes.py`. It does not replace [packet/app/codes.py](packet/app/codes.py). It does not replace the test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""Clinic code in force on the row date.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell rewrites ENDO-CLN back to END-01 and ignores the date.
While that shell is the file that runs, the identity check says the
stale clinic code was kept. The check does not name the code.
"""

from __future__ import annotations

CHANGE = "2024-06-01"
ENDO = {"END-01", "ENDO-CLN"}


def clinic(code: str, as_of: str, facility: str) -> str:
    """Return the endocrinology code in force at h-wadi.

    code is the code on the row. as_of is the row date. facility is
    the hospital. Before June 2024, END-01 stays. On and after that
    date, both endocrinology codes at h-wadi are ENDO-CLN. Any other
    facility keeps the code on the row.
    """
    # h-wadi, on or after the change, uses the new endocrinology code.
    if facility == "h-wadi" and as_of >= CHANGE and code in ENDO:
        return "ENDO-CLN"
    # A row before the change, or another facility, keeps its code.
    return code
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `2024-06-01`. You should see `END-01` inside the set. A row before June still returns that code. That is expected. You should not see `del as_of, facility`. If you see that line, you pasted the picture. Paste this block again.

## Replace the clinic-code test

This block replaces [work/tests/test_codes.py](work/tests/test_codes.py). The full path is `Week 03/Day 01/Student_Copy/work/tests/test_codes.py`. It does not replace the packet test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""Endocrinology at h-wadi changes in June 2024.

Chapter 06 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects the newer code to be rewritten backward.
This test expects END-01 before June, and ENDO-CLN on and after
the change, including a row that still says END-01. The line
parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from codes import clinic


class CodeTests(unittest.TestCase):
    """Endocrinology at h-wadi changes in June 2024."""
    def test_wadi_endo_changes_in_june_2024(self) -> None:
        """May keeps END-01. July at h-wadi is ENDO-CLN."""
        self.assertEqual(clinic("END-01", "2024-05-01", "h-wadi"), "END-01")
        self.assertEqual(clinic("ENDO-CLN", "2024-07-01", "h-wadi"), "ENDO-CLN")
        # A July row that still carries the old code is rewritten.
        self.assertEqual(clinic("END-01", "2024-07-01", "h-wadi"), "ENDO-CLN")


if __name__ == "__main__":
    unittest.main()
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `test_wadi_endo_changes_in_june_2024`. You should see `parents[1]`. Leave that line. `END-01` is still on the May line and on the July line that gets rewritten. That is expected.

## Replace the cluster job

This block replaces [work/app/cluster.py](work/app/cluster.py). The full path is `Week 03/Day 01/Student_Copy/work/app/cluster.py`. It does not replace [packet/app/cluster.py](packet/app/cluster.py). It does not replace the test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""One person at the case date. A shared phone or a reused MRN stays split.

Chapter 06 replaces the work copy with this file. Leave the packet
shell unchanged.

The shell merges on a shared national id, a shared phone, or a
shared MRN, and it counts rows. While that shell is the file that
runs, the identity check says a mother and a newborn were merged,
twins were merged, a reused MRN was linked, and a row count was
used as a patient count. The check does not name a national id.
"""

from __future__ import annotations


def partition(rows: list[dict]) -> list[list[str]]:
    """Group rows that are the same person.

    A shared national id links two rows. A newborn and a twin stay
    out of that link. A row whose replaces field names another
    national id joins that person. Phone, MRN, and merge_with are
    not links. A failed check digit is not read, so that person stays.
    """
    parent = {row["row_id"]: row["row_id"] for row in rows}
    by_national_id: dict[str, str] = {}
    for row in rows:
        # A mother and a newborn stay apart. Twins stay apart.
        if row["relation"] in {"newborn", "twin"}:
            continue
        national_id = row["national_id"]
        if not national_id:
            continue
        if national_id in by_national_id:
            _union(parent, row["row_id"], by_national_id[national_id])
        else:
            by_national_id[national_id] = row["row_id"]
    for row in rows:
        # A visitor number replaced by an Iqama is one person.
        if not row["replaces"]:
            continue
        for other in rows:
            if other["national_id"] == row["replaces"]:
                _union(parent, row["row_id"], other["row_id"])
    groups: dict[str, list[str]] = {}
    for row in rows:
        groups.setdefault(_find(parent, row["row_id"]), []).append(row["row_id"])
    return sorted(sorted(group) for group in groups.values())


def patient_count(rows: list[dict]) -> int:
    """Count people. A row count is not this number."""
    # The shell returns the length of rows. This returns the group count.
    return len(partition(rows))


def removals(waitlist: list[dict]) -> list[str]:
    """Propose a removal. The person stays in the cluster file.

    Only a late death flag and a seen-elsewhere flag are proposals.
    A bounced row, a resubmitted row, and an empty flag stay.
    """
    flags = {"death-late", "seen-elsewhere"}
    return sorted(row["row_id"] for row in waitlist if row["flag"] in flags)


def _find(parent: dict[str, str], item: str) -> str:
    """Find the group id, and compress the path on the way.

    The steps point the current row at its grandparent and move there
    until a row points at itself.
    """
    while parent[item] != item:
        parent[item] = parent[parent[item]]
        item = parent[item]
    return item


def _union(parent: dict[str, str], left: str, right: str) -> None:
    """Put two row ids in the same group."""
    parent[_find(parent, left)] = _find(parent, right)
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `death-late`. You should see `newborn` and `twin` on the skip line. The word phone can still appear in a comment that says phone is not a link. That is expected. You should not see `return len(rows)`. If you see that return, you pasted the picture. Paste this block again.

## Replace the cluster test

This block replaces [work/tests/test_cluster.py](work/tests/test_cluster.py). The full path is `Week 03/Day 01/Student_Copy/work/tests/test_cluster.py`. It does not replace the packet test.

Open the work file. Select the whole file and delete it. Copy the lines inside the block below from this chapter file. Use Paste Without Formatting. Do not copy the backtick lines. Paste. Save.

```text
"""A newborn, twins, and a reused MRN stay split.

Chapter 06 replaces the work copy with this file. Leave the packet
shell test unchanged.

The shell test expects a shared stand-in id to be one group. This
test expects those rows to stay apart, a replaces link to join,
and only two removal flags. The stand-in letters are not history
ids. The line parents[1] stays as it is.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from cluster import partition, patient_count, removals


def _row(row_id: str, national_id: str, phone: str, mrn: str, relation: str = "", replaces: str = "") -> dict:
    """Return one cluster row, including an optional replaces link.

    The ids, the relation, and the replaces value are stored. Merge stays empty. The finished test uses replaces to join two rows and leaves the other pairs apart.
    """
    return {
        "merge_with": "",
        "mrn": mrn,
        "national_id": national_id,
        "phone": phone,
        "relation": relation,
        "replaces": replaces,
        "row_id": row_id,
    }


class ClusterTests(unittest.TestCase):
    """Finished expectations for rows that stay split.

    A shared stand-in id stays apart. A replaces link joins the named rows. Only flagged removals are dropped. This is not the packet shell.
    """
    def test_newborn_twins_and_a_reused_mrn_stay_split(self) -> None:
        """People stay apart unless replaces names the other id."""
        mother = [_row("mother", "N", "1", "A"), _row("newborn", "N", "2", "B", relation="newborn")]
        twins = [_row("twin-a", "T1", "9", "C", relation="twin"), _row("twin-b", "T2", "9", "D", relation="twin")]
        reused = [_row("reuse-a", "R1", "3", "M"), _row("reuse-b", "R2", "4", "M")]
        linked = [_row("visit", "V", "5", "E"), _row("iqama", "I", "6", "F", replaces="V")]
        self.assertEqual(partition(mother), [["mother"], ["newborn"]])
        self.assertEqual(partition(twins), [["twin-a"], ["twin-b"]])
        self.assertEqual(partition(reused), [["reuse-a"], ["reuse-b"]])
        self.assertEqual(partition(linked), [["iqama", "visit"]])
        # Two people, not two rows counted as one and not one row counted as two.
        self.assertEqual(patient_count(mother), 2)
        waiting = [
            {"flag": "death-late", "row_id": "wl-death"},
            {"flag": "seen-elsewhere", "row_id": "wl-seen"},
            {"flag": "", "row_id": "wl-open"},
        ]
        self.assertEqual(removals(waiting), ["wl-death", "wl-seen"])


if __name__ == "__main__":
    unittest.main()
```

Open the work file you just saved. Search inside that file, not inside this chapter. You should see `test_newborn_twins_and_a_reused_mrn_stay_split`. You should see `parents[1]`. Leave that line. The stand-in letters `N`, `T1`, and `M` are not history ids. That is expected. A mother and a newborn are two groups. Twins are two groups. A reused MRN is two groups. The Iqama row joins the visitor row.

This page is done when you have saved all six work files. Search each one, not this chapter. `dates.py` has `return _from_hijri(value).isoformat()`. `test_dates.py` has `test_month_boundary_stays_on_the_civil_day`. `codes.py` has `2024-06-01`. `test_codes.py` has `test_wadi_endo_changes_in_june_2024`. `cluster.py` has `death-late`. `test_cluster.py` has `test_newborn_twins_and_a_reused_mrn_stay_split`. The packet copies still contain `timedelta`, `del as_of, facility`, and `return len(rows)`. That is expected. Do not run a command on this page. Do not run the check until [chapter 10](10-finish.md).

Next: [07 — The sample](07-the-sample.md).
