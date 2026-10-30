# 04 — The note

[intake.md](work/intake.md) is the one-page note. [scenario-log.json](work/scenario-log.json) is the log the worker writes. The check runs the worker again and does not read a log you typed by hand.

## The intake note

The steps are the diagram: `referral.submitted`, extract, the criteria in force, the duplicate check, a suggested clinic, and a coordinator holding the approval.

The acceptance line is the product decision. The workflow stops when a coordinator holds the approval. It does not book.

The in-flight line is the rule for a referral that has already started. It keeps the criteria version it started with. A later draft does not replace that version.

The check looks for a coordinator, or the word human, and for the words in-flight, criteria, and version.

## The log

`booked` is false on every row. Live rows use `crit-endo-v3` and the state `approval.held`. The clinic is `ENDO-CLN` wherever the facility is `h-wadi`.

| scenario | due | facility | duplicate | hold | dead_letter | What the row shows |
| --- | --- | --- | --- | --- | --- | --- |
| order | 2027-01-13 | h-wadi | false | open | false | Higher sequence kept. One approval, `apr-ref-150` |
| happy | 2027-01-13 | h-wadi | false | open | false | The ordinary path. One approval, `apr-ref-100` |
| friday | 2027-01-17 | h-wadi | false | open | false | Thursday counted, Friday and Saturday skipped |
| holiday | 2027-03-14 | h-wadi | false | open | false | The three March holidays skipped |
| ain | 2027-01-14 | h-ain | false | none | false | No hold, no clinic, not booked. One approval, `apr-ref-140` |
| replay | 2027-01-13 | h-wadi | false | open | false | The same event id twice, and still one approval, `apr-ref-110` |
| duplicate | 2027-01-13 | h-wadi | true | open | false | Flagged, still held, not booked. One approval, `apr-ref-160` |
| compensation | 2027-01-13 | h-wadi | false | released | false | The hold was released. The state is still `approval.held` |
| dead-letter |  |  | false | none | true | Not applied. No approval. The state is `dead-letter` |

The file order is the order the referrals were first seen. The check groups by scenario name, so that order is enough.

Next: [05 — Knowledge](05-knowledge.md).
