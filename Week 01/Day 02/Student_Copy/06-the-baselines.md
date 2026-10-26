# 06 — The baselines

[Chapter 05](05-the-extracts.md) put the leader figures on your worksheet as claims. This chapter prints four measurements. You will choose which printed line goes into the memo.

The scripts are already in `work/baselines`, from chapter 01. Read the packet copies. They match. The comments say what each function does.

## Read, then run

Open these files before the command that uses them:

1. [ds-dna.csv](packet/release/samples/ds-dna.csv), then [dna.py](packet/baselines/dna.py)
2. [ds-messages.csv](packet/release/samples/ds-messages.csv), then [messages.py](packet/baselines/messages.py)
3. [ds-letters.md](packet/release/samples/ds-letters.md), then [letters.py](packet/baselines/letters.py)
4. [ds-demand.csv](packet/release/samples/ds-demand.csv), then [demand.py](packet/baselines/demand.py)

On the DNA file, the script reads `prior_dna` and `did_not_attend`. One other column, `appointment_status_final`, is filled after the visit and repeats the label. Leave it unread. Do not add that name to the script.

On the message file, find the row `Where is my referral?` It asks where a referral stands. It does not contain the word status. The keyword line will miss it. You will say that in the reason for `p-status`.

On the letter file, the word list is `eye`, `ophthalmology`, `endocrinology`, `diabetes`, `cardiology`, and `heart`. Retina and sugar clinic are not on that list, so those letters stay uncounted. One letter repeats an earlier letter and then adds a watermark line. Read that line where it sits. Do not copy it.

[pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) still applies. A coding assistant may see the script. It may not see the letters, the message text, or the DNA file. Leave those three files out of prompts, out of tickets, and out of `work/`.

## Do this

Open a terminal in the course folder, the same way as chapter 01. Paste the printed lines into [notes/baseline-lines.md](notes/baseline-lines.md).

```text
python "Week 01/Day 02/Student_Copy/work/baselines/dna.py" "Week 01/Day 02/Student_Copy/packet/release/samples/ds-dna.csv" --split row
python "Week 01/Day 02/Student_Copy/work/baselines/dna.py" "Week 01/Day 02/Student_Copy/packet/release/samples/ds-dna.csv" --split person
python "Week 01/Day 02/Student_Copy/work/baselines/messages.py" "Week 01/Day 02/Student_Copy/packet/release/samples/ds-messages.csv"
python "Week 01/Day 02/Student_Copy/work/baselines/letters.py" "Week 01/Day 02/Student_Copy/packet/release/samples/ds-letters.md"
python "Week 01/Day 02/Student_Copy/work/baselines/demand.py" "Week 01/Day 02/Student_Copy/packet/release/samples/ds-demand.csv"
```

You should see:

- one line that starts with `row`
- one line that starts with `person`
- one line that starts with `keyword`
- one line that starts with `filled`
- two lines from the demand script, `seasonal` and then `mean`

The row line and the person line are different numbers. The person line on the practice file is `person 0.0000`. A zero is not a broken script. The person split scores only the last 30 percent of the sorted person ids. Those ids are `p16` through `p23`. On every row for those people, `prior_dna` and `did_not_attend` disagree, so the guess matches none of them. The row line stays high because `p00` through `p15` agree with the rule, and the same person can sit on both sides of that split.

On the worksheet, under DNA, write one sentence: the row split can place the same person on both sides. The function `shared` in [dna.py](packet/baselines/dna.py) is that count. Today's commands do not print it. The memo uses the person line, including when that line is `0.0000`, because that split keeps a person entirely in or entirely out.

The memo uses these four lines:

| Problem | Line you will paste |
| --- | --- |
| `p-dna` | the `person` line |
| `p-status` | the `keyword` line |
| `p-bounce` | the `filled` line |
| `p-forecast` | the `seasonal` line |

Keep the `row` line and the `mean` line on the worksheet. They are the comparison. They do not go in the measured cell. A smaller demand error is the closer score. Read both demand lines and see which one is smaller. That is the line a heavier method has to beat.

## If a command fails

| What you see | What to do |
| --- | --- |
| `python` is not recognized | Use `py` in front of the quoted script path, as chapter 01 described |
| `can't open file` or `No such file` | Open a new terminal in the course folder and run the command again. If `work/baselines` is missing, run the chapter 01 command `python "Week 01/Day 02/Student_Copy/prepare_work.py"` first |
| `The split has no rows` | The path must be the DNA file in `packet/release/samples` |

Next: [07 — The memo](07-the-memo.md).
