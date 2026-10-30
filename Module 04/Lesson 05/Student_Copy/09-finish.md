# 09 — Finish

[Chapter 08](08-the-pages.md) filed the pages and both notes. This chapter replaces `knowledge.md` and runs the five checks. Use the failure table at the bottom only when a check fails. It is not more work.

You do not build the pack again. Scroll to the heading Replace the knowledge file. That is the only paste on this page. There is no picture above it.

## Replace the knowledge file

Chapter 01 copied [knowledge.md](packet/templates/knowledge.md) to [work/knowledge.md](work/knowledge.md). The full path is `Module 04/Lesson 05/Student_Copy/work/knowledge.md`. The copy has two empty numbered lines. Do not type into the empty lines. This block replaces the whole file. It does not replace the template in `packet/templates`.

1. Open the work file named here, [work/knowledge.md](work/knowledge.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `session.cancelled`, then `p-clock`.

```text
# Knowledge

1. A new consultant leave creates session.cancelled.
2. p-clock is first. p-waitlist depends on identity.
```

Open [work/knowledge.md](work/knowledge.md). Line 1 says a new consultant leave creates `session.cancelled`. Line 2 says `p-clock` is first and `p-waitlist` depends on identity. Both answers stay on their numbered lines. The first numbered line contains `session.cancelled`. The second names a first problem that is not `p-triage` and not `vendor-bot`, and it names a dependency. A second sentence on the next line, without a number, does not count.

Stay on this page. The next heading is Run the checks. Do not open the failure table unless a check prints `failed`.

## Run the checks

The suite window is inside `work/`. Leave it. Open a new terminal in the course folder. If `dir` already shows `alwaha`, you are inside `problem_simulation`. Skip the `cd` line and run the python lines. `--work` is required. `--profile practice` is required. Run one python line, read the line it prints, then run the next python line. Do that five times, in this order. There is no sixth command. The first line, `chk-m04-l05-integrate passed.`, is not the end. Stop when a line says `failed` and use the table for that line. You are done with the checks only when all five passed lines are on the screen.

```text
cd problem_simulation
python -m alwaha.check integrate --release rel-m04-l05 --work "../Module 04/Lesson 05/Student_Copy/work" --profile practice
python -m alwaha.check ops --release rel-m04-l05 --work "../Module 04/Lesson 05/Student_Copy/work" --profile practice
python -m alwaha.check rcp --release rel-m04-l05 --work "../Module 04/Lesson 05/Student_Copy/work" --profile practice
python -m alwaha.check readout --release rel-m04-l05 --work "../Module 04/Lesson 05/Student_Copy/work" --profile practice
python -m alwaha.check individual --release rel-m04-l05 --work "../Module 04/Lesson 05/Student_Copy/work" --profile practice
```

You should see five lines, in this order:

```text
chk-m04-l05-integrate passed.
chk-m04-l05-ops passed.
chk-m04-l05-rcp passed.
chk-readout passed.
chk-individual-m04-l05 passed.
```

There is no sixth passed line. If you see those five passed lines, do not work the table. Scroll to the last heading, Done.

## If a check fails

This table is not a paste. Do not copy it into a file. Use it only when a check prints `failed`.

A failed check prints `failed`, then one or more lines that start with a dash. The word before `failed` names the check. Read every dash line before you pick a row. Then run that check again. A failure does not print a lag, a survey count, a SAR figure, a hash, or the attack text. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

A bus miss is two lines. A late-leave miss on the integrate check is two lines. A gates miss is two lines. An empty operations page is three lines. An empty readout is the long list. Do not stop on the first dash line of a pair. Do not treat one line as the pair.

| What it prints | Where to go |
| --- | --- |
| `Build rel-m04-l05 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-m04-l05`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the check again. Each of the five checks can print this line |
| `staff sign-in rejects a staff role` | This is `chk-m04-l05-integrate`. The message does not name the actor. Open [staff.json](packet/release/iam/staff.json) and search for `staff`. [Chapter 06](06-the-connections.md). Paste `signin.py` and `test_signin.py` again. You should see `Accept a staff role. Refuse a service token.` Label the return: a staff role is accepted |
| `a service token is accepted as staff` | This is `chk-m04-l05-integrate`. The message does not name the actor id. Open [staff.json](packet/release/iam/staff.json) and search for `service`. [Chapter 06](06-the-connections.md). Paste `signin.py` and `test_signin.py` again. You should see `Accept a staff role. Refuse a service token.` Label the return: the service token is refused |
| `the bus drops an event with an unknown field`, then `the bus misses session.cancelled` | These two lines together are the bus. This is `chk-m04-l05-integrate`. Do not collapse them into one line. Open [events.jsonl](packet/release/bus/events.jsonl) and search for `evt-extra`. A row is one long line. [Chapter 06](06-the-connections.md). Paste `bus.py` and `test_bus.py` again. You should see `Keep the event, including a field this consumer does not know.` Label the return: the extra field is kept, and `session.cancelled` is kept |
| `the bus misses session.cancelled` | This is the second bus line. It follows `the bus drops an event with an unknown field`. Use that two-line row. Paste `bus.py`, not `leave.py` |
| `the handoff has no summary` | This is `chk-m04-l05-integrate`. Open [handoff.jsonl](packet/release/cc/handoff.jsonl) and search for `call-empty`. [Chapter 06](06-the-connections.md). Paste `handoff.py` and `test_handoff.py` again. You should see `A handoff with no summary is refused.` Label the return: a summary is kept, and an empty summary is refused |
| `late leave leaves the session published`, then `leave does not emit session.cancelled` | These two lines together are late leave on `chk-m04-l05-integrate`. Do not collapse them. They are not the knowledge line. Open [leave.jsonl](packet/release/hr/leave.jsonl) and search for `published`. Do not write a minute count. [Chapter 06](06-the-connections.md). Paste `leave.py` and `test_leave.py` again. You should see `Late leave cancels the published session.` Label the return: the status is cancelled, and the event is `session.cancelled` |
| `leave does not emit session.cancelled` | If the line above it is `late leave leaves the session published`, this is the second integrate line. Use that two-line row. Paste `leave.py`. If the failed check is `chk-readout` and the line is `knowledge.md does not say which event leave creates`, use the knowledge row. Do not treat these as the same miss |
| `the warehouse clock starts at booking` | This is `chk-m04-l05-integrate`. The message does not name the referred date. Open [feed.jsonl](packet/release/warehouse/feed.jsonl) and search for `referred_at`. [Chapter 06](06-the-connections.md). Paste `warehouse.py` and `test_warehouse.py` again. You should see `The referral clock is the referred date.` Label the return: the clock is the referred date |
| `sprint.md does not open the requests first` | This is `chk-m04-l05-integrate`. [Chapter 05](05-the-sprint.md). The page needs requests, then sign-in, then bus, then handoff, then leave, then warehouse, then ranking, then proposal. Paste `sprint.md` again |
| `the access-mgr notes miss the summary` | This is `chk-m04-l05-integrate`. The message names the summary. [Chapter 08](08-the-pages.md). Paste `access-mgr.notes.md` again. Keep the pipes. You should see the summary. The question file is not the note |
| `the ea notes miss late leave` | This is `chk-m04-l05-integrate`. The message does not list every word the note needs. The note needs leave, `session.cancelled`, and bi. [Chapter 08](08-the-pages.md). Paste `ea.notes.md` again. Keep the pipes. The question file is not the note |
| `the deployment architecture misses a required section` | This is `chk-m04-l05-ops`. The message does not name the section. Open [architecture-deploy.md](work/architecture-deploy.md). Zones needs zone-private, zone-hospital, and zone-public. Flows needs cc, bi, hr, and the bus. Boundary needs a clinician and urgency. [Chapter 08](08-the-pages.md). Paste `architecture-deploy.md` again. Keep the headings |
| `the operations plan misses an owner`, then `the operations plan leaves the clinical safety cell empty`, then `the operations plan skips G4` | These three lines together are an empty operations page. This is `chk-m04-l05-ops`. Do not use the two-line gates row. [Chapter 08](08-the-pages.md). Paste `operations.md` again. Owners and Incident need a line. RACI needs `med-dir`. Gate needs G4 and the checklist |
| `the operations plan leaves the clinical safety cell empty`, then `the operations plan skips G4` | These two lines, with no owner line above them, are the gates miss. This is `chk-m04-l05-ops`. Do not collapse them into the empty-page row. Open [assistant.json](packet/release/raci/assistant.json) and search for `G4`. Open [stage-gate.md](packet/release/gates/stage-gate.md) and search for `G4`. [Chapter 07](07-the-proposal.md). Paste `gates.py` and `test_gates.py` again. You should see `Name the clinical safety owner at go-live.` Label the return: the cell is `med-dir`, and the gate is G4 |
| `the operations plan skips G4` | This is the second gates line when the line above it is the empty clinical safety cell and there is no owner line. Use that two-line row. Paste `gates.py`. If the owner line is also there, use the three-line empty-page row |
| `the roadmap starts with p-triage` | This is `chk-m04-l05-rcp`. The message does not say whether the function or the Roadmap section failed. The Ranking section can still contain the words "ranks `p-triage` first" and then say that ranking is not the value model. That sentence is not this miss. Open [model.json](packet/release/value/model.json) and search for `p-clock`. The function returns the first problem whose blockers list is empty. The first id under the Roadmap heading must not be `p-triage` or `vendor-bot`. If [rank.py](work/app/rank.py) still says `Put the blocked problem first.`, paste `rank.py` and `test_rank.py` from [chapter 07](07-the-proposal.md). You should see `Return the first problem that has no blocker.` Label the return: the first open problem is `p-clock`. If the Roadmap section starts with `p-triage`, paste `proposal.md` from [chapter 08](08-the-pages.md) |
| `the ranking follows the dot-vote` | This is `chk-m04-l05-rcp`. The Ranking section must say the dot-vote is not the value model. [Chapter 08](08-the-pages.md). Paste `proposal.md` again |
| `the proposal misses a dependency` | This is `chk-m04-l05-rcp`. The message does not name the pair. The Ranking section needs a pair such as `p-waitlist` and identity. [Chapter 08](08-the-pages.md). Paste `proposal.md` again. Label the ranking: `p-waitlist` depends on identity |
| `success metrics were not measured` | This is `chk-m04-l05-rcp`. The message does not name the measurement. The Metrics section needs `site-b` and a problem id from the value model. The digits 70 in that section count as unmeasured. Do not put those digits in Metrics. [Chapter 08](08-the-pages.md). Paste `proposal.md` again. Label the metrics: site-b served, and `p-status` is a measured problem |
| `the adoption plan misses the phone-only channel` | This is `chk-m04-l05-rcp`. The message names phone-only. The Adoption section also needs `phc-rim` and the readiness survey. Do not copy a count. [Chapter 08](08-the-pages.md). Paste `proposal.md` again |
| `the proposal's client is not Al-Waha` | This is `chk-m04-l05-rcp`. The Client section needs Al-Waha. [Chapter 08](08-the-pages.md). Paste `proposal.md` again |
| `the proposal treats the two savings as separate` | This is `chk-m04-l05-rcp`. The Plan section needs the words same and call. The two savings count the same calls. [Chapter 08](08-the-pages.md). Paste `proposal.md` again |
| `the proposal contains a banned sentence` | This is `chk-m04-l05-rcp`. The message does not name the sentence. Open [proposal.md](work/rcp/proposal.md) and remove a sentence that says triage is already approved, that the assistant may set clinical urgency, that the assistant sets clinical urgency, or that the external model may receive identified patient data. Paste `proposal.md` again from [chapter 08](08-the-pages.md) |
| `rcp/proposal.md is missing` | This is `chk-m04-l05-rcp`. The file belongs at [work/rcp/proposal.md](work/rcp/proposal.md). [Chapter 08](08-the-pages.md). Paste `proposal.md` again |
| `the readout does not leave urgency with a clinician`, then `the readout does not keep patient data off the external model`, then `the readout does not name the first problem's dependency`, then `the readout does not say the handoff needs a summary`, then `the readout does not name session.cancelled`, then `the readout does not answer the double-counted benefit`, then `the readout does not name a phone-only channel`, then `the ask log is missing`, then `the readout does not cite a source` | These lines together are an empty readout. This is `chk-readout`. Do not shorten the list. Do not stop on the first dash line. [Chapter 08](08-the-pages.md). Paste `readout.md` again. Ranking needs `p-clock` and identity. Handoff needs a summary. Leave needs `session.cancelled`. Benefit needs the same calls. Channel needs phone-only and `phc-rim`. The page needs a clinician and urgency, and it needs `ext-large`. Asks needs a line. A cite is a person such as access-mgr or finance |
| `the readout does not leave urgency with a clinician` | If this is the only dash line, the readout needs a clinician and urgency. If the long list above is also there, use that row. [Chapter 08](08-the-pages.md). Paste `readout.md` again |
| `the readout does not keep patient data off the external model` | The message does not name `ext-large`. The readout must name `ext-large`. If this line is inside the long empty-readout list, use that row. [Chapter 08](08-the-pages.md). Paste `readout.md` again. Label the line: patient data stays off `ext-large` |
| `the readout does not name the first problem's dependency` | The Ranking section needs `p-clock` and identity. [Chapter 08](08-the-pages.md). Paste `readout.md` again |
| `the readout does not say the handoff needs a summary` | The Handoff section needs a summary. [Chapter 08](08-the-pages.md). Paste `readout.md` again |
| `the readout does not name session.cancelled` | This is the readout Leave section. It is not the integrate line, and it is not the knowledge line. [Chapter 08](08-the-pages.md). Paste `readout.md` again |
| `the readout does not answer the double-counted benefit` | The Benefit section needs the same calls. The demo does not say which two lines those are. [Chapter 08](08-the-pages.md). Paste `readout.md` again |
| `the readout does not name a phone-only channel` | The Channel section needs phone-only and `phc-rim`. Do not copy a count. [Chapter 08](08-the-pages.md). Paste `readout.md` again |
| `the ask log is missing` | The Asks section is empty. [Chapter 08](08-the-pages.md). Paste `readout.md` again |
| `the readout does not cite a source` | The message does not name the source. A cite is one of cdo, med-dir, dpo, ciso, finance, access-mgr, or ea, or a file path from the pack. The finished readout names access-mgr and finance. [Chapter 08](08-the-pages.md). Paste `readout.md` again |
| `the readout contains a banned sentence` | This is `chk-readout`. Open [readout.md](work/readout.md) and remove a sentence that says triage is already approved, that the assistant may set clinical urgency, that the assistant sets clinical urgency, or that the external model may receive identified patient data. Paste `readout.md` again from [chapter 08](08-the-pages.md) |
| `readout.md is missing` | This is `chk-readout`. Paste `readout.md` from [chapter 08](08-the-pages.md) |
| `retro.md is missing` | This is `chk-readout`. Paste `retro.md` from [chapter 08](08-the-pages.md) |
| `the retro note is missing a heading` | This is `chk-readout`. The message does not name the heading. Keep, Drop, and Open each need a line. [Chapter 08](08-the-pages.md). Paste `retro.md` again |
| `knowledge.md does not say which event leave creates` | This is `chk-readout`. It is the leave-event line. It is not `leave does not emit session.cancelled`. Line 1 of the block on this page. That line contains `session.cancelled` |
| `knowledge.md does not name a first problem and a dependency` | This is `chk-readout`. Line 2 of the block on this page. That line names `p-clock` and a dependency. It does not name `p-triage` or `vendor-bot` as the first problem. Both answers stay on their numbered lines |
| `the guardrail lets the attack book` | This is `chk-individual-m04-l05`. The message does not print the attack text. Open [attack.json](packet/release/personal/attack.json) and search for `atk-direct`. Do not copy the text. [Chapter 07](07-the-proposal.md). Paste `personal.py` and `test_personal.py` again. You should see `Stop a direct attack. Do not book.` Label the return: the direct family is blocked, and it is not booked |
| `the personal lab is missing` | This is `chk-individual-m04-l05`. [personal.py](work/app/personal.py) is missing. Paste it from [chapter 07](07-the-proposal.md). Do not delete it |
| `the personal lab did not run` | This is `chk-individual-m04-l05`. Paste `personal.py` again from [chapter 07](07-the-proposal.md). Do not repair the spaces by hand |
| `the harness did not run` | The failed line names the check. The message does not name the module. A traceback from the suite names a test file. The app file is the same name without `test_`. Sign-in reads [staff.json](packet/release/iam/staff.json). The bus reads [events.jsonl](packet/release/bus/events.jsonl). The handoff reads [handoff.jsonl](packet/release/cc/handoff.jsonl). Leave reads [leave.jsonl](packet/release/hr/leave.jsonl). The warehouse reads [feed.jsonl](packet/release/warehouse/feed.jsonl). The ranking reads [model.json](packet/release/value/model.json). The gates read [assistant.json](packet/release/raci/assistant.json). Paste that module again from the chapter that replaces it. Do not repair the spaces by hand. Do not delete any of the eight app files. The suite imports all eight |
| `a watermarked sample is in the work directory` | A file that carries the mark is under `work/`. Delete that copy. The message does not print the watermark. Do not delete `signin.py`, `bus.py`, `handoff.py`, `leave.py`, `warehouse.py`, `rank.py`, `gates.py`, or `personal.py` |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | Run `dir`. If the list shows `alwaha`, you are already inside `problem_simulation`. Skip the `cd` line. If the list shows `app` and `tests`, this window is inside `work/`. If it shows neither, this window is not the course folder. Open a new terminal in the course folder, the one whose `dir` lists `problem_simulation` and `Module 02`, and run the block from the `cd` line |
| `SyntaxError` or `IndentationError` | Run `python "Module 04/Lesson 05/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 09 again from the chapter source. Do not repair the spaces by hand. A second run puts the shell tests back. `Ran 8 tests` and `OK` after that is the shell again. Chapter 07's search table is how you tell the shell from the filled files. Do not stop at that count |

## Done

The five checks print `chk-m04-l05-integrate passed.`, then `chk-m04-l05-ops passed.`, then `chk-m04-l05-rcp passed.`, then `chk-readout passed.`, then `chk-individual-m04-l05 passed.` There is no sixth passed line. `knowledge.md` answers both questions. The first says a new consultant leave creates `session.cancelled`. The second says `p-clock` is first and `p-waitlist` depends on identity.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

The rehearsal ends here. The [course guide](../../../learning/README.md) says a later real client is not in these folders. The [case folder](../../../case/README.md) says the later project is a different client. There is no further release. The course guide is the map of the days you have finished.

## What the two weeks leave

The sponsor asked for an AI front desk that books, reschedules, answers, and chases referrals, live before Ramadan. The rehearsal did not build that sentence.

Classroom module 1 proved a small assistant, then signed a patient and a coordinator in, took the cluster's feeds, tested the receipt against the case clock, and deployed a private-cloud URL. Intake stops for a coordinator. A patient can ask for status and book. A return waits. A letter cannot book. Triage stayed blocked. A booking at Ain stayed queued for the nightly file.

Classroom module 2 separated people from rows, served a registered adapter inside the quota, cited an in-force document the asker may see, and wrote requirements that do not copy the sponsor sentence. It put a screen in front of the tools, filled the DPIA the first module left open, rebuilt an incident from spans, held chat's latency while a batch ran, moved traffic when site-a died, and connected the contact center, the warehouse, and HR. The proposal's client is still Al-Waha. `p-clock` is first. `p-waitlist` depends on identity. A clinician still owns urgency. Patient data stays off `ext-large`.

This section adds no file and no command.
