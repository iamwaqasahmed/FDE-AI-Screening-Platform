# 09 — Finish

The checks grade the agent, the trace it writes when they run it, the architecture, the design, the readout, the trace note, and the shape of the knowledge file. They run the agent again. A trace you typed by hand is not the trace they grade. The sentences in `knowledge.md` are still part of done. The trainer reads them. The design check grades the diagram, the urgency section, and the Stage 2 table. On `knowledge.md` it only requires two numbered lines with a word after the number. It does not grade those sentences.

Use the failure table at the bottom only when a check fails. It is not more work.

## Do this

1. Create `knowledge.md` in the same `work` folder as `readout.md`. The full path is `Week 01/Day 05/Student_Copy/work/knowledge.md`. On Windows, if the new file becomes `knowledge.md.txt`, rename it so the name ends in `.md` only. Open it, select all, delete anything already there, and paste the block below. These are the finished sentences. Line 1 names one failure the scenario set exposed. Line 2 names the stage gate that is still open. [pol-stage-gate.md](packet/kickoff/corpus/pol-stage-gate.md) is the gate list. G2 is the DPIA. Save.

```text
# Knowledge

1. The timeout failure: the offer did not return, and the agent did not book.

2. G2 is still open.
```

2. Open a terminal in the course folder, the same way as chapter 01. If that window is already inside `problem_simulation`, skip the `cd` line and run the five python lines. Then run:

```text
cd problem_simulation
python -m alwaha.check agent --release rel-w1d5 --work "../Week 01/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check trajectory --release rel-w1d5 --work "../Week 01/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check design --work "../Week 01/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check readout --work "../Week 01/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check individual --work "../Week 01/Day 05/Student_Copy/work" --profile practice
```

## You should now see

```text
chk-w1-agent passed.
chk-w1-trajectory passed.
chk-w1-design passed.
chk-readout passed.
chk-individual-w1 passed.
```

`work/knowledge.md` has both answers. The first says the timeout failure is the offer that did not return, and the agent did not book. The second says G2 is still open.

## If a check fails

A failed scenario names the case. It does not print the count, the slot, or an interview sentence. A watermark message does not print the watermark. Where a check fails without naming the missing fact, go back to the chapter that has the inputs, then write the label yourself.

| What it prints | Where to go |
| --- | --- |
| `python` is not recognized | [Chapter 01](01-setup.md). Use `py` instead of `python` in the command, including the runner command in chapter 06 |
| `SyntaxError` or `IndentationError` | The paste in [chapter 06](06-the-agent.md) lost its spaces. Select the whole file, delete it, and paste the block again. Do not repair it by hand. If the spaces vanish again as you paste, turn off Format On Paste, or use Paste Without Formatting, then paste once more |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and run the check again |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python lines |
| `Build rel-w1d4 and rel-w1d5 first.` | [Chapter 01](01-setup.md). Run both builds again with `--profile practice` |
| `Build rel-w1d5 first.` | [Chapter 01](01-setup.md). Run the `rel-w1d5` build again |
| `run.py is missing` or `agent did not run` | [Chapter 06](06-the-agent.md). `work/agent/` needs `run.py`, `model.py`, `schema.py`, `memory.py`, and `tools.py`. Replace the three files with the blocks in that chapter, and leave `tools.py` and `run.py` |
| `trace is not a list` or `trace is missing a field` or `log is missing a field` | The agent did not write the fields in chapter 06. Paste those three files again |
| `is missing` | That scenario never reached the trace. The scenario files stay in `packet/day4` and `packet/release`. The check uses the packs from chapter 01. Run both builds again |
| `count does not match the tool` | The reply count is still the starter's number. The demo in chapter 06 prints both numbers. The message does not print the count. Use the tool result |
| `booked a slot` | That case booked. Emergency, injection, reason, reject, return, and timeout do not book. A letter is not a tool call. The message does not print the slot |
| `did not book` | `book`, `replay`, `resume`, or `race-slot` books after the patient confirms and one approval, then sends SMS. `race-slot` books once |
| `booked twice` | `slots.book` ran more than once on that case. `race-slot` keeps a single booking |
| `does not name the failure` | The row for `timeout` or `race-slot` left `failure` empty or set a different name. Chapter 06 names both |
| `was sent` | The return tool ran. A return waits. The approval id stays pending. The message does not print the id |
| `message does not match` | SMS is sent only after a booking, on `book`, `replay`, `resume`, and `race-slot`. The message does not print the SMS text |
| `dropped the facility` | The `memory` case lost the facility from the turn that named the hospital. The message does not print the id |
| `refusal does not name the constraint` | The `reason` reply must carry the constraint the offer tool returned. The message does not print the constraint |
| `applied more than one decision` | `replay` decided the same approval id twice. The second copy changes nothing |
| `decision does not match` | A coordinator decision was skipped, or an extra one was invented |
| `reused a blocked preference` | `consent` is false. The stored preference is not applied. The message does not print the preference |
| `approval was not held` | The return has no coordinator decision. The approval id stays in pending. The message does not print the id |
| `left an approval open` | A pending id was left on a case that does not wait |
| `approval does not match` | The id on the coordinator turn is the id the row keeps. The message does not print the id |
| `trace does not match` | The tool list for that case is not the one the policy allows. The message does not print the list. Chapter 06 names the tools for timeout, race-slot, and emergency |
| `repeated a read` | `referral.status` ran more than once. `resume` and `memory` call it once |
| `wrote before approval` | `slots.book` or `referral.return` ran with no approval id on the row |
| `did not redirect` | The `emergency` turn matches the routing list. Call `safety.redirect`. Do not book |
| `refusal was not logged` | `emergency`, `consent`, `reason`, `reject`, and `timeout` log a refusal. `race-slot` logs one too, because the second offer is taken |
| `logged a refusal` | A case that proceeds logged a refusal. A booked visit that is not `race-slot` does not |
| `trace does not cite the tool` | The row is missing the tool it called. Status cites `referral.status`. A constraint or a timeout cites `slots.offer` |
| `trace does not cite the document` | A redirect cites `pol-clinical-safety`. A booking, a rejection, and a waiting return cite `pol-approval`. The message does not print the document text |
| `trace contains a blocked preference` | The stored preference string is in the trace. Leave it out. The message does not print the preference |
| `architecture.md or design.md is missing` | [Chapter 07](07-the-diagram.md). From the course folder, run `python "Week 01/Day 05/Student_Copy/prepare_work.py" pages`, then paste those two files. If you already filled the readout, paste it again from chapter 08 after that command |
| `the diagram has no human step` | The diagram section needs the word coordinator, human, or approval. Use the architecture block in chapter 07 |
| `the design does not leave urgency with a clinician` | The section `What we will not build` needs both clinician and urgency. Use the design block in chapter 07 |
| `design contains a banned sentence` or `readout contains a banned sentence` | Take out the sentence that lets the assistant set clinical urgency, or that sends identified patient data to the external model. The message does not print the sentence |
| `the design note is missing a required fact` | The check does not name the fact. Use the Stage 2 table in chapter 07, and keep the pipe characters. The diagram also needs `wf-intake`, `wf-self-service`, the three zones, and `referral.status` |
| `knowledge.md needs two answers` | Two lines that start with `1.` and `2.` and then a word. Use the block above |
| `readout.md is missing` | [Chapter 08](08-the-readout.md). Paste the readout. Do not run `pages` again if the diagram is already filled. If the blank is gone, copy [readout.md](packet/templates/readout.md) into `work/` by hand, then paste the chapter 08 block over it |
| `the readout does not answer the deadline` | The check does not print the number of weeks. Use the Deadline row in chapter 08. That sentence cites `cdo`. Paste the readout block again if the heading is empty |
| `the readout does not say where patient data sits` | Use the Data row in chapter 08. That sentence cites `dpo` |
| `the readout does not name a failure` | The Failure section needs `timeout` or `race-slot`. Use the Failure row in chapter 08 |
| `the readout does not cite the failure` | The Failure row in chapter 08 already includes the citation `pol-approval`. Paste that block again |
| `the readout does not name an open gate` | The Gate section needs a gate id from [pol-stage-gate.md](packet/kickoff/corpus/pol-stage-gate.md). The finished sentence says G2 |
| `the readout does not cite the gate` | The Gate section needs `pol-stage-gate` |
| `the readout does not say what it will not build` | The Will not build section needs the word clinician |
| `the ask log is missing` | The Asks section needs the two open items from chapter 08 |
| `the ask log promises triage` | The Asks section must not add triage. The finished sentence says neither ask adds triage |
| `trace-note.md is missing` | [Chapter 08](08-the-readout.md). Paste the trace note |
| `the trace note does not name the tool` | The Tool section needs `safety.redirect`. The emergency row in the trace is the input. The finished label is in chapter 08 |
| `the trace note does not name the document` | The check does not print the document id. The Document section needs `pol-clinical-safety` |
| `the refusal line does not match` | The Refused section needs `yes`. It must not say the visit was not refused |
| `a watermarked sample is in the work directory` | A scenario file, or the watermark line, was copied into `work/`. The message does not print the watermark. Delete that copy. Leave the scenario files in `packet/day4/scenarios` and `packet/release/scenarios` |

## Done

The day is done when the five checks print `passed` and `work/knowledge.md` answers both questions.

Keep `work/` and the trace worksheet. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

Tomorrow is the first morning of Week 2. `his-wadi` publishes a new spec. You leave with a patient and a coordinator who can open the assistant. Booking waits.

Open [Week 2, Day 1](../../../Week%2002/Day%2001/Student_Copy/README.md) and read `00-background.md` before any command.
