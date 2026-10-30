# 09 — The pages

[Chapter 08](08-the-advanced.md) left the suite green. This chapter replaces the approach memo and the residency note. You do not run a check on this page. The checks are only in [chapter 10](10-finish.md).

You replace two files under `work/`:

1. [approach.md](work/approach.md), under Replace the approach memo
2. [residency.md](work/residency.md), under Replace the residency note

Use the four steps from [chapter 05](05-the-sprint.md) on each one. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the templates in `packet/templates` unchanged.

Keep the pipe characters. A table the check reads is a row of cells separated by `|`. If a paste drops the pipes, the check cannot see the row.

The second table on the approach page is the measurement block. The cost cell and the hash cell are already in that block. Do not type a second hash. Do not copy a hash from [cloud.json](packet/release/fixtures/cloud.json). Do not type a held-out item id onto this page.

The blank [approach.md](packet/templates/approach.md) mentions a Module 1 day note. You do not open that note, and you do not rerun the Module 1 baseline scripts. The numbers in the block are those lines, already filled. Words in the pasted table such as `samples/ds-letters.md` and `extracts/access-costs.md` are names already filled in. They are not links. You do not go find those files. The customization `f1` of `1.0000` is the share of fields that match when every field matches, written with four decimal places. The hash cell is the `lora-local` hash you read in chapter 03. The hours row in the customization table is blank on purpose. Its f1, cost, and hash cells stay empty because hours stay on retrieval. Do not move the adapter figures onto that row. An empty cell on a Module 1 problem id, or an empty extraction or intent cell, means the paste was only part of the block. Select the whole work file, delete it, and paste the block again.

## Replace the approach memo

Chapter 01 copied [approach.md](packet/templates/approach.md) to [work/approach.md](work/approach.md). The full path is `Module 03/Lesson 02/Student_Copy/work/approach.md`. The copy has empty cells. Do not type into the empty cells. This block replaces the whole file. It does not replace the template in `packet/templates`.

Open `work/approach.md`. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. This block replaces `approach.md`.

```text
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
| extraction | lora | 1.0000 | 3 | sha256:8c515636b689ad80 |
| intent | lora | 1.0000 | 3 | sha256:8c515636b689ad80 |
| hours | retrieve |  |  |  |

## Tools

The clock is a query against the wait-time mart. Slot allocation is a workflow on the session book. Referral status is a tool, not a sentence in the prompt. Clinical urgency is not a model call.
```

Open [work/approach.md](work/approach.md). Search inside that file, not inside this chapter. You should see `Hours stay on retrieval.` You should see `p-dna` with `classical-ml`, and `p-info` with `retrieve`. The Module 1 names `claim` and `gradient boosting` are still in the file. That is expected. The customization rows for extraction and intent say `lora`. The hours row says `retrieve`. Search for `Clinical urgency is not a model call.` That sentence is the last line. If it is missing, you pasted only the top of the block. Select the whole file, delete it, and paste again. The pipe characters are still on every table row. If a pipe is missing, paste the block again. The paths `samples/` and `extracts/` stay as words in the cells. Do not try to open them.

## Replace the residency note

This block replaces [work/residency.md](work/residency.md). The full path is `Module 03/Lesson 02/Student_Copy/work/residency.md`. It does not replace the template in `packet/templates`. Keep the pipe characters.

Open that work file. The path must contain `Student_Copy\work`. If the path contains `packet`, close it. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the backtick lines. Paste. Save.

```text
# Residency

| field | zone |
| --- | --- |
| national id | zone-private |
| date of birth | zone-private |
| name | zone-private |
| phone | zone-private |
| clinic hours | public |
```

Open [work/residency.md](work/residency.md). Search inside that file, not inside this chapter. You should see `zone-private` four times, and `clinic hours` with `public`. The columns are `field` and `zone`. If the pipes are gone, paste the block again.

This page is done when both searches pass and both tables still have their pipe characters. The templates in `packet/templates` are still blank. That is expected. Do not run a check from this page.

Next: [10 — Finish](10-finish.md).
