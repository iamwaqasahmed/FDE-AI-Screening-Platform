# 08 — Trainer session

Students can skip this page. The answers are in chapters 01 through 07.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not open the clerk file on a screen. Do not paste the watermark into a slide or a prompt.

[dpo.notes.md](work/interviews/dpo.notes.md), [dpo.questions.txt](work/interviews/dpo.questions.txt), [coord-lead.notes.md](work/interviews/coord-lead.notes.md), and [coord-lead.questions.txt](work/interviews/coord-lead.questions.txt) are for you. The checks do not read them. Students were not asked to run an interview. The Data Protection Officer's unsigned draft, and the coordinator lead's note about a phone photo, stay in these files.

The history ids stay in [identifiers.jsonl](sources/release/history/identifiers.jsonl). The converted civil days are not in that file. Do not put an id or a converted day on a slide. The demo, from `problem_simulation`, prints four lines and nothing else:

```text
cd problem_simulation
python -m alwaha.demo.merge --profile practice
```

The first line is the mother's MRN. The second is the newborn's MRN. The third is the national id they share. The fourth is `These two MRNs stay two people.` The first three lines are computed. Do not type them onto a slide.

`pit.py` and `budget.py` are the advanced path. The three checks pass if those files are absent. Do not tell a student to delete them. When the files are present, they have to keep the invite cutoff and the budget spend. The packet copies are the shells. The work copies are the replacements. `.github/workflows/ci.yml` matches the packet. Do not add a comment to only one side.

From the course folder, the three checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check identity --release rel-w3d1 --work "../Week 03/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check labels --release rel-w3d1 --work "../Week 03/Day 01/Solution_Copy/work" --profile practice
python -m alwaha.check synthetic --release rel-w3d1 --work "../Week 03/Day 01/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is cluster, then relabel, then sample, then scan. Adjudication is on the list because the labels are used after a person has time to adjudicate. [annotate.yaml](sources/release/openapi/annotate.yaml) names the call.

## Block 2 — The clusters

Open their `dates.py`, `codes.py`, and `cluster.py` beside the files in this folder. The shell shifts a Hijri day of 1 or of 29 and later. The filled file does not. The shell keeps `END-01` by rewriting `ENDO-CLN`. The filled file changes h-wadi on and after `2024-06-01`. The shell merges a shared phone, a shared MRN, and `merge_with`, and it counts rows. The filled file skips a newborn and a twin, ignores phone and MRN, links `replaces`, and counts groups. A failed check digit stays a person in both files, because neither file reads that field.

## Block 3 — The sample

Open their `labels.py`, `synthetic.py`, and `scan.py`. ann-v1 copies the clerk fields. ann-v2 reads the text. The shell sample returns the first clerk letter, which carries the watermark and a national id. The filled sample ignores the letters. The shell scan accepts every file. The filled scan refuses the mark prefix and a history id. A clean line is still accepted.

## Block 4 — The advanced path

Open their `pit.py` and `budget.py` only if they replaced them. The suite is `Ran 8 tests` and `OK` when all eight filled tests are in place. The three checks do not call these two files. If a student deleted them, the checks can still pass and the suite cannot. Ask them to paste the two files back. Do not treat deletion as the fix.

## Block 5 — The pages

Open their `patients.md` and `classes.md`. One patient is not one row, not one MRN, and not one national id. The class table needs the pipe characters. National id, date of birth, name, and phone are phi. The note says the synthetic file was scanned before it was shared.

## Block 6 — Knowledge

The first sentence is a row count is not a patient count because a mother and a newborn can share a national id, twins can share a phone, and an MRN can be reused. The second sentence is a fidelity card compares a synthetic sample with the real specialty mix, the phrase frequencies, and the label margins. Both sentences are numbered lines. A wrapped second line does not count.

## Close

A pass is three lines: `chk-w3-identity passed.`, `chk-w3-labels passed.`, and `chk-w3-synthetic passed.`. If those three lines are on the screen, the failure table is not more work. Leave `problem_simulation/build` closed.
