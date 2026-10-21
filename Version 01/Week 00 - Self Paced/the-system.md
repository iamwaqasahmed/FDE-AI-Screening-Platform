# The system

This page says what the Week 00 system is, what a person does with it, and what comes back. The files it reads are [the Hartland data](data/README.md). The practice is [FDE.md](../FDE.md).

The client asked for an AI Screening Platform. The system this track builds is smaller than that sentence. It answers a question about diabetic eye screening from the messy extract and the written rules, and it writes the reply down. It does not grade a photograph, create a referral, or write into the hospital chart.

## What a person does with it

The extract is already on disk. A person does not upload it for each question.

Each use has two inputs:

- Who is asking. A clinic nurse, a grader, the director of screening.
- The question. For example, how many eligible people there are.

From `Week 00 - Self Paced`:

```text
python -m course screening_service.run --who "clinic nurse" --question "How many eligible people are there?"
```

Each use appends two lines:

| File | What one line is |
|---|---|
| `runtime/access.log` | When, who asked, the question, which tool ran, which corpus document it used, and whether the reply was refused |
| `runtime/results.jsonl` | The reply itself |

The result file is the file handed back. One line is one JSON object: `answer`, `tool`, `document_id`, `result`, `refused`, and `reason`. A letter reply may repeat a grader's code. It keeps `adds_diagnosis` false.

There is no new API and no feed into the electronic health record. The authority's connection is a file in and a file out. The file in is the extract already in [data/handover](data/handover). The file out is `runtime/results.jsonl`.

## From a question to that reply

1. The service receives who asked and the question.
2. The agent checks the question. A request to diagnose a photo, or to create a referral without a grader, stops here. The reply is a refusal.
3. For any other question, a model chooses one tool from a fixed list. The model does not receive the handover files.
4. That tool reads [data/handover](data/handover) or [data/corpus](data/corpus) and returns a dictionary. A coverage question comes back as an eligible count and a completed count. A rule question comes back as a document id and whether that document is in force.
5. The stored sentence is built from that dictionary. A different number written by the model is dropped.
6. The service checks the reply again. A diagnosis is not written out as a clinical finding.
7. The service appends the access log and the result file.

The tools the model may call are `coverage`, `unfinished_photos`, `grader_queue`, `urgent_wait`, `letter_timing`, `vendor_pilot`, `letter_fields`, and `retrieve`. The list is the [catalog](<Module 04 - The agent/02-the-catalog.md>).

## What it reads

| Folder | Role |
|---|---|
| [data/handover](data/handover) | The messy extract the authority's IT team would send: registry, grader workbook, hospital index, shared-folder listing, letters, referrals, vendor scores, plus the IT cover note and field glossary |
| [data/corpus](data/corpus) | The written rules: which procedure is in force, the grade codes, the letter templates, the data-protection rule, and the clinic note |

The cover note and the data dictionary are claims. The tools follow the issued procedure and the grade-code list when those claims disagree with the rows. That comparison is the work in [Module 01](<Module 01 - Problem Discovery/README.md>) and [Module 02](<Module 02 - Tools the agent can trust/README.md>).

The retinal photographs named in the index, the listing, and the workbook are not in the drop. The system cannot look at an eye.

## The pieces

The modules build one path. Later pieces call earlier ones. They do not replace them.

| Piece | Module | What it does |
|---|---|---|
| Tools | [Module 02](<Module 02 - Tools the agent can trust/README.md>) | The only part allowed to count. Coverage, the queue, waits, letters, and the vendor file come from these functions |
| Retrieval | [Module 03](<Module 03 - Retrieval/README.md>) | Cites a written rule with its document id and its status. A draft stays a draft |
| Agent | [Module 04](<Module 04 - The agent/README.md>) | Chooses one tool or the retriever, then repeats the dictionary that comes back. Refuses a retina grade, an unsigned referral, and a draft treated as current policy |
| Evaluation | [Module 05](<Module 05 - Evaluation/README.md>) | Scores a reply for tool, document, result, and refusal. The practice set is in that module. `data/eval` stays the instructor set |
| Service | [Module 06](<Module 06 - Run it in their environment/README.md>) | Starts the agent, writes the access log, and appends the result file |

[Module 07](<Module 07 - The handoff/README.md>) leaves a runbook and two pages. The clinical safety owner is unassigned, so the pilot stays stopped. [Module 08](<Module 08 - Capstone/README.md>) does not rebuild the platform. A new ask is refused or left for a later slice.

## Truth and eval

[data/truth](data/truth) and [data/eval](data/eval) are for grading this course. The IT team did not send them. A real engagement has no clean copy and no file of known answers.

The simulation writes both. `truth` is the clean copy of the same people and events: one id per person, one spelling per district, dates as `2025-07-09`. `eval` is `cases.jsonl`, one graded question per line. Each known answer in `expected` is taken from `truth`.

The tools, the agent, and the service do not read those folders. They answer from `handover` and `corpus`. A checker compares the reply with `eval`. Opening `truth` during Module 01 skips the discovery.

## What stays out of a run

- Retinal photographs, and any use of them to train a model.
- `data/truth` and `data/eval`.
- The API key.
- A diagnosis, a referral the grader has not signed, and the 14-day draft treated as current policy.

A grader still signs every result that refers, recalls, or reassures a patient.
