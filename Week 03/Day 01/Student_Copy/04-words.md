# 04 — Words

Read this page once. You do not need to memorize it, and you do not need to open every link. Scan the tables, then go to [chapter 05](05-the-sprint.md). When a later chapter uses a word you want in the file's own sentence, come back to that row and open the link. You do not paste anything on this page, and you do not run a command.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself. This page does not type a national id, a converted day, or a watermark. Those values stay in the files [chapter 03](03-the-request.md) already opened, or in the built pack.

## The people and the rows

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Patient | One person. Not one row, not one MRN, and not one national id. [Chapter 09](09-the-pages.md) writes that sentence |
| Row | One line in [identifiers.jsonl](packet/release/history/identifiers.jsonl). Several rows can belong to one person, and one row is not always one person |
| MRN | Medical record number. The `mrn` field on a history row. A reused MRN can be two people |
| National id | The `national_id` field on a history row. A mother and a newborn can share one. You read the shared value from the demo. You do not type it |
| Mother | The history row whose `row_id` is `mother` |
| Newborn | The history row whose `relation` is `newborn`. That row stays its own person |
| Twin | A row whose `relation` is `twin`. Twins can share a phone and stay two people |
| Reuse | The same MRN on two people. `reuse-a` and `reuse-b` in the history file |
| Hijri | A date whose `era` is empty and whose year is 1400 or later. `1448-07-29` and `1448-08-01` are the two in the history file |
| Gregorian | A date whose `era` is `gregorian`, or a civil day after conversion. You do not type a converted day |
| Check digit | The `check_digit` field. `fail` is still a person |
| Iqama | A residency number that can replace a visitor number. The history field is `replaces` |
| Visitor | The earlier number. The Iqama row points at it |
| Waitlist | [waitlist.jsonl](packet/release/history/waitlist.jsonl). A flag can propose a removal. The person stays in the cluster file |
| `death-late` | A late death flag. It is a removal proposal |
| `seen-elsewhere` | The person was seen at another site. It is a removal proposal |
| Data Protection Officer | [Sara Al-Mutairi](packet/kickoff/personas/dpo.md). Her id is `dpo`. The checks do not ask you to interview her |
| Coordinator lead | [Maha Al-Shammari](packet/kickoff/personas/coord-lead.md). Her id is `coord-lead`. The checks do not ask you to interview her |
| `ext-large` | The external model. [data-request.md](packet/release/notices/data-request.md) says patient data stays off it |
| Case date | `2027-01-24`, on the data request |

## The codes and the labels

| Word | Meaning |
| --- | --- |
| Clinic code | The `clinic_code` field. Read the rule in [clinics.md](packet/release/catalog/clinics.md) |
| `END-01` | The catalog code for endocrinology. Rows before June 2024 keep it |
| `ENDO-CLN` | The code h-wadi uses from June 2024 |
| `h-wadi` | Wadi Specialist Hospital. The clinic change applies there |
| ann-v1 | The clerk guideline. [ann-v1.md](packet/release/guidelines/ann-v1.md) records a phone photo as a scan, and it may leave the sub-specialty blank |
| ann-v2 | Today's guideline. [ann-v2.md](packet/release/guidelines/ann-v2.md) reads phone, photo, scan, retina, and pediatric from the text |
| Scan | A source type. Under ann-v2 it is a scan only when the text says scan and does not say phone or photo |
| Photo | A source type. Phone or photo in the text |
| Sub-specialty | Retina, pediatric, or blank. Blank is allowed when the text names neither |
| Retina | The rare sub-specialty. The fidelity card names it |
| Pediatric | A sub-specialty the text can name |
| Adjudication | A person labels a row. [annotate.yaml](packet/release/openapi/annotate.yaml) calls the operation `adjudicate`. The sprint books time for it |
| Adjudicated | The development labels in [adjudicated.jsonl](packet/release/letters/adjudicated.jsonl). They already follow ann-v2 |
| Clerk file | `letters/clerk.jsonl` in the built pack. It is not in this drawer. It carries a watermark. Do not copy it |

## The sample and the pages

| Word | Meaning |
| --- | --- |
| Fidelity card | [fidelity.json](packet/release/cards/fidelity.json). It compares a synthetic sample with the real specialty mix, the phrase frequencies, and the label margins |
| Specialty mix | The share of `endo` and `ophth` on the card |
| Phrase | The word Kindly, and how often it appears |
| Label margin | The share of the rare sub-specialty on the card |
| Synthetic sample | Invented rows. They are not copied from a real letter |
| Watermark | The mark on the clerk file. The check message does not print it. A copy of that file in `work/` fails the check |
| Phi | A class on [classes.md](packet/templates/classes.md). National id, date of birth, name, and phone are phi |
| Classification | The note that says the synthetic file was scanned before it was shared |
| Sprint | The order of the work. Cluster, then relabel, then sample, then scan, and adjudication |
| Shell | The starter copy in `packet/app`. It shifts a Hijri boundary, keeps the stale clinic code, merges a mother with a newborn, copies ann-v1, copies a real letter, and accepts every file |
| `practice` | The shared classroom world. The build in chapter 01 uses it |
| `rel-w3d1` | Today's file drop |
| Suite | The tests under `work/tests`, together with the app files they call. [Chapter 08](08-the-advanced.md) runs it. It is not a check |
| CI | [ci.yml](work/.github/workflows/ci.yml). It already runs the suite. You do not replace it. The packet copy is the same file |
| Label budget | [labels.json](packet/release/budget/labels.json). `price` is the cost of one label. `sar` is the budget. `budget.py` spends it. The three checks do not call that file |
| Invite time | The date `pit.py` uses as a cutoff. A later row is not a feature of the invite. The three checks do not call that file |

## What the check will see

| Piece | What a pass means |
| --- | --- |
| `dates.py` | A Hijri month boundary stays on the civil day |
| `codes.py` | h-wadi endocrinology follows the June 2024 change |
| `cluster.py` | A mother and a newborn stay apart, twins stay apart, a reused MRN stays two people, and the count is people |
| `patients.md` | One patient is defined with the words the check looks for |
| `sprint.md` | Cluster, then relabel, then sample, then scan, and adjudication |
| `labels.py` | A phone photo is a photo, a named sub-specialty is filled, and the guideline is ann-v2 |
| `synthetic.py` | The sample sits inside the fidelity card and carries no history id and no watermark |
| `scan.py` | A marked file and a history id are refused. A clean line is accepted |
| `classes.md` | National id, date of birth, name, and phone are phi, and the note says the file was scanned |
| `knowledge.md` | Two numbered answers |
| `pit.py` | Present for the suite. The three checks do not require it. Do not delete it |
| `budget.py` | Present for the suite. The three checks do not require it. Do not delete it |
| Demo | The four lines from chapter 03. They do not print a converted day |

The history ids, the two MRNs, and the shared national id stay in the history file and on the demo. This page does not store them.

This page is done when you have scanned the tables. You have not pasted a file. You have not run a command.

Next: [05 — The sprint](05-the-sprint.md).
