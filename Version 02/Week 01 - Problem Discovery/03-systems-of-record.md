# Systems of record

**Day 1.** Open `data/handover` now. Start with the notes, not the extracts.

## Read first

`handover/interfaces/` is nineteen short notes. Each one says the trust zone, what the system is the system of record for, the interface, and a known defect. `handover/owners.csv` names the owners. One role has no name. That blank is part of the drop.

Copy both into [templates/systems.csv](templates/systems.csv). For each system record the id (the file name), the zone, the fact it owns, and the defect the note admits. Then write four lines of your own:

- Which system owns the signed grade.
- Which system owns a dispatch.
- Which systems can hold a seen date. There are two, and they disagree.
- Which system owns a model score, and where it is hosted.

A model score is not a signed grade. The note says so. Do not collapse them.

## Fill these findings

| Item | What it holds |
|---|---|
| `systems` | `id` and `zone` for all nineteen |
| `safety_owner` | `named` true only if `owners.csv` has a name |
| `record_owners` | `grade`, `dispatch`, `score`, and `seen` (a list) |
| `vendor_hosting` | `region`, `eu` or `uk` |
| `no_master_key` | `master` false, and the person-keys you can actually find as columns |

The key names the checker expects are `registry_no`, `local_pid`, `mrn`, `lab_pid`, and `booking_id`. Confirm each column exists before you list it. There is no column that joins all five.

**Finish.** The systems table exists, and you can say which system you would trust for a signed result.

Next: [Profile before you trust](04-profile-before-you-trust.md).
