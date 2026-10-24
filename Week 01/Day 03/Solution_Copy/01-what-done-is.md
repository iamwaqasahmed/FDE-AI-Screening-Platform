# 01 — What done is

This page is the map. The day is finished by the worker, the scenario log, the intake note, and the knowledge file.

Open `work/` and find each row.

| In this folder | What it is for |
| --- | --- |
| [workflow/worker.py](work/workflow/worker.py) | `wf-intake`, from `referral.submitted` to a held approval. Explained in [chapter 03](03-the-worker.md) |
| [workflow/calendar_count.py](work/workflow/calendar_count.py) | Working days from the business calendar. Explained in chapter 03 |
| [workflow/tools.py](work/workflow/tools.py) | The mock client. It was not changed |
| [scenario-log.json](work/scenario-log.json) | The log the worker writes. Explained in [chapter 04](04-the-note.md) |
| [intake.md](work/intake.md) | The one-page note. Explained in chapter 04 |
| [ea.notes.md](work/interviews/ea.notes.md) | What the enterprise architect says when asked about the hospitals. You were not asked to write this note. The check does not read it |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 05](05-knowledge.md) |

The checker prints `passed` when it can run the worker and the note has the human step and the in-flight line. It does not grade the sentences in `knowledge.md`. The trainer reads those.

The check runs `worker.py` again. A log you typed by hand is not what it grades. This copy of the log is here so you can read the rows beside chapter 04.

The event file is not in this folder. A copy of it here would fail the check.

Next: [02 — The stream](02-the-stream.md).
