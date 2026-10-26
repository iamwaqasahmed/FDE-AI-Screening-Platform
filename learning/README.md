# How to work through the four weeks

You are with the Al-Waha Health Cluster, a made-up health system. Nothing here is a real patient's record. The job is one assistant for patient access: referrals, appointments, reminders, and the phone line. A clinician assigns urgency. The assistant does not.

These four weeks are one rehearsal. Weeks 5 and 6 are a different client. They are not in these folders.

## Start here

1. Read this page once.
2. Open [Week 1, Day 1](<../Week 01/Day 01/Student_Copy/README.md>).
3. Read [00 — Background](<../Week 01/Day 01/Student_Copy/00-background.md>) before any command.
4. Follow that day's chapters in number order. Finish a chapter before you open the next one.

When a day is done, its finish chapter names the next folder. Open that folder's student README, then its background. Do not start a day inside `packet/`.

## What a day is made of

| Piece | What it is |
| --- | --- |
| The day folder README | Who the day is for. Students go to `Student_Copy` |
| `Student_Copy` | The lesson |
| Numbered chapters | Read from 00 upward. Each chapter ends with the next one |
| `packet/` | The files a chapter tells you to open. Not a second lesson |
| `work/` | The folder you fill in. The checks read it. Chapter 01 creates it |
| `notes/` | Worksheets, where a chapter uses them. Some days tell you to keep them out of `work/` |
| `Solution_Copy` | A finished comparison. Closed until the finish chapter says the day is done |
| Solution `work/` | One finished example. Do not start there |

If you are working alone, the solution folder is already on disk. Leave it closed until that day's finish chapter says the checks have passed. Then open the solution README, not its `work/` folder. Read the solution chapters in order. The trainer chapter at the end is optional.

The [concept index](concept-index.md) is a lookup. Open it when a word from an earlier day comes back. It is not the next chapter. [Review questions](review.md) are optional. Nothing on that page is filed. The checks do not read it.

Several finish pages say the trainer reads `knowledge.md`. Working alone, you do that comparison yourself. After Done is true, open the solution knowledge chapter and set your sentences beside it. The checks still do not grade those sentences.

From Week 1 Day 3, many chapters ask you to paste a finished Python file. [How to read a replacement chapter](how-to-read-a-chapter.md) says which block is a picture of the shell and which block you paste. The section How the replacement works, on the chapter itself, is the path through that file. Read it before you paste. It adds no command.

## What to leave closed

- `Solution_Copy`, until the finish chapter.
- `problem_simulation/build`. That folder is the grader's private files. Reading it skips the day.
- `course_design/` and `problem_simulation/design`. Those are for facilitators.
- `instructional/`. That folder is an author record. It is not a lesson.

The case write-up is [../case/README.md](../case/README.md). The longer word list is [../case/access_language.md](../case/access_language.md). A day's own words chapter is enough for that day. Use the case list when a later chapter uses a word the day's list does not define.

## What you already need

The syllabus asks for working English and some familiarity with programming, databases, APIs, cloud basics, or machine learning. Not every person needs all of those. Chapter 01 of each day checks for Python 3.12 or newer and tells you how to install it. Later days tell you to skip the installer when `python --version` already prints 3.12 or newer.

On macOS and Linux, `python3 --version` is the command to try when `python` is not found. Chapter 01 of each day says the same thing. Use whichever command prints 3.12 or newer for the rest of that day.

Read the chapters in a text editor that can show the file itself, not only a preview. The preview can drop the spaces Python needs. When a chapter says to paste, paste without formatting. Any editor with a file list and a terminal is enough. [Terminal and Python basics](terminal-and-python-basics.md) is there if the words `cd`, `python -m`, or `Ran 1 test` are new. It adds no file and no command.

You do not need a cluster on the first morning. The chapter says when a file is only the shape of a later deploy.

If you keep this folder under git, copy `Student_Copy/work` somewhere safe before you pull a newer copy of the course. From Week 2 Day 2 on, `work/` is already in the published tree as the blank starter. A pull can meet the files you edited. Week 1 Days 1 to 3 ignore `work/` instead. The checks read the folder either way.

## How the weeks move

Each week page says what that week already contains. It does not add work.

| Week | Page | You leave the week with |
| --- | --- | --- |
| 1 | [Week 1](<../Week 01/README.md>) | A small working proof, a picture of the design, and a note that says why |
| 2 | [Week 2](<../Week 02/README.md>) | The assistant signed in, and deployed on the private cloud |
| 3 | [Week 3](<../Week 03/README.md>) | Models fitted to the cluster, answers from the cluster's documents, and an evaluation |
| 4 | [Week 4](<../Week 04/README.md>) | Security, monitoring, a design that can take a surge, and a plan for running it |

New files arrive each morning. A choice that was reasonable yesterday can be incomplete today. Stay inside the day you are on.

## The twenty days

| Day | Open this | What that day is |
| --- | --- | --- |
| Week 1 Day 1 | [Student copy](<../Week 01/Day 01/Student_Copy/README.md>) | Arrival. Access, a pipeline that rejects a secret, two interviews |
| Week 1 Day 2 | [Student copy](<../Week 01/Day 02/Student_Copy/README.md>) | The leaders' numbers. Baselines and an approach memo |
| Week 1 Day 3 | [Student copy](<../Week 01/Day 03/Student_Copy/README.md>) | Intake, from a submitted referral to a held approval |
| Week 1 Day 4 | [Student copy](<../Week 01/Day 04/Student_Copy/README.md>) | A patient can ask for status and book. A return waits for a person |
| Week 1 Day 5 | [Student copy](<../Week 01/Day 05/Student_Copy/README.md>) | Score the proof, draw it, and answer steering |
| Week 2 Day 1 | [Student copy](<../Week 02/Day 01/Student_Copy/README.md>) | Sign-in for a patient and a coordinator. Booking waits |
| Week 2 Day 2 | [Student copy](<../Week 02/Day 02/Student_Copy/README.md>) | Referrals and cancellations arrive from cluster systems |
| Week 2 Day 3 | [Student copy](<../Week 02/Day 03/Student_Copy/README.md>) | Tests, the receipt clock, and two usability tasks |
| Week 2 Day 4 | [Student copy](<../Week 02/Day 04/Student_Copy/README.md>) | Deploy on the private cloud, with a health probe |
| Week 2 Day 5 | [Student copy](<../Week 02/Day 05/Student_Copy/README.md>) | The Ain change. A live slot there is not promised |
| Week 3 Day 1 | [Student copy](<../Week 03/Day 01/Student_Copy/README.md>) | One person, labels under the new guideline, a synthetic sample |
| Week 3 Day 2 | [Student copy](<../Week 03/Day 02/Student_Copy/README.md>) | A registered adapter. The external fine-tune is closed |
| Week 3 Day 3 | [Student copy](<../Week 03/Day 03/Student_Copy/README.md>) | Cite an in-force document the asker may see |
| Week 3 Day 4 | [Student copy](<../Week 03/Day 04/Student_Copy/README.md>) | A draft benchmark and the workshop |
| Week 3 Day 5 | [Student copy](<../Week 03/Day 05/Student_Copy/README.md>) | One remeasured fix, and the requirements |
| Week 4 Day 1 | [Student copy](<../Week 04/Day 01/Student_Copy/README.md>) | Guardrails, the DPIA, access, and deletion |
| Week 4 Day 2 | [Student copy](<../Week 04/Day 02/Student_Copy/README.md>) | The incident, the board, and the hours cache |
| Week 4 Day 3 | [Student copy](<../Week 04/Day 03/Student_Copy/README.md>) | Chat holds its latency while a batch runs |
| Week 4 Day 4 | [Student copy](<../Week 04/Day 04/Student_Copy/README.md>) | Site-a dies. The rent-versus-buy note |
| Week 4 Day 5 | [Student copy](<../Week 04/Day 05/Student_Copy/README.md>) | The last connections, and the proposal |

## One person, five parts

Each student copy is written so you hold the lead, the AI or data work, the application work, the product work, and the architecture. The case folder describes a team of five when a cohort rotates those parts. Follow the student copy in front of you.

## When a command fails

Use the failure table in the chapter you are in. The finish chapter's table names the check line and the chapter to go back to. Do not copy a watermark into a ticket or a prompt to ask why a scan failed. The chapter says to delete the hit and run the scan again.

`knowledge.md` is part of done. On most days the checks do not grade its sentences. The trainer, or you, comparing with the solution, does. Paste the block the finish chapter gives you. Do not add a second answer file.
