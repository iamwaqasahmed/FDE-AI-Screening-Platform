# 07 — Trainer session

Students can skip this page. The answers are in chapters 01 through 06.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not open the webhook file on a screen. Do not paste the watermark into a slide or a prompt.

The interview notes, [hl7.md](work/hl7.md), and [wa.md](work/wa.md) are for you. The check does not read them. Students were not asked to write them. `dms` stays later. [dms.md](sources/release/channels/dms.md) says the change feed is not part of today's check. Do not build it.

From the course folder, the check prints `passed`:

```text
cd problem_simulation
python -m alwaha.check journey --release rel-w2d2 --work "../Week 02/Day 02/Solution_Copy/work" --profile practice
```

The HL7 demo, from the same folder, prints two lines and nothing else:

```text
cd problem_simulation
python -m alwaha.demo.hl7 --profile practice
```

```text
file order: sequence 1 stands
sequence order: sequence 2 stands
```

The file lists sequence 2, then sequence 1, then a mapping row with no sequence. File order keeps the last of those two sequenced rows, sequence 1. It does not keep the mapping row. Sequence order sorts by the sequence number and keeps sequence 2. The lines do not print the dropped field, the extra field, thyroid, or ZSS.

## Block 1 — The sprint

Open [chapter 02](02-the-sprint.md) beside their `sprint.md`.

The subscribe sentence is above the mart sentence. The check says `sprint.md does not sequence the subscription before the mart` when the mart comes first, or when one of the two ideas is missing. It does not print the words it looked for.

## Block 2 — The states

Open [chapter 04](04-the-pages.md) beside their `states.md`.

The four rows are rebooked, notified, compensated, and escalated. Each second cell is a sentence. The check says `a patient-visible state is missing` and does not name the state.

## Block 3 — The zones

Open their `zones.md` beside chapter 04.

`int-engine` is in `zone-hospital` because `h-nakhl` and `h-safra` are, and their HL7 arrives through the engine. `wf-session-cancelled` is in `zone-private` because the dev namespace serves `h-wadi`. The check says `zone crossing is missing` and does not name the piece.

[ea.notes.md](work/interviews/ea.notes.md) says the same placement. Students were not asked to write that note.

## Block 4 — The SMS

Open their `sms.md` beside chapter 04.

The sentence is `Your booking has a new time.` The check wants the word booking, and it rejects a ten-digit number. [sms.py](work/app/sms.py) adds the booking id when it sends.

## Block 5 — The mart

Open [chapter 05](05-the-mart.md).

The practice extract is `person_key`, `wait_days`, `booking_date`, then `pt-200`, `14`, `2026-06-01`. The clock column is `booking_date`. The wait figure is 14. Their `mart.md` names `booking_date` and does not contain 14. Their `mart.py` returns that column and `trusted` false.

The check says `the mart clock is not named` and does not print the column. It says `wait number was used as truth` and does not print the figure. The shell used `wait_days` as the clock and set `trusted` true.

The sentence with `booking_date` belongs on their mart page and in this mart file. It does not belong on the door or in the blank template.

## Block 6 — The three files

`intake.py`, `cancel.py`, and `mart.py` differ from the starter. Every other file under `work/app` matches the starter byte for byte.

The starter intake still polls. The check says `intake still polls`.

The finished intake calls `registry.keep` for `referral.submitted`. The registry row lists `event_id`, `topic`, `occurred_at`, `sequence`, `referral_id`, `patient_key`, and `letter`. The webhook also carries `priorityHint`. That key is ignored and is not stored. The event is not rejected for it. The check says `an unknown field stopped intake` or `an unknown field was stored`, and it does not print `priorityHint`.

`letter` stays off the record. The letter value is the watermark. The webhook file is not in this folder.

The starter cancel books every delivery, leaves the hold open, and books the no-slot case. The check says `replay booked again`, `the hold was left open`, and `no-slot cancellation was booked`.

The finished cancel returns the stored row for a repeated event id, releases the hold when `bkg-2` is rejected, and stores `escalated` when `slot` is false.

## Block 7 — Knowledge

Open [chapter 06](06-knowledge.md) beside their `work/knowledge.md`.

Line 1 is `eref owns referral.submitted.` Line 2 is `A replay does not book a second time.` The check accepts any first line that contains `eref`, and any second line that contains `book` plus `not` or `once`. The finished sentences are the ones in chapter 06. When line 1 is wrong, the message does not print the owner.

## Block 8 — The notes the check skips

[ea.notes.md](work/interviews/ea.notes.md) has five turns. The strategy is a claim. `h-nakhl` and `h-safra` still send HL7 v2, and `h-wadi` is on the private cloud. `eref` pushes, and polling is the old path. `eref` owns `referral.submitted`. The engine is in `zone-hospital`.

[access-mgr.notes.md](work/interviews/access-mgr.notes.md) has five turns. No-shows are a claim. A large share of contact-center calls ask for a referral status. A cancelled session is told by SMS. WhatsApp is the new channel, and a reply dies after the session window. The mart wait figure is not the number at the desk.

[hl7.md](work/hl7.md) says the mapping drops `sub_specialty`. [int-engine.jsonl](sources/release/feeds/int-engine.jsonl) has two SIU rows and one mapping row. The raw mapping has `SCH` `endo` and `ZSS` `thyroid`. The mapped object keeps `specialty` `endo` and drops that other value. The demo does not print `sub_specialty`, `thyroid`, or `ZSS`.

[wa.md](work/wa.md) matches [wa.md](sources/release/channels/wa.md). A template message needs a registered template. A reply after the session window is rejected. SMS is the channel the check scores.

## Close

Keep this intake, this cancellation worker, and these pages. The next morning brings a new pack. Leave later day folders closed.

Misses to keep in your pocket: a sprint that reads the mart first, a states page with an empty cell, a zones page with no engine, an SMS page with a national id, a mart note that copies 14 or trusts the wait column, a polling intake left in place, a replay that books again, a hold left open, a no-slot cancellation that books, a webhook file copied into `work/`, and a knowledge file that never names `eref`.
