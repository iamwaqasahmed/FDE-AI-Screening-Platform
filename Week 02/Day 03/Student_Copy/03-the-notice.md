# 03 — The notice

[Chapter 00](00-background.md) named Al-Waha and the front-desk wish. This chapter is the third morning of Week 2. The receipt timing change, the access clauses, and the usability scripts arrive.

The case date on today's drop is 19 January 2027. The note is from the patient representative, [Abdullah Al-Harthy](packet/kickoff/personas/patient-rep.md). His id is `patient-rep`. The phone line is still the door most families use.

## What you do on this page

You read the files linked below. You run one command. You replace the notes file. You do not edit the packet. You do not run a check.

If chapter 01 told you to use `py` instead of `python`, use `py` in the command on this page too.

## What arrived today

[timing.md](packet/release/notices/timing.md) says the SMS partner has withdrawn the wall-clock wait. Search for `Pin the case clock`. The interval is in this pack. Search for `receipt-late`. While that switch is on, the receipt stays pending after the clock has moved.

[guide.md](packet/release/clock/guide.md) is how you pin that clock. Search for `PUT /clock`. The body has one field, `at`. Search for `Advance`. You move the pinned time. You do not wait on the wall clock.

[receipt.json](packet/release/clock/receipt.json) holds the interval and the switch. The file has this shape. This block is a picture of that file. Do not paste it into a Python file.

```text
{
  "minutes": 5,
  "switch": "receipt-late"
}
```

Two fields. `minutes` is the interval. Read the number under that field. [Chapter 08](08-the-receipt.md) has the test that reads this file. This page does not ask you to type the number into a test. `switch` is the fault name. [Chapter 09](09-the-pages.md) has the sentence that uses it.

[clock.yaml](packet/release/openapi/clock.yaml) is the clock spec. Search for `pinClock`. [sms.yaml](packet/release/openapi/sms.yaml) is the SMS spec. Search for `The receipt follows the case clock`. A due receipt is one response. A receipt that is still pending is another. Search for `Still pending`.

[access.md](packet/release/standards/access.md) is the clause list. The columns are Id and Clause. Search for `plain-language`. Four ids are on that page. [Chapter 09](09-the-pages.md) cites them. This block is a picture of that table. Do not paste it into `usability.md`. The block that replaces `usability.md` is in chapter 09.

```text
| Id | Clause |
| --- | --- |
| plain-language | The task uses short words. |
| caregiver-complete | A caregiver can finish the task. |
| named-control | A control has a name, not a color alone. |
| one-action | The task has one next step. |
```

[scripts.jsonl](packet/release/usability/scripts.jsonl) is one script on each line. The fields are `actor`, `id`, `layer`, and `task`. This block is a picture of that file. Do not paste it into `usability.md`.

```text
{"actor": "patient", "id": "status-short", "layer": "foundation", "task": "Ask where the referral is. Use a short message."}
{"actor": "caregiver", "id": "caregiver", "layer": "foundation", "task": "A caregiver asks about her mother's referral."}
{"actor": "pop-literacy", "id": "phone-only", "layer": "advanced", "task": "Ask the same question by phone, with no app."}
```

The first two lines are `foundation`. Those two are today's table. The third line is `phone-only`. Its layer is `advanced`. Leave it out of the table in chapter 09.

[cases.json](packet/release/calendar/cases.json) is the two calendar cases. The fields are `count`, `id`, and `start`. This block is a picture of that file. Do not paste it into a Python file. The file does not contain the date a case lands on. You count that in [chapter 06](06-the-calendar.md).

```text
[
  {
    "count": 2,
    "id": "thursday",
    "start": "2027-01-21"
  },
  {
    "count": 3,
    "id": "eid",
    "start": "2027-03-09"
  }
]
```

[business-calendar.json](packet/carried/calendar/business-calendar.json) is the Week 1 calendar the count uses. Search for `working_days`. Sunday through Thursday are working days. Search for `Friday`. Friday and Saturday are the weekend. Search for `holidays`. Three March dates are on that list. The tests read this same document from `data/rel-w1d3`. You read this copy.

[hijri.json](packet/release/calendar/hijri.json) is a later reading. The checks do not grade a note about it. You do not write one today.

[model.json](packet/release/fixtures/model.json) is the recorded reply. Open it. Search for `intent`. The file has two fields, `intent` and `text`. The text starts with a sentence and then a watermark. Leave the file in the packet. Do not copy it into `work/`. Do not paste it into a prompt. This page does not show a picture of that file.

## Run the receipt demo

Open a terminal in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.demo.receipt --profile practice
```

You should see exactly these two lines, and nothing else:

```text
switch off: passed
switch on: failed
```

The first line is the suite with the switch off. The second line is the same suite with the switch on. The lines do not print the old delay, `pending`, `due`, the switch name, or a watermark.

Open [receipt-lines.md](notes/receipt-lines.md). Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. Leave both pipes on each row. The checks do not read this file.

```text
# Receipt lines

The checks do not read this page.

| Line | What the demo printed |
| --- | --- |
| Switch off | switch off: passed |
| Switch on | switch on: failed |
```

Read the file back. The row `Switch off` has `switch off: passed` in the next cell. The row `Switch on` has `switch on: failed` in the next cell. If a row is one long line, select the whole file, delete it, and paste the block again.

## What you already decided

`wf-self-service` can report status and book inside the approval rules. Today the book call from chat waits. The new work is the suite: the calendar counts the cluster week, the reply is judged by its fields, and the receipt follows the case clock.

`h-wadi` is the hospital on the private cloud. A live deploy of this assistant onto the cluster is a later day. Today you run the suite on your machine.

Next: [04 — Words](04-words.md).
