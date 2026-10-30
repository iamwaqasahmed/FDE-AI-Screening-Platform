# Tradeoffs, deletions, new lessons, sources

## Recommendation

Keep one lesson. Change the finish line from "LoRA wins" to "the legal method is the one you serve." Required work runs on CPU: three price and residency scenarios, a gateway, an honest rules baseline, a rank-1 or rank-2 update on a frozen matrix, a hash the student computes, and a memo that can say the rules won the easy slice. QLoRA of a large model is a refusal, taught with Dettmers' 48GB and >780GB figures, not a training job.

The challenge thesis is the right pressure and the wrong slogan if it is taught as fact. Opened studies do not show reasoning models retiring adapters on extraction. Bucher and Martini (2024) found fine-tuned encoders beating zero-shot GPT-4-class models on classification. Tang, Hasan, and Runkler (2025) found few-shot prompting about 10% F1 ahead of fine-tuned models in scarce industrial NER, and fine-tuning still ahead when their data were abundant. Peng and colleagues (2024) found soft prompt tuning and ordinary fine-tuning within a few points on clinical concept extraction. Niess and colleagues (2025) found prompting too hallucinated for their financial span task until they fine-tuned. Ovadia and colleagues (2024) found RAG beating unsupervised fine-tuning for new facts. Use those papers as the decision's evidence, with those limitations, and do not average them into a win-rate.

## Explicit deletions

Delete these from the student objective, the checks, and the pasted chapters:

1. **The prompt must lose.** `slice-lora` fails when the prompt clears both floors (`CLEARS = "the prompt baseline clears the slice"`). The chapter instructs the student to keep `extract` and `intent` incompetent so this line does not appear. That teaches the opposite of the syllabus. A competent local prompt or a rules baseline is a legal serve on the easy slice.
2. **The gold pre-fail when external is cheap.** If `external_sar <= max_sar`, the slice fails before student code runs. Combined with `prices.py`, where the external rate is the local rate plus at least 8 SAR and the cap is 8 SAR on 1,000 tokens, the external model cannot be the cheaper legal option. Delete the pre-fail. Add a scenario where it is cheaper and still illegal because of PHI.
3. **Pasted `method: lora` and `f1: 1.0000`.** The customization block in chapter 09 labels keyword match ratio as a LoRA win. The measurement block in `m03_l02.py` builds the same fiction for the solution. The memo should show the script's ratio and the method that actually ran.
4. **`qlora.py` as `(rank + 31) // 32` then `min` with the quota.** Clamping reports success for an over-quota job. Replace it with `refuse`.
5. **The objective sentence** "a registered adapter beats the prompt baseline inside the quota and the price cap" in `module-03.md`, the slide, the curriculum map, and the student README. Replacement: a legal method, registered if it is weights, inside quota, VRAM card, price, and latency, with PHI still on the private side.
6. **Calling the match ratio F1 in check output** without the words-page caveat. Either rename the message to field match or keep the caveat next to every use. Do not report a precision-recall F1 the grader did not compute.
7. **Rank and hash as literals inside `serve`.** The solution returns `"rank": 8` and copies the hash. After the redesign, both come from the fit record. The literal is the costume.
8. **Allowing a generation call with no hash.** `allow` currently returns true when `hash` is missing. Close it.

Do not delete:

- The ruling, the four PHI names, `zone-private` versus public hours.
- Hours on retrieval, DNA as classical ML, triage blocked, the Module 1 approach table.
- The gateway canary demo and non-leaking check messages.
- `local-embed` present and not served, and `cloud-tune` unregistered.
- One person, five roles, no student interview.
- The advanced-path separation for the preference string edit and the domain filter, once the real fit has moved into the foundation.
- The closed cloud fine-tune as a sprint sentence.

## Tradeoffs

**Decision lab versus a real PEFT run.** A PEFT run on a 7B model would look like the job title and would exclude every student without a large GPU. The opened QLoRA result that is safe to cite needs 48GB for a 65B model. No opened source gave a laptop VRAM number to hide behind. The CPU matrix teaches the update, the identity initialization, the hash, and the loss. It does not teach bitsandbytes errors, NF4 quality, or sequence packing. Those belong in a later optional lab or in a reading note. **Proven** constraint: self-paced, no GPU. **Experimental** artifact: the toy update.

**Letting the prompt win versus a single leaderboard.** A single winner is easier to grade and is what `slice-lora` is today. It also makes "always LoRA" the rational student behavior. Slice-specific winners are more grading code and a memo that can be correct in more than one way. The check stays deterministic because each slice has one legal family in the pack card. The student is not free to pick at random. They are free to pick the card's winner, which sometimes is not LoRA. **Proven** as an assessment pattern (the hardness note already says simpler methods must lose some slices; it should also say heavier methods must lose slices where they are unnecessary or illegal).

**Hash register versus MLflow.** A JSON allow-list is inspectable in a text editor and matches the trap (do not load an unregistered hash). MLflow aliases are how production actually retargets a name, and they are mutable, which is why they are not a substitute for the digest. Teaching both in prose is cheap. Standing up a tracking server is not. **Proven** documentation, **Experimental** as a required service. Stay with JSON.

**Local detector versus field allow-list.** The allow-list of four fields is auditable and is the ruling. A detector catches a name typed inside the letter and will both miss and over-fire. Ship the allow-list as the policy and one planted name as the backstop. Do not call an external model to classify sensitivity. **Proven** policy, **Emerging** detector.

**Quoting Azure's privacy page.** The page is an accurate description of one vendor's commitments as of the copy opened (change log through 3 October 2025), including a real distinction between geography of storage and geography of Global or DataZone processing. Quoting it helps the student resist a sales slide. Quoting it without the ruling lets a student treat "not used to train" as permission. The chapter needs both, with the ruling winning. The case law stays fictional. Do not map the ruling onto a national statute in the student text.

**Soft-prompt literature versus this lab.** Peng and colleagues' best frozen result used an 8.9B clinical model and trainable prompt vectors. That is not a paragraph a student writes, and it is not runnable here. Mention it so "prompting" is not one word for four techniques (zero-shot, few-shot, hard prompts with unfrozen weights, soft prompts). Do not add a soft-prompt exercise. **Proven** paper, **out of scope** as a lab.

**Match ratio versus a proper F1.** Implementing precision and recall would be more honest to the word F1 and would not change who wins on a two-field exact match. It is not worth a new metric in this lesson. It is worth not using the word. Lesson 4 can introduce a real F1 when the labels are richer.

**Moving the fit into the foundation versus keeping chapter 08 optional.** If the fit stays optional, most students will stop at the register, which is the current outcome and the current journey note. The register is necessary and not sufficient for a lesson called "The adapter." The cost is a longer foundation and a training script to maintain. Pay that cost. Leave preferences and domain filtering optional.

## New lessons to spawn

Do not split Lesson 2 into two required lessons. The decision, the gateway, and the CPU fit are one story. Splitting "the memo" from "the fit" recreates today's failure mode: students finish the memo with a pasted `1.0000`.

Spawn nothing required. Offer two optional attachments:

- **Inside Lesson 4, not a new lesson.** Rescore the same three slices with whatever metric Lesson 4 standardizes, and require the Lesson 2 method labels to stay. A pasted perfect score that Lesson 4 cannot reproduce is a finding. This is **Proven** as curriculum hygiene and depends on Lesson 4 existing, which it does.
- **An optional appendix, not a lesson,** for readers who have a 24GB-class or larger GPU: the PEFT quantization guide's 4-bit load and `target_modules="all-linear"`, on a tiny public model, with synthetic non-clinical text. Time-box it as reading plus the refusal card if the GPU is smaller than the job. Do not make it `rel-m03-l02`. **Experimental** as a cohort extra. If attendance data later show that most learners have no GPU, the appendix stays dark.

Do not spawn "train the production clinical model." The case forbids training on identifiable letters, the quota is one GPU, and the cloud fine-tune is closed. A later module that wants domain adaptation should use the unlabeled filter (`item_id` absent) and still not promise a quality lift the course has not measured.

Do not move this lesson earlier. It depends on Lesson 1's labels and on Module 1's families. It should stay before retrieval (Lesson 3), because the decision to leave hours on retrieval is what Lesson 3 builds. It should stay before evaluation (Lesson 4), because Lesson 4 needs a method label it can remeasure.

## Ideas labeled in one place

| Idea | Label | Use |
| --- | --- | --- |
| LoRA update \(W_0 + BA\), merge for inference, many adapters on one base | Proven (Hu et al., 2021, arXiv:2106.09685) | Required explanation and the CPU fit |
| 10,000× fewer trainable parameters and 3× memory versus Adam on GPT-3 175B | Proven as their comparison only | Do not generalize to the laptop |
| QLoRA, NF4, double quant, paged optimizers; 65B from >780GB to <48GB | Proven (Dettmers et al., 2023) | The refusal card for a large job |
| Guanaco at 99.3% of ChatGPT on Vicuna | Emerging, and the paper discounts chatbot benchmarks | Do not cite as an extraction result |
| PEFT `LoraConfig`, zero-init \(B\), `merge_and_unload` | Proven (Hugging Face PEFT docs) | Reading; identity-adapter failure |
| Attention-only as the typical PEFT target | Proven as the docs' default | Contrasted with the next row |
| All-linear adapters; LoRA matches full fine-tuning in low-data post-training; attention-only lags | Emerging (Thinking Machines, 2025; also the PEFT QLoRA recipe for all-linear) | Advanced reading, not a graded sweep |
| Fine-tuned encoders beat zero-shot GPT-4/Claude on those classification tasks | Proven inside Bucher and Martini, 2024 | Evidence against "prompting has won" |
| Few-shot prompt selection beat fine-tunes by ~10% F1 in scarce industrial NER; fine-tune won when data were abundant | Emerging (Tang et al., 2025) | Evidence against "always fine-tune" |
| Soft prompts versus model tuning on clinical extraction, small gaps | Proven as Peng et al., 2024, on those datasets | Vocabulary only |
| Fine-tune reduced hallucinations versus prompting on FinCausal 2025 | Emerging (Niess et al.) | Format and span failure mode |
| RAG beat unsupervised fine-tuning for knowledge injection | Proven inside Ovadia et al., EMNLP 2024 | Support for hours-on-retrieval, not a ban on supervised adapters |
| MLflow aliases; stages deprecated since 2.9 | Proven (MLflow docs) | One paragraph |
| JSON hash allow-list checked on the request | Proven as the control this case needs | Required |
| Azure: not used to train; Global/DataZone may process outside one region; abuse monitoring may store prompts | Proven as that vendor page on the day it was opened | Reading excerpt, not permission |
| Presidio-style local detection | Emerging as a backstop | One planted name |
| CPU frozen-matrix LoRA as "the clinic model" | Experimental | Required only if labeled `lora-cpu` |
| Case `vram_gb` on `local-small` | Experimental fixture | Must be marked as a case card |
| "Reasoning models beat LoRA on this extraction" | Unverified | Do not teach |

## Sources

LoRA. Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. "LoRA: Low-Rank Adaptation of Large Language Models." arXiv:2106.09685, 2021. https://arxiv.org/abs/2106.09685

QLoRA. Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. "QLoRA: Efficient Finetuning of Quantized LLMs." arXiv:2305.14314, 2023. https://arxiv.org/abs/2305.14314

PEFT. Hugging Face. "LoRA" conceptual guide and "Quantization" developer guide, including the 4-bit QLoRA load and `target_modules="all-linear"`. https://huggingface.co/docs/peft/main/conceptual_guides/lora and https://huggingface.co/docs/peft/developer_guides/quantization

Classification, zero-shot versus fine-tune. Martin Juan José Bucher and Marco Martini. "Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification." arXiv:2406.08660. https://arxiv.org/abs/2406.08660

Domain NER, few-shot versus fine-tune. Yongjian Tang, Rakebul Hasan, and Thomas Runkler. "FsPONER: Few-shot Prompt Optimization for Named Entity Recognition in Domain-specific Scenarios." arXiv:2407.08035. https://arxiv.org/pdf/2407.08035

Clinical prompt tuning. Cheng Peng, Xi Yang, Kaleb E. Smith, Zehao Yu, Aokun Chen, Jiang Bian, and Yonghui Wu. "Model tuning or prompt tuning? A study of large language models for clinical concept and relation extraction." Journal of Biomedical Informatics, 2024. https://doi.org/10.1016/j.jbi.2024.104630

Hallucinated spans. Georg Niess, Houssam Razouk, Stasa Mandic, and Roman Kern. "Addressing Hallucination in Causal Q&A: The Efficacy of Fine-tuning over Prompting in LLMs." FinCausal 2025, ACL anthology. https://aclanthology.org/2025.finnlp-1.27.pdf

Retrieval versus unsupervised fine-tuning. Oded Ovadia, Menachem Brief, Moshik Mishaeli, and Oren Elisha. "Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs." EMNLP 2024. https://aclanthology.org/2024.emnlp-main.15/

LoRA versus full fine-tuning, 2025 lab note. Thinking Machines Lab. "LoRA Without Regret." https://thinkingmachines.ai/blog/lora/

Model registry. MLflow. "ML Model Registry" and the workflow note that stages are deprecated as of 2.9 in favor of aliases. https://mlflow.org/docs/latest/ml/model-registry/ and https://mlflow.org/docs/latest/ml/model-registry/workflow.md

Residency and gateways. Microsoft Learn. "Data, privacy, and security for Foundry Models sold by Azure." https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy — and "Access Foundry Models and Other Language Models Through a Gateway." https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/azure-openai-gateway-guide

Local detection, repository blurb only. Microsoft Presidio. https://github.com/microsoft/presidio

Course files this evaluation is based on, not external sources: `course_design/module-03.md` Lesson 2, `course_design/slides/module-03-lesson-02.md`, `instructional/curriculum-understanding-map.md` Module 3 Lesson 2, student chapters 00 and 03–10, `problem_simulation/alwaha/check/model_m03_l02.py`, `lora_m03_l02.py`, `engagement/m03_l02_rules.py`, `samples/prices.py`, and the pack files `ruling.md`, `reg-models.json`, `quota.json`, and `price-cap.json`.
