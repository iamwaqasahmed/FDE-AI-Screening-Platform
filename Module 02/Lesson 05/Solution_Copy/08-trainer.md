# 08 — Trainer session

Students can skip this page. The answers are in chapters 01 through 07.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not open the live-slot fixture on a screen. Do not paste the watermark into a slide or a prompt.

[ea.notes.md](work/interviews/ea.notes.md) and [ea.questions.txt](work/interviews/ea.questions.txt) are for you. The checks do not read them. Students were not asked to run an interview. The Module 2, Lesson 2 journey command points at another day's work. It is not a step today.

The quota number stays in [quota.json](sources/m01_l04/registry/quota.json). The clinic codes stay in [nightly.json](sources/release/fixtures/nightly.json) and [missed.json](sources/release/fixtures/missed.json). Do not put those values on a slide.

The smoke files in `work/app`, `work/tests`, and `work/deploy` match the packet copies byte for byte. `deployment.yaml` and `ci.yml` match as well. They were copied from Lesson 4 and not rewritten. Do not add a comment to only one side.

From the course folder, the four checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check deploy --release rel-m02-l05 --work "../Module 02/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check journey --release rel-m02-l05 --work "../Module 02/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check readout --release rel-m02-l05 --work "../Module 02/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check individual --release rel-m02-l05 --work "../Module 02/Lesson 05/Solution_Copy/work" --profile practice
```

The demo, from the same folder, prints six lines and nothing else:

```text
cd problem_simulation
python -m alwaha.demo.ain --profile practice
```

```text
Change request cr-ain: include h-ain.
1. What does the deployed assistant still not do?
2. Will you include Ain, and where in the sequence?
3. How does a patient at Ain get a confirmed slot?
4. What does the starter dashboard show?
5. What will this proof not build?
```

The lines do not print nightly, a clinic code, or `CANARY-`.

## Block 1 — The sprint

Open [chapter 02](02-the-sprint.md) beside their `sprint.md`.

Smoke comes before change, change before readout, and readout before retro. The check says `sprint.md does not sequence the change before the readout` when that order breaks. It does not print the four words it looked for.

## Block 2 — The booking

Open [chapter 03](03-the-booking.md) beside their three modules.

`h-ain` with an empty fault returns `queued`. `return "booked"` stays on the next line for the live-slot fault and for another hospital. A missing night returns `previous`. The type line can still say `None`. A queued status stays `queued` when the notice fails. The shell messages are `a live slot was promised`, `a missed night cleared the slots`, and `a failed notice confirmed a slot`.

## Block 3 — The contract

Open [chapter 04](04-the-contract.md) beside their contract.

`holds` accepts `queued` and rejects `booked`. The test contains `holds`. The second test still writes `booked` inside `assertFalse`. That is the fault going red. The shell message is `the contract test accepted the live-slot fault`.

## Block 4 — The pages

Open [chapter 05](05-the-pages.md) beside their three pages.

The zone table has `url` / `zone-private` and `sched-ain` / `zone-hospital`. The operator steps name health and prod. The deployment note keeps the Lesson 4 headings and adds Ain and Change. Ain names `h-ain`, `sched-ain`, nightly, and `zone-hospital`. Change names `cr-ain` and sequences it after the smoke test. The message `the deployment note is missing a required fact` does not name the fact.

## Block 5 — The readout and the retro

Open [chapter 06](06-the-readout.md) beside their two pages.

Smoke has health and hash. Change has `cr-ain` and a sequence word. File has nightly, `sched-ain`, and `zone-hospital`. Patients has `queued`. Monitoring has latency, and Stage 2 or Module 2. Model has `local-small` and quota. Asks is not empty. The retro headings Keep, Drop, and Open each have text.

## Block 6 — Knowledge

Open [chapter 07](07-knowledge.md) beside their `knowledge.md`.

The first line says Ain cannot confirm a slot today because `sched-ain` publishes a nightly file, and a booking stays queued. The second line says Stage 2 adds the operations stack beyond request rate, error rate, and model latency, in Module 2.

## Close

The four checks print `passed` on this folder's `work/`. A booking at Ain stays queued for the nightly file.
