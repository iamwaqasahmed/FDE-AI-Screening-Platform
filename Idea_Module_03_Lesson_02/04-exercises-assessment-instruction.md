# Exercises, assessment, and the no-GPU path

## Prerequisites

From earlier lessons, the student already has:

- Families for the nine problem ids, including `p-info` as retrieval, `p-dna` as classical ML, and `p-triage` as blocked.
- The idea that a row split can leak and a person split can look like failure. This lesson must not reopen DNA with a language model.
- PHI versus public, and the habit of not pasting a canary into `work/`.
- A working Python environment. The journey log used Python 3.14. The CPU fit uses the standard library plus whatever numeric library the course already accepts. If the course cannot depend on PyTorch, implement \(W\), \(A\), and \(B\) as nested lists and a dozen steps of hand-written gradients on a squared error. That is uglier and still teaches the update. Prefer a tiny NumPy or PyTorch CPU script if one of those is already in the environment. Do not add a CUDA wheel to setup.

Not required: a GPU, Hugging Face login, bitsandbytes, MLflow server, or the PEFT package. The PEFT pages are reading. The graded fit is the small script. Students who already have PEFT may use it only on the optional branch, and the check does not import it.

Reading load before any paste: the ruling, the register, the quota, the price cap, and one scenario file. The Azure privacy excerpt is a single printed paragraph in the chapter, with the URL, not a browsing assignment.

## Path A — required, no GPU

Time box for a self-paced reader who already did Lesson 1: one sitting for the decision and the gateway, one sitting for the fit and the memo. The fit script should finish in seconds on CPU.

### Exercise 1 — Say what is not a model call

Open hours, the DNA line in the approach template, and the triage line. Write three sentences: hours stay on retrieval because the document changes; DNA stays a table because the features are columns; triage is not built. This is the current knowledge item, kept, and it happens before anyone says LoRA.

### Exercise 2 — Price three scenarios

Given the pack's three scenario files, implement `quote(job, cap, rates)` and `fit(job, quota, device)`.

`quote` returns model, SAR, and seconds. `fit` returns `refuse` or a record `{method, gpus, vram_gb, rank}`.

Worked shape of a correct `fit`, not a rank formula:

- If the job is `full_ft` and `vram_gb_required` is greater than the device, or `gpus_required` is greater than the quota, return `refuse`. Do not clamp.
- If the job is `qlora` and the device has `cuda: false`, return `refuse` with reason `no-cuda`. The CPU teaching fit is a different method name, `lora-cpu`, so it is not reported as QLoRA.
- If the job is `retrieve` or `classical_ml` or `blocked`, `fit` is not called.

The student computes SAR on paper for scenario 1 before running the function, using `tokens / 1000 * rate`, and checks the function against that arithmetic. The chapter does not print the answer. The check compares to the pack rates.

Facilitator trap: a student edits `seconds` on the prompt job until it fits. The scenario file is read-only in the pack. The work copy that drifts from the pack hash fails.

### Exercise 3 — Gateway

Implement `allow`. Cases the unit tests already suggest, plus the new ones:

- PHI fields to `ext-large`, approved hash, price irrelevant: false.
- Cloud hash, empty fields, model name `local-small`: false.
- Generation call with no hash: false.
- Hours retrieval with no hash: not this function. `task("hours")` returns `retrieve`.
- Public hours text to `ext-large` with no PHI fields: the ruling allows public leaflets to leave. This call may return true only if the price scenario also fits. Split the decision: `allow` is residency and hash; `quote` is money. A public call that is over the cap is allowed by `allow` and rejected by `quote`. The student writes one sentence on that split so they do not hide a price failure inside a 403.
- Letter text containing the planted name, fields empty, model `ext-large`: false via the local detector.

Run the existing demo. The one-line refusal stays.

### Exercise 4 — Easy slice, labeled honestly

Replace the shell extractor and intent classifier with the English rules, or with a local prompt that calls those rules. `served()` on the prompt is false if an adapter will be served for the dialect slice, and may be true for the easy slice if the memo's easy-slice method is `rules` or `prompt`. The check no longer requires `served()` to be false in all cases. It requires that the served method for each slice is the method on the memo.

Delete the instruction "do not copy relabel into prompt.py or the slice fails." Replace it with "if the prompt is competent, label it as the method that won."

### Exercise 5 — CPU low-rank fit

Train the frozen-\(W\) adapter on the synthetic dialect and format pairs. Initialization: \(B = 0\). After training, \(B\) is not all zeros. Save the file. The script prints the SHA-256 and writes a register row with status `approved`, base `local-small`, zone `zone-private`.

Score three ways and write the numbers the script prints into the memo without retyping a hash:

- English dev letters, method `rules`.
- Dialect held-out, method `lora-cpu`.
- Format held-out, method `lora-cpu`. A prose decoder fails this one even at a perfect entity match.

If the dialect match ratio is under the floor, the student adds pairs or trains more steps. They do not edit the held-out file. They do not paste `1.0000`.

### Exercise 6 — Memo and residency

`approach.md` keeps the nine Module 1 rows. The customization table becomes:

| task | slice | method | match | sar | seconds | hash |
| --- | --- | --- | --- | --- | --- | --- |

Rows at least: extraction-english, extraction-dialect, extraction-format, intent, hours, dna, triage, and one refuse row for full fine-tune. Hours, DNA, and triage have empty hash cells. The refuse row has empty match and hash. SAR and seconds are filled only for methods that would have been called.

`residency.md` keeps the five rows. Add one sentence under the table: a vendor statement that prompts are not used to train foundation models does not put PHI on `ext-large`. The knowledge file's two answers stay: which problem stays on retrieval, and which hash is legal. The second answer names `lora-local` on `reg-models` and does not print the digest.

### Exercise 7 — Optional GPU branch

If `cuda` is false, the script prints `no GPU; fixture path` and exits 0. The required path already passed.

If `cuda` is true, the script loads the 65B-class job card and prints `refuse` because `vram_gb_required` is above the device or, if someone set a 48GB device, it still does not download weights unless the student passes `--i-understand-this-downloads`. Default is refuse. No grade depends on a download.

## Path B — what the facilitator does

The trainer chapter stays optional for students. In the debrief, show one failing scenario rather than re-pasting six files:

- Open scenario 2 and ask why a lower SAR is still a 403.
- Open the fit record and ask why \(B = 0\) is not an adapter.
- Open `reg-models` and ask why an alias named `champion` without a matching hash is not enough. One sentence on MLflow aliases is enough.
- Do not read a hash aloud. The current trainer note is right about that.

## Assessment

Keep two check ids if the release map requires them. Change what they mean.

### `chk-m03-l02-model`

Pass when:

- Task routing: hours `retrieve`, DNA `classical-ml`, triage `blocked`, and no PHI egress.
- Quote and fit for all three scenarios match the pack arithmetic. At least one scenario refuses `ext-large` on price. At least one refuses it on PHI while the price is inside the cap. Full fine-tune is `refuse` on the published device.
- English slice field-match is at least 0.8 for the method the memo names `rules` or `prompt`.
- Dialect and format slices are at least 0.8 for the method the memo names `lora-cpu`.
- The served hash equals the hash of the adapter file and the approved row.
- Residency table and the vendor-ban sentence are present.
- Sprint order: baseline, fit, register, memo, and the cloud fine-tune is closed.
- Method labels match artifacts: a file with no \(A\) and \(B\) cannot be labeled `lora-cpu`.

Fail messages stay non-leaking. Suggested lines:

- `the quote does not match the pack rates`
- `the job was over the quota and was not refused`
- `the call sends phi to ext-large`
- `the price was inside the cap and the call still sends phi`
- `the hash is not on reg-models`
- `the hash was not computed from the adapter file`
- `the method label does not match the artifact`
- `hours questions are not left on retrieval`
- `dna is not a tabular model`
- `the dialect slice is outside the budget`
- `the format slice is outside the budget`

Do not print the digest, the SAR, the VRAM figure, or a gold label.

### `slice-lora`

Pass when the decision is slice-specific:

- The English keyword baseline does **not** have to lose. It must lose the dialect slice if it is the method served there.
- `ext-large` does not clear a slice by being named on a quote that sits inside the cap while PHI is present.
- An identity adapter does not clear the dialect slice.
- A rules file mislabeled `lora` does not clear the slice.

Delete the gold pre-check that fails the slice whenever `external_sar <= max_sar`. That line makes a cheap external model a grader bug instead of a student decision.

The unit suite remains the fast loop. The checks remain the release gate. A green suite that only tests the English rules is not the model check. State that in the finish chapter, as the current chapter already says a green suite can fail the pages.

## Solution approach

The solution pack contains:

- `quote` and `fit` with no clamped GPU count.
- `allow` with the missing-hash hole closed for generation.
- English rules labeled `rules`.
- A deterministic CPU training script. Seed fixed in the pack so the digest is stable for the solution and different for a student who changes the learning rate. The check hashes the student's file; it does not expect the solution digest.
- A memo whose match cells are whatever the script prints at that seed, not a hand-typed `1.0000`. The solution chapter tells the facilitator to run the script rather than to memorize the ratio.
- `refuse` for full fine-tune and for QLoRA-on-CUDA when the device card says no CUDA.

The solution must be allowed to lose. On the English slice the solution's adapter does not have to beat the rules. If it does, the memo still labels the rules as the method shipped for that slice when the rules are cheaper or simpler. Shipping the adapter everywhere is a fail if the easy slice's card says the rules meet the floor at lower latency. That is the judgment.

## Rubric for the memo, if a human reads it

The checks cover the table. A human reading, including the student reading their own page, looks for four sentences:

1. Which slice the rules won, and why a prompt was enough.
2. Which slice the low-rank update won, and that the win is dialect or format, not a general claim about LoRA.
3. Why `ext-large` lost in the scenario where it was cheaper.
4. Why the 65B job was refused, using the words quota and VRAM, without inventing a laptop measurement.

Must-not-claim: "the adapter beat GPT," "QLoRA fits on any GPU," "F1 is 1.0 so we fine-tuned," "Azure does not store prompts so PHI may leave." The last claim is false even before the ruling: the opened privacy page describes abuse-monitoring storage unless modified, and Global processing.

## Instructional design notes

One person, five roles, no timetable. That part of the current lesson is right. Do not add a group interview. The DPO and finance notes can remain in the solution folder for a facilitator who wants a three-minute contradiction: finance says the external model is under the cap this week, the DPO says the ruling does not move. Scenario 2 is that contradiction in a file, so a solo student still meets it.

Chapter prose should keep the course's habit of saying which block is a picture and which block is the paste, if the course stays a paste course. The new failure mode is a student pasting the English rules into the dialect trainer and labeling the result `lora-cpu`. The search-after-paste table should look for `B` initialized at zero and for a later assignment that updates `B`, not for the string `rank: 8`.

Advanced versus foundation. Foundation is exercises 1 through 6. Advanced is the MLflow alias fixture, the domain-row filter, the preference edit, and the optional CUDA refusal script. `slice-lora` reads the foundation artifacts and the dialect slice. It does not read the preference edit. That separation can stay so a reader who is out of time still has a coherent gate, provided the CPU fit has moved into the foundation. Today the thing called QLoRA is advanced and ungraded by the release checks, which is why students can "finish the adapter" without it. If the fit stays advanced, the lesson title should change to "The register." Prefer moving the fit into the foundation and leaving string-edit preferences advanced.

## What not to automate

Do not auto-grade the prose quality of the four sentences beyond keyword checks of the kind the current knowledge file uses. Do not call an external model to judge the memo. That would spend the price cap on the grader and would put student text on a path the lesson just taught them to distrust. The table is the assessment. The sentences are for the reader.
