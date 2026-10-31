# Decisions that differ from IDEA

`IDEA/` is unchanged. This simulation implements its problem and changes the setting.

| IDEA | This build | Why |
| --- | --- | --- |
| Al-Waha, a fictional Saudi cluster | Northline, with sites in Washington and British Columbia | The course brief for this implementation requires a United States and Canada setting |
| Ain nightly file | Cedar Ridge nightly file | Same constraint: no slot API |
| Sunday–Thursday office week | Monday–Friday office week. Clinical sites still run on weekends | That is the office calendar in both countries. A Saturday clinic stamp is not an office day |
| Hijri dates in the opening gold | Gregorian instants with `America/Vancouver` and `America/Los_Angeles` | The opening case is January 2027, which is Pacific standard time, so daylight-saving is not in the first fixture |
| SAR prices | CAD for the BC member, USD noted on the WA site | The two currencies are on the extracts |
| Package must not be a cloud SDK | Standard library only | Matches IDEA |

The three logs, the refusal of a shared KPI, the sealed promises, and the rule that student extracts do not name `dec-accept` are implemented as specified.

Checkers for INV-02 through INV-08 call a function the student submits. They do not contain `repair`. Holdout inputs are in `src/access/sealed_holdouts.py` and were confirmed absent from `student_pack/` after `init`. The template scanner does not call AWS.

What is not built, because it is the student's work: `repair.bind`, the capability check inside the student's service, the student's outbox, the citation function, the AWS template, and the handoff page.

What is staged as evidence and not solved: the letter that contains both clinical words and `APR-4417`, the hours document that changed from 21:00 to 17:00, a second hours row whose stored hash does not match its body, the cache that dropped the coverage window, a payer timeout with no window, two offers of one slot version, a redelivered handset key, a poison trailer, a Saturday file, a reused medical-record number, and the channel utterance that was not delivered.
