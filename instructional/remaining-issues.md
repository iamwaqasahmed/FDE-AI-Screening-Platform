# Remaining issues

These were left alone because changing them would change the course, hide material the repository already publishes, or assert a fact the files do not support.

## The implementation is a guided replacement

From Week 1 Day 3 onward, the chapter states what the shell gets wrong and then gives the file to paste. The checks look for phrases inside those files. The section How the replacement works now walks the path through that file. The paste itself stays. Removing it, or making the reader derive a second design, would change the course.

## Knowledge answers are on the finish page

Several finish chapters include the sentences that belong in `knowledge.md`. That is the existing guidance. The solution knowledge chapter explains why those sentences match the case. The optional review asks the same ideas without printing a second answer key.

## Solutions sit next to the morning chapters

A clone contains every `Solution_Copy`. The day pages now say to leave that folder closed until Done is true. The folders were not moved, renamed, or encrypted. A reader can still open them early. That is a property of publishing the course as one tree.

## Later days are on disk during Day 1

The same is true of Week 4. Each background says to stay inside today's folder. The repository was not split into timed releases. The root README already describes the releases as files the days use, not as a server that withholds them.

## "Vector of tokens"

The words table and the embed docstring use that phrase for a map from token to weight. A reader who has met neural embeddings will hear a different object. The plain reading on Week 3 Day 3 states what this day's file does. The table cell and the docstring were not changed, because the finish chapter tells the reader to search for `local-embed: a token vector, including codes.`

## Facilitator traps stay in the day maps

`course_design/day-map-week-*.md` names the mistake each world is built to invite. [The curriculum map](curriculum-understanding-map.md) repeats those traps so a later editor does not sand them off. Neither file is linked from the morning chapters. `instructional/` is listed as closed on the root README.

## Stray bytecode in some day folders

`.pyc` files are present under a few `packet/` and `app/` trees, outside `__pycache__` in at least the Week 1 Day 4 listing observed during the packet comparison. They were hashed with the other non-Markdown files and were not modified. They were not deleted. They are not part of the lesson.

## `data/rel-*` is not a mirror of `packet/`

The release pack under `data/rel-wNdN` is the morning's new files. The student packet also carries kickoff pages, shells, and templates, often under `packet/release` plus `packet/kickoff`. The chapters open `packet/`. No merge of the two trees was attempted.

## External links were not re-checked

Chapter 01 still points at python.org, git-scm.com, and `https://github.com/iamwaqasahmed/FDE-AI-Screening-Platform.git`. Those URLs were already in the course. This pass did not fetch them. If the clone URL is stale, that is a pre-existing setup fact, not something this edit verified.

## The syllabus file is still a PDF export

`FDE Program Syllabus.md` still contains `Original PDF page` comments. It is the accepted program text. It was not cleaned up.

## This review did not run every grader in the course

An earlier pass did not run `alwaha.check`. A later pass ran the Week 1 solution checks, after building `rel-w1d1` through `rel-w1d5` for `practice`. Those Week 1 checks printed `passed`. Weeks 2 through 4 were not run in that pass. The checks write under `problem_simulation/build`, which the course tells readers to leave closed.

## An expert read is not a classroom

The walk-through in the validation report is one reader who already knew the day maps. It is not evidence that every participant will pass a day without questions. The failure tables remain the recovery path when a check fails.
