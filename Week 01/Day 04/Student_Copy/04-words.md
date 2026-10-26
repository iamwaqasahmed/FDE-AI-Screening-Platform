# 04 — Words

Read this page once. You will look back at it while you read the rules and replace the agent. You do not need to memorize it.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself.

## The service

| Word | Meaning |
| --- | --- |
| Health cluster | A group of hospitals and primary care centers that plan and deliver care for one population. This client is the Al-Waha Health Cluster |
| Referral | A request from a local clinic for a hospital appointment. The patient asks where it is, or asks to book from it |
| Patient | The person the referral is about. A patient turn is a line in the scenario whose role is `patient` |
| Coordinator | The staff member who decides an approval. A coordinator turn carries the decision and the approval id. [Maha Al-Shammari](packet/kickoff/personas/coord-lead.md) leads that queue |
| Medical director | The clinician who sent today's rules. [Dr. Faisal Al-Otaibi](packet/kickoff/personas/med-dir.md). Clinicians own urgency. The assistant does not grade it |
| Specialty | One hospital service line. A letter in today's slice uses the word endocrinology |
| Endocrinology | Hormones and diabetes. The letter uses the word. The agent does not decide the specialty |
| Slot | One bookable appointment. [slots.offer](packet/release/tools/mcp-cluster.json) lists one, or names the constraint that blocks it. [slots.book](packet/release/tools/mcp-cluster.json) writes the booking |
| SMS | The text message sent after a booking. The tool is `sms.send`. It runs after the book, not before |
| Return | Sending a referral back. `referral.return` is the tool. [pol-approval.md](packet/release/policy/pol-approval.md) says it is not sent until a coordinator decides |
| Letter | The referral text. [pol-approval.md](packet/release/policy/pol-approval.md) says text inside a letter is data. It is not a tool call |

## The agent

| Word | Meaning |
| --- | --- |
| `wf-self-service` | The workflow you leave today. A patient can ask for status and book a slot. A return cannot leave without a coordinator |
| Tool | One action the agent may call. The catalog is [mcp-cluster.json](packet/release/tools/mcp-cluster.json). The mock that pretends to run them is [tools.py](packet/agent/tools.py). You read that file. You do not edit it |
| `mcp-cluster` | The name of the tool server in the catalog. The six tools below are that server's list |
| `referral.status` | A read. It returns the queue count for one referral. The reply count has to be that result. `approval` on this tool is false |
| `referral.return` | A write. It sends a return. `approval` is true, so it waits for an approval id. Today's rows do not call it |
| `slots.offer` | A read. It lists a slot, or it returns the constraint and an empty slot list. `approval` is false |
| `slots.book` | A write. It books a slot. `approval` is true. It runs only after the patient confirms and a coordinator approves |
| `sms.send` | A write that sends the SMS after the booking. `approval` is false. It still waits until the booking has happened |
| `safety.redirect` | A write that hands the conversation to a person. `approval` is false. It does not book |
| Schema | The shape of one reply and one trace row. The fields live in [schema.py](packet/agent/schema.py). Chapter 06 replaces the copy under `work/` |
| Intent | The short name on the reply, such as `status`, `book`, `return`, `emergency`, or `refusal` |
| Memory | Facts kept for one session. [memory.py](packet/agent/memory.py) is the store. A later turn in the same session can recall them |
| Session | The id that groups turns the memory may reuse. A different session does not see those facts |
| Approval | The coordinator's decision. The id is on the coordinator turn while they are deciding, and on the write after they have decided |
| Pending | An approval id that is still waiting. A return that has not been decided sits here. It is not sent |
| Redirect | The handoff when a turn matches the routing list. The visit is not booked. The trace cites `safety.redirect` and `pol-clinical-safety` |
| Trace | The list of rows the runner writes. One row per scenario. The checks run the agent again, so a trace you typed by hand is not the one they grade |
| Citation | A tool name or a document name on the row, naming what the row relied on |
| `tool_trace` | The tool names in the order they were called |
| Privilege boundary | The line between reading and writing. The extractor reads the letter. It does not hold the book tool or the message tool |
| Extractor | The part that reads a letter. A second agent is worth its tokens when that part would otherwise hold the book tool. Status stays one agent and one tool |
| Tokens | The spend of a second agent. You add one when a letter could book on its own. You do not add one for a status question |
| Mock | A stand-in that pretends to be the hospital tools. [tools.py](packet/agent/tools.py) is the mock |
| Scenario | The name of one case, such as `status` or `book`. The check names the case when a row is wrong. It does not print the count, the slot, or the clause |
| Replay | The same approval id arriving again. [pol-approval.md](packet/release/policy/pol-approval.md) says replaying an approval id changes nothing |
| Injection | A letter that tells the agent to ignore the policy and book. The letter is data. The turn is the question. Status still comes from the status tool |
| Refusal | What the patient sees when the visit does not proceed. The product sentence is in chapter 07. The row sets `refusal_logged` when that happens |
| Consent | Permission to reuse a stored preference in a later session. The scenario field is `consent` |
| Retention | How long a stored fact may be kept. The approval policy says a later session may reuse a preference only when consent and retention allow. No scenario today has a retention field. The graded case is `consent` set to false |
| Preference | A stored wish from an earlier session, such as a request to book the same way as last time. If consent does not allow it, the string stays out of the trace |
| Constraint | A limit on a slot. When the scenario names one, the offer tool returns it, the reply names it, and nothing is booked |
| Watermark | A marker planted in a file so a copy can be recognized. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts, tickets, and the work you submit. One letter in [ds-agent.jsonl](packet/release/scenarios/ds-agent.jsonl) carries one. Read it where it sits |

## The routing list

[pol-clinical-safety.md](packet/release/policy/pol-clinical-safety.md) is the routing list. The document id is `pol-clinical-safety`. Its status is in force. Matching a phrase creates a handoff to a human. It does not create an urgency grade, a diagnosis, or a referral decision.

The phrases on that page are:

- chest pain
- cannot breathe

A turn that contains either phrase is a redirect, even when the same turn also asks for a slot. No scenario today contains `cannot breathe`. The emergency row uses chest pain.

## The Thursday sentence

[pol-approval.md](packet/release/policy/pol-approval.md) says approvals on Thursday afternoon get rubber-stamped. That sentence is on the page. Neither of today's checks scores it. You do not build a Thursday path.

## The hospitals and the systems

[zones.md](packet/kickoff/world/zones.md) is the map. Today's scenarios carry `h-wadi`. The tool map in [tools.py](packet/agent/tools.py) also knows Ain.

| Id | Meaning |
| --- | --- |
| `h-nakhl` | Nakhl General Hospital, in `zone-hospital` |
| `h-safra` | Safra General Hospital, in `zone-hospital` |
| `h-wadi` | Wadi Specialist Hospital, in `zone-private`. A turn that says Wadi Specialist Hospital uses this id |
| `h-ain` | Ain Diabetes and Eye Center, in `zone-hospital`. A turn that says Ain Diabetes and Eye Center uses this id |
| `phc-nakhl-01` | Nakhl Central PHC, a primary health care center |
| `phc-safra-03` | Safra South PHC, a primary health care center |
| `phc-wadi-02` | Wadi Family PHC, a primary health care center |
| `phc-rim` | Rim Village PHC, a primary health care center. A reason turn can mention Rim. The constraint on that case is not this id |
| `zone-hospital` | Hospital data centers |
| `zone-private` | The private cloud. `h-wadi` sits here |
| `zone-public` | The public cloud |

You have the words the later chapters use.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The rules](05-the-rules.md).
