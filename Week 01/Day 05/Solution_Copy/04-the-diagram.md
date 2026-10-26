# 04 — The diagram

[architecture.md](work/architecture.md) is the picture. [design.md](work/design.md) is the approach and what this proof will not build. The check says `the design note is missing a required fact` and does not name the fact. This page names each one, and the file it comes from.

## The diagram

`referral.submitted` enters `wf-intake`, and `wf-intake` waits for the coordinator. The patient enters `wf-self-service`, which can call `referral.status` and can also wait for the coordinator. The coordinator is the human step. A return and a booking wait there, and the booking is `slots.book`.

The check says `the diagram has no human step` when the diagram section has none of the words coordinator, human, or approval.

The zones are `zone-hospital`, `zone-private`, and `zone-public`. They are the three lines in [zones.md](sources/kickoff/world/zones.md).

The tool line lists `referral.status`, `referral.return`, `slots.offer`, `slots.book`, `sms.send`, and `safety.redirect`. Those are the names in [mcp-cluster.json](sources/release/tools/mcp-cluster.json).

## The approach

[problems.md](sources/carried/problems.md) names the problems.

`p-status` is an assistant with a status tool. `p-clock` and `p-slots` need no model. `p-waitlist` is where identity still splits people. The citations are `cdo` and `pol-approval`.

## What this proof will not build

This proof will not build `p-triage`. A clinician assigns every clinical urgency. [med-dir.md](sources/kickoff/personas/med-dir.md) says clinicians own urgency. [pol-stage-gate.md](sources/kickoff/corpus/pol-stage-gate.md) says the same thing at G3.

The check says `the design does not leave urgency with a clinician` when that section is missing either word. A sentence that lets the assistant set clinical urgency fails as `design contains a banned sentence`. The message does not print the sentence.

## Stage 2

The table keeps the columns `topic`, `what is still open`, and `citation`.

| topic | what is still open | where it sits |
| --- | --- | --- |
| residency | Patient data stays off ext-large | [zones.md](sources/kickoff/world/zones.md) names `ext-large` on `zone-public`. The cell cites `dpo` |
| identity | Duplicate rows and a split identity on p-waitlist | [problems.md](sources/carried/problems.md) names `p-waitlist` and does not say duplicate or split. The cell cites that register. Duplicate and split are the open item, not a sentence from the register. [ea.md](sources/kickoff/personas/ea.md) supports the hospital row, not this one. The check looks for `p-waitlist`, `split`, or `duplicate`. It does not match the citation to her card |
| criteria | The v4 criteria are still a draft | [crit-endo-v4.md](sources/carried/criteria/crit-endo-v4.md) says draft. The cell cites `crit-endo-v4` |
| hospital | h-ain has no live slot API | [pol-sla.md](sources/carried/policy/pol-sla.md) says `h-ain` has no slot API. [ea.md](sources/kickoff/personas/ea.md) will not promise a live slot where none exists. The cell cites `ea` |

`pol-stage-gate` is also named on the design, so the page cites a document the check accepts.

Next: [05 — The readout](05-the-readout.md).
