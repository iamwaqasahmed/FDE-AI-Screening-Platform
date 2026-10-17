# Problem simulation

This folder builds a fictional client engagement for forward deployed engineer practice. Hartland Regional Health Authority reports to a Ministry of Health. Nothing here is a real health system, and nothing here is a protocol for patient care.

The authority's request is an AI Screening Platform. The records and the written rules are the world you work in. Start with [problem discovery](../problem_discovery.md). That module tells you when to open the tables.

## What you are given

Two folders at the repository root are the client drop.

| Folder | What it is |
|---|---|
| [data/handover](../data/handover) | The extract IT would send: registry, grader workbook, image manifests, letters, referrals, vendor scores, a data dictionary, and a cover note |
| [data/corpus](../data/corpus) | The written rules a service is allowed to retrieve: procedures, letter templates, the data-protection rule, grade codes, and the pilot clinic note |

`data/handover/README.txt` is the authority's cover note. It is part of the drop. This file is the course note.

The manifests name image files. The bytes are not in the drop. A capture is a path, a date, and a row in the workbook.

## What you are not given

`data/truth` and `data/eval` are for grading. They are not inputs. The Python in this folder and `config.yaml` are how the world was generated. They are not the client brief. Opening them skips the discovery the exercise is for.

## What the later work uses

The system you eventually build is an agent with retrieval and tools.

- Tools read the handover tables: who is on the registry, who has a photo, who has a result, who was referred.
- Retrieval reads the corpus: which rule is in force, which letter to draft, what a grade code means, what the service must refuse.
- A grader still signs every result that changes care. The agent does not invent a diagnosis from a retinal photo.

The skill list for that work is in [FDE.md](../FDE.md).
