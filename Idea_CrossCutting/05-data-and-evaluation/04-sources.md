# Sources

Read on 30 October 2026. Each item is a page that was opened or a paper page that was retrieved for this note. Teaching points are limited to what those pages support.

## Record linkage

- Splink repository. States what the library is for: probabilistic linkage and deduplication without a unique id, Fellegi-Sunter with customizations, unsupervised training, term-frequency adjustments, user-defined fuzzy matching, DuckDB or Spark. States the data shape it wants: several columns that are not highly correlated. States what it refuses: a single bag-of-words column. The `fake_1000` quickstart lives behind the docs link, not as a health corpus.
  https://github.com/moj-analytical-services/splink/
- Getting started. `link_type="dedupe_only"`, name and date-of-birth comparisons, blocking, estimates of the random-match probability, u by sampling, m by expectation maximization, then clustering. The 0.95 threshold in that snippet is a demo argument.
  https://moj-analytical-services.github.io/splink/getting_started.html
- Fellegi-Sunter topic guide. Defines λ, m, and u. m is data quality (typos, aliases, estimated dates such as 1 January, moves). u is coincidence, with date of birth high-cardinality and sex low-cardinality. Match weights add because comparisons are assumed independent. Match probability is a nonlinear function of the total weight.
  https://moj-analytical-services.github.io/splink/topic_guides/theory/fellegi_sunter.html
- Estimating model parameters (tutorial 4). Same three parameters, and the remark that labels estimate them more accurately than unlabeled data alone. Blocking rules decide which pairs are scored.
  https://moj-analytical-services.github.io/splink/demos/tutorials/04_Estimating_model_parameters.html

Splink's own pages do not describe Hijri dates, Arabic morphology, or mother/newborn pairs. Those are course requirements applied to the documented assumptions: normalize calendars before blocking, do not treat correlated household fields as independent evidence, and keep a non-identity edge out of the person cluster.

## Synthetic clinical data, and its limits

- Walonoski et al., "Synthea: An approach, method, and software mechanism for generating synthetic patients and the synthetic electronic health care record," JAMIA. Modular, probability-driven lifecycle; population rates vary by run and approach the input probabilities rather than a predetermined table. The paper also notes how thin published validation of synthetic records has been.
  https://academic.oup.com/jamia/article/25/3/230/4098271
- Chen, Chun, Patel, Chiang, and James, "The validity of synthetic clinical data: a validation study of a leading synthetic data generator (Synthea) using clinical quality measures," BMC Medical Informatics and Decision Making, 2019. On a Massachusetts Synthea cohort of 1,193,439: colorectal screening compliance 63% (reported Massachusetts 77.3%, national 69.8%); COPD 30-day mortality 0.7% (reported 7% and 8%); no hip/knee complications (reported about 2.9% and 2.8%); no controlled blood pressure after hypertension (reported about 74.5% and 69.7%). Authors: reliable for demographics and for average service probabilities; weak for heterogeneous outcomes; generators of this kind do not model departure from guidelines.
  https://doi.org/10.1186/s12911-019-0793-0
- Walonoski et al., Synthea COVID-19 model paper. The introduction records the criticisms the authors were answering: limited variation by provider, limited heterogeneous outcomes after major interventions, and clinical notes that were not yet sufficient.
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7531559/
- Synthea README and default properties. Exports include FHIR R4, STU3, DSTU2, C-CDA, and CSV. Defaults follow the documented configuration, including Massachusetts-oriented demographics. `generate.payers.loss_of_care` is commented as experimental: missed care can be turned on, and side effects of that missed care are not handled. `exporter.clinical_note.export` exists and is separate from the structured record.
  https://github.com/synthetichealth/synthea/blob/master/README.md
  https://github.com/synthetichealth/synthea/blob/master/src/main/resources/synthea.properties
- Clinical notes are templates. Issue 286 was closed because a template exporter shipped. Discussion 1556: the notes a user inspected were rudimentary restatements of structured data; the maintainer pointed to `chatty-notes`, with the caveats that it was one-shot, aimed at an old ChatGPT API, and special-cased for osteoarthritis.
  https://github.com/synthetichealth/synthea/issues/286
  https://github.com/synthetichealth/synthea/discussions/1556

No page above describes a generator for bilingual conflicting circulars, Hijri/Gregorian identity twins, channel templates, or stale warehouse snapshots. The course's own fact-spec pipeline (facilitator design `problem_simulation/design/05-corpus.md` and `07-datasets.md`) is the document generator that was found in this repository: facts fixed, phrasing allowed, missing or extra facts rejected.

## RAG evaluation

- Es, James, Espinosa-Anke, and Schockaert, "RAGAs: Automated Evaluation of Retrieval Augmented Generation," arXiv:2309.15217, also EACL 2024 demo. Reference-free faithfulness, answer relevance, and context relevance, scored by prompting an LLM. Faithfulness is the share of extracted statements the judge says the retrieved context supports. The authors report context relevance as the hardest dimension, and that ChatGPT often failed to select the crucial sentences, especially in longer contexts.
  https://arxiv.org/abs/2309.15217
  https://aclanthology.org/2024.eacl-demo.16/
- Current RAGAS docs. Faithfulness remains supported-claims over all claims in the response, given the retrieved context. Context precision with a reference compares chunks to a reference answer. Without a reference, the LLM compares chunks to the generated response.
  https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/
  https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/context_precision/
- Roychowdhury, Soman, Ranjani, Gunda, Chhabra, and Bala, "Evaluation of RAG Metrics for Question Answering in the Telecom Domain," arXiv:2407.12873. Independent look at RAGAS on specialized QA. They call out missing derivations of the numbers. Faithfulness generally tracked expert judgment and still moved when statements were split awkwardly. Context relevance depended on context length and was hard to interpret. Answer relevance used cosine similarity as an absolute component, which they argue is a poor basis for a threshold.
  https://arxiv.org/abs/2407.12873

## LLM-as-judge and calibration

- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena," NeurIPS 2023 datasets and benchmarks, arXiv:2306.05685. Position bias: on similar answers, swap consistency was 23.8% (Claude-v1), 46.2% (GPT-3.5), and 65.0% (GPT-4). Verbosity: a repetitive-list attack succeeded against Claude-v1 and GPT-3.5 on 91.3% of 23 items and against GPT-4 on 8.7%. Identical answers were tied, which the authors call a calibration check, and it did not survive the verbosity attack. Self-enhancement: GPT-4's self win rate was about 10 points higher than humans, Claude-v1 about 25, and the study does not claim that proves the bias. Non-tie agreement, GPT-4 versus humans on MT-Bench, about 85%, against about 81% human-human. Agreement rose when the two models were far apart. Reference-guided grading reduced math failures where the judge copied the candidate's mistake. Few-shot examples raised GPT-4 swap consistency from 65% to 77.5% and did not raise human agreement; the authors warn that consistency is not accuracy.
  https://arxiv.org/abs/2306.05685
  https://papers.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf
- Liu, Yang, Huang, Zhang, Huang, Wei, Deng, Sun, and Zhang, "Calibrating LLM-Based Evaluator," arXiv:2309.13308. AutoCalibrate: build a human label set, draft rubrics from few-shot labels, keep the rubrics that correlate, and revise them on disagreements. The target is correlation with experts, not a higher score on the system's own outputs. This is the sense of calibration `slice-judge` needs: a judge checked on a held-out human set before it gates a release.
  https://arxiv.org/abs/2309.13308

## Offline and online evaluation

- Kohavi, Tang, and Xu, *Trustworthy Online Controlled Experiments*, Cambridge University Press, 2020. Chapter 1 defines the overall evaluation criterion as the quantitative objective of the experiment: measurable in the short window of the test, and believed to drive the longer-term goal. One criterion, possibly a weighted combination, forces the tradeoff. Random assignment of a persistent unit is what supports a causal claim. The open chapter PDF matches the book text on that definition.
  https://doi.org/10.1017/9781108653985
  https://experimentguide.com/wp-content/uploads/TrustworthyOnlineControlledExperiments_PracticalGuideToABTesting_Chapter1.pdf
- Metrics chapter (book chapter 7). The criterion has to be sensitive and timely enough to use during an experiment, and still pointed at the long-term objective.
  https://doi.org/10.1017/9781108653985.010
- Kohavi, Longbotham, Sommerfield, and Henne, "Controlled experiments on the web: survey and practical guide," Data Mining and Knowledge Discovery, 2009. Earlier statement of the same criterion, and of why randomization is the causal step. Useful if the 2020 book is not on the reader's shelf.
  https://doi.org/10.1007/s10618-008-0114-1
- Gruson, Chandar, McInerney, Beutel, Chi, et al. (Spotify), "Offline Evaluation to Make Decisions About Playlist Recommendation Algorithms," RecSys 2019. Offline metrics on ordinary interaction logs are biased by the interface and by the ranker that produced the logs. Online tests are the causal standard and are slower and riskier. A debiased offline estimator can be used to choose what is worth testing online; the paper's claim is correlation with online results for that playlist task, not a general license to skip the online test.
  https://pchandar.github.io/files/papers/Gruson2019.pdf

## Course pages used as the local specification

These are not external sources. They are the constraints this note fits.

- `instructional/curriculum-understanding-map.md`, the Module 3 week (mislabeled "Module 2 — Data, adaptation, retrieval, evaluation" in the heading).
- `problem_simulation/design/11-eval-and-hardness.md`, especially `chk-eval` and `slice-judge`.
- `problem_simulation/design/05-corpus.md` and `07-datasets.md`, the fact-spec documents and the gold fields for letters, messages, DNA, and retrieval.
