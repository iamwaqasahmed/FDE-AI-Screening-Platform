# How to work through the modules

You are with the Al-Waha Health Cluster, a made-up health system. Nothing here is a real patient's record. The job is one assistant for patient access: referrals, appointments, reminders, and the phone line. A clinician assigns urgency. The assistant does not.

The course is four modules. Each module is five lessons. You work in order, at your own pace. Nothing in this folder is due on a clock. Finish a lesson's checks before you open the next lesson.

A file drop still has an id such as `rel-m01-l01`. That id is the pack name the checks use. It is not a morning, and it is not a deadline.

## Start here

1. Read this page once.
2. Open [Module 1, Lesson 1 — Arrival](<../Module 01/Lesson 01/Student_Copy/README.md>).
3. Read [00 — Background](<../Module 01/Lesson 01/Student_Copy/00-background.md>) before any command.
4. Follow that lesson's chapters in number order. Finish a chapter before you open the next one.

When a lesson's checks have passed, its finish chapter names the next lesson. Open that lesson's student README, then its background. Do not start a lesson inside `packet/`.

## What a lesson is made of

| Piece | What it is |
| --- | --- |
| The lesson folder README | Who the lesson is for. Students go to `Student_Copy` |
| `Student_Copy` | The lesson |
| Numbered chapters | Read from 00 upward. Each chapter ends with the next one |
| `packet/` | The files a chapter tells you to open. Not a second lesson |
| `work/` | The folder you fill in. The checks read it. Chapter 01 creates it |
| `notes/` | Worksheets, where a chapter uses them |
| `Solution_Copy` | A finished comparison. Closed until that lesson's finish chapter says the checks have passed |
| Solution `work/` | One finished example. Do not start there |

If you are working alone, the solution folder is already on disk. Leave it closed until that lesson's finish chapter says the checks have passed. Then open the solution README, not its `work/` folder. Read the solution chapters in order. The trainer chapter at the end is optional.

The [concept index](concept-index.md) is a lookup. Open it when a word from an earlier lesson comes back. It is not the next chapter. [Review questions](review.md) are optional. Nothing on that page is filed. The checks do not read it.

From Module 1, Lesson 3 on, many chapters ask you to paste a finished Python file. [How to read a replacement chapter](how-to-read-a-chapter.md) says which block is a picture of the shell and which block you paste. The section How the replacement works, on the chapter itself, is the path through that file. Read it before you paste. It adds no command.

## What to leave closed

- `Solution_Copy`, until that lesson's finish chapter.
- `problem_simulation/build`. That folder is the grader's private files. Reading it skips the lesson.
- `course_design/` and `problem_simulation/design`. Those are for facilitators.
- `instructional/`. That folder is an author record. It is not a lesson.

The case write-up is [../case/README.md](../case/README.md). The longer word list is [../case/access_language.md](../case/access_language.md). A lesson's own words chapter is enough for that lesson. Use the case list when a later chapter uses a word the lesson's list does not define.

## What you already need

The syllabus asks for working English and some familiarity with programming, databases, APIs, cloud basics, or machine learning. Not every person needs all of those. Chapter 01 of the first lesson checks for Python 3.12 or newer and tells you how to install it. Later lessons tell you to skip the installer. `python --version` should already print 3.12 or newer.

On macOS and Linux, `python3 --version` is the command to try when `python` is not found. Chapter 01 of the first lesson says the same thing. Use whichever command prints 3.12 or newer for the rest of the course.

Read the chapters in a text editor that can show the file itself, not only a preview. The preview can drop the spaces Python needs. When a chapter says to paste, paste without formatting. Any editor with a file list and a terminal is enough. [Terminal and Python basics](terminal-and-python-basics.md) is there if the words `cd`, `python -m`, or `Ran 1 test` are new. It adds no file and no command.

You do not need a cluster on the first lesson. The chapter says when a file is only the shape of a later deploy.

If you keep this folder under git, copy `Student_Copy/work` somewhere safe before you pull a newer copy of the course. From Module 2, Lesson 2 on, `work/` is already in the published tree as the blank starter. A pull can meet the files you edited. Lessons 1, 2, and 3 ignore `work/` instead. The checks read the folder either way.

## The four modules

Each module page lists its five lessons. It does not add work.

| Module | Page | You leave the module with |
| --- | --- | --- |
| 1 | [Module 1 — Prove the approach](<../Module 01/README.md>) | You leave with an approach, an intake path, an agent, and a readout you can defend. |
| 2 | [Module 2 — Put it in the cluster](<../Module 02/README.md>) | You leave with sign-in, feeds, tests, a private-cloud URL, and the Ain change. |
| 3 | [Module 3 — Make the answers honest](<../Module 03/README.md>) | You leave with honest labels, a registered adapter, citations, a measurement, and requirements. |
| 4 | [Module 4 — Run it](<../Module 04/README.md>) | You leave with guardrails, an incident you can reconstruct, a surge plan, a site drill, and a proposal. |

## The twenty lessons

| Module | Lesson | Open this | What that lesson is |
| --- | --- | --- | --- |
| 1 | 1 | [Arrival](<../Module 01/Lesson 01/Student_Copy/README.md>) | Who asked, an access request, a pipeline that rejects a secret, and two interviews. File drop `rel-m01-l01` |
| 1 | 2 | [The approach](<../Module 01/Lesson 02/Student_Copy/README.md>) | Four baselines and an approach memo. Every problem gets a family. File drop `rel-m01-l02` |
| 1 | 3 | [Intake](<../Module 01/Lesson 03/Student_Copy/README.md>) | Intake runs from referral.submitted to a held approval. It does not book. File drop `rel-m01-l03` |
| 1 | 4 | [The agent](<../Module 01/Lesson 04/Student_Copy/README.md>) | A patient can ask for status and book. A return waits for a person. File drop `rel-m01-l04` |
| 1 | 5 | [Score the proof](<../Module 01/Lesson 05/Student_Copy/README.md>) | Score the proof, publish the diagram, and answer steering. File drop `rel-m01-l05` |
| 2 | 1 | [Sign in](<../Module 02/Lesson 01/Student_Copy/README.md>) | A signed-in patient and a signed-in coordinator can open the assistant. Booking waits. File drop `rel-m02-l01` |
| 2 | 2 | [Feeds](<../Module 02/Lesson 02/Student_Copy/README.md>) | Intake and cancellation flow through cluster systems. File drop `rel-m02-l02` |
| 2 | 3 | [The receipt](<../Module 02/Lesson 03/Student_Copy/README.md>) | The receipt clock and two usability tasks. File drop `rel-m02-l03` |
| 2 | 4 | [Deploy](<../Module 02/Lesson 04/Student_Copy/README.md>) | A private-cloud URL with a health probe and a named model hash. File drop `rel-m02-l04` |
| 2 | 5 | [The Ain change](<../Module 02/Lesson 05/Student_Copy/README.md>) | A booking at Ain stays on the nightly file. A live slot is not promised. File drop `rel-m02-l05` |
| 3 | 1 | [Honest data](<../Module 03/Lesson 01/Student_Copy/README.md>) | One person, labels that follow the current guideline, and a synthetic sample. File drop `rel-m03-l01` |
| 3 | 2 | [The adapter](<../Module 03/Lesson 02/Student_Copy/README.md>) | A registered adapter inside the quota. The external fine-tune is closed. File drop `rel-m03-l02` |
| 3 | 3 | [Cite](<../Module 03/Lesson 03/Student_Copy/README.md>) | Cite an in-force document the asker is allowed to see. File drop `rel-m03-l03` |
| 3 | 4 | [Measure](<../Module 03/Lesson 04/Student_Copy/README.md>) | A draft benchmark that names the planted failures. File drop `rel-m03-l04` |
| 3 | 5 | [One fix](<../Module 03/Lesson 05/Student_Copy/README.md>) | One remeasured improvement, and requirements a later team could start from. File drop `rel-m03-l05` |
| 4 | 1 | [Guardrails](<../Module 04/Lesson 01/Student_Copy/README.md>) | The hidden attacks fail. The DPIA is filled. One access request and one deletion are handled. File drop `rel-m04-l01` |
| 4 | 2 | [The incident](<../Module 04/Lesson 02/Student_Copy/README.md>) | Reconstruct the incident. Old clinic hours leave the cache. File drop `rel-m04-l02` |
| 4 | 3 | [The surge](<../Module 04/Lesson 03/Student_Copy/README.md>) | Chat holds its latency while a batch runs. File drop `rel-m04-l03` |
| 4 | 4 | [The drill](<../Module 04/Lesson 04/Student_Copy/README.md>) | The assistant keeps serving when site-a dies. File drop `rel-m04-l04` |
| 4 | 5 | [The proposal](<../Module 04/Lesson 05/Student_Copy/README.md>) | The last connections, and a proposal that can be presented. File drop `rel-m04-l05` |

A later lesson can make a choice from an earlier lesson incomplete. Stay inside the lesson you are on.

## One person, five parts

Each student copy is written so you hold the lead, the AI or data work, the application work, the product work, and the architecture. The case folder describes a team of five when a cohort rotates those parts. A person working alone keeps all five for every lesson. Follow the student copy in front of you.

## When a command fails

Use the failure table in the chapter you are in. The finish chapter's table names the check line and the chapter to go back to. Do not copy a watermark into a ticket or a prompt to ask why a scan failed. The chapter says to delete the hit and run the scan again.

`knowledge.md` is part of done. On most lessons the checks do not grade its sentences. The trainer, or you, comparing with the solution, does. Paste the block the finish chapter gives you. Do not add a second answer file.
