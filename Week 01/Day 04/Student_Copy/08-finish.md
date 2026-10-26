# 08 — Finish

The checks grade the agent, the trace it writes when they run it, the agent note, and the shape of the knowledge file. They run the agent again. A trace you typed by hand is not the trace they grade. The sentences in `knowledge.md` are still part of done. The trainer reads them. On that file the checks only require two numbered lines with a word after the number. They do not grade those sentences.

Use the failure table at the bottom only when a check fails. It is not more work.

## Do this

1. In the same `work` folder as `agent-note.md`, create a new file named `knowledge.md`. Save it as `Week 01/Day 04/Student_Copy/work/knowledge.md`. Paste the block below. Then replace each numbered line with your own sentence. Delete the words `Your answer` and write the sentence on that same line.

- Line 1 is the second agent. A second agent is worth its tokens when the extractor would otherwise hold the book tool. A letter is data. Status stays one agent and one tool. Your line 1 says that.
- Line 2 is the booking. The patient has confirmed, and a coordinator has decided the approval. The book tool runs after that, and then the SMS. Your line 2 says that. [pol-approval.md](packet/release/policy/pol-approval.md) is the sentence.

```text
# Knowledge

1. Your answer. Say when a second agent is worth its tokens.

2. Your answer. Say what must be true before a slot is booked.
```

2. Open a terminal in the course folder, the same way as chapter 01. If that window is already inside `problem_simulation`, skip the `cd` line and run the two python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check agent --work "../Week 01/Day 04/Student_Copy/work" --profile practice
python -m alwaha.check trajectory --work "../Week 01/Day 04/Student_Copy/work" --profile practice
```

## You should now see

```text
chk-w1-agent passed.
chk-w1-trajectory passed.
```

`work/knowledge.md` has both answers. The first says a second agent is worth its tokens when the extractor would otherwise hold the book tool. The second says the patient has confirmed and a coordinator has decided the approval.

A miss in the note or in the knowledge file is printed by both checks. Fix that file once, then run both commands again.

## If a check fails

A failed scenario names the case. It does not print the count, the slot, or the clause. A watermark message does not print the watermark. Go back to the chapter that has that input.

| What it prints | Where to go |
| --- | --- |
| `python` is not recognized | [Chapter 01](01-setup.md). Use `py` instead of `python` in the command, including the runner command in chapter 06 |
| `SyntaxError` or `IndentationError` | The paste in [chapter 06](06-the-agent.md) lost its spaces. Select the whole file, delete it, and paste the block again. Do not repair it by hand |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and run the check again |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python line |
| `Build rel-w1d4 first.` | [Chapter 01](01-setup.md). Run the build again with `--profile practice` and `--release rel-w1d4` |
| `run.py is missing` or `agent did not run` | [Chapter 06](06-the-agent.md). `work/agent/` needs `run.py`, `model.py`, `schema.py`, `memory.py`, and `tools.py`. Replace the three files with the blocks in that chapter, and leave `tools.py` and `run.py` |
| `trace is not a list` or `trace is missing a field` or `log is missing a field` | The agent did not write the fields in chapter 06. Paste those three files again |
| `is missing` | That scenario never reached the trace. The scenario files stay in `packet/release`. The check uses the pack from chapter 01. Run that build again |
| `count does not match the tool` | The reply count is still the starter's number. The demo in chapter 06 prints both numbers. The message does not print the count. Use the tool result |
| `booked a slot` | That case booked. Emergency, injection, reason, reject, and return do not book. A letter is not a tool call. The message does not print the slot |
| `did not book` | `book`, `replay`, or `resume` books after the patient confirms and one approval, then sends SMS |
| `was sent` | The return tool ran. A return waits. The approval id stays pending. The message does not print the id |
| `message does not match` | SMS is sent only after a booking, on `book`, `replay`, and `resume`. The message does not print the SMS text |
| `dropped the facility` | The `memory` case lost the facility from the turn that named the hospital. The message does not print the id |
| `refusal does not name the constraint` | The `reason` reply must carry the constraint the offer tool returned. The message does not print the constraint |
| `applied more than one decision` | `replay` decided the same approval id twice. The second copy changes nothing |
| `decision does not match` | A coordinator decision was skipped, or an extra one was invented |
| `reused a blocked preference` | `consent` is false. The stored preference is not applied. The message does not print the preference |
| `approval was not held` | The return has no coordinator decision. The approval id stays in pending. The message does not print the id |
| `left an approval open` | A pending id was left on a case that does not wait |
| `approval does not match` | The id on the coordinator turn is the id the row keeps. The message does not print the id |
| `booked twice` | `slots.book` ran more than once on that case |
| `trace does not match` | The tool list for that case is not the one the policy allows. The message does not print the list. Chapter 06 names the tools for each case |
| `repeated a read` | `referral.status` ran more than once. `resume` and `memory` call it once |
| `wrote before approval` | `slots.book` or `referral.return` ran with no approval id on the row |
| `did not redirect` | The `emergency` turn matches the routing list. Call `safety.redirect`. Do not book |
| `refusal was not logged` | `emergency`, `consent`, `reason`, and `reject` log a refusal |
| `logged a refusal` | A case that proceeds logged a refusal. A booked visit does not |
| `trace does not cite the tool` | The row is missing the tool it called. Status cites `referral.status`. A constraint cites `slots.offer` |
| `trace does not cite the document` | A redirect cites `pol-clinical-safety`. A booking, a rejection, and a waiting return cite `pol-approval`. The message does not print the document text |
| `trace contains a blocked preference` | The stored preference string is in the trace. Leave it out. The message does not print the preference |
| `agent-note.md is missing` | [Chapter 07](07-the-note.md). From the course folder, run `python "Week 01/Day 04/Student_Copy/prepare_work.py" note`, then paste the note |
| `the note does not list the status tool` | The tool list needs `referral.status`. Use the note in chapter 07 |
| `the note does not separate extract from book and message` | The privilege boundary needs the word extract, and the word book or the word message. Use the note in chapter 07 |
| `the note does not say what the patient sees on a refusal` | The refusal needs at least three words. Use the sentence in chapter 07 |
| `knowledge.md needs two answers` | Two lines that start with `1.` and `2.` and then a word. Replace the two lines in the block above |
| `a watermarked sample is in the work directory` | A scenario file, or the watermark line, was copied into `work/`. The message does not print the watermark. Delete that copy. Leave the scenario files in `packet/release/scenarios` |

## Done

The day is done when both checks print `passed` and `work/knowledge.md` answers both questions.

Keep `work/` and the trace worksheet. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

Tomorrow you score the scenario set, including a timeout, and you publish the diagram and the design.

Open [Week 1, Day 5](../../Day%2005/Student_Copy/README.md) and read `00-background.md` before any command.
