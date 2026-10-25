# 08 — Trainer session

Students can skip this page. The answers are in chapters 01 through 07.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not open the fixture file on a screen. Do not paste the watermark into a slide or a prompt.

[hijri.md](work/hijri.md) and the patient-representative notes are for you. The checks do not read them. Students were not asked to write them. [hijri.json](sources/release/calendar/hijri.json) is the later reading. `phone-only` stayed out of today's table. Do not add it.

From the course folder, the checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check tests --release rel-w2d3 --work "../Week 02/Day 03/Solution_Copy/work" --profile practice
python -m alwaha.check ux --release rel-w2d3 --work "../Week 02/Day 03/Solution_Copy/work" --profile practice
```

The receipt demo, from the same folder, prints two lines and nothing else:

```text
cd problem_simulation
python -m alwaha.demo.receipt --profile practice
```

```text
switch off: passed
switch on: failed
```

The lines do not print the old delay, `pending`, `due`, the switch name, or the watermark. The test file uses `pending` and `due`. The demo does not.

## Block 1 — The sprint

Open [chapter 02](02-the-sprint.md) beside their `sprint.md`.

The suite sentence is above the usability sentence. The check says `sprint.md does not sequence the suite before sign-off` when the sign-off comes first, or when one of the two ideas is missing. It does not print the words it looked for.

## Block 2 — The calendar

Open [chapter 03](03-the-calendar.md) beside their calendar files.

Sunday through Thursday count. Friday and Saturday do not. The holiday list is skipped. `NAMES` still lists Friday. The check says `the calendar does not match` when the shell still counts Friday or ignores the holiday list. It does not name a date.

## Block 3 — The reply

Open [chapter 04](04-the-reply.md) beside their schema and the two tests.

An empty sentence with `intent` passes. A sentence with no `intent` fails. The journey reads `booked` on the state. The fixture stays in the pack. The check says `the reply schema is missing` or `the journey followed the sentence`. It does not name a field.

## Block 4 — The receipt

Open [chapter 05](05-the-receipt.md) beside their receipt files.

The test reads `minutes` from the clock file. The switch holds the receipt pending. The shell test waits, and the check says `the receipt test sleeps`. A receipt that is due while the switch is on produces `the suite accepted the receipt fault`. A result that misses the clock produces `the receipt test does not match the clock`. None of those messages names an interval or a delay.

## Block 5 — The usability table

Open [chapter 06](06-the-pages.md) beside their `usability.md`.

`status-short` and `caregiver` are finished. The four clause ids are in the clause column. `phone-only` is not a row. The check says `a usability script is unfinished` or `an accessibility clause is missing`. It does not name the script or the clause.

## Block 6 — The definition of done

The sentence in `dod.md` names `receipt-late` and says the suite goes red. The check says `the fault is not in the definition of done` when the name or the word red is missing. The message does not name the switch.

## Block 7 — The zone crossings

The receipt row is `zone-private` to `partner`. The calendar row is `zone-private` to `zone-private`. The check says `a zone-crossing case is missing`. It does not name the case.

## Block 8 — The fixture note

The note says the journey reads the recorded fixture and asserts the mock state. The fixture file is not in `work/`. A copy there fails with `a watermarked sample is in the work directory`. The message does not print the watermark.

## Block 9 — Knowledge

Line 1 says a fixed sleep follows the wall clock and the receipt follows the case clock. Line 2 says the journey asserts the mock state from a recorded fixture. The check looks for those ideas. It does not print a model answer.

## Block 10 — The notes the check skips

[hijri.md](work/hijri.md) says a due date drawn from the Hijri list is never a Friday or a Saturday. The interview note has three turns: the phone line, the Ramadan slots, and the caregiver who books. Students were not asked to write either file. The checks do not read them.

## Close

Both checks print `passed` on the finished `work/` in this folder. Booking from chat still waits. A live cluster deploy is a later day.
