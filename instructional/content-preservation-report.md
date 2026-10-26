# Content preservation report

The underlying course is intact. This pass changed how the days are found and how a few terms are explained. It did not change what a check accepts.

## Protected files

Before any Markdown edit, SHA-256 digests were recorded for every non-Markdown file outside `.git` and outside directories named `__pycache__`. Files named `.pyc` that sit directly in a day folder were included, because they were on disk. 3,459 files were hashed.

After the edit, the same 3,459 paths were hashed again.

| Result | Count |
| --- | --- |
| Paths in the baseline | 3,459 |
| Missing after the edit | 0 |
| Digest changed | 0 |

The baseline list is [protected-file-checksums.txt](protected-file-checksums.txt).

`git status` shows modifications and new files only under Markdown paths, plus this `instructional/` folder and `learning/`. No `.py`, `.csv`, `.json`, `.jsonl`, `.yaml`, or `.yml` path is modified.

## Markdown files modified

102 tracked Markdown files:

- The root [README](../README.md), with a solo-learner paragraph and two rows in the audience table. The existing reading order is still there.
- [course_design/README.md](../course_design/README.md), one paragraph pointing at this folder.
- For each of the 20 days: the day README, the student README, `04-words.md`, the finish chapter, and the solution knowledge chapter.

## New files

| Path | Who it is for |
| --- | --- |
| `learning/README.md` | Participants |
| `learning/concept-index.md` | Participants |
| `learning/review.md` | Participants. Optional. Not a deliverable |
| `Week 01/README.md` through `Week 04/README.md` | Participants |
| `instructional/` | Authors. Participants are told to leave it closed |

## Requirements left as written

Checked by diff scope and by re-reading the inserted sections against the chapters they sit in:

- Problem statements, release ids, and the Al-Waha scenario were not rewritten.
- Exercise steps, paste blocks, check commands, and pass lines were not rewritten.
- Expected deliverables in each student README were not rewritten.
- Reference solutions under `Solution_Copy/work` were not rewritten.
- Datasets and client documents in `packet/`, `sources/`, and `data/` were not rewritten.
- No day was added or removed. No mandatory topic was added as a new exercise.

The new sections say, where a reader might wonder, that they add no file and no command. The optional review page says the checks do not read it.

## Wording that was clarified, not replaced

The Week 3 Day 3 words table still says an embedding is "a vector of tokens." That phrase matches the course's own term "token vector" in `embed.py`. A plain reading under the table says what that file computes: a weight per token, including hyphenated codes, compared by cosine similarity. The table cell was left so a search for the course's phrase still lands.

## Issues seen and not patched

Recorded in [remaining-issues.md](remaining-issues.md). None of them were "fixed" by changing a check, a paste block, or a client file.
