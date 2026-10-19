# Pathway by site and date

**Days 3 and 4. Be the data scientist.** A limit is not "the national procedure". It is the clause that was in force for that site on that date. `corpus/register.csv` is maintained by hand. Several documents it calls draft are in force in the signed header. Read the header.

## What binds

- A draft never binds. `sop-urgent-draft` proposes a clock. It is not the rule.
- A withdrawn memo binds between its effective date and its sunset, and not after. The Oakridge memo is that shape.
- A site document beats the national document when both are in force. Hill Counties repeats an ungradable photograph on a shorter interval than the national rule. The warehouse never picked that up.
- North City Eye Clinic and Harbour Eye Clinic each start a specialist clock on a date of their own. Before that date the national text sets no specialist clock.

Build `pathway_rules.csv` with one row per rule: `site`, `topic`, `grade`, `clause_id`, `document_id`, `days`, `effective`, `sunset`. Use the document id as the clause id. The corpus does not publish a second code. Leave `site` blank when the document applies everywhere. Leave `days` blank when the text sets no clock. Topics to cover:

`eligibility`, `coverage_window`, `grade_turnaround`, `letter_turnaround`, `specialist_review`, and `recall` with a grade of `R0`, `R1`, or `U`.

Read the sentences. "Two years" is 730 days. "Ten weekdays" is 10. "A fortnight" is 14. "Three months" is 90. "Two months" is 60. "One year" is 365. Version 3 does not restate the coverage window. Inherit it from version 2, and cite version 3, because version 3 is the document in force.

The header in [templates/pathway_rules.csv](templates/pathway_rules.csv) is the shape. The checker tries your table against many site, topic, grade, and date combinations. It does not show you which ones. Ninety-five percent have to resolve to the right document and the right number of days.

## Fill these findings

| Item | What it holds |
|---|---|
| `site_rules` | Hill's recall days and document and start date, the national ungradable days, each adopting site's specialist days and start date, and the Oakridge memo's id, start, and sunset |
| `stale_register` | `documents` whose register status is `draft` while the header says `in_force`, and `register_says` as `draft` |

**A miss that looks like progress.** One national limit, applied to every site and every year, because the current PDF is the one on the top of the pile.

**Finish.** The pathway file cites document ids and dates from the headers, and both findings are filled.

Next: [Cohorts](09-cohorts.md).
