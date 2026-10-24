# Approach

The measured cells for the four samples are the lines the baselines printed. Other measured cells are leader figures, marked claim. DNA stays on gradient boosting.

| id | family | measured | citation | system | reason |
| --- | --- | --- | --- | --- | --- |
| p-bounce | extract+retrieve | filled 5 | samples/ds-letters.md | referral letters | The specialty is a field in the letter. A return still has to name the clause in force. The word list fills 5 of 7 letters, so it is only a baseline. |
| p-waitlist | no-model | claim 510000 | extracts/access-costs.md | waitlist | Rows the coordinators do not trust are a matching rule. The 510000 SAR is the director's figure for returned referrals, and it is a claim. |
| p-dna | classical-ml | person 0.0000 | samples/ds-dna.csv | appointment list | This is a table with a label. prior_dna is the feature. The row split printed 0.7692 and the person split printed 0.0000. The same person sits on both sides of the row split, so the memo uses the person line. appointment_status_final is filled after the visit and matches the label, so the script does not use it. |
| p-status | agent | keyword 0.3125 | samples/ds-messages.csv | referral record | The keyword fires on 0.3125 of the messages. "Where is my referral?" is a status question and does not contain the word. Status has to be a tool call. |
| p-slots | no-model | claim 230000 | extracts/access-costs.md | session book | Empty chairs are a workflow when a session or a patient is cancelled. A sentence must not hold the slot. 230000 SAR is the director's figure for empty sessions, and it is a claim. |
| p-clock | no-model | claim 14 | extracts/dashboard.md | wait-time mart | The chart names the column booking_date. The fix is the query that starts the clock. 14 days is the board's median, and it is a claim. |
| p-info | retrieve | claim 430 | extracts/access-costs.md | clinic documents | Hours, preparation, and required documents are answers in a document that is in force for that reader. 430 calls is the director's figure, and it is a claim. |
| p-forecast | forecast | seasonal 2.1667 | samples/ds-demand.csv | monthly session volumes | The seasonal error on 2026 is 2.1667. The mean error is 12.0324. A heavier model has to beat the seasonal line. |
| p-triage | blocked | claim 3000000 | extracts/sponsor-ask.md | clinician | The sponsor asks the assistant to set clinical urgency and claims 3000000 SAR a year. A clinician assigns urgency. We do not build this. |

## Customization

Extraction and intent use the registered adapter. Hours stay on retrieval.

| task | method | f1 | cost | hash |
| --- | --- | --- | --- | --- |
| extraction | lora | 1.0000 | 3 | sha256:0539840c7b3e824e |
| intent | lora | 1.0000 | 3 | sha256:0539840c7b3e824e |
| hours | retrieve |  |  |  |

## Tools

The clock is a query against the wait-time mart. Slot allocation is a workflow on the session book. Referral status is a tool, not a sentence in the prompt. Clinical urgency is not a model call.
