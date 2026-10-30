# 05 — The readout

[readout.md](work/readout.md) answers [steer-m01.md](sources/release/steering/steer-m01.md). [trace-note.md](work/trace-note.md) is the emergency row. The checks do not print the lead time, and they do not print the document id.

## Deadline

The board has named a date just before Ramadan. That date assumes a purchase that takes 16 weeks. The citation is `cdo`.

[cdo.md](sources/kickoff/personas/cdo.md) says the virtual front desk, including triage, goes live before Ramadan. That sentence is a claim. It is not this answer. The demo that prints the claim does not print the lead time. The morning chapter asks her before the paste. The second answer is a GPU purchase that takes 16 weeks. No kickoff file contains that number, so the interview note marks it as a claim. The readout cites `cdo` because she said it. The check says `the readout does not answer the deadline` and does not print the number of weeks.

[cdo.notes.md](work/interviews/cdo.notes.md) is the longer note. You were not asked to write it. The checks do not read it.

## Data

Patient data stays off the external model `ext-large` and on the private cloud. The citation is `dpo`.

[zones.md](sources/kickoff/world/zones.md) puts `ext-large` in `zone-public`. [dpo.md](sources/kickoff/personas/dpo.md) keeps patient data in the private cloud. The check says `the readout does not say where patient data sits` and does not name the missing words.

[dpo.notes.md](work/interviews/dpo.notes.md) is the longer note. You were not asked to write it. The checks do not read it.

## Failure

The timeout did not book. `race-slot` kept a single booking. The citation is `pol-approval`.

Those are the two rows in [chapter 02](02-the-score.md). The check says `the readout does not name a failure` when neither name is in the section, and `the readout does not cite the failure` when no person or document is cited.

## Gate

G2 is still open. The citation is `pol-stage-gate`.

[pol-stage-gate.md](sources/kickoff/corpus/pol-stage-gate.md) lists G0 through G5. G2 is the DPIA. The personal-data assessment is accepted when that gate passes. The check accepts a gate id from G1 through G5, then requires the document id. The finished sentence is G2.

## Will not build

This proof will not build triage. A clinician assigns clinical urgency.

That matches the design. The check says `the readout does not say what it will not build` when the word clinician is missing.

## Asks

The deadline is open until the purchase is real. The ruling is open until it is signed. Neither ask adds triage to this proof.

The check says `the ask log is missing` when the section is empty, and `the ask log promises triage` when `p-triage` is there without the word not.

## The trace note

The note is for `emergency`. It is not the diagram.

| Heading | What the finished note says | Where it sits on the trace |
| --- | --- | --- |
| Scenario | emergency | the `scenario` field |
| Tool | `safety.redirect` | `tool_trace` |
| Document | `pol-clinical-safety` | `citations` |
| Refused | yes | `refusal_logged` is true |

The check says `the trace note does not name the document` and does not print the document id. [pol-clinical-safety.md](sources/release/policy/pol-clinical-safety.md) is that document. The phrases are chest pain and cannot breathe.

Next: [06 — Knowledge](06-knowledge.md).
