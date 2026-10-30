# Security and governance research

Design notes for a self-paced forward-deployed engineer (FDE) strand. The setting is the fictional Al-Waha Health Cluster. Cluster policies in the course (`pol-stage-gate`, `pol-deploy`, the PDS-analogue, the NCC-analogue, the 72-hour teaching clock) are case rules. They are not Saudi law, not an ISO certificate, and not an OWASP compliance claim.

This folder does not change course files. It says what a later strand can teach on top of Module 4 Lesson 1, which controls are settled enough to grade, and which topics are past this audience.

## What the course already teaches

Module 4 Lesson 1 ("Guardrails and the DPIA") already has the learner turn on guardrails, close stale access, fill a five-heading DPIA, and handle one access request and one deletion request. The hidden set must not move a booking, a canary, or an approval. A suite that only tests direct injection fails. Deleting the database row and leaving the vector index fails.

Zones the learner already meets, from the systems note and the hidden-world site table:

| Zone | What sits there | Teaching constraint |
| --- | --- | --- |
| `zone-hospital` | Nakhl, Safra, Ain; HL7 feeds and the nightly slot file | Local codes, delayed files, PHI in the source systems |
| `zone-private` | Wadi, `site-a` and `site-b`, referrals, consent, IAM, the assistant | Default home for PHI and for the model that may see it |
| `zone-public` | `ext-large` | Public corpus only. PHI stays off this zone |
| Community | PHCs, including the distant `phc-rim` | Templates and travel context, not a second hospital record |
| National | `nid` read API | Strong auth. Identifiers are not copied into prompts |
| Partner | SMS, WhatsApp, insurance | A booking fact may cross. A national id does not |

Catalog classes are `public`, `internal`, and `phi`. National id, date of birth, name, and phone are `phi`. Clinic hours and public leaflets are `public`. `phi` is a cluster label. It is not the statutory category "Sensitive Data" or "Health Data."

Attack-family ids in the lesson (`atk-direct` through `atk-hoard`) are a teaching map onto the OWASP Top 10 for LLM Applications, 2025 edition. The map is a bridge. It is not a finding that the cluster "meets OWASP."

## How to use these notes

1. Read [01-control-catalog.md](01-control-catalog.md) for controls, maturity, and where sources disagree.
2. Read [02-what-to-teach-hands-on.md](02-what-to-teach-hands-on.md) before adding a lab. Several candidates are already graded in Module 4 Lesson 1. The strand should extend them, not restage them.
3. Read [03-governance-artifacts.md](03-governance-artifacts.md) for the pages a learner should leave behind.
4. Read [04-sources.md](04-sources.md) before citing a framework in learner-facing text.

## Maturity labels

- **Proven.** Widely taught, graded in ordinary security or privacy practice, and stable enough for a pass/fail check.
- **Emerging.** Accepted direction in current guidance, with the exact control still changing. Grade the decision and the residual risk, not a vendor product.
- **Experimental.** Research, a single-vendor pattern, or a claim that current primary sources do not treat as settled. Name it. Do not grade it as the control that makes the assistant safe.

## Safety limit

Labs stay on architecture and governance: allowlists, zone rules, redaction, deletion maps, purpose checks, and an evaluation where a guardrail is allowed to miss. Do not add exploit strings, jailbreak collections, filter-bypass recipes, or attack procedures. The course's own dev file already labels families. New labs should reuse those labels.

## Audience limit

The learner is one FDE who also runs the pipeline, the workflow, the readout, and the handover. The strand is not a CISO course, a penetration-test course, a law clinic, or an ISO audit engagement.
