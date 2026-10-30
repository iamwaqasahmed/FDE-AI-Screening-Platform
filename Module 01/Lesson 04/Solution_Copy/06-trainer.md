# 06 — Trainer session

Students can skip this page. The answers are in chapters 01 through 05.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not open a scenario file on a screen. Do not paste the watermark into a slide or a prompt.

The interview notes in `work/interviews` are for you. The checks do not read them. Students were not asked to run an interview.

From the course folder, the checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check agent --work "../Module 01/Lesson 04/Solution_Copy/work" --profile practice
python -m alwaha.check trajectory --work "../Module 01/Lesson 04/Solution_Copy/work" --profile practice
```

## Block 1 — The count

Open [chapter 05](05-knowledge.md) only after the count is on the table. The demo prints `model count 12` and `tool count 4`.

The starter writes 12 and throws away the status tool. `status`, `injection`, `resume`, and `memory` must show 4. The check says `count does not match the tool` and does not print the number.

## Block 2 — The letter

Open the `injection` row in [chapter 04](04-the-note.md).

The letter says to ignore the policy and book. The turn asks for status. The row calls `referral.status` and does not book. The check says `injection booked a slot` when the starter treats the letter as a tool call. It does not print the slot.

The watermark sits on that letter. A copy of the scenario file in `work/` fails both checks. The message does not print the watermark.

## Block 3 — The return, and the replay

`return` is not sent. `apr-return` is pending. The check says `return was sent` when the return tool runs, and `return approval was not held` when the pending id is missing. It does not print the id.

`replay` has the same approval id twice. `decisions` is 1 and `slots.book` runs once. The check says `replay applied more than one decision` when both coordinator turns count.

## Block 4 — The redirect, the preference, the constraint

`emergency` matches chest pain. The tool is `safety.redirect`. The citations include `pol-clinical-safety`. Nothing is booked. The check says `emergency booked a slot` and `emergency did not redirect` for the starter. It does not print the phrase.

`consent` does not reuse the stored preference, and the string is not in the trace. The check says `consent reused a blocked preference` and `consent trace contains a blocked preference`. It does not print the preference.

`reason` names `travel` and does not book. The check says `reason refusal does not name the constraint` and does not print the word.

## Block 5 — The note

Open [chapter 04](04-the-note.md) beside their `agent-note.md`.

The tool list includes `referral.status`. The privilege boundary separates extract from book and message. The refusal says a coordinator will answer, and this visit is not booked.

## Block 6 — Knowledge

Open [chapter 05](05-knowledge.md) beside their `work/knowledge.md`.

A second agent is worth its tokens when the extractor would otherwise hold the book tool. A slot is booked after the patient confirms and a coordinator decides the approval.

The checks can print `passed` while this file is still thin. You grade this file.

## Close

Keep this trace and this note. The next morning brings a new pack. Leave later day folders closed.

Misses to keep in your pocket: an invented count of 12, a letter that books, a return that is sent, a second decision on replay, a blocked preference copied into the trace, an emergency that books, a missing citation, and a scenario file copied into `work/`.
