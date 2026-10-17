# Problem simulation

The factory for the Hartland engagement. It builds the world. It is not the client brief.

Hartland Regional Health Authority is an invented regional health service that reports to a Ministry of Health. Nothing here is a real health system, and nothing here is a protocol for patient care.

The authority asked for an AI Screening Platform. The files describe diabetic eye screening: a photograph of the back of the eye, a person who reads it, a letter, and sometimes a referral to an eye specialist.

No health background is required. The words are in [Health language](<../Module 01 - Problem Discovery/01-health-language.md>).

## Start here

Participants start at the [course guide](../README.md), then [who this course is for](../target_audience.md), then [Module 01](<../Module 01 - Problem Discovery/README.md>). This folder is how the world was built. Leave `config.yaml` and `src/` closed during Module 01.

The module is a sequence. It tells you when to open the tables. The plain-language map of those tables is [data/README.md](../data/README.md).

## The client drop

| Folder | What it is |
|---|---|
| [data/handover](../data/handover) | The extract IT would send: registry, grader workbook, image indexes, letters, referrals, vendor scores, a data dictionary, and a cover note |
| [data/corpus](../data/corpus) | The written rules a service may retrieve: the issued procedure, a draft urgent pathway, letter templates, the data-protection rule, grade codes, and the clinic note |

`data/handover/README.txt` is the authority's cover note. It is part of the drop. This file is the course note about how the world was made.

The indexes name image files. The picture bytes are not in the drop. A capture is a path, a date, and a row.

## Closed during Module 01

Opening these skips the discovery.

| Path | Why it stays closed |
|---|---|
| `data/truth` | Clean hidden copy of the same people and events. Used for grading |
| `data/eval` | Questions with known answers |
| `config.yaml` | The quotas and rules used to generate the files |
| `src/` | The Python that writes `data/` |

The authored rule text also lives in `corpus/` in this folder. Read the copy in `data/corpus`. It is the same text, and it is the copy the module points at.

## What the later modules study

The reference agent, retriever, and tools. Participants read that code and run the checkers. They do not regenerate this world to finish the course.

- **Tools** read the handover: who is on the registry, who has a photo, who has a result, who was referred.
- **Retrieval** reads the corpus: which rule is in force, which letter to draft, what a grade code means, what the service must refuse.
- A grader still signs every result that changes care. The agent prepares a queue and a letter. A diagnosis from a retinal photo is outside what it is allowed to do.

The practice is [FDE.md](../FDE.md).

## Rebuild

This command is for the person maintaining the simulation. Participants leave it unrun. Finishing the course uses the extract already in `data/`.

Install `requirements.txt` in this folder first. One seed rewrites `data/truth`, `data/handover`, `data/corpus`, and `data/eval`.

```text
python -m problem_simulation.src.run
```
