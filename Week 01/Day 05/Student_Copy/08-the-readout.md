# 08 — The readout

[Chapter 07](07-the-diagram.md) copied the blank readout and the blank trace note, and it filled the diagram and the design. This chapter fills the other two. Do not run `prepare_work.py pages` again. That command would replace the diagram and the design you just saved.

## The steering opening

Open a terminal in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.demo.readout --profile practice
```

You should see six lines. The first is:

```text
The virtual front desk, including triage, goes live before Ramadan.
```

Then the five questions, numbered:

```text
1. What, if anything, goes live before Ramadan?
2. Where does patient data sit for this proof?
3. Which failure did the scenario set expose, and what did the agent do?
4. Which stage gate is still open?
5. What will this proof not build?
```

That first line is the claim on [cdo.md](packet/kickoff/personas/cdo.md). It is not the plan. The demo does not print how many weeks the purchase takes. The deadline check says `the readout does not answer the deadline` and does not print that number.

## The six answers

Read this table once. Each row is one heading in [readout.md](work/readout.md). The sentence is what goes under that heading. Do not rebuild the file from the table. The block in Replace the readout is the file you paste.

| Heading | What you write under it |
| --- | --- |
| Deadline | The board has named a date just before Ramadan. That date assumes a purchase that takes 16 weeks. Citation: cdo. |
| Data | Patient data stays off the external model ext-large and on the private cloud. Citation: dpo. |
| Failure | The timeout did not book. race-slot kept a single booking. Citation: pol-approval. |
| Gate | G2 is still open. Citation: pol-stage-gate. |
| Will not build | This proof will not build triage. A clinician assigns clinical urgency. |
| Asks | The deadline is open until the purchase is real. The ruling is open until it is signed. Neither ask adds triage to this proof. |

The Failure sentence uses the `timeout` and `race-slot` rows from [chapter 06](06-the-agent.md). The Gate sentence uses [pol-stage-gate.md](packet/kickoff/corpus/pol-stage-gate.md). G2 is the DPIA, and it is still open. Will not build keeps urgency with a clinician. Asks does not add triage.

The deadline check looks for the number of weeks and for `cdo`. It does not print them. The data check looks for `ext-large`, `private`, and `dpo`. The failure check looks for `timeout` or `race-slot`, and for a citation. The gate check looks for a gate id and for `pol-stage-gate`. None of those messages name the missing fact.

Do not write that the assistant sets clinical urgency. The check says `readout contains a banned sentence` and does not print the sentence. If the ask log contains `p-triage` and does not contain the word not, the check says `the ask log promises triage`.

## Replace the readout

Open [work/readout.md](work/readout.md). Select the whole file. Delete it. Paste the block below. Save. Keep the six heading lines.

After you save, those headings are still there, in this order: Deadline, Data, Failure, Gate, Will not build, Asks. Each one has the sentence from the table under it.

This block replaces `work/readout.md` only.

```text
# Readout

## Deadline

The board has named a date just before Ramadan. That date assumes a purchase that takes 16 weeks. Citation: cdo.

## Data

Patient data stays off the external model ext-large and on the private cloud. Citation: dpo.

## Failure

The timeout did not book. race-slot kept a single booking. Citation: pol-approval.

## Gate

G2 is still open. Citation: pol-stage-gate.

## Will not build

This proof will not build triage. A clinician assigns clinical urgency.

## Asks

The deadline is open until the purchase is real. The ruling is open until it is signed. Neither ask adds triage to this proof.
```

## The trace note

The note is yours. It is not the diagram. The check reads [trace-note.md](work/trace-note.md) for the emergency scenario: the tool, the document, and whether the reply was refused.

Open [trace.json](work/trace.json). Search `"emergency"`, the same way as chapter 06. On that object, `tool_trace` is the tool, `citations` includes the document, and `refusal_logged` true means the reply was refused. The table below is that row. The block under the table is the file you paste. Do not rebuild the file from the table.

The check says `the trace note does not name the tool`, `the trace note does not name the document`, or `the refusal line does not match`. It does not print the document id.

| Scenario | Tool | Document | Refused |
| --- | --- | --- | --- |
| emergency | safety.redirect | pol-clinical-safety | yes |

Open [work/trace-note.md](work/trace-note.md). Select the whole file. Delete it. Paste the block below. Save.

This block replaces `work/trace-note.md` only.

```text
# Trace note

## Scenario

emergency

## Tool

safety.redirect

## Document

pol-clinical-safety

## Refused

yes
```

Next: [09 — Finish](09-finish.md).
