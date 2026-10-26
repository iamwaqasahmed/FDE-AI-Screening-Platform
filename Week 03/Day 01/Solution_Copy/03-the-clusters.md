# 03 — The clusters

Open the finished [dates.py](work/app/dates.py), [codes.py](work/app/codes.py), and [cluster.py](work/app/cluster.py) and put them beside yours.

## Dates

[identifiers.jsonl](sources/release/history/identifiers.jsonl) has two Hijri rows. Search for `hijri-end`. The `dob` is `1448-07-29` and `era` is empty. Search for `hijri-start`. The `dob` is `1448-08-01`. The converted civil day is not written in that file, and it is not written here.

`gregorian` returns a Gregorian string unchanged, and it returns a year under 1400 unchanged. A Hijri date uses the tabular calendar. The day is not shifted. The shell adds one day when the Hijri day is 1 or at least 29. While that shell is the file that runs, the check says `a Hijri month boundary is off by a day`. The message does not name the converted day.

The filled test checks a 14-day gap from `1448-07-15` to `1448-07-29`, then a 2-day gap to `1448-08-01`. `_hijri_jd` is still in the file. That is expected. `timedelta` is not.

## Clinic codes

[clinics.md](sources/release/catalog/clinics.md) says the catalog code is `END-01`. In June 2024, h-wadi changed that clinic to `ENDO-CLN`. Rows before June 2024 keep `END-01`.

`clinic` rewrites `END-01` or `ENDO-CLN` to `ENDO-CLN` only when the facility is `h-wadi` and the row date is on or after `2024-06-01`. Any other row keeps its code. `END-01` remains in the set. That is expected. The shell ignores the date and the facility and rewrites `ENDO-CLN` back to `END-01`. While that shell is the file that runs, the check says `the stale clinic code was kept`. The message does not name the code.

## One person

The history rows you opened in the morning are the inputs. A mother and a newborn can share a national id. Twins can share a phone. An MRN can be reused. `partition` links a shared national id, skips `relation` of `newborn` or `twin`, and links `replaces`. Phone, MRN, and `merge_with` are not links. A failed check digit is not read, so that person stays. `patient_count` counts groups. `removals` proposes only `death-late` and `seen-elsewhere`. The person stays in the cluster file.

The shell merges on a shared national id, a shared phone, or a shared MRN, follows `merge_with`, counts rows, and returns every waitlist row. While that shell is the file that runs, the check says a mother and a newborn were merged, twins were merged, a reused MRN was linked, and a row count was used as a patient count. The message does not name a national id.

`the clusters do not match` is the line the check uses when the groups, the removals, or the count disagree and none of those four lines were added. The message does not name the groups.

## The path through the files

The morning chapter [06-the-clusters.md](../Student_Copy/06-the-clusters.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [04 — The sample](04-the-sample.md).
