# 03 — The change

[Chapter 02](02-the-role.md) said you hold all five parts. This chapter is the change request and the file Ain actually publishes.

## What you do on this page

Three steps. You do not edit a file. You do not paste a block from this page into `work/`.

1. Open each linked file. In Cursor or VS Code, Ctrl+click the link on Windows, or Command+click on macOS. If the link does not open, the path is in the sentence beside it.
2. Search that file. Press Ctrl+F on Windows or Command+F on macOS, then type the word this page names. Every fenced block below is a picture of a file you just opened. Leave the picture on this page.
3. Run the demo under Run the demo. You should see six lines. Then keep reading this page through the fixtures. The last line of the page names chapter 04.

If chapter 01 told you to use `py` instead of `python`, use `py` in the command on this page too.

Case date: 21 January 2027. The drop is from the steering committee.

## Read the change request

Open [cr-ain.md](packet/release/notices/cr-ain.md). Search for `cr-ain`. The card asks to include `h-ain`. It tells you to sequence the work. It does not say how a patient gets a slot. The next block is a picture of that file. Do not paste it.

```text
# cr-ain

Change request cr-ain: include h-ain.

Sequence the work. A refusal needs a reason. The interface note for sched-ain is in this pack.

Case date: 2027-01-21.
```

## Run the demo

Open a terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation`. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. If `cd problem_simulation` says the path cannot be found, this window is not the course folder. Open a new one from chapter 01, then run the command again.

```text
cd problem_simulation
python -m alwaha.demo.ain --profile practice
```

You should see these six lines, and nothing else:

```text
Change request cr-ain: include h-ain.
1. What does the deployed assistant still not do?
2. Will you include Ain, and where in the sequence?
3. How does a patient at Ain get a confirmed slot?
4. What does the starter dashboard show?
5. What will this proof not build?
```

The prompt returns after the last line. The demo does not print nightly, a clinic code, or `CANARY-`. Open [steer-m02.md](packet/release/steering/steer-m02.md) and search for `sequence`. The five questions are the same five lines. The next block is a picture of that file. Do not paste it.

```text
# steer-m02

The steering committee asks these questions.

1. What does the deployed assistant still not do?
2. Will you include Ain, and where in the sequence?
3. How does a patient at Ain get a confirmed slot?
4. What does the starter dashboard show?
5. What will this proof not build?
```

Question 1 is what the deployed assistant still does not do. Booking from chat waited after Lesson 4. Question 4 is the starter dashboard. Open [starter.md](packet/m02-l04/dashboard/starter.md) and search for `latency`. The dashboard shows request rate, error rate, and model latency. Question 5 is what this proof will not build. The rest of the operations stack waits until Module 2.

## Read the file path

Open [sched-ain.md](packet/release/systems/sched-ain.md). Search for `nightly`. Ain sits in `zone-hospital`. The schedule is a nightly full file. The last file wins. A missed night leaves the previous file. A real-time booking returns queued. The next block is a picture of that file. Do not paste it.

```text
# sched-ain

Ain Diabetes and Eye Center (`h-ain`) sits in `zone-hospital`.

The schedule is a nightly full file. The last file wins. There is no intraday API. The file uses local clinic codes. A missed night leaves the previous file.

A real-time booking returns queued until that file is applied.
```

Open [sched-ain.yaml](packet/release/openapi/sched-ain.yaml). Search for `queued`. `POST /files` stores the nightly file. `POST /book` returns queued. The next block is a picture of that file. Do not paste it.

```text
openapi: 3.0.3
info:
  title: sched-ain
  version: "1"
paths:
  /files:
    post:
      operationId: acceptFile
      responses:
        "202":
          description: The nightly file is stored. The last file wins.
  /book:
    post:
      operationId: book
      responses:
        "202":
          description: A real-time booking returns queued.
```

## Read the fixtures

Open [queued.json](packet/release/fixtures/queued.json). Search for `queued`. The next block is a picture of that file. Every field has a column. Do not paste it into `work/`.

```text
{
  "facility": "h-ain",
  "status": "queued"
}
```

| field | what you read |
| --- | --- |
| facility | `h-ain` |
| status | `queued` |

Open [nightly.json](packet/release/fixtures/nightly.json). Search for `clinic_code`. Read the value in the file. The three fields are the whole file. You are not asked to type that value anywhere today.

| field | what you read |
| --- | --- |
| clinic_code | the value in this file |
| facility | `h-ain` |
| status | `file` |

Open [missed.json](packet/release/fixtures/missed.json). Search for `clinic_code`. This is the previous file, the one a missed night leaves behind. Read the value. It is different from the value in the nightly file. That difference is the whole point of opening the two files. Close them. You will not be asked to type either code.

| field | what you read |
| --- | --- |
| clinic_code | the value in this file |
| facility | `h-ain` |
| status | `previous` |

Open [live-slot.json](packet/release/fixtures/live-slot.json). Search for `fault`. This file is a picture in the drawer. Do not copy it into `work/`. Do not paste it into a prompt. The contract test reads it from the built pack.

| field | what you read |
| --- | --- |
| facility | `h-ain` |
| fault | `live-slot` |
| status | `booked` |
| watermark | a mark on this file. The check message does not print it |

The live-slot fault is a booking whose status is `booked`. A queued booking is the one that holds. [Chapter 07](07-the-contract.md) uses those two words. It does not copy this file.

## What you are deciding

Module 1, Lesson 3 already recorded this limit. The SLA policy said `h-ain` has no slot API, and a hold or a booking there returns queued. You did not book it. Today's nightly file is the path that was missing. A real-time booking still returns queued. You do not go back and change the Module 1 worker.

Include `h-ain`. Sequence `cr-ain` after the smoke test. A patient at Ain sees a queued booking until the nightly file arrives. The starter dashboard still shows request rate, error rate, and model latency. Stage 2 adds the rest in Module 2.

This page is done when those six demo lines are on the screen, you have read the clinic code in the nightly file and the clinic code in the missed-night file, and you have not copied a picture into `work/`.

Next: [04 — Words](04-words.md).
