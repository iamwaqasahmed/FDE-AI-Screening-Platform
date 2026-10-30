# Industry research — adapters, prompts, registries, residency

Sources below were opened. Numbers appear only when the opened page states them. This note does not treat a vendor abstract as a clinical result, and it does not fill gaps with a win-rate.

## LoRA — Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang, and Chen

Page opened: [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) (arXiv:2106.09685, submitted 17 June 2021, revised 16 October 2021). The HTML version of v2 was also opened.

The method freezes the pretrained weights and adds a low-rank update. For a frozen matrix \(W_0\), the layer computes \(W_0 x + (\alpha / r) B A x\), with trainable \(A\) and \(B\). The paper's hypothesis, credited to earlier intrinsic-dimension work, is that the change in weights during adaptation itself has low rank. On GPT-3 175B they report that a rank of one or two can be enough when the full dimension is 12,288.

Claims on the abstract, which are about full fine-tuning, not about prompting:

- Versus GPT-3 175B fine-tuned with Adam, LoRA reduced trainable parameters by 10,000 times and the GPU memory requirement by 3 times.
- Quality was on par or better than full fine-tuning on RoBERTa, DeBERTa, GPT-2, and GPT-3, with higher training throughput.
- Unlike earlier adapter layers, there is no extra inference latency, because the low-rank factors can be merged into \(W_0\).
- One frozen base can carry many task-specific modules. Switching tasks is swapping \(A\) and \(B\).

Limitations that the lesson must say out loud. The models are 2021-scale, not instruction-tuned reasoning models. "On par or better" is versus full fine-tuning of the same base, on the tasks they ran. It is not a result about extraction from referral letters, and it is not a result about a prompted larger model. The memory multiple (3 times, not 100 times) is for optimizer state on the frozen weights under Adam, not a promise that any LoRA job fits in an arbitrary GPU quota. Rank is a capacity knob. The course's `rank: 8` literal does not teach that knob.

**Proven** as the update rule, the merge-for-latency claim, and the "many adapters, one base" deployment pattern. **Not proven** as the default customization for every clinic task.

## QLoRA — Dettmers, Pagnoni, Holtzman, and Zettlemoyer

Page opened: [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) (arXiv:2305.14314, 23 May 2023; the abs page calls it an extended NeurIPS submission). The HTML article was opened.

QLoRA backpropagates through a frozen 4-bit quantized model into LoRA adapters. The three memory devices they name are 4-bit NormalFloat (NF4), double quantization of the quantization constants (they estimate about 0.37 bits per parameter, about 3GB on a 65B model), and paged optimizers for spikes. They state that average memory for fine-tuning a 65B model drops from more than 780GB to under 48GB without degrading runtime or predictive performance relative to a 16-bit fully fine-tuned baseline, so a 65B model fits on one 48GB GPU. They also say their best Guanaco model reached 99.3% of ChatGPT on the Vicuna benchmark after 24 hours on one GPU, and that a 7B Guanaco needs 5GB at deployment and outperformed a 26GB Alpaca by more than 20 percentage points on that benchmark.

The same paper says current chatbot benchmarks are not trustworthy for ranking chatbots, and it includes a lemon-picked analysis of where Guanaco fails relative to ChatGPT. The 99.3% figure is a Vicuna score, GPT-4-judged in their setup, not an extraction F1. The 5GB figure is inference for the 7B model, not training memory. The 48GB figure is one professional GPU for a 65B QLoRA job. It is the right number to teach as a refusal threshold for that job. It is the wrong number to paste onto the course's fictional `local-small`.

**Proven** as a memory technique and as a concrete "this job does not fit a small GPU" example for 65B-class full fine-tuning versus 65B QLoRA. **Emerging** as a claim about matching ChatGPT, because the paper itself discounts chatbot benchmarks. **Not a laptop lab.**

## PEFT as the library, and a disagreement the lesson should keep

Pages opened:

- [LoRA conceptual guide](https://huggingface.co/docs/peft/main/conceptual_guides/lora). The page warned that `main` may require a source install and named stable v0.21.0 at the time of the fetch.
- [Quantization guide](https://huggingface.co/docs/peft/developer_guides/quantization).

PEFT's account of LoRA matches Hu: frozen base, low-rank update matrices, merge with `merge_and_unload()` so inference does not pay for a separate adapter load. Default initialization is Kaiming-uniform for \(A\) and zeros for \(B\), so an untrained adapter is an identity. That single fact belongs in the lesson: serving a freshly initialized adapter does nothing, which is why a registry row with no training is not an adapter.

Parameters the student should see as names, not as a training ritual: `r`, `target_modules`, `lora_alpha`, `bias`, `use_rslora` (scale by \(\alpha / \sqrt{r}\) rather than \(\alpha / r\)). The conceptual guide says LoRA is typically applied to attention blocks only. The quantization guide says QLoRA-style training sets `target_modules="all-linear"`, loads with `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True)`, then `prepare_model_for_kbit_training`. It repeats the 65B-on-48GB example. It also says quantized models are usually not trained further because low precision is unstable, and that PEFT makes it practical because only the added weights are trained.

LoftQ is documented as an initialization that tries to reduce quantization error. The guide's constraints (safetensors, bitsandbytes 4-bit, and `replace_lora_weights_loftq` doing one iteration) are instructor detail, not a student exercise.

**Proven** as the API a later optional lab would call. The attention-only default versus `all-linear` is a live disagreement, not a footnote. See the next section.

## When LoRA matches full fine-tuning — Schulman and Thinking Machines, 2025

Page opened: [LoRA Without Regret](https://thinkingmachines.ai/blog/lora/) (Thinking Machines Lab, the page fetched for this note).

They separate two regimes. LoRA underperforms when the setting looks like pretraining, which they identify with large datasets that exceed LoRA's storage, pointing at Biderman and colleagues, 2024, "LoRA Learns Less and Forgets Less." For post-training dataset sizes they report that LoRA can match full fine-tuning's sample efficiency and final performance if two conditions hold: the adapter is applied to all layers, especially MLP and MoE, and the trainable parameter count is not capacity-constrained relative to the information in the data. Attention-only LoRA underperformed even when rank was raised to match parameter count. LoRA matched full fine-tuning on their reinforcement-learning runs even at rank 1. They also report an optimal learning rate about 10 times the full fine-tuning rate, and a larger batch-size penalty that raising rank did not remove.

This is a lab blog about loss and reward on instruction, reasoning, and RL runs. It is not a referral-letter extraction study, and it does not compare LoRA with prompting. It is still the right 2025 text for this lesson, because the course's QLoRA file treats rank as a GPU-count formula and never asks which matrices are trained. The PEFT conceptual guide's "attention blocks only" and this blog's "attention-only is not enough" should both be on the page, labeled differently: the first is the library's typical setting (**Proven** as documentation), the second is a 2025 empirical claim about matching full fine-tuning (**Emerging**).

## Prompting versus fine-tuning — only studies opened here

The thesis says teaching LoRA as the default is outdated if reasoning models and careful prompting win on extraction. The studies opened do not support a single winner. They support a decision.

### Zero-shot large models versus fine-tuned encoders, classification

[Bucher and Martini](https://arxiv.org/abs/2406.08660), "Fine-Tuned 'Small' LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in Text Classification" (arXiv:2406.08660). They compare fine-tuned RoBERTa, DeBERTa, Electra, and XLNet with zero-shot GPT-3.5, GPT-4, and Claude Opus on sentiment, approval, emotion, and party-position tasks over news, tweets, and speeches. Their abstract says fine-tuning with application-specific data was superior in all cases they ran. In the training-size ablation, RoBERTa Large starts to beat their most consistent zero-shot baseline (BART) once the training set exceeds 200 examples, on the datasets in that figure. Zero-shot was closer on ordinary sentiment and failed to beat a naive baseline on the less standard stance and emotion tasks.

Limitations. This is zero-shot, not a carefully engineered few-shot prompt and not a reasoning model. The fine-tune is a full encoder fine-tune, not LoRA on a decoder. The texts are not clinical. "In all cases" means their four applications. It does not mean fine-tuning wins extraction in a hospital.

**Proven** inside those bounds: a fine-tuned smaller encoder can beat a zero-shot general model on classification when labeled data exists. **Not** a license to skip prompting, and **not** a LoRA-versus-GPT result.

### Few-shot prompting versus fine-tuning, domain NER

[Tang, Hasan, and Runkler](https://arxiv.org/pdf/2407.08035), "FsPONER: Few-shot Prompt Optimization for Named Entity Recognition in Domain-specific Scenarios" (arXiv:2407.08035v2, 1 April 2025). They select few-shot examples (random, TF-IDF, or both) and compare GPT-4-32K, GPT-3.5-Turbo, LLaMA 2-chat, and Vicuna with fine-tuned BERT and LLaMA 2-chat 7B on industrial manufacturing and maintenance NER. The abstract says that in the scarce-data scenarios they considered, FsPONER with TF-IDF surpassed the fine-tuned models by approximately 10% F1. The discussion qualifies that: on generic entity types with little data, few-shot prompting can beat fine-tuning on the full set; on FabNER, where data are abundant, fine-tuning still leads. They flag hallucination, unstable output format, and long inference time when many shots are in the prompt, and they say GPU budget, time, and cost have to be part of the choice.

Limitations. Manufacturing NER, not clinical concept extraction. The "approximately 10%" is their scarce industrial setting, not a universal delta. The prompted models include GPT-4-32K, which is not the same object as a 2026 reasoning model. Format drift is directly relevant to this lesson: an adapter or a schema constraint can be the right tool because the prompt will not stay inside a JSON contract, even when its entities are good.

**Emerging.** Real, narrow, and the cleanest opened support for "do not fine-tune by default when labels are scarce and a strong prompted model is allowed to see the text."

### Soft prompts versus model tuning, clinical extraction

[Peng, Yang, Smith, Yu, Chen, Bian, and Wu](https://doi.org/10.1016/j.jbi.2024.104630), Journal of Biomedical Informatics, 26 March 2024, "Model tuning or prompt tuning? A study of large language models for clinical concept and relation extraction." They compare four strategies on GatorTron (345M, 3.9B, 8.9B) and smaller clinical transformers, on adverse drug events and social-determinants benchmarks: fine-tuning without prompts, hard prompts with unfrozen weights, soft prompts with unfrozen weights, and soft prompts with frozen weights. When models are unfrozen, GatorTron-3.9B with soft prompting had strict F1 0.9118 and 0.8604 on concept extraction, ahead of traditional fine-tuning by about 0.6 to 3.1 points and ahead of hard-prompt unfrozen models by about 1.2 to 2.9 points, as stated in the abstract. Frozen small models lagged; scaling the frozen model to 8.9B made frozen soft prompts competitive, and that frozen 8.9B setting was their best cross-institution result.

Limitations. "Soft prompt" here means trainable continuous embeddings, not a paragraph written for a reasoning model. Hard prompts are also used with unfrozen weights, so this is not "prompt instead of training." Gains over ordinary fine-tuning are small. The datasets are clinical benchmarks, which is closer to the case than FsPONER, and still not this course's four-line letter slice.

**Proven** as a clinical result that prompt-style adaptation and full model updates are close, and that freezing a large clinical model can transfer. **Not** evidence that a chat prompt replaces an adapter.

### Fine-tuning versus prompting when the failure mode is hallucination

[Niess, Razouk, Mandic, and Kern](https://aclanthology.org/2025.finnlp-1.27.pdf), FinCausal 2025 workshop (ACL anthology, pages 253–258). On English and Spanish financial causal questions they found prompt optimization and few-shot examples insufficient to beat extractive BERT-style taggers, with hallucinations. Fine-tuning generative models was, in their words, essential for minimizing hallucinations. Their fine-tuned multilingual model placed first on Spanish and second on English in that shared task.

Limitations. A six-page competition write-up on financial reports, not a controlled LoRA study, and not healthcare. "Essential" is their finding on that task. It is useful as a counterweight to FsPONER: when the output must be a span that exists in the source, an unconstrained prompt can lose for a reason other than F1.

**Emerging.** Teach the failure mode (the model writes a span that is not in the letter), not their leaderboard.

### What was not opened

No 2024–2026 paper was opened here in which a reasoning model (a deliberative model used with a long prompt) beat a LoRA adapter on clinical field extraction. The thesis should stay conditional. Saying "reasoning models have won" would invent a win-rate. The honest sentence is: opened studies disagree, and they disagree for reasons the lesson can score — data scarcity, output format, hallucination, and whether the comparator was zero-shot or a trained encoder.

## Retrieval is not a worse fine-tune

[Ovadia, Brief, Mishaeli, and Elisha](https://aclanthology.org/2024.emnlp-main.15/), EMNLP 2024, "Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs" (pages 237–250). They compare unsupervised fine-tuning with RAG for injecting facts, on MMLU topics and on current events. RAG consistently beat unsupervised fine-tuning both for knowledge the base model had seen and for new knowledge. Fine-tuning beat the base model in most of their settings and still was not competitive with RAG. Models struggled to absorb a new fact from unsupervised fine-tuning unless the fact was repeated in many paraphrases. Combining the fine-tuned model with RAG sometimes helped and sometimes hurt.

Limitations. The fine-tune is unsupervised continued training, not a supervised LoRA extraction head. The tasks are multiple-choice knowledge, not "which sub-specialty is this letter." The result does not say retrieval beats adapters at tagging `source_type`. It does say that putting changeable facts into weights is a weak injection method compared with showing the document.

That is the right citation for leaving hours on retrieval. The course's reason is stronger than the paper's and should stay primary: hours are a document that changes, with an audience and a version, and Lesson 3 will cite it. Ovadia is the external support for not "solving" `p-info` by adapting `local-small`. **Proven** for knowledge injection under their protocol. **Misapplied** if someone cites it as "never fine-tune."

## Registries — MLflow, and why a hash list is not the same object

Pages opened: [MLflow Model Registry](https://mlflow.org/docs/latest/ml/model-registry/) and the [workflow page](https://mlflow.org/docs/latest/ml/model-registry/workflow.md).

A registered model has a name, versions, aliases, tags, and annotations. A version URI looks like `models:/MyModel/1`. An alias is a mutable pointer: `models:/MyModel@champion` can be moved to a new version without changing the serving code. Stages (`Staging`, `Production`, `Archived`) are deprecated as of MLflow 2.9 and scheduled for removal; the migration note says aliases plus per-environment access control replace them. Tags such as `validation_status:approved` are how a team records a check without overloading the name.

The course's `reg-models.json` is a different, smaller object, and the smaller object is the one the trap needs. Each row has an id, a truncated `sha256:` digest, a status, and a zone. `lora-local` also has a base. The grader refuses any served hash other than the gold adapter hash, and refuses the cloud hash even if the model name is `local-small`. An alias or a display name is not an integrity check. MLflow will cheerfully retarget `@champion`. A residency review needs the bytes.

Teach both, with labels:

- **Proven.** An allow-list of content hashes, status `approved`, and a zone, checked on the request path. This is what `route.allow` already sketches.
- **Proven.** Aliases as the human pointer, from the MLflow docs, so "what is in production" can move without editing the router. The alias must resolve to a hash that is still on the list. Moving the alias does not approve the bytes.
- **Experimental** in this course if someone replaces the JSON file with a live MLflow server. Self-paced students do not need that server. A JSON register plus a SHA-256 the student computes is the whole lab. The current digest is 16 hex characters. Call it a teaching prefix, or store a full SHA-256. Do not describe 16 hex digits as a collision-resistant registry.

The cloud fine-tune stays closed even if a vendor registry would accept the job. Registration is not permission to train off the private cloud.

## VRAM and when to refuse

From the pages above, the only memory figures safe to teach as measurements are:

- Hu: about 3 times less GPU memory than Adam full fine-tuning for the GPT-3 175B comparison they report, because frozen weights do not keep optimizer state.
- Dettmers: more than 780GB down to under 48GB for 65B; one 48GB GPU; about 3GB saved by double quantization on that model; 5GB inference for their 7B Guanaco.
- PEFT quantization guide: the same 65B-on-one-48GB-GPU sentence, and the requirement for a 4-bit load before the adapter is attached.

No opened page stated a VRAM number for a 7B or 8B QLoRA training run on an 8GB or 12GB laptop GPU. Do not invent one. The refusal rule for the lesson is procedural:

- If the job card says full fine-tune of a 65B-class model, refuse. The paper's 780GB figure is why.
- If the job card says QLoRA of a 65B-class model, refuse unless the device card shows at least 48GB. The course quota is one GPU and does not state VRAM. One GPU is not 48GB.
- If `torch.cuda` is absent, refuse every job whose card requires CUDA. Offer the CPU teaching fit in file 03, labeled as a model of the update, not as QLoRA.
- If the card's published `vram_gb` for the case's own `local-small` exceeds the device, refuse. That `vram_gb` is a case fixture the authors write. It must be labeled "case card, not a Hugging Face measurement."
- Clamping the request down to `quota["gpus"]` and returning success, which is what `qlora.py` does, hides the refusal. Delete that behavior.

Rank does not buy a smaller GPU by itself. QLoRA's saving is the quantized frozen base and the absence of optimizer state on those weights. A higher rank increases trainable parameters and activation cost. Schulman's capacity story says a higher rank can be required when the dataset is large, and still will not fix a batch-size penalty. The course formula "32 ranks share one GPU" teaches neither paper.

## Residency — a gateway that blocks PHI, not a privacy policy

Page opened: [Data, privacy, and security for Foundry Models sold by Azure](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy) (Microsoft Learn; the change log on that page runs through 3 October 2025). Also opened in search and saved locally: [Access Foundry models through a gateway](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/azure-openai-gateway-guide).

The privacy page is easy to misread as "external is fine." It says prompts, completions, embeddings, and training data are not available to other customers, are not available to the model provider, and are not used to train foundation models without permission. Fine-tuned models are exclusive to the customer. It also says prompts and responses are processed in the customer-specified geography unless the deployment is Global or DataZone. Global processing may occur in any geography where that model is deployed. DataZone processing may occur anywhere inside the data zone (for example anywhere in the EU, or anywhere in the United States). Data at rest stays in the designated geography. Abuse monitoring can store a sample of prompts and completions for human review unless the customer is approved for modified monitoring. Batch processing is called out as a Global deployment type. Preview features may not follow the same storage rules.

None of that equals the case ruling. The ruling says patient data stays off `ext-large` and training stays on the private cloud. A vendor promise that they will not train on the prompt is not a promise that the prompt stayed in `zone-private`. Uploading a fine-tune file is exactly the cloud fine-tune the sprint closes, even if the resulting weights are customer-exclusive.

The architecture-center gateway guide adds the operational point: a gateway sees raw prompts and completions, so it is inside the compliance boundary. It can make a public model endpoint private, and then the gateway itself is the new entry. Identity at the account level is not identity at the deployment level. For strict sovereignty they recommend a separate gateway per geopolitical boundary, and they warn that Global and DataZone change where inference runs even when data at rest does not move.

Presidio was opened only as the GitHub repository blurb ([microsoft/presidio](https://github.com/microsoft/presidio)): a framework for detecting, redacting, masking, and anonymizing sensitive data in text, images, and structured data. Search snippets of the analyzer tree describe local recognizers and an Azure OpenAI recognizer. The lesson should use a local detector as a backstop. It should not send the letter to an external model in order to ask whether the letter contains PHI. That call is the egress the ruling forbids.

**Proven** controls to teach:

- Field allow-list before the HTTP call. The four names are the policy. Clinic hours are not on the list.
- Zone on the register row. `ext-large` is `zone-public`. An approved hash does not authorize a PHI payload.
- Geography of processing is a property of the deployment type, read from the vendor's own page, and it is still not the private cloud.
- The gateway is in scope because it sees the text. The canary demo stays.

**Emerging.** Using a local NER or regex detector for free text that is not in a structured field. It will miss paraphrases and it will false-positive on clinic names. It is a backstop, not the ruling.

**Experimental.** A student-built HTTP gateway process. The current `route.allow` function is enough for the self-paced check. A second process adds failure modes (timeouts, partial logs) that belong in Module 4.

## Bottom line for the redesign

LoRA is a low-rank update that can be merged, stored as a small file, and refused when the base does not fit. QLoRA is how a large frozen base might fit on one big GPU, and how a 65B full fine-tune does not. Prompting wins some scarce-data NER settings and loses some classification and span settings. Retrieval wins fact injection under Ovadia's protocol and wins hours in this case for a sharper reason. Classical ML stays the DNA method because the input is a table. A hash allow-list is the integrity control. A vendor privacy page is not a residency control. The lesson that falls out of these pages is the decision, the register, and a fit small enough to run without a GPU — not an adapter that is scripted to win.
