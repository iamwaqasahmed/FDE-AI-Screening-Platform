# Problem simulation

Facilitators only. Participants leave this folder closed. The participant-facing case is [../case/README.md](../case/README.md). The course that sits on this world is [../course_design/README.md](../course_design/README.md).

This folder generates the Al-Waha world from a seed. The twenty teaching releases are `rel-m01-l01` through `rel-m04-l05`. The population, exports, and corpus are `python -m alwaha.worldbuild`. The mocks are `python -m alwaha.serve`. The readiness record is `python -m alwaha.audit`.

## Releases built so far

Learners meet these releases as four modules of five lessons, in this order, with no timetable. The id in each command is the pack name. It is not a schedule.

From this folder:

```text
python -m alwaha.build --profile practice --release rel-m01-l01
python -m alwaha.build --profile practice --release rel-m01-l02
python -m alwaha.build --profile practice --release rel-m01-l03
python -m alwaha.build --profile practice --release rel-m01-l04
python -m alwaha.build --profile practice --release rel-m01-l05
python -m alwaha.build --profile practice --release rel-m02-l01
python -m alwaha.build --profile practice --release rel-m02-l02
python -m alwaha.build --profile practice --release rel-m02-l03
python -m alwaha.build --profile practice --release rel-m02-l04
python -m alwaha.build --profile practice --release rel-m02-l05
python -m alwaha.build --profile practice --release rel-m03-l01
python -m alwaha.build --profile practice --release rel-m03-l02
python -m alwaha.build --profile practice --release rel-m03-l03
python -m alwaha.build --profile practice --release rel-m03-l04
python -m alwaha.build --profile practice --release rel-m03-l05
python -m alwaha.build --profile practice --release rel-m04-l01
python -m alwaha.build --profile practice --release rel-m04-l02
python -m alwaha.build --profile practice --release rel-m04-l03
python -m alwaha.build --profile practice --release rel-m04-l04
python -m alwaha.build --profile practice --release rel-m04-l05
python -m unittest discover -s tests -q
```

Module 1, Lesson 1 writes `../data/rel-m01-l01`. Module 1, Lesson 2 writes `../data/rel-m01-l02` and adds its gold beside the Lesson 1 truth in `build/practice/truth`. Module 1, Lesson 3 writes `../data/rel-m01-l03` and adds `events_gold.json` beside that truth. Module 1, Lesson 4 writes `../data/rel-m01-l04` and adds `agent_gold.json` beside that truth. Module 1, Lesson 5 writes `../data/rel-m01-l05` and adds `m01_l05_gold.json` beside that truth. Module 2, Lesson 1 writes `../data/rel-m02-l01` and adds `m02_l01_gold.json` beside that truth. Module 2, Lesson 2 writes `../data/rel-m02-l02` and adds `m02_l02_gold.json` beside that truth. Module 2, Lesson 3 writes `../data/rel-m02-l03` and adds `m02_l03_gold.json` beside that truth. Module 2, Lesson 4 writes `../data/rel-m02-l04` and adds `m02_l04_gold.json` beside that truth. Module 2, Lesson 5 writes `../data/rel-m02-l05` and adds `m02_l05_gold.json` beside that truth. Module 3, Lesson 1 writes `../data/rel-m03-l01` and adds `m03_l01_gold.json` beside that truth. Module 3, Lesson 2 writes `../data/rel-m03-l02` and adds `m03_l02_gold.json` beside that truth. Module 3, Lesson 3 writes `../data/rel-m03-l03` and adds `m03_l03_gold.json` beside that truth. Module 3, Lesson 4 writes `../data/rel-m03-l04` and adds `m03_l04_gold.json` beside that truth. Module 3, Lesson 5 writes `../data/rel-m03-l05` and adds `m03_l05_gold.json` beside that truth. Module 4, Lesson 1 writes `../data/rel-m04-l01` and adds `m04_l01_gold.json` beside that truth. Module 4, Lesson 2 writes `../data/rel-m04-l02` and adds `m04_l02_gold.json` beside that truth. Module 4, Lesson 3 writes `../data/rel-m04-l03` and adds `m04_l03_gold.json` beside that truth. Module 4, Lesson 4 writes `../data/rel-m04-l04` and adds `m04_l04_gold.json` beside that truth. Module 4, Lesson 5 writes `../data/rel-m04-l05` and adds `m04_l05_gold.json` beside that truth. Rebuilding Module 1, Lesson 1 clears that truth folder. Rebuilding a later day leaves the other days' packs where they are. Participants use the packs and the commands in [Module 1 Lesson 1](<../Module 01/Lesson 01/Student_Copy/home.md>), [Module 1 Lesson 2](<../Module 01/Lesson 02/Student_Copy/home.md>), [Module 1 Lesson 3](<../Module 01/Lesson 03/Student_Copy/home.md>), [Module 1 Lesson 4](<../Module 01/Lesson 04/Student_Copy/home.md>), [Module 1 Lesson 5](<../Module 01/Lesson 05/Student_Copy/home.md>), [Module 2 Lesson 1](<../Module 02/Lesson 01/Student_Copy/home.md>), [Module 2 Lesson 2](<../Module 02/Lesson 02/Student_Copy/home.md>), [Module 2 Lesson 3](<../Module 02/Lesson 03/Student_Copy/home.md>), [Module 2 Lesson 4](<../Module 02/Lesson 04/Student_Copy/home.md>), [Module 2 Lesson 5](<../Module 02/Lesson 05/Student_Copy/home.md>), [Module 3 Lesson 1](<../Module 03/Lesson 01/Student_Copy/home.md>), [Module 3 Lesson 2](<../Module 03/Lesson 02/Student_Copy/home.md>), [Module 3 Lesson 3](<../Module 03/Lesson 03/Student_Copy/home.md>), [Module 3 Lesson 4](<../Module 03/Lesson 04/Student_Copy/home.md>), [Module 3 Lesson 5](<../Module 03/Lesson 05/Student_Copy/home.md>), [Module 4 Lesson 1](<../Module 04/Lesson 01/Student_Copy/home.md>), [Module 4 Lesson 2](<../Module 04/Lesson 02/Student_Copy/home.md>), and [Module 4 Lesson 3](<../Module 04/Lesson 03/Student_Copy/home.md>), and [Module 4 Lesson 4](<../Module 04/Lesson 04/Student_Copy/home.md>), and [Module 4 Lesson 5](<../Module 04/Lesson 05/Student_Copy/home.md>). They leave `build/` and `design/` closed.

`python -m alwaha.interview --persona <id> --script questions.txt` prints the answer and does not print a score.

`python -m alwaha.check repo --work <dir>` and `python -m alwaha.check interview --work <dir>` print pass or fail for Lesson 1. `approach` and `brief` do the same for Module 1, Lesson 2. `events` does the same for Module 1, Lesson 3. `agent` and `trajectory` do the same for Module 1, Lesson 4. Module 1, Lesson 5 runs `agent` and `trajectory` with `--release rel-m01-l05`, then `design`, `readout`, and `individual`. Module 2, Lesson 1 runs `auth` and `journey` with `--release rel-m02-l01`. Module 2, Lesson 2 runs `journey` with `--release rel-m02-l02`. Module 2, Lesson 3 runs `tests` and `ux` with `--release rel-m02-l03`. Module 2, Lesson 4 runs `deploy` with `--release rel-m02-l04`. Module 2, Lesson 5 runs `deploy`, `journey`, `readout`, and `individual` with `--release rel-m02-l05`. Module 3, Lesson 1 runs `identity`, `labels`, and `synthetic` with `--release rel-m03-l01`. Module 3, Lesson 2 runs `model` and `lora` with `--release rel-m03-l02`. Module 3, Lesson 3 runs `rag`, `hybrid`, and `acl` with `--release rel-m03-l03`. Module 3, Lesson 4 runs `eval` and `judge` with `--release rel-m03-l04`. Module 3, Lesson 5 runs `eval`, `rcp`, `readout`, and `individual` with `--release rel-m03-l05`. Module 4, Lesson 1 runs `redteam`, `privacy`, `access`, and `fair` with `--release rel-m04-l01`. Module 4, Lesson 2 runs `incident` and `cache` with `--release rel-m04-l02`. Module 4, Lesson 3 runs `slo` and `surge` with `--release rel-m04-l03`. Module 4, Lesson 4 runs `slo` with `--release rel-m04-l04`. Module 4, Lesson 5 runs `integrate`, `ops`, `rcp`, `readout`, and `individual` with `--release rel-m04-l05`. They do not print the missing fact, the fitting family, the due date, the tool count, the removed field, the extra field, the dropped field, the wait figure, the owner, the interval, the old delay, the hash, the quota, the national id, the clinic code, the converted date, the watermark, a fidelity rate, a gold label, an F1, a price, an interview sentence, a doc id, a span, a clause, a log id, a visit count, a judge item, a rate, the due instant, a lag, a survey count, or the attack text.

`python -m alwaha.demo.split --profile practice` prints the two DNA scores and how many people sit on both sides of the row split. Read those three lines aloud. Do not name the cause.

`python -m alwaha.demo.order --profile practice` prints the two arrivals and how many approvals the apply holds. Read those lines aloud. Do not name the cause.

`python -m alwaha.demo.count --profile practice` prints an invented count and the status tool's count. Read those two lines aloud. Do not name the cause.

`python -m alwaha.demo.readout --profile practice` prints the steering questions and the public opening line. Read those lines aloud. Do not add the hidden answer.

`python -m alwaha.demo.fhir --profile practice` prints the v1 client failure, then the generated client's success. Do not name the field or the clinic code.

`python -m alwaha.demo.hl7 --profile practice` prints the file-order outcome, then the sequence-order outcome. Do not name the dropped field.

`python -m alwaha.demo.receipt --profile practice` prints the suite with the receipt switch off, then the same suite with the switch on. Do not name the interval or the old delay.

`python -m alwaha.demo.deploy --profile practice` prints the root image rejected, then the registered image accepted. Do not name the hash or the national id.

`python -m alwaha.demo.ain --profile practice` prints the change-request card and the five steering questions. Do not add the nightly-file sentence or a clinic code.

`python -m alwaha.demo.merge --profile practice` prints two MRNs, the national id they share, and the line that they stay two people. Do not add the converted date or the watermark.

`python -m alwaha.demo.gateway --profile practice` prints that the gateway refused the prompt. Do not read the watermark aloud.

`python -m alwaha.demo.duplicate --profile practice` prints two leaflet titles and that one is superseded. Do not read the clause aloud.

`python -m alwaha.demo.judge --profile practice` prints that the judge marked the citation correct, and that the citation is not the in-force document. Do not read the item aloud.

`python -m alwaha.demo.brief --profile practice` prints that the sponsor asks for triage in the front desk, and that the DPO keeps patient data off the external model. Do not name a non-goal or a price.

`python -m alwaha.demo.letter --profile practice` prints the family id and that the letter booked a slot. Do not read the instruction aloud.

`python -m alwaha.demo.trace --profile practice` prints a tool, a hash, and a token count. Do not read the error text aloud.

`python -m alwaha.demo.cold --profile practice` prints that the first window is missed, and the cold start. Do not read a price or the backlog count aloud.

`python -m alwaha.demo.drill --profile practice` prints that site-a is down and site-b is serving. Do not read a budget, a hash, or a price aloud.

`python -m alwaha.demo.benefit --profile practice` prints the steering question about the double-counted benefit. Do not read the two lines that count the same calls.

## Principles

- **One seed.** One seed writes every file, every mock, and every gold answer. A second build with the same seed matches.
- **Closed truth.** `truth/` and `eval/` are never part of the participant pack. A grading service scores submissions without handing the key back.
- **A technique earns its place.** A method is taught when a simpler method loses on a published slice. The slices are in [design/11-eval-and-hardness.md](design/11-eval-and-hardness.md).
- **Foundation and advanced layers.** Every syllabus topic has a foundation check and further checks. Deeper work can earn credit. Day content chooses the depth.
- **Daily releases.** `rel-m01-l01` through `rel-m04-l05` are written by the same seed. A later release can invalidate an earlier design. See [design/10-release-schedule.md](design/10-release-schedule.md).
- **Stable ids.** Lessons cite facilities, personas, systems, files, and checks by id. Counts and dates that the seed can change are measurements, not constants in the prose.
- **Fictional and safe.** Fictional people and facilities. No real patient data. Page images are synthetic. Clinical weights and red-flag lists are teaching devices. The assistant routes emergency wording to a human and leaves urgency decisions to a clinician.
- **Small modules.** Generator modules stay under about 200 lines, one purpose each.

## Design notes

| Note | What it fixes |
|---|---|
| [01 Hidden world](design/01-hidden-world.md) | Causes, scale, calendar, sites, case clock |
| [02 Real problems](design/02-real-problems.md) | The nine problems, value, and approach fit |
| [03 Reference system](design/03-reference-system.md) | The assistant facilitators hold back |
| [04 Systems and environments](design/04-systems-and-environments.md) | Exports, defects, zones, catalog |
| [05 Corpus](design/05-corpus.md) | Documents, versions, permissions |
| [06 Engagement and delivery](design/06-engagement-and-delivery.md) | Personas, workshops, backlog, adoption |
| [07 Datasets](design/07-datasets.md) | Letters, messages, tables, scenarios |
| [08 Live services](design/08-live-services.md) | Mocks, identity, events, gateway, contract |
| [09 Traffic and threats](design/09-traffic-and-threats.md) | Patients, staff, load, attacks, canaries |
| [10 Release schedule](design/10-release-schedule.md) | What arrives each day |
| [11 Eval and hardness](design/11-eval-and-hardness.md) | Checks, slices, packs, grading |
| [12 Generator build](design/12-generator-build.md) | Packages, reuse, gates |
| [Traceability](design/traceability/README.md) | Every syllabus element to a check |

## Regulatory analogues

Case documents use the fictional names. Facilitators may say what each one resembles. The resemblance is for teaching, and the case text is not a statement of the real law.

| In the case | Resembles |
|---|---|
| Personal Data Statute (PDS) | Saudi Personal Data Protection Law |
| National Data Classification Standard (NDCS) | National data-classification rules |
| National Cyber Controls (NCC) | National cybersecurity controls |
| National AI Ethics Principles (NAEP) | National AI ethics principles |

## Version 01

Copy and adapt. Do not import. Version 01 stays frozen. Paths are under `Version 01/Module 01 - Module 06/problem_simulation/`. What moves, and what is rewritten, is listed in [design/12-generator-build.md](design/12-generator-build.md).
