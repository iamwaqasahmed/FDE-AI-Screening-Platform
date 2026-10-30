# Module 03 Lesson 02 — The adapter: research index

Independent curriculum research for `rel-m03-l02`. These notes do not change the course. They argue for a different definition of done.

## Recommendation

Stop teaching LoRA as the method that is required to win. The current finish line is a registered row named `lora-local` that beats a prompt the chapter itself keeps weak, inside a price world that already places `ext-large` over `max_sar`. The graded "adapter" is keyword rules plus a hash copied from `reg-models.json`. `qlora.py` is integer division of rank by 32. The student-journey record already says the adapter is a register row and a quota fit, not a trainer. Keep that honesty, and make it the objective.

The lesson should teach three judgments a person can make on a laptop with no GPU:

1. Which family is legal for this task: local prompt, LoRA or QLoRA on an approved base, full fine-tune, retrieval, or classical ML — or blocked, or refused because the job does not fit the GPU quota, the VRAM card, or the price and latency cap.
2. Which artifact may be served: a full content hash on `reg-models` with status approved, not a display name and not the closed cloud fine-tune.
3. Which bytes may leave: the four PHI fields stay off `ext-large` even when a later price sheet would make the external call cheap.

A tiny on-prem fit still belongs in the lesson. It is a frozen matrix plus a low-rank update trained on synthetic letters, hashed, and registered. That is the Hu update rule, runnable on CPU. It is not a 65B QLoRA job, and the page must say so. QLoRA of a large base is a refuse-or-optional path: Dettmers and colleagues report a 65B model fine-tune moving from more than 780GB to under 48GB on one GPU. A one-GPU quota and a student machine without CUDA do not meet that bar. The student refuses the job and still passes.

The challenge thesis is only half supported by sources opened for this note. Careful prompting sometimes beats fine-tuning, and fine-tuning sometimes beats zero-shot prompting. No paper opened here shows a reasoning model beating a LoRA adapter on this clinic's extraction. Adapters still earn their place when the win is dialect, output format, latency after merging, cost under the cap, or residency. Those are the slices to score. A fake fine-tune that always wins teaches the opposite decision.

## What to delete

- The pass rule that the prompt baseline must not clear `slice-lora`.
- Pasted customization rows that label keyword accuracy `lora` and `1.0000`.
- The QLoRA function that clamps GPU demand down to the quota and still returns success.
- The objective sentence "a registered adapter beats the prompt baseline" as the definition of done.

Keep the ruling, the four PHI fields, hours on retrieval, DNA as `classical-ml`, triage blocked, the gateway canary, and the closed cloud fine-tune.

## Files

| File | Question it answers |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What `chk-m03-l02-model` and `slice-lora` actually grade, and which of that is worth keeping |
| [02-industry-research.md](02-industry-research.md) | LoRA, QLoRA, PEFT, prompting versus fine-tuning, registries, VRAM, residency — only pages that were opened |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | Decision architecture, five alternatives, quota and price simulation, synthetic slices, failures |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | No-GPU path, exercises, checks, solution shape, prerequisites |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | Tradeoffs, deletions, whether to split the lesson, citations |

## Labels used throughout

- **Proven.** A mechanism or control stated in a paper or official doc opened for this research, or a behavior read in this repo's grader.
- **Emerging.** A 2024–2026 result that is real but narrow, or a lab write-up that is not a clinical extraction trial.
- **Experimental.** A teaching stand-in (CPU rank update, case VRAM cards) that must not be described as a measured LLM result.

## One-page recommendation for the next edit

Change the objective in `course_design/module-03.md` and the slide from "a registered adapter beats the prompt baseline" to "the served method is legal, registered if it is weights, inside quota and price, and PHI did not leave." Add three price and residency cards so local is not always the cheap winner and external is not always over the cap. Score a dialect or format slice where a real low-rank update can beat English keyword rules, and an easy slice where a local prompt or the rules are the right method and must be labeled as such. Replace `fit` so an over-quota job returns `refuse`. Keep `slice-lora` as a name if the check id must stay stable, but change its meaning: the prompt is allowed to win a slice; `ext-large` fails on PHI or on price, not because the gold file pre-fails whenever the external price is inside the cap. Do not add a required GPU lab. Put the 48GB QLoRA figure in the advanced chapter as the reason a large job is refused on this quota.

Do not spawn a second required lesson. A later measurement lesson (Module 3 Lesson 4) can re-score the same cards once metrics exist, so nobody pastes `1.0000` again. A "train a 7B model" lesson is out of scope for this self-paced path.
