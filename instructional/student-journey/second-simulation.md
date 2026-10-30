# Second simulation

The second run is the Python 3.12 pass over the same clone, after the prose edits. The edits did not change paste blocks or check commands, so the 3.12 pass repeats the practical journey rather than a different course.

What it repeats:

1. Every release build named in a setup chapter.
2. `prepare_work.py` for every day.
3. Every Replace block the runner can attach to a work path.
4. Every finish-page check, on the student work and on the solution work.

What the integrated read checked besides the commands:

- The entry path still starts at the learning guide and Module 1 Lesson 1.
- `python3` is now stated before a macOS or Linux reader meets a failing `python` command.
- A solo reader is told to compare `knowledge.md` with the solution knowledge chapter. The checks still do not grade it.
- The concept index term for the release id matches the background.
- No new page reveals a facilitator trap. The traps stay in `course_design/` and in the author note outside the repo.

The Python 3.12 summary matches the cold start for Module 2 Lesson 1 through Module 4, Lesson 5. The first Python 3.14 summary does not: Module 2 Lesson 5 printed `Build rel-m02-l04 and rel-m02-l05 first.` after both builds had exited 0. The 3.12 log and the cold-start log for that day passed. A later export, with `problem_simulation/build` removed first, ran that day again on Python 3.14 and passed the four student checks and the four solution checks. The `logs/pass1/m02_l05.log` failure is stale. A cold start then deleted the build and that day's `work/` before each day. Module 1 Lesson 3, Module 1 Lesson 4, and Module 2 Lesson 1 through Module 4, Lesson 5 passed from that empty state. The grader suite under Python 3.12 printed `Ran 368 tests` and `OK`. That suite was not run again for the handwritten pages.

The added prose was read again from `git diff` on Markdown (99 added lines, 4 removed) and from `learning/terminal-and-python-basics.md`, which is untracked and was read in full. The additions are the `python3` note, one failure-table row, the editor and solo-reader notes, the `rel-m01-l01` wording, and the author records. They do not contradict each other. They do not name a facilitator trap. The Lesson 2 chapter already tells the reader which family fails for `p-clock`, `p-slots`, and `p-triage`. That text was already in the chapter. It was not part of this diff.

The handwritten export then passed Module 1 Days 1, 2, and 5. Details are in [technical validation](technical-validation.md).

## Integrated read

A later pass read each background's "What today is" against the previous solution chapter's "Carry this forward", then the finish page's "What you open next".

Module 1 runs from arrival to a scored agent. Lesson 1 does not build the assistant. Lesson 2 measures the leaders' numbers and keeps triage blocked. Lesson 3 stops intake at a held approval. Lesson 4 lets a patient ask for status, and a letter stays data. Lesson 5 scores a timeout that does not book and leaves G2 open. The Module 2 Lesson 1 background opens on that same result: a new `his-wadi` spec, and booking still waits.

Module 2 reuses Module 1's status tool under the name `status`, and it says so. Lesson 1 is sign-in. Lesson 2 replaces polling with the `eref` webhook and keeps the mart clock off the truth. Lesson 3 moves the receipt onto the case clock. Lesson 4 is a private-cloud URL and a probe, not a live cluster. Lesson 5 queues Ain for the nightly file. The Module 3, Lesson 1 background separates that sign-in note from the waitlist person.

Module 2 builds on leakage and retrieval. Lesson 1 is one person, not one row. Lesson 2 selects a registered adapter and does not train it. Lesson 3 cites an in-force span. Lesson 4 names the planted failures and does not pick a winner. Lesson 5 remeasures one retrieval failure and leaves G2 open. The Module 4, Lesson 1 background opens the attack window on that result.

Module 2 can be told as one engagement. Guardrails and the DPIA, then a board that is not CPU, then chat holding a reserve while a batch runs, then site-b after site-a dies, then a proposal that does not start with triage and does not build the sponsor sentence. Module 4, Lesson 5 does not open a Lesson 21.

The outside names added in this pass sit on the day that already teaches the idea: RAG on Module 1 Lesson 2, tool calling and prompt injection on Module 1 Lesson 4, unit test and end-to-end test on Module 2 Lesson 3, PEFT on Module 3, Lesson 2, vector database on Module 3, Lesson 3, prompt injection again on Module 4, Lesson 1, SLI on Module 4, Lesson 2, batching on Module 4, Lesson 3, and load balancing on Module 4, Lesson 4. None of those sentences names a facilitator trap.
