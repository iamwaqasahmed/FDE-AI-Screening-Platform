# 01 — What done is

This page is the map. The day is finished by the sprint, the calendar, the reply, the receipt, the four tests, the usability table, the definition of done, the zone rows, the fixture note, the workflow, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | The suite comes first. Usability sign-off is later. Explained in [chapter 02](02-the-sprint.md) |
| [app/calendar_count.py](work/app/calendar_count.py) | Counts Sunday through Thursday and skips the holiday list. Explained in [chapter 03](03-the-calendar.md) |
| [app/schema.py](work/app/schema.py) | Requires `intent`. The journey reads `booked` on the state. Explained in [chapter 04](04-the-reply.md) |
| [app/receipt.py](work/app/receipt.py) | Follows the case clock. The switch keeps the receipt pending. Explained in [chapter 05](05-the-receipt.md) |
| [tests/test_calendar.py](work/tests/test_calendar.py) | The two case dates. Explained in chapter 03 |
| [tests/test_schema.py](work/tests/test_schema.py) | An empty sentence with intent passes. A sentence with no intent fails |
| [tests/test_receipt.py](work/tests/test_receipt.py) | Reads `minutes` from the clock file. Does not wait |
| [tests/test_journey.py](work/tests/test_journey.py) | Loads the fixture from the pack and asserts the mock state |
| [usability.md](work/usability.md) | `status-short` and `caregiver` finished, with the four clause ids. Explained in [chapter 06](06-the-pages.md) |
| [dod.md](work/dod.md) | `receipt-late` is on the list. The suite goes red when that switch is on |
| [crossings.md](work/crossings.md) | The receipt leaves `zone-private` for `partner`. The calendar stays in `zone-private` |
| [fixtures.md](work/fixtures.md) | The journey reads the recorded fixture and asserts the mock state |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 07](07-knowledge.md) |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | Runs the suite. It was copied and not edited |
| [hijri.md](work/hijri.md) | A later reading. The checks do not read this file |
| [patient-rep.notes.md](work/interviews/patient-rep.notes.md) | What the patient representative says. The checks do not read it |

The checks print `passed` when the calendar matches the cluster week, an empty sentence with `intent` passes, a sentence with no `intent` fails, the journey trusts `booked` on the state, the receipt follows the clock file and stays pending while the switch is on, the receipt files do not wait, the two foundation scripts are finished with the four clause ids, the definition of done names the switch and says the suite goes red, both zone rows are present, the fixture note names the fixture and the state, the sprint puts the suite before usability, the workflow runs the suite, and both knowledge answers are present.

The fixture file is not in this folder. A copy of it here would fail the check. The message does not print the watermark.

Next: [02 — The sprint](02-the-sprint.md).
