# Index with status and dates

**Days 1 and 2. Data engineer.** A chunk without its header is the wrong unit. The header is the signed record: document id, title, status, effective date, sunset, site, version, and the edges `supersedes`, `cites`, `applies_to`, and `constrains`. `corpus/register.csv` is maintained by hand. Where it disagrees with the header, the header wins. Week 2 already found documents the register calls draft while the header says `in_force`.

## What binds

Use the same reading as Week 2. The index has to apply it, not only store it.

- A draft never binds. `sop-urgent-draft` proposes a clock. Site documents cite it. A citation is not adoption.
- A withdrawn memo binds between its effective date and its sunset, and not after.
- A site document beats the national document when both are in force. Leave `site` blank on a document that applies everywhere.
- A superseded document binds only before its sunset. The current PDF on the top of the pile is not the rule for 2019.

Every chunk you retrieve should carry the header it came from. A binding question asks which document is in force at a site on a date, and how many days the text allows. The answer uses `clause_id` for the document id. There is no second code in the corpus. `limit` is the number of days, and it is blank when the text sets no clock.

`pathway_rules.csv` from Week 2 is the regression. If the index and that file disagree, fix the index.

The questions do not name the document you should cite. If your answer's document id appears in the question, you have leaked the key into the prompt.

## Fill these findings

| Item | What it holds |
|---|---|
| `policy_graph` | `drafts` that never bind, `withdrawn` documents with `effective` and `sunset`, `overlays` that beat the national text (`document_id`, `sites`, `from`), and `stale_register` whose register status is draft while the header says `in_force` |

**A miss that looks like progress.** Trusting `corpus/register.csv` because it has a status column and a path. The header is the signed record.

**Finish.** The index can reject a draft, a document outside its dates, and a national rule where a site rule is in force. `policy_graph` is filled from the headers.

Next: [Originals, scans, and duplicates](05-originals-scans-and-duplicates.md).
