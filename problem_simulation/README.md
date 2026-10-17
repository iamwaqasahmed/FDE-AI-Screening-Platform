# Problem simulation

This folder is the factory for a fictional client engagement. It builds the world. It is not the client brief.

Hartland Regional Health Authority is an invented regional health service that reports to a Ministry of Health. Nothing here is a real health system, and nothing here is a protocol for patient care. The authority's request is an AI Screening Platform. Diabetic eye screening is the program the files describe: a photograph of the back of the eye, a person who reads it, a letter, and sometimes a referral to an eye specialist.

No health background is required. The words are taught in [Health language](<../Module 01 - Problem Discovery/01-health-language.md>).

## Where to start

Read the [course journey](../README.md) first, then [who an FDE is](../FDE.md), then [Module 01 — Problem Discovery](<../Module 01 - Problem Discovery/README.md>).

The module is a sequence. It tells you when to open the tables. The plain-language map of those tables is [data/README.md](../data/README.md).

## What you are given

Two folders are the client drop.

| Folder | What it is |
|---|---|
| [data/handover](../data/handover) | The extract IT would send: registry, grader workbook, image indexes, letters, referrals, vendor scores, a data dictionary, and a cover note |
| [data/corpus](../data/corpus) | The written rules a service may retrieve: the issued procedure, a draft urgent pathway, letter templates, the data-protection rule, grade codes, and the clinic note |

`data/handover/README.txt` is the authority's cover note. It is part of the drop. This file is the course note about how the world was made.

The indexes name image files. The picture bytes are not in the drop. A capture is a path, a date, and a row.

## What to leave closed during Module 01

| Path | Why it stays closed |
|---|---|
| `data/truth` | Clean hidden copy of the same people and events. Used for grading |
| `data/eval` | Questions with known answers |
| `config.yaml` in this folder | The quotas and rules used to generate the files |
| `src/` in this folder | The Python that writes `data/` |

Opening those skips the discovery. The authored rule text also lives in `corpus/` here. Read the copy in `data/corpus`. It is the same text, and it is the copy the module points at.

## What the later work uses

The system you eventually build is an agent with retrieval and tools.

- Tools read the handover: who is on the registry, who has a photo, who has a result, who was referred.
- Retrieval reads the corpus: which rule is in force, which letter to draft, what a grade code means, what the service must refuse.
- A grader still signs every result that changes care. The agent does not invent a diagnosis from a retinal photo.

The skill list for that work is in [FDE.md](../FDE.md).

## Rebuilding the world

After Module 01, the same files can be regenerated from this folder:

```text
python -m problem_simulation.src.run
```

Run that from the repository root, with the packages in `requirements.txt` installed. One seed rewrites `data/truth`, `data/handover`, `data/corpus`, and `data/eval`.
