# 08 — Trainer session

Students can skip this page. The answers are in chapters 01 through 07.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not open the deploy log on a screen. Do not paste the watermark into a slide or a prompt.

[provenance.md](work/provenance.md), [limits.md](work/limits.md), [rollback.md](work/rollback.md), [quota.md](work/quota.md), and the security-officer notes are for you. The check does not read them. Students were not asked to write them. The quota number stays in [quota.json](sources/release/registry/quota.json). Do not put that number on a slide.

From the course folder, the check prints `passed`:

```text
cd problem_simulation
python -m alwaha.check deploy --release rel-m02-l04 --work "../Module 02/Lesson 04/Solution_Copy/work" --profile practice
```

The deploy demo, from the same folder, prints two lines and nothing else:

```text
cd problem_simulation
python -m alwaha.demo.deploy --profile practice
```

```text
root image: rejected
registered image: accepted
```

The lines do not print a hash, a token, the quota, a national id, or the watermark. The admission test uses the stand-in `NID-sample`. The demo does not.

## Block 1 — The sprint

Open [chapter 02](02-the-sprint.md) beside their `sprint.md`.

The deploy sentence is above the readout sentence. The check says `sprint.md does not book the readout after the deploy` when the readout comes first, or when one of the two ideas is missing. It does not print the words it looked for.

## Block 2 — The image

Open [chapter 03](03-the-image.md) beside their admission files and the Dockerfile.

Root and `0` are rejected. A clean account is accepted. The national id leaves the emitted log. The Dockerfile ends on `USER 1000`. The word `root` can remain on the rejection line. The check says `the image runs as root` or `a national id is in the deploy log`. It does not name the id.

## Block 3 — The probe

Open [chapter 04](04-the-probe.md) beside their health files and the manifest.

The approved `local-small` row supplies the hash and the prompt. The candidate argument stays on the function line and is not used. The manifest is in `ns-team`, refuses a root account, and calls `/v1/health`. The check says `the health probe does not report the registered hash` when the shell hash is still in place. It does not name the hash.

## Block 4 — The endpoint

Open [chapter 05](05-the-endpoint.md) beside their router, credentials, and workflow.

The route is `ep-local-small`, `local-small`, and `zone-private` for prod and for dev. Prod reads `prod.json`. The work workflow runs the suite. The packet workflow does not. The check says `the router leaves the private endpoint`, `prod uses the dev credential`, or `the pipeline is not in CI`. It does not name a token.

## Block 5 — The zone row

The columns are `surface` and `zone`. The row is `url` and `zone-private`. The check says `the url is not in zone-private` when the row is missing. Keep the pipes.

## Block 6 — The operator steps

The steps name the health probe and the prod credential. The check says `the operator steps are missing` when either word is absent.

## Block 7 — The deployment note

Open [chapter 06](06-the-pages.md) beside their `deployment.md`.

The headings are URL, Zone, Probe, Credentials, Monitoring, Boundary, and Operator steps. Boundary leaves urgency with a clinician and keeps patient data off `ext-large`. Monitoring names Module 2. The page cites `endpoint/guide.md` and names `pol-deploy`. It says the container user is non-root. It does not say the container runs as root. The check says the note is missing a required fact, does not cite a source, or contains a banned sentence. The missing-fact message does not name the fact.

## Block 8 — Knowledge

Line 1 names `zone-private`. Line 2 says a rollback changes the model hash. The check looks for those ideas. It does not print a model answer.

## Block 9 — The notes the check skips

The four notes and the interview are in this folder. Students were not asked to write them. A copy of the deploy log in `work/` fails with `a watermarked sample is in the work directory`. The message does not print the watermark.

## Close

The check prints `passed` on the finished `work/` in this folder. Booking from chat still waits.
