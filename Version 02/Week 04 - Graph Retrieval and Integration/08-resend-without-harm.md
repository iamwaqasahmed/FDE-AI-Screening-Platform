# Re-send without harm

**Day 3. Software engineer and product manager.** The lost requests are the ones to look at. Not every lost request should be printed again.

## Who is held

Write `resend.csv` after the contract exists. One row per lost request: `request_id`, `local_pid`, `action`, `reason`. The header is in [templates/resend.example.csv](templates/resend.example.csv).

`action` is `resend` or `hold`. A hold reason is `seen`, `deceased`, or `moved`. Apply them in that order, which is Week 2's order: a clinic letter that shows the visit, then a version 3 flag of `DECEASED`, then `MOVED`. Someone already seen is held even if a flag is also set. A lost invitation to a person flagged deceased is held too. A lost request with none of those is a re-send.

Leave `reason` blank on a re-send. Do not add a name column, and do not add a date of birth. The file is keyed by the original request id, so a second run writes the same file. Do not allocate a new id.

The request names a template, `referral-chase`, that the handover's template folder does not hold. Which template to print is the programme manager's decision. Do not invent the wording.

## The freeze

A print run is not a release. A new template is. `handover/delivery/freeze_calendar.csv` has the bureau freeze, FRZ-0302, and the letters release windows. The next window is the first letters window on or after today. The last window before the freeze, and the first after it, are the ones a template change would have to use. A re-send of an existing letter does not wait for them.

## Fill these findings

| Item | What it holds |
|---|---|
| `resend_summary` | `resend`, `hold_seen`, `hold_deceased`, `hold_moved`, and `key` |
| `resend_window` | `freeze`, `start`, `end`, `next_window`, `last_before`, `first_after`, and `resend_needs_release` |

`key` is `request_id`. `resend_needs_release` is false. Dates are `YYYY-MM-DD`.

**A miss that looks like progress.** Re-sending every lost request, including people already seen and people flagged deceased. The file is easy to generate. It is the wrong file.

**Finish.** `resend.csv` matches the contract. A lost request to a deceased person is a hold. A lost chase inside the bound is a re-send.

Next: [The baselines](09-the-baselines.md).
