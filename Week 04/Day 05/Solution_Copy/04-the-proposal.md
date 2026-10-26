# 04 — The proposal

Three modules. The shell of each one is what the morning packet still holds. The filled copy is in this folder. The work tests are not the shell tests. A filled app beside a shell test fails the suite. A shell app beside a filled test fails the suite.

## Ranking

The shell puts the blocked problem first. That shell makes the rcp check say `the roadmap starts with p-triage`. The same line can also come from a Roadmap section that starts with `p-triage`. The message does not say which one failed.

[rank.py](work/app/rank.py) returns the first problem whose blockers list is empty. [model.json](sources/release/value/model.json) lists `p-triage` with a blocker, then `p-clock` with none. The first open problem is `p-clock`. `vendor-bot` is not first either.

## Gates

The shell leaves the clinical safety cell empty and skips go-live. That shell makes the ops check say two lines: `the operations plan leaves the clinical safety cell empty`, then `the operations plan skips G4`. Those two lines are the gates miss. An empty operations page is those two lines plus `the operations plan misses an owner`. Do not collapse them.

[gates.py](work/app/gates.py) returns `med-dir` and G4 when the item's gate is G4. [assistant.json](sources/release/raci/assistant.json) leaves the owner empty and names gate G4. [stage-gate.md](sources/release/gates/stage-gate.md) says G4 is go-live.

## Personal lab

The shell lets the attack book. That shell makes the individual check say `the guardrail lets the attack book`. The message does not print the attack text.

[personal.py](work/app/personal.py) blocks a row whose family is `atk-direct` and does not book it. [attack.json](sources/release/personal/attack.json) is that row. Do not copy the text.

A ranking miss fails `chk-w4-rcp`. A gates miss fails `chk-w4-ops`. A personal miss fails `chk-individual-w4`. Do not move a miss onto a different check.

The suite prints `Ran 8 tests` and `OK` only after the filled tests are pasted beside the filled app. The shell suite prints the same count. That earlier pass is the shell.

Next: [05 — The pages](05-the-pages.md).
