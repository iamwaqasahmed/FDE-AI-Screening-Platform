# 05 — The reading

[Chapter 04](04-words.md) defined the words. This chapter is the reading. Open the files in this order. You do not create or edit a file here. Read the page, or search it, then go to the next number.

Do not copy a scenario file into `work/`. Do not paste a scenario line into a prompt.

## 1. The steering questions

Open [steer-m01.md](packet/release/steering/steer-m01.md).

There are five questions. You will answer them in [chapter 08](08-the-readout.md). This page only names the questions.

Three answers are not on this page:

- How many weeks the purchase takes. Layla Al-Harbi's card does not say it either. Chapter 08 asks her, with the interview command, before you paste the deadline. Listen for the number of weeks in her second answer.
- A statement that a gate has already passed. None has. [Chapter 04](04-words.md) said G2 is still open. Section 9 of this chapter shows the gate list. The words "is accepted" say what G2 does when it passes. It has not passed.
- Where patient data sits. That is on the zones page in section 8, and on Sara Al-Mutairi's card in section 13.

The trace does not contain the weeks or the gate.

## 2. The approval policy

Open [pol-approval.md](packet/m01-l04/policy/pol-approval.md).

A booking waits for the patient's confirmation and a coordinator's decision, then an SMS. A return is not sent until a coordinator decides. A letter is data. Status comes from the status tool. Replaying an approval id changes nothing. Emergency wording redirects and does not book.

The Thursday sentence is on that page. None of today's checks scores it. You do not build a Thursday path.

## 3. The routing list

Open [pol-clinical-safety.md](packet/m01-l04/policy/pol-clinical-safety.md).

Search for `phrases:`. The two phrases are chest pain and cannot breathe. A match is a handoff. The document id is `pol-clinical-safety`.

## 4. The tool catalog

Open [mcp-cluster.json](packet/m01-l04/tools/mcp-cluster.json).

The six names are `referral.status`, `referral.return`, `slots.offer`, `slots.book`, `sms.send`, and `safety.redirect`. `referral.return` and `slots.book` have `approval` true. The others do not.

## 5. Yesterday's order

Open [order.json](packet/m01-l04/scenarios/order.json).

The names, in order, are `status`, `book`, `return`, `emergency`, `injection`, `replay`, `resume`, `reject`, `memory`, `consent`, and `reason`. The agent still has to pass every one.

## 6. Yesterday's scenarios

Open these three files and search with Ctrl+F. On Windows that is Ctrl+F. On macOS it is Command+F. Search for the scenario name, read that row, and close the file. Do not copy the row.

- [ds-agent.jsonl](packet/m01-l04/scenarios/ds-agent.jsonl). Search `status`, `book`, `return`, `emergency`, `injection`, `replay`, `resume`, and `reject`. Those eight names are in this file. `replay`, `resume`, and `reject` are not in the sessions file. One letter in this file carries a watermark. Read it where it sits. Leave it there.
- [ds-sessions.jsonl](packet/m01-l04/scenarios/ds-sessions.jsonl). Search `memory` and `consent`. Those two names are the whole file. A search here for `replay` finds nothing. That name is in the agent file.
- [ds-reason.jsonl](packet/m01-l04/scenarios/ds-reason.jsonl). Search `reason`.

`emergency` is the row whose turn matches the routing list. You will write the trace note for that scenario. `injection` is the letter that tells the agent to book. The letter is data. The turn is the question.

## 7. Today's two cases

Open [order.json](packet/release/scenarios/order.json). The names are `timeout` and `race-slot`.

Open [ds-failures.jsonl](packet/release/scenarios/ds-failures.jsonl). Search `timeout`, then search `race-slot`.

`timeout` asks to book, and the offer is the kind that does not return. The letter on that row is data. One letter in this file carries a watermark. Do not copy the letter. Do not copy the file into `work/`.

`race-slot` is two patients, each asking to book, each confirming, each with a coordinator approval. They are offered one slot. You do not copy the slot id into a note, a prompt, or `work/`.

## 8. The zones

Open [zones.md](packet/kickoff/world/zones.md).

The three zones are `zone-hospital`, `zone-private`, and `zone-public`. `zone-public` is `ext-large`. `h-wadi` is Wadi Specialist Hospital. `h-ain` is Ain Diabetes and Eye Center.

## 9. The stage gates

Open [pol-stage-gate.md](packet/kickoff/corpus/pol-stage-gate.md).

The document id is `pol-stage-gate`. The gates run from G0 to G5. G2 is the DPIA. The personal-data assessment is accepted at that gate. G3 says a clinician still assigns every clinical urgency.

## 10. The problem register

Open [problems.md](packet/carried/problems.md).

Search `p-status`, `p-clock`, `p-slots`, `p-waitlist`, and `p-triage`. `p-waitlist` is waitlist rows the coordinators do not trust. The file does not say duplicate, and it does not say one person stored as two. [Chapter 07](07-the-diagram.md) uses those words for the open item. The check looks for `p-waitlist`, `split`, or `duplicate` on that row. `p-triage` is the sponsor wanting the assistant to set clinical urgency.

## 11. The hospital with no slot API

Open [pol-sla.md](packet/carried/policy/pol-sla.md).

Search `h-ain`. That hospital has no slot API in this release. A hold or a booking there returns queued.

Open [ea.md](packet/kickoff/personas/ea.md). Huda Al-Ghamdi will not promise a live slot where none exists.

## 12. The draft criteria

Open [crit-endo-v4.md](packet/carried/criteria/crit-endo-v4.md).

The document id is `crit-endo-v4`. The status is draft. It is not in force.

## 13. The people the readout cites

Open the cards and read the first sentence of each.

- [cdo.md](packet/kickoff/personas/cdo.md). Layla Al-Harbi. The virtual front desk, including triage, goes live before Ramadan. That is the claim. It is not the deadline answer.
- [dpo.md](packet/kickoff/personas/dpo.md). Sara Al-Mutairi. Patient data needs care. Her goals keep patient data in the private cloud. The Asks sentence in [chapter 08](08-the-readout.md) says the ruling is still unsigned. That sentence is not on this card. It is the second answer from the Lesson 1 interview: an unsigned ruling says patient data stays off the external model ext-large, and training stays on the private cloud. If you still have `Module 01/Lesson 01/Student_Copy/work/interviews/dpo.notes.md`, that claim row is the same sentence. You do not interview her again today.
- [med-dir.md](packet/kickoff/personas/med-dir.md). A clinician decides every clinical urgency.

You have read the pack the agent uses, and the pages the design cites.

Next: [06 — The agent](06-the-agent.md).
