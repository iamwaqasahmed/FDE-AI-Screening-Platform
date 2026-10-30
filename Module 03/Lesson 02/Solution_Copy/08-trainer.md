# 08 — Trainer session

Students can skip this page. The answers are in chapters 01 through 07.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not paste a watermark into a slide or a prompt.

[dpo.notes.md](work/interviews/dpo.notes.md), [dpo.questions.txt](work/interviews/dpo.questions.txt), [finance.notes.md](work/interviews/finance.notes.md), and [finance.questions.txt](work/interviews/finance.questions.txt) are for you. The checks do not read them. Students were not asked to run an interview. The Data Protection Officer's note says the ruling was signed this morning. Finance says the quota is a count of GPUs on the release and a cloud fine-tune is not in the budget. The spoken answers do not give the GPU count. That count stays in [quota.json](sources/release/budget/quota.json).

The demo, from `problem_simulation`, prints one line and nothing else:

```text
cd problem_simulation
python -m alwaha.demo.gateway --profile practice
```

The line is `the gateway refused the prompt`. It does not print the watermark.

`qlora.py`, `domain.py`, and `prefs.py` are the advanced path. The two checks pass if those files are absent. Do not tell a student to delete them. When the files are present, they have to keep the rank fit, the unlabeled domain lines, and the preference edit. The packet copies are the shells. The work copies are the replacements. The nine test files match the packet byte for byte. Do not add a comment to only one side. `.github/workflows/ci.yml` matches the packet.

From the course folder, the two checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check model --release rel-m03-l02 --work "../Module 03/Lesson 02/Solution_Copy/work" --profile practice
python -m alwaha.check lora --release rel-m03-l02 --work "../Module 03/Lesson 02/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is baseline, then adapter, then register, then memo. The cloud fine-tune is closed. [ruling.md](sources/release/notices/ruling.md) is the sentence they are repeating.

## Block 2 — The baseline

Open their `prompt.py`, `extract.py`, and `intent.py` beside the files in this folder. The shell serves the prompt and sends phi to `ext-large`. The filled prompt is not served, and it stays on `local-small`. `typed` and `status` remain inside `prompt.py`. That is expected. The shell relabel returns blanks. The filled relabel reads the text. The shell intent returns status for every message. The filled intent checks an emergency phrase first. `return "status"` remains after that rule. That is expected.

## Block 3 — The adapter

Open their `adapter.py`, `route.py`, and `cost.py`. The shell loads the cloud fixture and asks for more GPUs than the quota. The filled adapter returns the approved `lora-local` row and that row's hash. Do not put the hash on a slide. The shell router allows every call. The filled router refuses phi on `ext-large` and a hash that is not approved. The shell prices `ext-large`. The filled quote prices `local-small`. The message does not print a price.

## Block 4 — The advanced path

Open their `qlora.py`, `domain.py`, and `prefs.py` only if they replaced them. The suite is `Ran 12 tests` and `OK` when all nine filled modules are in place. The two checks do not call these three files. If a student deleted them, the checks can still pass and the suite cannot. Ask them to paste the three files back. Do not treat deletion as the fix.

## Block 5 — The pages

Open their `approach.md` and `residency.md`. The Module 1 families stay. Hours stay on retrieval. DNA stays tabular. The customization table is the measurement block already in [approach.md](work/approach.md). Do not read the hash aloud. The residency table needs the pipe characters. National id, date of birth, name, and phone are `zone-private`. Clinic hours are `public`.

## Block 6 — Knowledge

The first sentence is hours questions for p-info stay on retrieval. The second sentence is the legal hash is lora-local on reg-models. Both sentences are numbered lines. A wrapped second line does not count. The second sentence names the register row. It does not print the hash.

## Close

A pass is two lines: `chk-m03-l02-model passed.` and `slice-lora passed.`. If those two lines are on the screen, the failure table is not more work. Leave `problem_simulation/build` closed.
