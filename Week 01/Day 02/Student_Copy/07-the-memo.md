# 07 — The memo

[Chapter 06](06-the-baselines.md) printed the lines. [Chapter 04](04-words.md) named the family words. This chapter fills two files. The checks read them. The tables below are the cells that make the check pass. You still read the why, and you may reorder the ranking.

## Copy the blanks

Open a terminal in the course folder.

```text
python "Week 01/Day 02/Student_Copy/prepare_work.py" memo
```

You should see `Copied the blank memos to work/approach.md and work/brief.md.`

The blanks you are copying are [approach.md](packet/templates/approach.md) and [brief.md](packet/templates/brief.md). Leave those two unchanged. After the command, edit the copies: [work/approach.md](work/approach.md) and [work/brief.md](work/brief.md). The link opens once the command has written the file. If it does not open, run the command again from the course folder, then open `Week 01/Day 02/Student_Copy/work`.

Run the command once. A second run replaces whatever you have written. If the command says to run it first with no extra word, do the chapter 01 command, then this one.

Keep every `|` in the tables. Do not turn a table into a list. Do not add commas to a number. The files print `510000`, not `510,000`.

## The approach table

Keep the header row and the `| --- |` line in [work/approach.md](work/approach.md). The blank file already has one row per id. Replace each empty row with the matching line from this block. Paste the line with the `|` characters. Do not paste a second header.

The family cell is only the word, or `extract+retrieve` for the return. The why sentence is the reason cell. Use the family word from the block below. If a family is wrong, the check says `family does not fit` and does not name the word that would fit. A second family word on `p-slots`, `p-clock`, or `p-triage` fails the same way. It does not name the word to remove.

The measured cell for a sample is the whole printed line from [notes/baseline-lines.md](notes/baseline-lines.md). On the practice files those lines are the ones below. If your notes show a different line, paste your line. Use the person line, the keyword line, the filled line, and the seasonal line. The row line and the mean line stay in the notes.

The measured cell for the other five ids is the word `claim`, a space, and the digits from the file. Both sit in that one cell.

Read this before you paste the `p-waitlist` row. `510000` is the director's money figure for returned referrals in the cost note. It is not a count of untrusted waitlist rows. The waitlist has no baseline of its own, and `p-bounce` already uses the filled line, so the memo parks this figure on `p-waitlist` and marks it `claim`.

`p-bounce` already has a measurement: the `filled` line, how many letters name a specialty. The brief has one size for that id, and a measured size has to be the baseline. `510000` cannot replace `filled 5`. The waitlist row has no baseline, so the memo records the money figure there and marks it `claim`. Putting `510000` in the bounce cell, instead of the filled line, makes the check say `measured value does not match the baseline`. That same message appears when a sample row uses the `row` line or the `mean` line. The check does not say which of those mistakes it saw.

```text
| p-bounce | extract+retrieve | filled 5 | samples/ds-letters.md | referral letters | The specialty is a field in the letter, and a return still has to name the rule that is in force. See samples/ds-letters.md. |
| p-waitlist | no-model | claim 510000 | extracts/access-costs.md | waitlist | Rows the coordinators do not trust are a matching rule. 510000 is the director's figure for returned referrals, and it is a claim. See extracts/access-costs.md. |
| p-dna | classical-ml | person 0.0000 | samples/ds-dna.csv | appointment list | The person line keeps a person entirely in or entirely out. The row line can place the same person on both sides, so the memo uses the person line. appointment_status_final stays out of the script. See samples/ds-dna.csv. |
| p-status | agent | keyword 0.3125 | samples/ds-messages.csv | referral record | Status lives in the referral record, so a model has to call a tool. Where is my referral? does not contain the word status. See samples/ds-messages.csv. |
| p-slots | no-model | claim 230000 | extracts/access-costs.md | session book | Empty chairs are a workflow. A sentence must not hold the slot. 230000 is a claim. See extracts/access-costs.md. |
| p-clock | no-model | claim 14 | extracts/dashboard.md | wait-time mart | The chart names booking_date. The fix is the query. 14 is a claim. See extracts/dashboard.md. |
| p-info | retrieve | claim 430 | extracts/access-costs.md | clinic documents | Hours, preparation, and documents are a document that is in force for that reader. 430 is a claim. See extracts/access-costs.md. |
| p-forecast | forecast | seasonal 2.1667 | samples/ds-demand.csv | monthly session volumes | The seasonal line is smaller than the mean line. A heavier model has to beat the seasonal line. See samples/ds-demand.csv. |
| p-triage | blocked | claim 3000000 | extracts/sponsor-ask.md | clinician | A clinician assigns urgency. The claimed impact is a claim. We do not build this. See extracts/sponsor-ask.md. |
```

`measured value does not match the baseline` means a sample row used the `row` line or the `mean` line, or `p-bounce` has `510000` instead of the `filled` line. The check does not print the line it wanted. `needs a system and a reason` means one of those two cells is blank. `citation is not a release file or a persona` means the citation cell is not one of the short paths in the table.

### Tools

Under `## Tools`, write four sentences:

- The wait chart is a query on the wait-time mart.
- Empty chairs are a workflow on the session book.
- Referral status is a tool call, not a sentence in a prompt.
- Clinical urgency is not a model call.

The check does not read this section. It is the application-engineer part of the day.

### Optional

Under `## Cost`, count the words in [ds-letters.md](packet/release/samples/ds-letters.md) where the file sits. Divide that count by 1,000. Multiply by `price.ext_large_per_1k` and by `price.local_per_1k` from [prices.csv](packet/release/finance/prices.csv). Write the two results. Do not copy a line from the letter file into the memo.

Under `## Overlap`, two letters share the same three sentences, and one of them adds a watermark line. Write the two headings only, `letter-01` and `letter-06`. Do not copy a line from the file into `work/`.

The check does not read either section. Skip them if you want. The day is complete without them.

## The brief

Edit [work/brief.md](work/brief.md). Keep the three headings: Claims, Sizes, and Ranking. Keep each header row and its `| --- |` line.

### Claims

You do not need a row whose kind is `request`. Claim and fact are enough.

Delete the empty claims row. Paste these six lines under the header, with the `|` characters. The words are the words of the files you already opened.

```text
| bi-lead | The board pack shows a median wait of 14 days. | claim |
| bi-lead | The chart reads the column booking_date. | fact |
| vendor | Containment on the national contact-center pilot is 70 percent. That pilot is not the Al-Waha Health Cluster. | claim |
| access-mgr | No-shows are listed first, at 910000 SAR, then returned referrals, then empty sessions. | claim |
| cdo | The virtual front desk, including triage, is the program. Claimed impact: 3000000 SAR a year. | claim |
| med-dir | A clinician assigns urgency. | fact |
```

A leader's wish stays inside a row whose Kind is `claim`. Do not repeat that wish in a heading, in the sizes table, or in the ranking. Do not write that waiting time fell. Do not write that Al-Waha's own containment is about 70 percent. The vendor figure is a national pilot. Do not write that no-shows are the largest cost in the cluster. The cost row above already says they are listed first.

`brief contains a banned sentence` means one of those wishes is sitting outside a claim row. The message does not name the sentence. Move the sentence into the claims table, or delete it.

### Sizes

The blank file already has one size row per id. Replace each empty row with the matching line. The size cell is the digits only. The word `claim` goes in the kind cell, not in the size cell. A measured size is the digits from the printed line. If your notes show different digits, use your notes.

```text
| p-bounce | 5 | samples/ds-letters.md | measured |
| p-waitlist | 510000 | extracts/access-costs.md | claim |
| p-dna | 0.0000 | samples/ds-dna.csv | measured |
| p-status | 0.3125 | samples/ds-messages.csv | measured |
| p-slots | 230000 | extracts/access-costs.md | claim |
| p-clock | 14 | extracts/dashboard.md | claim |
| p-info | 430 | extracts/access-costs.md | claim |
| p-forecast | 2.1667 | samples/ds-demand.csv | measured |
| p-triage | 3000000 | extracts/sponsor-ask.md | claim |
```

`size is not the baseline measurement` means a measured row has the row line, the mean line, or a leader's figure. `source is not in the release` means the source cell is not a short path from this table. `size is not in the cited file` means the digits are not the digits printed in that file, often because a comma was added.

### Ranking

Delete the empty `1.` and paste these nine lines. `p-clock` is first because the column `booking_date` has to be named before any other number is used as a baseline. Any order of the nine ids also passes. Each id stays once. If you move `p-triage` to line 1, that same line has to say that a clinician assigns urgency. The last line already says it.

```text
1. p-clock — the median is a claim, and the column is booking_date.
2. p-info — hours, preparation, and documents are a document that is in force.
3. p-bounce — the filled count is the measurement, and the return needs the rule that is in force.
4. p-slots — empty chairs are a workflow.
5. p-waitlist — untrusted rows are a matching rule.
6. p-status — status is a tool call.
7. p-dna — use the person line.
8. p-forecast — use the seasonal line.
9. p-triage — a clinician assigns urgency. The claimed impact is a claim.
```

Talk about the problem id and the file. Leave a leader's wish in the claims table.

Next: [08 — Finish](08-finish.md).
