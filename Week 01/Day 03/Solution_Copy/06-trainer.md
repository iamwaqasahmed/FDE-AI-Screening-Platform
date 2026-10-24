# 06 — Trainer session

Students can skip this page. The answers are in chapters 01 through 05.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not open the event file on a screen. Do not paste the watermark into a slide or a prompt.

From the course folder, the check prints `passed`:

```text
cd problem_simulation
python -m alwaha.check events --work "../Week 01/Day 03/Solution_Copy/work" --profile practice
```

## Block 1 — The clock

Open [chapter 05](05-knowledge.md) beside their `knowledge.md`.

The SLA clock starts at `referral.submitted`. It does not start at booking. [pol-sla.md](sources/release/policy/pol-sla.md) is the sentence. `occurred_at` is the field.

The usual miss is starting the count at a booking that this workflow does not make.

## Block 2 — The calendar

Open [chapter 03](03-the-worker.md). Read the friday due date, 2027-01-17, and the holiday due date, 2027-03-14.

Ask which day they counted as day one. The submitted day counts when it is a working day. Friday and Saturday are the weekend. The three March dates in [business-calendar.json](sources/release/calendar/business-calendar.json) are holidays.

The check says `due date does not match the calendar` and does not print the date. The starter counted Monday through Friday.

## Block 3 — One approval, and the later letter

Open the replay row and the order row in [chapter 04](04-the-note.md).

Replay is the same event id twice. One approval. A second id is the miss `opened a second approval`.

Order arrives as sequence 2, then sequence 1. The higher sequence names `h-wadi`. The lower sequence names `h-ain` and is later in the file. Keep the higher sequence. The check says `suggestion does not match` and does not name the facility.

## Block 4 — Ain, and the released hold

`h-ain` has no slot API. The hold is `none`. The clinic is empty. `booked` is false. A queued reply is not a booking. The check says `ain booked a slot` when the starter treats that reply as booked.

Compensation takes a hold and then releases it. The state stays `approval.held`. The check says `hold does not match` and does not print the fitting hold.

## Block 5 — The dead letter, the criteria, the duplicate

The retry case is a dead letter. No approval, hold not open, event not applied. The check calls that miss `applied the poison event`.

The criteria in force is `crit-endo-v3`. The draft is the higher version. The check says `criteria is not the one in force` and does not print the clause.

The duplicate is flagged and still held, and it is not booked. The open row is `pt-160` and `endo`.

## Block 6 — Knowledge

Open [chapter 05](05-knowledge.md) beside their `work/knowledge.md`.

The clock is `referral.submitted`. A second delivery of the same event id changes nothing.

The check can print `passed` while this file is still thin. You grade this file.

## Close

Keep this log and this note. The next morning brings a new pack. Leave later day folders closed.

Misses to keep in your pocket: Friday counted as a working day, a second approval on the replay, a booking at `h-ain`, the draft criteria, a hold left open after compensate, a poison event applied, and the event file copied into `work/`.
