# 07 — Trainer session

Students can skip this page. The answers are in chapters 01 through 06.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not paste a watermark into a slide or a prompt.

Students run both interviews in chapter 03. They paste [access-mgr.notes.md](work/interviews/access-mgr.notes.md) and [ea.notes.md](work/interviews/ea.notes.md) in the pages chapter. The integrate check reads those notes. [access-mgr.questions.txt](work/interviews/access-mgr.questions.txt) and [ea.questions.txt](work/interviews/ea.questions.txt) are not the graded notes. The interview test reads the question files. It does not read the notes.

The demo, from `problem_simulation`, prints one line. The line is `Which benefit is counted twice?` It does not say which two lines count the same calls. It does not print a lag, a survey count, or the attack text. Do not type the leave lag. Do not type the phone-only count. Do not type the attack.

```text
cd problem_simulation
python -m alwaha.demo.benefit --profile practice
```

All eight app modules are required. The suite imports them. Do not tell a student to delete any of them. The shell tests and the filled tests are not the same bytes. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite. The packet workflow and this folder's workflow are the same test job. There is no second job. This day does not replace the workflow.

The shell suite prints `Ran 8 tests` and `OK`. That pass is the shell. It is not the finished day. This folder's suite prints `Ran 8 tests` and `OK`. The count is the same. The files are not.

From the course folder, the five checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check integrate --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check ops --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check rcp --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check readout --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
python -m alwaha.check individual --release rel-m04-l05 --work "../Module 04/Lesson 05/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is requests, then sign-in, then bus, then handoff, then leave, then warehouse, then ranking, then proposal. [README.md](sources/release/README.md) is the release note they open.

## Block 2 — The connections

Open their sign-in, bus, handoff, leave, and warehouse files beside the files in this folder. The shell treats every token as staff. The filled sign-in accepts staff and refuses a service token. The shell drops an unknown field and a cancellation. The filled bus keeps both. A bus miss is two lines. The shell returns an empty summary. The filled handoff refuses an empty summary. The shell leaves the session published. The filled leave cancels it and emits `session.cancelled`. A late-leave miss is two lines. That pair is not the knowledge line. The shell reads the booking date. The filled warehouse returns the referred date. Do not read a minute count off the check.

## Block 3 — The proposal

Open their rank, gates, and personal files beside the files in this folder. The shell starts with `p-triage`. The filled ranking returns the first problem with no blocker, which is `p-clock`. The shell leaves the clinical safety cell empty and skips G4. The filled gates name `med-dir` and G4. Those two lines are the gates miss. An empty operations page adds the missing owner. The shell lets the attack book. The filled lab blocks the direct family and does not book. Do not read the attack text off the check. The suite prints `Ran 8 tests` and `OK` only after the filled tests are pasted beside the filled app.

## Block 4 — The pages

Open their deployment architecture, operations plan, proposal, readout, retro, and both notes beside the files in this folder. Zones names zone-private, zone-hospital, and zone-public. Flows names cc, bi, hr, and the bus. Boundary names a clinician and urgency. RACI names `med-dir`. Gate names G4 and the checklist. Client names Al-Waha. Ranking says the dot-vote is not the value model and names a dependency. Roadmap does not start with `p-triage`. Plan says the two savings count the same calls. Metrics names site-b and a measured problem, and it does not contain the digits 70. Adoption names phone-only, `phc-rim`, and the readiness survey. The access-manager notes name the summary. The enterprise-architect notes name leave, `session.cancelled`, and bi. The pipes stay. An empty readout is the long list. Do not shorten it.

## Block 5 — Knowledge

Both answers must be numbered lines. A wrapped second line does not count. The first says a new consultant leave creates `session.cancelled`. The second says `p-clock` is first and `p-waitlist` depends on identity. The first line contains `session.cancelled`. The second contains `p-clock` and a dependency. It does not start the ranking at `p-triage` or `vendor-bot`.

## Close

A pass is five lines: `chk-m04-l05-integrate passed.`, then `chk-m04-l05-ops passed.`, then `chk-m04-l05-rcp passed.`, then `chk-readout passed.`, then `chk-individual-m04-l05 passed.` There is no sixth passed line. If those lines are on the screen, the failure table is not more work. Leave the build folder closed.
