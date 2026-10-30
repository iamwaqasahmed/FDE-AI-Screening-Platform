# 04 — Words

[Chapter 03](03-the-replay.md) opened the files. This chapter names the words before a later chapter asks you to use them. You do not paste a file on this page. There is no heading that starts with Replace. You do not memorize the tables. You come back to a row when a later chapter uses the word.

Do not copy a hash, a rate, a cost, or the error detail onto a page.

## The replay and the sprint

| Word | Meaning |
| --- | --- |
| Replay | The morning's incident, already on disk. [README.md](packet/release/README.md) says it is open |
| Alert | Already in the spans. [note.md](packet/release/replay/note.md) says not to add a new bug |
| SLO | 5 minutes from the first tool error. The note states that window |
| CPU | Stays flat through the replay. A board that only has CPU is not done |
| `referral.status` | The tool on the model span and the tool spans in [spans.jsonl](packet/release/replay/spans.jsonl) |
| Span | One row in that file. A row is one long line |
| `at` | The time on a span. The timeline uses the first `referral.status` error and the alert |
| Hash | A span can carry one. The demo prints one. Do not copy it onto a page |
| Token count | A span can carry one. The demo prints one. You do not copy the number onto a page |
| Error detail | A span can carry one. The demo does not print it. Do not type it |
| Sprint order | Replay, then dashboard, then timeline, then cache, then shadow. [Chapter 05](05-the-sprint.md) writes that order |

## The board

| Word | Meaning |
| --- | --- |
| Latency | How long the spans took. The board records it. The alert span stays out of that figure |
| Errors | Spans whose status is `error`, apart from the alert span |
| Tool failures | Those error spans that also name a tool |
| Alert time | The `at` value on the span named `alert`. The board keeps it |
| Hospital | A key on a gateway row. [gateway.jsonl](packet/release/meter/gateway.jsonl) names `h-wadi`, `h-nakhl`, and `h-safra` |
| Cost | A gateway row carries one. Do not copy a cost onto a page. The meter sums every hospital |

## The hours

| Word | Meaning |
| --- | --- |
| `circ-ramadan-hours` | The in-force hours circular. [circ-ramadan-hours.md](packet/release/dms/circ-ramadan-hours.md) says evening clinics close at 01:00 |
| `circ-ramadan` | The circular this one supersedes |
| `document.changed` | The topic on [document-changed.json](packet/release/events/document-changed.json). This event drops a cached answer when the document is the Ramadan circular |
| Cache | The stored clinic hours. Another document leaves that cache in place |
| Drift | A row in [signals.jsonl](packet/release/drifts/signals.jsonl). The three kinds are hours, criteria, and clinic |
| Ramadan hours | The name for kind `hours` |
| Criteria v4 | The name for kind `criteria`. The current id on that row is `crit-endo-v4` |
| Campaign clinic | The name for kind `clinic`. The current id on that row is `ophth-screen` |
| Stamped | A field on [overrides.jsonl](packet/release/actions/overrides.jsonl). The override rate is the share of stamped rows. Do not write the share on a page |
| `shadow-extract` | The id in [shadow-extract.json](packet/release/experiment/shadow-extract.json). The file has no `compared` field |
| Comparison | Both compared and matched. Promotion waits until both are true. The patient reply stays the registered reply |

## The pages and the notes

| Word | Meaning |
| --- | --- |
| Timeline | The first `referral.status` error and the alert. [Chapter 08](08-the-pages.md) writes it |
| Dashboard page | Latency, errors, and tool failures. CPU stays flat. That page is not the same file as `dashboard.py` |
| Runbook | [runbook.md](packet/release/templates/runbook.md). The headings are Detect, Scope, Impact, Timeline, Owner, Cache, and Shadow |
| Lead | Owns the timeline |
| CISO | The security interview. The notes name the replay, the alert, CPU, and the dashboard |
| Patient representative | The phone-line interview. The notes name the evening close and the circular |
| Question file | The file the interview command reads. The check does not read it |

## What the check will see

| Word | Meaning |
| --- | --- |
| Incident check | `chk-m04-l02-incident`. It loads `spans.py`, `dashboard.py`, `meter.py`, `drift.py`, `override.py`, and `shadow.py`. It also reads the sprint, the dashboard page, the timeline, the runbook, the knowledge file, and both notes files |
| Cache check | `slice-cache`. It loads `cache.py`. Do not rename it |
| Watermark | A mark in a file under `work/`. The message does not print the mark |

This page is done when you have scanned the tables.

## A plain reading

A trace is the spans. A metric is a count you put on the board: latency, errors, tool failures. Those counts are the indicators, often called SLIs. The five-minute window on the note is the objective, the SLO. CPU can stay flat while those move. A board that only has CPU misses the incident.

`referral.status` is the Module 1 status tool. Module 2, Lesson 1 recorded that same read on the trace as `status`. Today's spans use the Module 1 name again. It is not a new tool.

Drift, here, means what you serve no longer matches the world. The three kinds in the file are hours, criteria, and clinic. The criteria row is `crit-endo-v4` seen as `crit-endo-v3`. Module 1, Lesson 3 held intake on v3 while v4 was a draft. Module 3, Lesson 3 put v4 in force for three specialties. An in-flight referral kept the version it started on. The clinic row's current id is `ophth-screen`. The eye-screening campaign Module 3, Lesson 4 announced is ophthalmology demand. This row does not rename that campaign. Read the ids on the drift file.

The hours page on Module 3, Lesson 3, `circ-ramadan`, was in force and closed evening clinics at 21:00. That page is in the Module 2 folder. Today's `circ-ramadan-hours` supersedes it and closes them at 01:00. A cached answer drops when `document.changed` names `circ-ramadan-hours`. A different document does not clear that cache. Yesterday's supply module, in the Module 4, Lesson 1 folder, used the string `circ-ramadan` as a fallback citation id. Do not go back and edit it.

Shadow traffic compares a candidate with the registered reply. It must not change what the patient is sent. Promotion waits until the comparison was both compared and matched. The shadow file has no `compared` field, so the shell that promotes anyway is the miss.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
