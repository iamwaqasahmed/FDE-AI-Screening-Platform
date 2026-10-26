# Documentation validation report

Checked after the navigation edit and the link repair. This is an expert review of the pages, plus mechanical checks. It is not a claim that a classroom will have no questions.

## Links

A checker walked Markdown links in the root README, the course-design README, `learning/`, `instructional/`, each week page, and each day's README, student README, words chapter, finish chapter, and solution knowledge chapter. Fenced code blocks were ignored. `http` and `https` links were not fetched. Percent-encoded spaces were decoded before the path was resolved. Angle-bracket destinations were taken whole.

The first run truncated any destination that still contained a raw space. Those destinations were rewritten with `%20`, which is the form the release notes in this repository already use. Angle-bracket links in the new guides were left as written.

The last run of the first pass checked 1,815 links in 118 files. None were missing.

A later pass added How the replacement works to 37 lab chapters. The first draft of the solution-side pointer used one `../` too many. Those 37 links were corrected to `../Student_Copy/`. They resolve. Fenced `text` blocks in those chapters were hashed before and after the insert and did not change. Links to `work/` files inside the original chapters still point at files that `prepare_work.py` creates. Those files are not in the repository until that command runs. That was already true.

## Paths that were walked as a student

1. Root README to [learning/README.md](../learning/README.md) to [Week 1, Day 1](<../Week 01/Day 01/Student_Copy/README.md>).
2. That README's order table still starts at `00-background.md` and ends at the finish chapter. "Where you are" sits above the deliverables and does not replace them.
3. The finish chapter's new section comes after Done, points at the solution README, and points at Week 1 Day 2.
4. Week 1 Day 5's finish section points at Week 2 Day 1. Week 4 Day 5's finish section says the rehearsal ends and does not invent a Day 6.
5. The Week 3 Day 2 plain reading matches `adapter.py` as the chapter pastes it: select the approved `lora-local` row, copy its hash, do not run a trainer. `qlora.py` maps rank to a GPU count inside the quota.
6. The Week 3 Day 3 plain reading matches the replacement docstring in the index chapter: tokens, hyphenated codes, a weight per token, cosine similarity.
7. The Week 2 Day 3 plain reading was corrected to the knowledge sentence already on the finish page, and to the clock guide's instruction to advance the pinned time rather than sleep.

## Heading structure

New sections are level-2 headings in files that already have one level-1 title: "Where you are", "What you open next", "A plain reading", "Carry this forward". They do not sit inside tables or fenced blocks. On the words pages they sit after the last table and before the existing `Next:` line.

## Terminology

The concept index definitions were taken from the words pages and the plain readings. Spot checks: handoff and summary are rows on the Week 4 Day 5 words page; the health probe is a row on the Week 2 Day 4 words page; the judge calibration note is on the Week 3 Day 4 words page.

## What was not validated

- Live runs of `python -m alwaha.check`. See [remaining issues](remaining-issues.md).
- Every pre-existing link in packet documents and in chapters that this pass did not edit. The checker covered the words and finish chapters in full, including their older links, for the 20 days. It did not cover every Markdown file under `packet/`.
- The installer URLs in chapter 01.

## Checksums

Non-Markdown preservation is in [the preservation report](content-preservation-report.md). 3,459 files matched their pre-edit digest.
