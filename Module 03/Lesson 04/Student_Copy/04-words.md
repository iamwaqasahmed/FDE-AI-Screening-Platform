# 04 — Words

Read this page once. You do not need to memorize it, and you do not need to open every link. Scan the tables, then go to [chapter 05](05-the-sprint.md). When a later chapter uses a word you want in the file's own sentence, come back to that row and open the link. You do not paste anything on this page, and you do not run a command. If you are lost on this page, scroll to the line that starts with Next. That line is the end of the reading.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself. You do not go out to `case/` or `data/` to learn a word. The copies are in `packet/release`.

## The protocol and the scores

| Word | Meaning |
| --- | --- |
| Hidden-test protocol | Today's file drop. The labels stay on the grading service. Open [hidden-test.md](packet/release/notices/hidden-test.md) |
| Grading service | Where the labels live. The development slice does not show them |
| Label | The correct answer for a row. [score.jsonl](packet/release/slices/score.jsonl) has outputs and no label field |
| Held-out slice | The rows the eval check scores. They are not the three lines in `score.jsonl` |
| Extraction | The three fields `source_type`, `specialty`, and `sub_specialty`. The score is a field F1 |
| Citation | A document id and a span. Accuracy is how often both match |
| Journey | A state and an approval. A pass needs both |
| Budget | The floor in [metrics.json](packet/release/budget/metrics.json). Extraction, citation, and journey each have one |
| In force | The document the asker may see. Module 3, Lesson 3 left an index that cites one |
| In-flight referral | A referral that already started. It keeps the version it started on |
| Unauthorized circular | Not a citation. The failure log names it in an output, not as a type |
| Ophthalmology | The eye service. The short name on the demand file is the series in [ophth.csv](packet/release/demand/ophth.csv) |
| Case date | `2027-01-27`, on the notices and on the release index |

## The forecast and the campaign

| Word | Meaning |
| --- | --- |
| Eye-screening campaign | Announced on the case date. It starts the next month. Open [campaign.md](packet/release/notices/campaign.md) |
| Later window | Year 2027, months 2 and 3. Read the visits from `ophth.csv`. Do not copy them onto a page |
| Fit window | The same months in the earlier year. Copying those visits forward ignores the campaign |
| District | A column on `ophth.csv`. The rows name the districts. You read them in the file |
| Visits | The count on a demand row. The check does not print one |
| Session plan | A plan that copies last year's months misses the campaign |

## The four failures

| Word | Meaning |
| --- | --- |
| Planted failure | One of the four log rows. The type is not on the row. Open [failures.jsonl](packet/release/slices/failures.jsonl) |
| `log-night` | The reply cites a clause that is not on file. The benchmark names this a hallucination |
| `log-circular` | The reply uses a document that is not in force. The benchmark names this a retrieval failure |
| `log-friday` | The offer uses Friday, and the gender preference is ignored. The benchmark names this a reasoning gap |
| `log-approval` | The booking has no approval. The benchmark names this a workflow issue |
| Hallucination | A citation of a clause that is not on file. The log file does not contain this word |
| Retrieval failure | A citation that is not the in-force document the asker may see |
| Reasoning gap | The offer uses Friday. Module 1's calendar does not count Friday as a working day. The same log line also ignores a gender preference |
| Workflow issue | The booking has no approval. On the benchmark, this failure is a design bug |
| Design bug | A fault in the design, recorded on the benchmark. The workflow failure is one |
| Evidence | What the workshop stays on. A ranking is not evidence by itself |

## The judge and the gate

| Word | Meaning |
| --- | --- |
| Calibration subset | The scored rows a judge may be checked on. Open [calibration.jsonl](packet/release/slices/calibration.jsonl) |
| Fluent | The reply reads as settled. Fluency is not the calibration label |
| `pass` | The calibration label on a row. The judge follows this field |
| Calibrate | Check the judge on the calibration subset, because a fluent wrong citation can be marked correct |
| Evaluation gate | The job in [.github/workflows/ci.yml](packet/.github/workflows/ci.yml). On Windows, `.github` is hidden. Tick Hidden items. The packet copy is commented. Chapter 07 replaces the work copy |
| Regression | The gate runs `tests.test_gate`. A fluent wrong citation is not accepted |
| Watermark | A mark on a sample file. A copied mark fails the check. The message does not print the mark |

## The workshop

| Word | Meaning |
| --- | --- |
| Seat | A person in the room. The ids are `cdo`, `access-mgr`, `phc-lead`, and `dpo`. Open [seats.md](packet/release/workshop/seats.md) |
| `cdo` | Layla Al-Harbi, the chief digital and transformation officer |
| `access-mgr` | Noura Al-Qahtani, the access manager |
| `phc-lead` | Dr. Hassan Al-Dosari, the primary-health-care lead |
| `dpo` | Sara Al-Mutairi, the data protection officer |
| Dot-vote | The ranking method in [dot-vote.json](packet/release/workshop/dot-vote.json) |
| `p-triage` | The first id in that ranking |
| Vendor bot | The second id in that ranking. The file writes it `vendor-bot` |
| Value model | What the notes refuse to treat the ranking as. The phrase is `not the value model` |
| Ramadan | The season the seat note names. The go-live wish sits just before it |
| Patient data | What the data protection seat says needs care |

## The experiment

| Word | Meaning |
| --- | --- |
| ab-status | A wording experiment on status replies. Open [ab-status.md](packet/release/notices/ab-status.md) |
| Arm | One wording. The file names two. You do not write which one won |
| Pre-registered metric | The metric named before a second count is read. It is `honest_pending` |
| `honest_pending` | The only metric the comparison uses. It is on [ab-status.json](packet/release/experiment/ab-status.json) |
| Contained | A second count in that file. It is not the metric |
| Wilson interval | A range around a district's rate. Chapter 08 replaces `intervals.py` |
| `practice` | The shared classroom world. The build and the demo both use it |
| `rel-m03-l04` | The name of today's pack |

## What the check will see

| Word | Meaning |
| --- | --- |
| Eval check | `chk-eval`. It loads `score.py`, `forecast.py`, and `failures.py`, and it reads the four graded pages and the work workflow |
| Judge check | `slice-judge`. It loads `judge.py` and the calibration subset. It does not read the four pages or the workflow |
| Graded pages | `sprint.md`, `benchmark.md`, `workshop.md`, and `knowledge.md` |
| `experiment.md` | The pre-registered metric. A miss on this page does not fail a check. You still paste it |
| `gate.py` | The regression the suite runs. The checks do not load it. You do not delete it |
| `intervals.py` and `experiment.py` | The advanced path. The two checks do not require them. The suite does. You do not delete them |

This page is done when you have scanned the tables. You do not need to open every link before chapter 05. Come back when a later chapter uses a word you want in the file.

## A plain reading

The score called F1 is still the share of fields that match, the same share as Module 3, Lesson 2. It is not the harmonic mean of precision and recall. The development slice shows outputs and no labels. The grader holds the labels. You do not invent a label field in that file.

A Wilson interval is a range around a count of correct rows out of a district's rows. The range stays between 0 and 1. An empty district is not a rate of zero. There is no evidence, so the range is the whole interval from 0 to 1. You do not derive the formula. The file already contains it. `1.96` in that file is the usual width for this kind of range.

The experiment file has two counts. `contained` is higher for one arm. `honest_pending` is the metric named before you look. The page you write does not say which arm won.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
