# 2 — Enterprise problem

## The three parties

| Party | Owns | Must not own |
| --- | --- | --- |
| Al-Waha cluster | The hospital record, the clinician’s urgency, the nightly file at Ain | The patient’s login, the payer’s eligibility decision |
| National Desk | The signed-in channel, public leaflets, reminders that carry no national id | Clinical urgency, the hospital record |
| Coverage Partner | A yes, a no, or a timeout on coverage | The slot, the referral text, the assistant’s reply |

The student works for the cluster. A vendor release, `assistant-0.9`, is already connected to the Desk and is already answering.

## The collapse

Each party has a clock that is true for that party.

| Clock | Log | Starts when |
| --- | --- | --- |
| Request | `log_channel` | The person asked |
| Receipt | `log_hospital` | The referral was accepted into the record |
| Coverage | `log_payer` | Eligibility was answered |

`assistant-0.9` publishes one number called wait. The warehouse can recompute it. The recomputation matches the receipt clock. The screen talks to the patient as if the number were time since they asked. Auditors who only recompute the warehouse will bless it.

Each party also has a decision.

| Decision | Who may write it |
| --- | --- |
| `dec-clinical` | A clinician |
| `dec-route` | Desk rules. Emergency wording and any return go to a person |
| `dec-accept` | The Desk, when it accepts the request. This starts the patient wait. It does not book |
| `dec-cover` | The payer |
| `dec-slot` | The hospital file. A sentence in the channel log is not a slot |

`assistant-0.9` stores one field called urgency. The sponsor has asked the assistant to “handle urgency.” A disclaimer does not split the field.

## Other failures already in the running system

These are consequences of the same habit: treating a locally valid artifact as the authority.

- A schema-valid tool call books a slot. The approval id was copied out of a referral letter by a component allowed to read the letter.
- A reminder is sent twice, or a cancel in a file and a cancel on a queue are treated as two events.
- An answer quotes a passage exactly. The passage was scored before the audience filter, or the body changed under a familiar version id.
- A judge agrees with a file because the label was on the row it scored. A small comparison looks like a win and does not clear a pre-registered bar.
- CPU is flat and latency is inside the line. The phone quotes yesterday’s hours.
- A cloud call succeeds in a nearby region. The processor record is elsewhere, or the bytes were restricted. A quotation is restricted in the same illustrative sense as a health file and a national id. Changing the story from a clinic to a tender does not change the class.

## People who disagree

The medical director wants the assistant to grade urgency. The safety rule says a clinician does. The protection officer will not release the letter corpus the sponsor has already described. The contact center wants containment. Abandoned calls and emergency wording are not containment. Finance prefers the external model because a spreadsheet says it is cheaper today. The Desk wants one front door before a holiday. The cluster will not confirm a slot the nightly file has not released.

Interviews return claims. Gold marks which sentences are claims. A binding that promotes a claim to a record fails.

## What “stop” means

Refusing `dec-clinical` ends that feature. The access workflow is a different build. Later investigations are that build. A chapter that calls the refusal a stop and then continues the same feature has planted the sentence.

## Why this problem and not another industry

A procurement desk and a permit office were examined. Their work objects sit in the same illustrative restricted tier as a health file: quotations, bid files, identity on an application. Moving industry does not make a student account a safe host. The clinical owner is the decision this audience most needs to refuse. The cloud lesson is identical either way: class the bytes, then decide whether they may leave the laptop.
