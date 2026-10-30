# 04 — The memo

Open [approach.md](work/approach.md) and [brief.md](work/brief.md). This page says why each row is filled the way it is. Another ranking order can pass. A reason can use different words when the family, the measurement, and the citation stay the same.

## Approach

| id | Family | Measured | Why |
| --- | --- | --- | --- |
| `p-bounce` | `extract+retrieve` | `filled 5` | The specialty is a field in the letter, cited as `samples/ds-letters.md`. A return still has to name the clause that is in force. The system is the referral letters |
| `p-waitlist` | `no-model` | `claim 510000` | Untrusted rows are a matching rule. 510000 SAR is the director's figure for returned referrals in [access-costs.md](sources/release/extracts/access-costs.md). It is not a count of those rows. `p-bounce` already uses `filled 5`, so this money figure cannot go there. It is a claim. The system is the waitlist |
| `p-dna` | `classical-ml` | `person 0.0000` | A table with a label. The citation is `samples/ds-dna.csv`. The system is the appointment list |
| `p-status` | `agent` | `keyword 0.3125` | Status has to be a tool call against the referral record. The citation is `samples/ds-messages.csv` |
| `p-slots` | `no-model` | `claim 230000` | Empty chairs are a workflow on the session book. 230000 SAR is the director's figure for empty sessions, and it is a claim. Adding a model word beside `no-model` makes the family fail |
| `p-clock` | `no-model` | `claim 14` | [dashboard.md](sources/release/extracts/dashboard.md) names `booking_date`. The fix is the query on the wait-time mart. 14 days is the board's median, and it is a claim |
| `p-info` | `retrieve` | `claim 430` | Hours, preparation, and documents are a document in force for that reader. 430 calls is the director's figure. The system is the clinic documents |
| `p-forecast` | `forecast` | `seasonal 2.1667` | The citation is `samples/ds-demand.csv`. The system is the monthly session volumes |
| `p-triage` | `blocked` | `claim 3000000` | [sponsor-ask.md](sources/release/extracts/sponsor-ask.md) asks the assistant to set clinical urgency and claims 3000000 SAR a year. [pol-stage-gate.md](sources/kickoff/corpus/pol-stage-gate.md) says a clinician assigns urgency. The system is the clinician. The family cell is only `blocked` |

`## Tools` names the same boundary: the clock is a query, slots are a workflow, status is a tool, and clinical urgency is not a model call. The check does not read that section.

`## Cost` counts 84 words in the letter file. A word is a run of characters with spaces around it, and the headings count. At the price sheet, 84 / 1000 × 20 = 1.68 SAR on `ext-large`, and 84 / 1000 × 3 = 0.252 SAR on `local-small`. The letters are watermarked, so this is a count on the file, not a call. The check does not read it. [zones.md](sources/kickoff/world/zones.md) is where `ext-large` is named. The prices are in [prices.csv](sources/release/finance/prices.csv).

`## Overlap` names letter-01 and letter-06. They share the same three sentences. letter-06 adds a watermark line. The line is not copied here.

## Brief

The claims table in [brief.md](work/brief.md) keeps leader sentences in rows marked `claim`, and two facts: the column `booking_date`, and that a clinician assigns urgency.

The sizes use the four baseline numbers as `measured`, and the five leader figures as `claim`, each with the pack path of the file that contains the digits.

The ranking in this example is one order that passes:

1. `p-clock`, because the column has to be right before any other number is used as a baseline.
2. `p-info`, because the answers are documents.
3. `p-bounce`, the letter field plus the clause in force.
4. `p-slots`, a workflow.
5. `p-waitlist`, a matching rule.
6. `p-status`, a tool.
7. `p-dna`, the person line.
8. `p-forecast`, the seasonal line.
9. `p-triage`, with the words that a clinician assigns urgency, and the 3000000 SAR left as a claim.

Any order of the nine ids passes. If `p-triage` is the first line, that same line has to say that a clinician assigns urgency.

Next: [05 — Knowledge](05-knowledge.md).
