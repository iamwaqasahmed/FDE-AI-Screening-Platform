# 06 — Trainer session

Students can skip this page. The answers are in chapters 01 through 05.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not open a scenario file on a screen. Do not paste the watermark into a slide or a prompt.

The interview notes in `work/interviews` are for you. The checks do not read them. Students were not asked to run an interview.

From the course folder, the checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check auth --release rel-m02-l01 --work "../Module 02/Lesson 01/Solution_Copy/work" --profile practice
python -m alwaha.check journey --release rel-m02-l01 --work "../Module 02/Lesson 01/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open [chapter 02](02-the-sprint.md) beside their `sprint.md`.

The generate sentence is above the booking sentence. The check says `sprint.md does not sequence the client before booking` when booking comes first, or when one of the two ideas is missing. It does not print the words it looked for.

## Block 2 — The states

Open [chapter 03](03-the-sign-in.md) beside their `states.md`.

The file has to contain the patient, the coordinator, and `loa-1`. The finished table also has the booking row at `loa-2`, marked not this day. The check says `states.md is missing a sign-in state` and does not print the role list or the assurance level.

The staff list in [loa.md](sources/release/identity/loa.md) is coordinator, contact-center, records, and audit. The check signs in records and expects the console. It signs in a foreign role and expects a refusal. It signs in `svc-integration` and expects a refusal. Those three messages do not print the role list.

## Block 3 — The token

Open their `token-flow.md` beside chapter 03.

The session row is written in the application database. A service token is not a patient token. The check says `token-flow.md does not say where the session row is written` or `token-flow.md does not keep a service token off the patient`.

The table in [session.py](work/app/session.py) has four columns: `session_id`, `subject`, `role`, and `loa`. An extra column fails. A missing column fails. The message does not print the stored role or the stored level.

## Block 4 — The client

Open [chapter 04](04-the-status.md).

Run the demo if you need the two lines again. The first line is the hand-written client. The second line is the generated client. The lines do not name a field. Their `work/app/client.py` has to be the file the generator writes. Every other file under `work/app` has to match the starter. The check says `his-wadi read failed` when the hand-written client is still in place. It does not name a field or a count.

Count, state, and facility are copied from the scenario row by [contract.py](work/app/contract.py). The check says they do not match and does not print the number. The status tool is the name `status`. A book call fails the journey. An approval stays `later`.

## Block 5 — Knowledge

Open [chapter 05](05-knowledge.md) beside their `work/knowledge.md`.

Line 1 is `Booking and cancellation require loa-2.` Line 2 is `The session row lives in the application database.` The check accepts any first line that contains `loa-2` and any second line that contains `database`. The finished sentences are the ones in chapter 05. When line 1 is wrong, the message does not print the level.

## Block 6 — The interview

[ea.notes.md](work/interviews/ea.notes.md) is yours. Students were not asked to write it. The checks do not read it.

The note has three turns. The strategy is a claim. `h-nakhl` and `h-safra` still send HL7 v2, and `h-wadi` is the hospital on the private cloud. That second turn is a fact. [zones.md](sources/kickoff/world/zones.md) places `h-wadi` in `zone-private`. The third turn points at [fhir-v2.md](sources/release/notices/fhir-v2.md) and releases no new fact. HL7 v2 here is the older hospital message. It is not the FHIR spec in today's drop.

## Close

Keep this client, this session row, and these three pages. The next morning brings a new pack. Leave later day folders closed.

Misses to keep in your pocket: booking written above the client, a states page with no patient, a session row with an extra column, a service token accepted as the patient, a hand-written client left in place, a status question that books, a scenario file copied into `work/`, and a knowledge file that never names the booking level.
