# 03 — The replay

[Chapter 02](02-the-role.md) named the five parts. This chapter opens ten files, in order, and then you run one demo and two interviews. You do not paste a file on this page. There is no heading on this page that starts with Replace.

The blocks under Read these files are pictures. They replace nothing. Do not paste them. A picture belongs to the numbered item above it. The next item starts with the next number. Some items have no picture. Those items say so. Do not look for a block under them.

A jsonl row is one long line. Word wrap can make that line look like several lines. It is still one row. A json file is still one file when it wraps.

Open each link with Ctrl+click on Windows or Command+click on macOS, so the file opens in the editor. Do not double-click the file in File Explorer. A double-click can open Excel or a browser, and the search below will not match what you see. To search, Ctrl+F on Windows or Command+F on macOS, inside the file named in that item. A search inside this chapter does not count. Do not type in a packet file. Close it when the item is done.

Stay on the list until item 10. Then run the demo, then the two interviews. Finish one item before you open the next number. If you are lost, you are on the item you have open. Finish that item.

## Read these files

1. Open [README.md](packet/release/README.md). Search for `circ-ramadan-hours`. The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
# rel-m04-l02

From: the office of the Chief Information Security Officer
Case date: 2027-02-01

The incident replay is open. The Ramadan-hours circular is circ-ramadan-hours. Shadow traffic is shadow-extract. The lesson notes are [Module 4, Lesson 2](home.md).

Files:

- [actions/overrides.jsonl](actions/overrides.jsonl)
- [dms/circ-ramadan-hours.md](dms/circ-ramadan-hours.md)
- [drifts/signals.jsonl](drifts/signals.jsonl)
- [events/document-changed.json](events/document-changed.json)
- [experiment/shadow-extract.json](experiment/shadow-extract.json)
- [meter/gateway.jsonl](meter/gateway.jsonl)
- [replay/note.md](replay/note.md)
- [replay/spans.jsonl](replay/spans.jsonl)
- [templates/runbook.md](templates/runbook.md)
```

The day-notes link in that file does not open. It points inside this student copy. You do not need it. This chapter is the lesson.

This file is done when the search finds `circ-ramadan-hours` and you have read the case date. Close the file. The next item is number 2.

2. Open [note.md](packet/release/replay/note.md). Search for `flat`. The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
# Incident replay

The alert is already in the spans. Do not add a new bug. The alert SLO is 5 minutes from the first tool error. CPU stays flat.

Case date: 2027-02-01.
```

This file is done when the search finds `flat` and you have read the SLO. Close the file. The next item is number 3.

3. Open [spans.jsonl](packet/release/replay/spans.jsonl). Search for `referral.status`. There is no picture of this file. There is no block under this item. A picture would copy a hash or the error detail. Do not copy a hash. Do not copy the error detail. A row is one long line even when the editor wraps it. Find the first `referral.status` row whose status is `error`, then the row whose name is `alert`. The `at` value on that first error is `2027-02-01T09:12:00+03:00`. The `at` value on the alert is `2027-02-01T09:15:00+03:00`. Do not type those times into a file on this page. [Chapter 08](08-the-pages.md) pastes them. Close the file. The next item is number 4.

4. Open [circ-ramadan-hours.md](packet/release/dms/circ-ramadan-hours.md). Search for `in_force`. The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
# circ-ramadan-hours

- doc_id: circ-ramadan-hours
- family: hours
- status: in_force
- supersedes: circ-ramadan
- audience: public

Evening clinics close at 01:00. Daytime slots are not offered.
```

This file is done when the search finds `in_force` and you have seen that evening clinics close at 01:00. Close the file. The next item is number 5.

5. Open [document-changed.json](packet/release/events/document-changed.json). Search for `document.changed`. The next block is a picture of that file. Do not paste it. This block replaces nothing. The file is still one file when it wraps.

```text
{
  "body": "Evening clinics close at 01:00. Daytime slots are not offered.",
  "doc_id": "circ-ramadan-hours",
  "status": "in_force",
  "supersedes": "circ-ramadan",
  "topic": "document.changed"
}
```

This file is done when the search finds `document.changed` and the document id is `circ-ramadan-hours`. Close the file. The next item is number 6.

6. Open [signals.jsonl](packet/release/drifts/signals.jsonl). Search for `drift-criteria`. The next block is a picture of that file. Do not paste it. This block replaces nothing. Each row is one line.

```text
{"current": "circ-ramadan-hours", "id": "drift-hours", "kind": "hours", "seen": "circ-ramadan"}
{"current": "crit-endo-v4", "id": "drift-criteria", "kind": "criteria", "seen": "crit-endo-v3"}
{"current": "ophth-screen", "id": "drift-clinic", "kind": "clinic", "seen": "ophth-clinic"}
```

This file is done when you have seen three kinds: `hours`, `criteria`, and `clinic`. Close the file. The next item is number 7.

7. Open [overrides.jsonl](packet/release/actions/overrides.jsonl). Search for `stamped`. There is no picture of this file. There is no block under this item. A picture would be the rows the share is computed from. Do not write the share on a page. Each row is one line. This item is done when you have seen both `true` and `false`. Close the file. The next item is number 8.

8. Open [gateway.jsonl](packet/release/meter/gateway.jsonl). Search for `hospital`. There is no picture of this file. There is no block under this item. A picture would copy a cost. Do not copy a cost. Each row is one line. This item is done when you have seen `h-wadi`, `h-nakhl`, and `h-safra`. Close the file. The next item is number 9.

9. Open [shadow-extract.json](packet/release/experiment/shadow-extract.json). Search for `shadow-extract`. There is no picture of this file. There is no block under this item. A picture would copy a hash. Do not copy a hash. The file has no `compared` field. This item is done when you have seen the id `shadow-extract`. Close the file. The next item is number 10.

10. Open [runbook.md](packet/release/templates/runbook.md). Search for `Detect`. The next block is a picture of that file. Do not paste it. This block replaces nothing. The headings are empty. [Chapter 08](08-the-pages.md) fills the work copy.

```text
# tpl-runbook

## Detect

## Scope

## Impact

## Timeline

## Owner

## Cache

## Shadow
```

This file is done when you have seen the seven headings: Detect, Scope, Impact, Timeline, Owner, Cache, and Shadow. Close the file. The ten files are done. The next heading is Run the demo. You still do not paste a file.

## Run the demo

The demo uses the window that is still inside `problem_simulation`. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. If you closed that window, open a terminal in the course folder and run both lines.

```text
cd problem_simulation
python -m alwaha.demo.trace --profile practice
```

You should see three lines. The first line is `referral.status`. The other two are a hash and a token count. The error detail is not on the screen. Do not copy the hash into a file.

The prompt returns after the third line. That is the command finishing. There is no error.

## Interview the CISO

Stay in that same window, still inside `problem_simulation`. If you opened a new terminal in the course folder, run the `cd` line first. If you are already inside `problem_simulation`, skip the `cd` line.

```text
cd problem_simulation
python -m alwaha.interview --persona ciso --script "../Module 04/Lesson 02/Student_Copy/work/interviews/ciso.questions.txt"
```

You should see `Q1:` and `Q2:`, each followed by `A:`. The command prints no score. The first answer says the incident replay already contains the alert, and not to add a new bug. The second answer says a CPU dashboard misses the tool failures. You paste the notes in [chapter 08](08-the-pages.md). Do not type into [ciso.notes.md](work/interviews/ciso.notes.md) on this page. The question file is not the graded note.

## Interview the patient representative

The same window. Skip the `cd` line if you are already inside `problem_simulation`.

```text
cd problem_simulation
python -m alwaha.interview --persona patient-rep --script "../Module 04/Lesson 02/Student_Copy/work/interviews/patient-rep.questions.txt"
```

You should see `Q1:` and `Q2:`, each followed by `A:`. The command prints no score. The first answer says the phone line is the door most families still use. The second answer says she is still offered the old evening close after the circular. You paste the notes in [chapter 08](08-the-pages.md). Do not type into [patient-rep.notes.md](work/interviews/patient-rep.notes.md) on this page. The question file is not the graded note.

This page is done when you have finished all ten items, the demo has printed three lines, and both interviews have printed `Q1:` and `Q2:`. You have not pasted a file.

Next: [04 — Words](04-words.md).
