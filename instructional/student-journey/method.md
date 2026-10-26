# Student-journey method

Author record. Participants leave `instructional/` closed. This file is the brief the simulation follows. It does not add a lesson.

## Persona

A motivated learner who meets the syllabus prerequisites and has no instructor. Every page is read through two lenses:

- A programmer with no machine-learning or healthcare background.
- A data or machine-learning person with little terminal, git, testing, or deployment experience.

The environment the runner uses is Windows with `cmd`, as the chapters direct, plus a text editor and Python 3.12 or newer. macOS and Linux are reviewed by reading. They are not executed on this machine.

## What a Day N student simulation may see

- Student-allowed files up to Day N.
- The cumulative knowledge record for Days 1 to N-1.
- Earlier pages, reopened through links, as a real student would.

It does not open that day's `Solution_Copy` before the attempt. It does not open `course_design/`, `problem_simulation/design`, `problem_simulation/build`, `instructional/`, or any later day's folder.

The coordinating pass holds the author view: day maps, traps, edits, and preservation. That view is not given to a student-simulation step.

## Question checklist

At every paragraph, instruction, and activity:

- Understanding: meaning on a first reading, terms, background, hidden assumptions, examples.
- Context: why this page, why this activity, which Al-Waha problem, how it connects.
- Practical execution: which file, which command, which input, which output, what failure looks like, how to know it is done.
- Learning progression: taught before it is needed, consistent, difficulty reasonable.
- Solution review: matches the exercise, explains the decision, can be compared with the student's file.

## Reader brief

1. Use the persona and both lenses.
2. Know only the record so far, plus today's pages.
3. Read every file completely. Read long files in sections. Record lines and a content hash when the coverage row is filled.
4. Apply the question checklist. Flag a sentence that brings in an assumption, a requirement, or a term without explaining it.
5. Classify every concept: taught earlier (where), introduced now (adequately or not), or assumed.
6. Answer every "Before you paste, say" prompt and every worksheet from the pages alone.
7. Check the background recap against the record. Check that the README deliverables, the finish page's Done, and the solution's `01-what-done-is` agree.
8. Report each finding with: id, file and line, quote, the student's question, category, severity, evidence, proposed text in the course voice, placement, risk to protected content, and whether it is an intended challenge.

## Runner brief

1. Work only in the scratch copy. Run commands through `cmd /c` as printed, from the folder the chapter names. `PYTHONIOENCODING=utf-8` is for capture only.
2. Paste only by extracting the fenced block exactly. Do not hand-edit pasted code.
3. Write non-paste deliverables from the chapter alone. Do not look at the solution or at `build/` while attempting the day.
4. Capture every output and compare it with the "You should see" block. Ignore timings and dashed lines the chapter already says can differ.
5. Run the checks on the untouched starter first, and map each failure line to a table row.
6. Negative set, where the chapter documents the recovery: wrong folder; build skipped; picture pasted instead of the Replace block; indentation lost; missing or placeholder `knowledge.md`; watermarked file copied into `work/`; wrong or missing `--release`.
7. If a step blocks, follow the failure table up to three times. Then record a critical finding. After a documentation fix, re-run from the improved text.
8. Run the solution check from the Solution README after the attempt.
9. Report commands, outputs, mismatches, the failure-line map, negative results, and any block.

## Solution brief

1. Start only after the day's checks pass, or after a block is logged.
2. Read every solution Markdown file, the solution `work/` and `sources/`, and the day's `data/` Markdown.
3. Each solution chapter answers its morning chapter, says why, and can be compared file by file. The trainer chapter must not be the only place an essential fact appears.
4. Compare each Replace block with the solution file, and each picture block with the packet starter.
5. Check "Carry this forward" against the next day's background, and the knowledge answers against the case.

## Validator

- Pass 1: re-read every Student and Solution chapter of the day.
- Pass 2: every concept used has an explanation, or a reminder and a link back.
- Pass 3: re-trace the practical steps against the improved text and the captured run.
- Pass 4: navigation. Order tables, Next lines, and the finish page's step into the next day.
- Pass 5: solution alignment after the edits.
- Pass 6: protected files and protected structures unchanged. New facts have evidence. Traps are not answered early.
- Comprehension: state what the day taught, why it mattered to Al-Waha, and how the work was verified.

## Triage

1. Class: avoidable confusion (fix), intended challenge (keep, with a pointer that gives nothing away), protected-content defect (record), or out of scope (record).
2. Severity: critical means blocked or a wrong instruction. High means a needed concept is untaught or a stall is likely. Medium means ambiguity or a missing reason, output, or self-check. Low means polish.
3. Every fix cites evidence: a file and line, or a log line.
4. Merge duplicate findings.
5. Placement: a short inline note, a table row, a failure row, or an explainer page.

## Edits

1. Prose only. Leave fenced blocks, Replace headings, pass lines, existing failure keys, order tables, Done sections, and search tables untouched.
2. Prefer additions. Log every changed existing sentence.
3. Write in the course voice: short sentences, named files, named commands, named pass lines.
4. Add nothing from later days, and nothing that answers a trap.
5. If an addition would run past about 25 lines in a chapter already over about 400 lines, put it in `learning/explainers/` and link it where the topic is first used.
6. Shared files (`learning/`, week READMEs, the root README, `instructional/`) are edited in one place at a time.
7. An edit to an earlier day is re-checked on that day and logged.
8. Optional questions belong in `learning/review.md`. They are not filed.
9. Concept-index rows are added only for terms the pages teach.
10. Each day's patch is saved under the scratch `logs/patches/` folder.

## Severity and findings

A finding records: id, file, line, quote, the student's question, category, severity, evidence, proposed text, placement, protected-content risk, and class (fix, keep, record).
