# 05 — The pages

Open the finished [zones.md](work/zones.md), [operators.md](work/operators.md), and [deployment.md](work/deployment.md) and put them beside yours.

## The zone table

The columns are `surface` and `zone`, with the pipe characters kept. `url` is in `zone-private`. [guide.md](sources/m01_l04/endpoint/guide.md) states that address and that zone. `sched-ain` is in `zone-hospital`. [sched-ain.md](sources/release/systems/sched-ain.md) states that. [zones.md](sources/kickoff/world/zones.md) is the standing map: `h-ain` sits in `zone-hospital`, and the private cloud is `zone-private`.

While either row is missing, the check says `the url is not in zone-private` or `the file path is not in zone-hospital`.

## The operator steps

The steps say to read the health probe and to use the prod credential. The check looks for the words `health` and `prod` anywhere in the file. [prod.json](sources/m01_l04/credentials/prod.json) is the prod file. The page does not store the credential value.

While those words are missing, the check says `the operator steps are missing`.

## The deployment note

The Lesson 4 headings stay: URL, Zone, Probe, Credentials, Monitoring, Boundary, and Operator steps. Ain names `h-ain`, `sched-ain`, a nightly file, and `zone-hospital`, and it says a booking stays queued. Change names `cr-ain` and says it is sequenced after the smoke test.

The note cites `ciso`, `endpoint/guide.md`, `pol-deploy`, `notices/cr-ain.md`, and `systems/sched-ain.md`. [pol-deploy.md](sources/m01_l04/standards/pol-deploy.md) is the checklist. Probe names `local-small`, the word hash, and `non-root`. The hash value stays in [models.json](sources/m01_l04/registry/models.json). Monitoring names request rate, error rate, and model latency, and it says the rest waits until Module 2. [starter.md](sources/m01_l04/dashboard/starter.md) is that dashboard. Boundary leaves urgency with a clinician and keeps PHI off `ext-large`.

The check says `the deployment note is missing a required fact` when one of those facts is absent. The message does not name the fact. It says `the deployment note does not cite a source` when no source is named. It says `the deployment note promises a live slot` when the page says Ain has a live slot, that `h-ain` is out of scope, that every hospital has a live slot API, or that monitoring is complete. This finished page does not say those sentences.

Next: [06 — The readout](06-the-readout.md).
