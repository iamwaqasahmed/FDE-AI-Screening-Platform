# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check integrate --release rel-w4d5 --work "..\Week 04\Day 05\work"
python -m alwaha.check ops --release rel-w4d5 --work "..\Week 04\Day 05\work"
python -m alwaha.check rcp --release rel-w4d5 --work "..\Week 04\Day 05\work"
python -m alwaha.check readout --release rel-w4d5 --work "..\Week 04\Day 05\work"
python -m alwaha.check individual --release rel-w4d5 --work "..\Week 04\Day 05\work"
```

`chk-w4-integrate` scores sign-in, the bus, the handoff, late leave, the warehouse clock, the sprint order, and both interviews. A miss says staff sign-in rejects a staff role, a service token is accepted as staff, the bus drops an event with an unknown field, the bus misses session.cancelled, the handoff has no summary, late leave leaves the session published, leave does not emit session.cancelled, the warehouse clock starts at booking, sprint.md does not open the requests first, the access-mgr notes miss the summary, or the ea notes miss late leave.

`chk-w4-ops` scores the deployment architecture, the operations plan, and the gate record. A miss says the deployment architecture misses a required section, the operations plan misses an owner, the operations plan leaves the clinical safety cell empty, or the operations plan skips G4.

`chk-w4-rcp` scores the ranking function and `rcp/proposal.md`. A miss says the roadmap starts with p-triage, the ranking follows the dot-vote, the proposal misses a dependency, success metrics were not measured, the adoption plan misses the phone-only channel, the proposal's client is not Al-Waha, or the proposal treats the two savings as separate.

`chk-readout` reads `readout.md`, `retro.md`, and `knowledge.md` against `steer-w4`. A miss says the readout does not name the first problem's dependency, does not say the handoff needs a summary, does not name session.cancelled, does not answer the double-counted benefit, does not name a phone-only channel, does not leave urgency with a clinician, or does not keep patient data off the external model. It also says knowledge.md does not say which event leave creates, or knowledge.md does not name a first problem and a dependency.

`chk-individual-w4` is the personal lab. A miss says the guardrail lets the attack book.

A miss does not print a lag, a survey count, a SAR figure, a hash, or the attack text.

A watermarked file copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can play the finance question:

```text
python -m alwaha.demo.benefit --profile practice
```

The line is the steering question about the double-counted benefit. It does not say which two lines count the same calls.

Then write `work/knowledge.md` from [templates/knowledge.md](templates/knowledge.md), with two short answers:

1. Which event should a new consultant leave create?
2. Which problem is first in your ranking, and which dependency does it have?

The day is done when all five checks print `passed` and the knowledge file has both answers.
