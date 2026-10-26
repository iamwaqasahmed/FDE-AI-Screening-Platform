# Final student experience

## What a solo reader can do

A reader who opens the root README is sent to the learning guide, then to Week 1 Day 1. Each day folder says to leave the solution closed until the finish page. The finish page names the next morning. Week 4 Day 5 does not invent another day.

From Week 2 Day 1 through Week 4 Day 5, pasting the Replace blocks and running the finish commands produced the pass lines the chapters name. That was done from a fresh clone, with `work/` created by `prepare_work.py`, not by copying the solution into place first.

Week 1 still asks the reader to write the access request, the interviews, the memo, the brief, and the trace note. Those pages are fences in the chapters, not Replace headings, so the first runner skipped them. A later export filled them from those fences, without opening the solution, and the finish checks passed. See the day notes for Week 1 Days 1, 2, and 5.

## Quality bars

| Bar | Evidence |
| --- | --- |
| Self-sufficiency | Setup now covers `python3`, an editor, and the solo reading of `knowledge.md`. |
| Clarity | The new notes name the command and the file. They do not add a second vocabulary. |
| Completeness | Every finish command was run. Solution copies passed all twenty days. |
| Continuity | Week pages and the guide still list the same twenty days. |
| Practical reproducibility | Verified on Windows. Python 3.14 ran the cold start, the handwritten Week 1 pages, and a later Week 2 Day 5 export with an empty build. That rerun passed the four student checks and the four solution checks. The earlier `logs/pass1/w2d5.log` failure is stale. Python 3.12 ran the second full pass and the grader suite (`Ran 368 tests`, `OK`). macOS was not executed. |
| Conceptual depth | The existing "How the replacement works" sections were left in place. This pass did not replace them with a shorter summary. |
| Navigability | Unreachable-page count from the root README was zero for student chapters. |
| Solution quality | Solution checks passed. A few solution Python files have comments the chapter paste does not. The check accepts the chapter paste on the days the runner could paste. |
| Content integrity | Protected hashes: 0 changed. Paste blocks were not rewritten. |
| End-to-end coherence | One client, Al-Waha, from the access request through the proposal. The traps in the facilitator maps were not answered in the new pages. |

## Limit

This is one simulated run plus the scanners. It is not a classroom. A reader can still miss a sentence. The failure tables remain the recovery path.
