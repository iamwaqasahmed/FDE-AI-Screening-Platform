# Check

**Day 5.** From `Version 02`:

```text
python -m course agent_check --work <your folder>
```

`<your folder>` contains `findings.json`, `answers.jsonl`, `backlog.csv`, `sweep.csv`, `contracts/agent_trajectory.yaml`, `agent-card.md`, `cdo-reply.md`, and `press-line.md`. The data folder defaults to `data`. The shape of every item is [templates/findings.example.json](templates/findings.example.json). That file is a shape, not an answer. It does not pass.

The checker prints how many items passed, the count for each role, the answer rate overall and by slice, and pass or fail for the backlog, the sweep, the contract, the card, the reply, and the line. It does not print the expected value. A failed id is a place to look again.

To score an answers file on its own:

```text
python -m course agent_check.score --answers <file> --data data
python -m course agent_check.score --answers single_loop.jsonl --data data --baseline
```

`--baseline` is for the two agent baselines. Your own file is scored without it.

## Pass

All of these, together:

- At least 80 percent of the items pass, and every role reaches at least 60 percent of its items.
- Answers are at least 0.80 overall and at least 0.30 above the better baseline. Every slice is at least 0.60. Veto, injection, approval, and resume are complete.
- The backlog has every open pilot ticket, with the duplicate, the missing criterion, and the freeze the file supports.
- The sweep has every lost chase letter inside the bound, with the hospital, the clause, and the days over.
- The contract has every field and at least 80 percent of its key facts.
- The card, the reply, and the line each cover at least 80 percent of their key facts, and none contains a banned sentence.
- The line is exactly two paragraphs and contains none of the forbidden terms.

## A second seed

You build it yourselves. From `problem_simulation`:

```text
python -m simulation --profile small
```

That writes `problem_simulation/build/data-small`. Use it while you are still changing the code. For the rerun that counts:

```text
python -m simulation --profile team-1
python -m course agent_check.questions --data problem_simulation/build/data-team-1 --out questions-team.jsonl
python -m course agent_check --work <a second folder> --data problem_simulation/build/data-team-1 --rerun
```

The sweep on that seed reads the build you point the services at:

```text
$env:HARTLAND_DATA = "build/data-team-1"
$env:HARTLAND_WEEK = "5"
$env:HARTLAND_CLOCK = "2026-11-02"
python -m serve --system all --port 8800
```

`--rerun` grades the computed items, the answers, the backlog, and the sweep. It skips the card, the reply, the line, and the contract. Reprint the questions for that seed. Counts, site names, and the build date have to come from the files. The same thresholds apply.

Do not tune the code on the assessment profile. That build is held out.

`python -m course agent_check.key` prints the gold. Participants do not run it. Opening `data/truth` has the same effect: it skips the week.

**Finish.** The check prints `Agent check passed.` Open the debrief only after that, or after you have decided the reply is finished and you want to see what it missed.

Next, when the reply exists: [Debrief](16-debrief.md).
