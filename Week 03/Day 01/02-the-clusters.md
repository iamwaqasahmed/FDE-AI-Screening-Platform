# The clusters

Copy [app](app) to `Week 03/Day 01/work/app`. Copy [tests](tests) to `Week 03/Day 01/work/tests`. Leave the copies in this folder unchanged, and edit the copies.

The shell merges on a shared national id, a shared phone, or a shared MRN. It counts rows. A newborn, a twin, and a reused MRN are marked on the row. A reversed merge stays reversed. A visitor number can be replaced by an Iqama. A failed check digit is still a person.

The shell converts a Hijri date one day late at the month boundary. The history rows use the same boundary as the Week 2 Hijri list.

The shell keeps END-01. After June 2024, endocrinology at h-wadi is ENDO-CLN.

A late death flag and a seen-elsewhere row are removal proposals. The person stays in the cluster file.

The product manager copies [templates/patients.md](templates/patients.md) to `work/patients.md` and defines one patient.

From `work`:

```text
python -m unittest discover -s tests -q
```
