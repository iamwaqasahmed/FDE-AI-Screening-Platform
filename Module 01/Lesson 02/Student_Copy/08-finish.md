# 08 — Finish

Two checks grade the approach memo and the brief. The knowledge file is still part of done. The trainer reads it against the solution. The checker does not print a score for it.

Use the failure table at the bottom only when a check fails. It is not more work.

## Do this

1. Open a terminal in the course folder, the same way as chapter 01. Then run:

```text
cd problem_simulation
python -m alwaha.check approach --work "../Module 01/Lesson 02/Student_Copy/work" --profile practice
python -m alwaha.check brief --work "../Module 01/Lesson 02/Student_Copy/work" --profile practice
```

2. In the `work` folder, create a new file named `knowledge.md`. Paste the heading below. Replace the two answer lines with your own sentences.

- Question 1 is `p-info`. [problems.md](packet/release/problems.md) describes it as patients calling for hours, preparation, and documents. That family word is `retrieve`. Fine-tuning would bake a document into the model. The document changes by site and by version. Say that in your sentence.
- Question 2 is `p-clock`, the board's wait chart. Its family cell is only `no-model`. The fix is the query on `booking_date`. Empty chairs, `p-slots`, are the same kind of answer if you would rather name that one. Say which id you mean, and why a model is the wrong tool.

```text
# Knowledge

1. Name a problem where retrieval fits better than fine-tuning.

Your answer. Name the problem id.

2. Name one problem where a model is the wrong tool.

Your answer. Name the problem id.
```

## You should now see

```text
chk-approach passed.
chk-brief passed.
```

`work/knowledge.md` has both answers, and each answer names a problem id.

## If a check fails

A failed check names the problem id and the kind of miss. It does not name the family that would fit, the baseline line it wanted, or the banned sentence. Go back to the chapter that has that input.

| What it prints | Where to go |
| --- | --- |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and run the two checks again |
| `approach.md is missing` or `brief.md is missing` | [Chapter 07](07-the-memo.md). From the course folder, run `python "Module 01/Lesson 02/Student_Copy/prepare_work.py" memo`, then fill the copies in `work/` |
| `approach table needs columns` or `sizes table needs id, size, source, and kind` or `claims table needs a Kind column` | Keep the header row and the dashed line under it. Do not turn the table into a list |
| `family does not fit` | The approach table in chapter 07. `p-bounce` is `extract+retrieve`. `p-slots` and `p-clock` are only `no-model`. `p-triage` is only `blocked` |
| `measured value does not match the baseline` or `size is not the baseline measurement` | [Chapter 06](06-the-baselines.md). Use the person line, the keyword line, the filled line, and the seasonal line. `person 0.0000` is the person line. `510000` stays on `p-waitlist`. It does not replace `filled 5` on `p-bounce`. In the brief, the size cell is the digits, and the kind cell is `measured` |
| `citation is not a release file or a persona` or `source is not in the release` | Use the short path from chapter 07, such as `extracts/dashboard.md` |
| `size is not in the cited file` | Copy the digits exactly as the file prints them. Remove a comma if you added one |
| `needs a system and a reason` | Fill both cells. Chapter 07 has a reason sentence for each id |
| `approach is missing` an id, `brief is missing` an id, or `ranking is missing` an id | Add that id. The nine ids are the rows in chapter 07 |
| `is duplicated` or `is ranked twice` | That id appears twice. Keep one row, or one numbered line |
| `unknown problem id` | The id is not one of the nine. Check the spelling, including the hyphen |
| `claims need at least two rows` or `the claims table needs a row marked claim` | Paste the six claim rows from chapter 07. Kind is `claim` or `fact` |
| `size kind must be measured or claim` | The kind cell is the word `measured` or the word `claim`, not the digits |
| `brief contains a banned sentence` | A leader's wish is outside a row whose Kind is `claim`. The message does not name the sentence. A claim row is skipped. A heading, the sizes table, and the ranking are not. Search `work/brief.md` for a sentence in the list under this table. Delete that copy. The six claim rows in chapter 07 may stay |
| `the first rank needs the urgency rule on the same line` | Line 1 is `p-triage` and does not say that a clinician assigns urgency. Use the nine lines in chapter 07, or add those words to line 1 |
| `a watermarked sample is in the work directory` | A sample file, or a line from the letter file, was copied into `work/`. The message does not print the watermark. Delete that copy. Leave the letter file in `packet/release/samples` |
| `Build rel-m01-l02 first.` | [Chapter 01](01-setup.md). Run the build again with `--profile practice` |

The check looks for these sentences outside a claim row. It matches them in any case. It does not print which one it found.

- `Triage is already approved.`
- `The assistant may set clinical urgency.`
- `No-shows are the largest cost in the cluster.`
- `Returns have no cause in the template.`
- `Thursday approvals are reviewed with care.`
- `The external model may receive identified patient data.`
- `The integration-engine log is clean.`
- `Every hospital has a live slot API.`
- `Waiting time fell last year.`
- `The vendor saving and the contact-center saving are separate.`
- `Every patient can use the app alone.`
- `Al-Waha containment is about 70 percent.`

## Done

This lesson is done when both checks print `passed` and `work/knowledge.md` answers both questions. The check does not read those sentences. Line 1 names `p-info` and says why retrieval fits better than fine-tuning. Line 2 names `p-clock` or `p-slots` and says why a model is the wrong tool. Search the file for those ids before you stop.

Keep `work/` and the worksheets. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

This lesson is done. The next day is intake, then the agent. The event stream, the SLA policy, and the business calendar arrive in the next folder. Intake runs from `referral.submitted` to a held approval. It does not book.

Open [the next lesson](<../../Lesson 03/Student_Copy/README.md>) and read `00-background.md` before any command.
