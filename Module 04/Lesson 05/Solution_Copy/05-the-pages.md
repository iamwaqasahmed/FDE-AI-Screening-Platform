# 05 — The pages

The suite does not read these pages. The checks do.

## Deployment architecture

An empty page makes the ops check say `the deployment architecture misses a required section`. The message does not name the section.

[architecture-deploy.md](work/architecture-deploy.md) keeps Zones, Flows, and Boundary. Zones names zone-private, zone-hospital, and zone-public. Flows names cc, bi, hr, and the bus. Boundary names a clinician and urgency.

## Operations plan

An empty page makes the ops check say three lines: `the operations plan misses an owner`, then `the operations plan leaves the clinical safety cell empty`, then `the operations plan skips G4`. That three-line miss is the empty page. It is not the two-line gates miss.

[operations.md](work/operations.md) keeps Owners, RACI, Gate, and Incident. RACI names `med-dir`. Gate names G4 and the checklist. Owners and Incident each have a line.

## Proposal

[proposal.md](work/rcp/proposal.md) keeps Client, Ranking, Roadmap, Plan, Metrics, and Adoption. Client names Al-Waha. Ranking says the dot-vote is not the value model and names a dependency: `p-waitlist` depends on identity. Roadmap starts with `p-clock`, not `p-triage`. Plan says the two savings count the same calls. Metrics names site-b and `p-status`. Metrics does not contain the digits 70. Adoption names phone-only, `phc-rim`, and the readiness survey. [readiness.json](sources/release/survey/readiness.json) names that group and that site. Do not copy a count.

A ranking that follows the dot-vote, a missing dependency, a roadmap that starts with `p-triage`, unmeasured metrics, a missing phone-only channel, a client that is not Al-Waha, or two savings treated as separate, fails `chk-m04-l05-rcp`.

## Readout and retro

[readout.md](work/readout.md) keeps Ranking, Handoff, Leave, Benefit, Channel, and Asks. Ranking names `p-clock` and identity. Handoff says a handoff needs a summary. Leave names `session.cancelled`. Benefit says the two savings count the same calls. Channel names phone-only and `phc-rim`. Asks names access-mgr and finance, leaves urgency with a clinician, and keeps patient data off `ext-large`. [steer-m04-l05.md](sources/release/steering/steer-m04-l05.md) is the question list. The demo prints `Which benefit is counted twice?` It does not say which two lines count the same calls.

An empty readout is the long list: urgency, the external model, the first problem's dependency, the handoff summary, `session.cancelled`, the double-counted benefit, the phone-only channel, the ask log, and a cite. Do not shorten that list.

[retro.md](work/retro.md) keeps Keep, Drop, and Open. Drop names a roadmap that starts with triage.

## Notes

Notes that miss the word summary make the integrate check say `the access-mgr notes miss the summary`. Notes that miss leave, `session.cancelled`, or bi make it say `the ea notes miss late leave`.

[access-mgr.notes.md](work/interviews/access-mgr.notes.md) names the summary. [ea.notes.md](work/interviews/ea.notes.md) names leave, `session.cancelled`, and bi. Keep the pipes. [access-mgr.questions.txt](work/interviews/access-mgr.questions.txt) and [ea.questions.txt](work/interviews/ea.questions.txt) are not the graded notes.

A page miss stays on the check that reads that page. An architecture miss or an operations miss fails `chk-m04-l05-ops`. A proposal miss fails `chk-m04-l05-rcp`. A readout miss, a retro miss, or a knowledge miss fails `chk-readout`. A notes miss fails `chk-m04-l05-integrate`.

Next: [06 — Knowledge](06-knowledge.md).
