# Problem simulation

Facilitators only. Participants leave this folder closed. The participant-facing case is [../case/README.md](../case/README.md). The course that sits on this world is [../course_design/README.md](../course_design/README.md).

This folder generates the Al-Waha world from a seed. Week 1, Week 2 Days 1 to 5, and Week 3 Day 1 are the first slices. The rest of the generator follows [design/12-generator-build.md](design/12-generator-build.md).

## Days built so far

From this folder:

```text
python -m alwaha.build --profile practice --release rel-w1d1
python -m alwaha.build --profile practice --release rel-w1d2
python -m alwaha.build --profile practice --release rel-w1d3
python -m alwaha.build --profile practice --release rel-w1d4
python -m alwaha.build --profile practice --release rel-w1d5
python -m alwaha.build --profile practice --release rel-w2d1
python -m alwaha.build --profile practice --release rel-w2d2
python -m alwaha.build --profile practice --release rel-w2d3
python -m alwaha.build --profile practice --release rel-w2d4
python -m alwaha.build --profile practice --release rel-w2d5
python -m alwaha.build --profile practice --release rel-w3d1
python -m unittest discover -s tests -q
```

Day 1 writes `../data/rel-w1d1`. Day 2 writes `../data/rel-w1d2` and adds its gold beside the Day 1 truth in `build/practice/truth`. Day 3 writes `../data/rel-w1d3` and adds `events_gold.json` beside that truth. Day 4 writes `../data/rel-w1d4` and adds `agent_gold.json` beside that truth. Day 5 writes `../data/rel-w1d5` and adds `day5_gold.json` beside that truth. Week 2 Day 1 writes `../data/rel-w2d1` and adds `w2d1_gold.json` beside that truth. Week 2 Day 2 writes `../data/rel-w2d2` and adds `w2d2_gold.json` beside that truth. Week 2 Day 3 writes `../data/rel-w2d3` and adds `w2d3_gold.json` beside that truth. Week 2 Day 4 writes `../data/rel-w2d4` and adds `w2d4_gold.json` beside that truth. Week 2 Day 5 writes `../data/rel-w2d5` and adds `w2d5_gold.json` beside that truth. Week 3 Day 1 writes `../data/rel-w3d1` and adds `w3d1_gold.json` beside that truth. Rebuilding Day 1 clears that truth folder. Rebuilding a later day leaves the other days' packs where they are. Participants use the packs and the commands in [Week 1, Day 1](<../Week 01/Day 01/README.md>), [Week 1, Day 2](<../Week 01/Day 02/README.md>), [Week 1, Day 3](<../Week 01/Day 03/README.md>), [Week 1, Day 4](<../Week 01/Day 04/README.md>), [Week 1, Day 5](<../Week 01/Day 05/README.md>), [Week 2, Day 1](<../Week 02/Day 01/README.md>), [Week 2, Day 2](<../Week 02/Day 02/README.md>), [Week 2, Day 3](<../Week 02/Day 03/README.md>), [Week 2, Day 4](<../Week 02/Day 04/README.md>), [Week 2, Day 5](<../Week 02/Day 05/README.md>), and [Week 3, Day 1](<../Week 03/Day 01/README.md>). They leave `build/` and `design/` closed.

`python -m alwaha.interview --persona <id> --script questions.txt` prints the answer and does not print a score.

`python -m alwaha.check repo --work <dir>` and `python -m alwaha.check interview --work <dir>` print pass or fail for Day 1. `approach` and `brief` do the same for Day 2. `events` does the same for Day 3. `agent` and `trajectory` do the same for Day 4. Day 5 runs `agent` and `trajectory` with `--release rel-w1d5`, then `design`, `readout`, and `individual`. Week 2 Day 1 runs `auth` and `journey` with `--release rel-w2d1`. Week 2 Day 2 runs `journey` with `--release rel-w2d2`. Week 2 Day 3 runs `tests` and `ux` with `--release rel-w2d3`. Week 2 Day 4 runs `deploy` with `--release rel-w2d4`. Week 2 Day 5 runs `deploy`, `journey`, `readout`, and `individual` with `--release rel-w2d5`. Week 3 Day 1 runs `identity`, `labels`, and `synthetic` with `--release rel-w3d1`. They do not print the missing fact, the fitting family, the due date, the tool count, the removed field, the extra field, the dropped field, the wait figure, the owner, the interval, the old delay, the hash, the quota, the national id, the clinic code, the converted date, the watermark, a fidelity rate, a gold label, or an interview sentence.

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

## Principles

- **One seed.** One seed writes every file, every mock, and every gold answer. A second build with the same seed matches.
- **Closed truth.** `truth/` and `eval/` are never part of the participant pack. A grading service scores submissions without handing the key back.
- **A technique earns its place.** A method is taught when a simpler method loses on a published slice. The slices are in [design/11-eval-and-hardness.md](design/11-eval-and-hardness.md).
- **Foundation and advanced layers.** Every syllabus topic has a foundation check and further checks. Deeper work can earn credit. Day content chooses the depth.
- **Daily releases.** `rel-w1d1` through `rel-w4d5` are written by the same seed. A later release can invalidate an earlier design. See [design/10-release-schedule.md](design/10-release-schedule.md).
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

Copy and adapt. Do not import. Version 01 stays frozen. Paths are under `Version 01/Week 01 - Week 06/problem_simulation/`. What moves, and what is rewritten, is listed in [design/12-generator-build.md](design/12-generator-build.md).
