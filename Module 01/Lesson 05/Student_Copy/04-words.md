# 04 — Words

Read this page once. You will look back at it while you read the pack and replace the agent. You do not need to memorize it.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself.

## The service

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Referral | A request from a local clinic for a hospital appointment. The patient asks where it is, or asks to book from it |
| Patient | The person the referral is about. A patient turn is a line in the scenario whose role is `patient` |
| Coordinator | The staff member who decides an approval. A coordinator turn carries the decision and the approval id. [Maha Al-Shammari](packet/kickoff/personas/coord-lead.md) leads that queue |
| Medical director | The clinician who sent the rules. [Dr. Faisal Al-Otaibi](packet/kickoff/personas/med-dir.md). Clinicians own urgency. The assistant does not grade it |
| Chief digital officer | [Layla Al-Harbi](packet/kickoff/personas/cdo.md). Her id is `cdo`. The deadline section of the readout cites her |
| Data protection officer | [Sara Al-Mutairi](packet/kickoff/personas/dpo.md). Her id is `dpo`. The data section of the readout cites her |
| Enterprise architect | [Huda Al-Ghamdi](packet/kickoff/personas/ea.md). Her id is `ea`. She will not promise a live slot where none exists |
| Steering committee | The group that sent today's questions. The questions are in [steer-m01.md](packet/release/steering/steer-m01.md) |
| Ramadan | The season the sponsor wants the front desk live before. The wish is a claim until a file supports it |
| Clinician | A person who assigns clinical urgency. The assistant does not |
| Triage | Setting clinical urgency. The problem id is `p-triage` on [problems.md](packet/carried/problems.md). This proof will not build it |
| Clinical urgency | How urgent a visit is. [med-dir.md](packet/kickoff/personas/med-dir.md) says a clinician decides every one |

## The agent

| Word | Meaning |
| --- | --- |
| `wf-intake` | The Lesson 3 workflow. It runs from `referral.submitted` to a held approval. It does not book |
| `wf-self-service` | The workflow you leave running today. A patient can ask for status and book a slot. A return cannot leave without a coordinator |
| Tool | One action the agent may call. The catalog is [mcp-cluster.json](packet/m01-l04/tools/mcp-cluster.json). The mock is [tools.py](packet/agent/tools.py). You read that file. You do not edit it |
| `mcp-cluster` | The name of the tool server in the catalog. The six tools below are that server's list |
| `referral.status` | A read. It returns the queue count for one referral. The reply count has to be that result |
| `referral.return` | A write. It sends a return. It waits for an approval id. Today's rows do not call it |
| `slots.offer` | A read. It lists a slot, returns a constraint, times out, or says the slot is taken |
| `slots.book` | A write. It books a slot. It runs only after the patient confirms and a coordinator approves. It does not run twice for one slot |
| `sms.send` | A write that sends the SMS after the booking |
| `safety.redirect` | A write that hands the conversation to a person. It does not book |
| Schema | The shape of one reply and one trace row. The fields live in [schema.py](packet/agent/schema.py). Chapter 06 replaces the copy under `work/` |
| Intent | The short name on the reply, such as `status`, `book`, `return`, `emergency`, or `refusal` |
| Memory | Facts kept for one session. [memory.py](packet/agent/memory.py) is the store. A later turn in the same session can recall them |
| Session | The id that groups turns the memory may reuse. A different session does not see those facts |
| Approval | The coordinator's decision. The id is on the coordinator turn while they are deciding, and on the write after they have decided |
| Pending | An approval id that is still waiting. A return that has not been decided sits here. It is not sent |
| Redirect | The handoff when a turn matches the routing list. The visit is not booked. The trace cites `safety.redirect` and `pol-clinical-safety` |
| Trace | The list of rows the runner writes. One row per scenario. The checks run the agent again, so a trace you typed by hand is not the one they grade |
| Citation | A tool name or a document id on the row, or in a design cell, naming what you relied on |
| `tool_trace` | The tool names in the order they were called |
| `failure` | A field on the trace row. `timeout` and `race-slot` write their names there. Other rows leave it empty |
| Scenario | The name of one case, such as `status` or `timeout`. The check names the case when a row is wrong. It does not print the count, the slot, or an interview sentence |
| Timeout | The offer did not return. The agent does not book. The row's `failure` is `timeout` |
| `race-slot` | Two patients are offered one slot. One booking is kept. The row's `failure` is `race-slot` |
| Replay | The same approval id arriving again. [pol-approval.md](packet/m01-l04/policy/pol-approval.md) says replaying an approval id changes nothing |
| Injection | A letter that tells the agent to ignore the policy and book. The letter is data. The turn is the question |
| Refusal | What the patient sees when the visit does not proceed. The row sets `refusal_logged` when that happens |
| Consent | Permission to reuse a stored preference in a later session. The scenario field is `consent` |
| Preference | A stored wish from an earlier session. If consent does not allow it, the string stays out of the trace |
| Constraint | A limit on a slot. When the scenario names one, the offer tool returns it, the reply names it, and nothing is booked |
| Watermark | A marker planted in a file so a copy can be recognized. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says it stays out of prompts, tickets, and the work you submit |
| Mock | A stand-in that pretends to be the hospital tools. [tools.py](packet/agent/tools.py) is the mock |

## The routing list

[pol-clinical-safety.md](packet/m01-l04/policy/pol-clinical-safety.md) is the routing list. The document id is `pol-clinical-safety`. Its status is in force. Matching a phrase creates a handoff to a human. It does not create an urgency grade, a diagnosis, or a referral decision.

The phrases on that page are:

- chest pain
- cannot breathe

A turn that contains either phrase is a redirect, even when the same turn also asks for a slot. The emergency scenario is that case. The trace note in chapter 08 is about that row.

## The diagram and the design

| Word | Meaning |
| --- | --- |
| Architecture | The picture of the two workflows, the zones, and the tools. The file is `architecture.md` |
| Diagram | The drawing inside the architecture page. It needs a human step. The word coordinator is that step |
| Human step | A person in the path. A return and a booking wait for the coordinator |
| Zone | Where a system runs. [zones.md](packet/kickoff/world/zones.md) names `zone-hospital`, `zone-private`, and `zone-public` |
| `zone-public` | The public cloud. [zones.md](packet/kickoff/world/zones.md) names it `ext-large` |
| `ext-large` | The external model in the public cloud. Patient data for this proof stays off it |
| Private cloud | `zone-private`. Patient data for this proof stays here |
| Residency | Where patient data sits. The stage 2 row uses this topic |
| Design | The page that names the approach and what this proof will not build. The file is `design.md` |
| Approach | Which problems this proof touches, and which need no model |
| `p-status` | Patients ask where a referral stands. [problems.md](packet/carried/problems.md). An assistant with a status tool |
| `p-clock` | The board's wait chart. It needs no model |
| `p-slots` | Sessions go out with empty chairs. It needs no model |
| `p-waitlist` | Waitlist rows the coordinators do not trust. [problems.md](packet/carried/problems.md) says that and does not say duplicate or split. [Chapter 07](07-the-diagram.md) calls the open item a split identity: duplicate rows, and one person stored as two |
| `p-triage` | The sponsor wants the assistant to set clinical urgency. This proof will not build it |
| Stage 2 | The table of what is still open. The columns are `topic`, `what is still open`, and `citation` |
| Identity | The stage 2 topic for the waitlist. The open item is duplicate rows and a split identity. The register names `p-waitlist` and does not say duplicate or split. The paste cites that register. [ea.md](packet/kickoff/personas/ea.md) supports the hospital row, where `h-ain` has no slot API. The check looks for `p-waitlist`, `split`, or `duplicate` in the identity cell |
| Criteria | The rules for a specialty. [crit-endo-v4.md](packet/carried/criteria/crit-endo-v4.md) is `crit-endo-v4`. Its status is draft |
| Draft | A document that is not in force. The v4 criteria are still a draft |

## The readout

| Word | Meaning |
| --- | --- |
| Readout | The page that answers the steering questions. The file is `readout.md` |
| Deadline | The heading for the board date. It cites `cdo` |
| Data | The heading for where patient data sits. It cites `dpo` |
| Failure | The heading that names `timeout` or `race-slot`, and cites a document or a person |
| Gate | A stage-gate id. [pol-stage-gate.md](packet/kickoff/corpus/pol-stage-gate.md) lists G0 through G5. The document id is `pol-stage-gate` |
| `G2` | The DPIA gate. The personal-data assessment is accepted when this gate passes. It is still open |
| DPIA | The personal-data assessment named on G2 |
| Will not build | The heading that says a clinician assigns clinical urgency |
| Asks | The ask log. The open items the lead writes. It must not promise triage |
| Stage gate | An approval the cluster requires before the next step, not a meeting |

## The trace note

| Word | Meaning |
| --- | --- |
| Trace note | Your note for one scenario. The file is `trace-note.md`. It is not the diagram |
| Emergency | The scenario whose turn matches the routing list. The note is for this row |
| Tool | The heading for the tool that row called. For emergency that is `safety.redirect` |
| Document | The heading for the document that row cited. For emergency that is `pol-clinical-safety` |
| Refused | The heading that says the visit was refused. The word `yes` matches |

## The hospitals

[zones.md](packet/kickoff/world/zones.md) is the map. Today's booking scenarios carry `h-wadi`. [pol-sla.md](packet/carried/policy/pol-sla.md) says `h-ain` has no slot API.

| Id | Meaning |
| --- | --- |
| `h-wadi` | Wadi Specialist Hospital, in `zone-private` |
| `h-ain` | Ain Diabetes and Eye Center, in `zone-hospital`. No live slot API in this release |

You have the words the later chapters use.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The reading](05-the-reading.md).
