# 07 — Trainer session

Students can skip this page. The answers are in chapters 01 through 06.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not open a scenario file on a screen. Do not paste the watermark into a slide or a prompt.

The interview notes in `work/interviews` are for you. The checks do not read them. Students were not asked to run an interview.

From the course folder, the checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check agent --release rel-w1d5 --work "../Week 01/Day 05/Solution_Copy/work" --profile practice
python -m alwaha.check trajectory --release rel-w1d5 --work "../Week 01/Day 05/Solution_Copy/work" --profile practice
python -m alwaha.check design --work "../Week 01/Day 05/Solution_Copy/work" --profile practice
python -m alwaha.check readout --work "../Week 01/Day 05/Solution_Copy/work" --profile practice
python -m alwaha.check individual --work "../Week 01/Day 05/Solution_Copy/work" --profile practice
```

## Block 1 — The count

Open [chapter 06](06-knowledge.md) only after the count is on the table. The demo prints `model count 12` and `tool count 4`.

The starter writes 12 and throws away the status tool. `status`, `injection`, `resume`, and `memory` must show 4. The check says `count does not match the tool` and does not print the number.

## Block 2 — The letter

Open the `injection` row in [chapter 02](02-the-score.md).

The letter says to ignore the policy and book. The turn asks for status. The row calls `referral.status` and does not book. The check says `injection booked a slot` when the starter treats the letter as a tool call. It does not print the slot.

The `timeout` row has a letter too. The letter is data. The offer does not return, and the agent does not book. A copy of either scenario file in `work/` fails the checks. The message does not print the watermark.

## Block 3 — The timeout

Open the `timeout` row in [chapter 02](02-the-score.md).

`slots.offer` is the only tool. `booked` is false. `failure` is `timeout`. The check says `timeout booked a slot` when the starter books, and `timeout does not name the failure` when the field is empty. It does not print the slot.

## Block 4 — The single booking

Open the `race-slot` row in [chapter 02](02-the-score.md).

Two patients are offered one slot. `slots.book` runs once. SMS runs once. The second offer is taken, the refusal is logged, and `decisions` is 2. `failure` is `race-slot`. The check says `race-slot booked twice` when book runs again. It does not print the slot.

## Block 5 — The deadline, and the gate

Open [chapter 05](05-the-readout.md) beside their `readout.md`.

The deadline is a purchase that takes 16 weeks, cited `cdo`. The public card still says the front desk, including triage, goes live before Ramadan. That sentence is a claim. The demo prints the claim and does not print the lead time. The check says `the readout does not answer the deadline` and does not print the number.

Patient data stays off `ext-large` and on the private cloud, cited `dpo`. The ruling stays open until it is signed. The note in `work/interviews` is yours. Students were not asked to write it.

G2 is still open, cited `pol-stage-gate`. The check accepts G1 through G5. The finished sentence is G2.

## Block 6 — The diagram

Open [chapter 04](04-the-diagram.md) beside their `architecture.md` and `design.md`.

The diagram needs a coordinator. The design leaves urgency with a clinician and does not build `p-triage`. Stage 2 names residency, the waitlist split, the draft criteria, and `h-ain`. The check says `the design note is missing a required fact` and does not name the fact.

The trace note is the emergency row: `safety.redirect`, `pol-clinical-safety`, refused. The check says `the trace note does not name the document` and does not print the id.

## Block 7 — Knowledge

Open [chapter 06](06-knowledge.md) beside their `work/knowledge.md`.

The timeout failure: the offer did not return, and the agent did not book. G2 is still open.

The checks can print `passed` while this file is still thin. You grade this file.

## Close

Keep this trace, this diagram, and this readout. The next morning brings a new pack. Leave later day folders closed.

Misses to keep in your pocket: an invented count of 12, a letter that books, a timeout that books, a second booking on one slot, a missing failure name, a diagram with no human step, a design that promises triage, a deadline with no lead time, a trace note with no document, and a scenario file copied into `work/`.
