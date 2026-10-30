# Module 03 Lesson 03 — Retrieval: research index

This folder is an independent curriculum review of Module 3, Lesson 3 (Cite, pack `rel-m03-l03`). It does not change the course. The lesson’s student chapters, solution, checks, and corpus stay where they are. The recommendation below is for a later redesign.

The challenge thesis is this. A hybrid ranker with an audience filter is necessary for this document store, and it is incomplete. The production problems are permission-aware retrieval, document-version binding, citation faithfulness, and conflict handling. Lexical-plus-vector fusion, contextual retrieval, GraphRAG, and agentic multi-hop answer different questions. This lesson should implement the first family’s policy half, a small reciprocal-rank fusion, and an extractive citation. It should name the other three.

## How to read the set

| File | Question it answers |
| --- | --- |
| [01-existing-lesson-evaluation.md](01-existing-lesson-evaluation.md) | What the chapters, the Python, and `chk-m03-l03-rag` / `slice-hybrid` / `slice-acl` actually teach and grade |
| [02-industry-research.md](02-industry-research.md) | What the primary sources say about fusion, context, graphs, multi-hop, long context, and faithfulness metrics |
| [03-redesign-architecture-and-simulation.md](03-redesign-architecture-and-simulation.md) | Which architecture to build on the existing Al-Waha corpus, and which planted failures to keep |
| [04-exercises-assessment-instruction.md](04-exercises-assessment-instruction.md) | Self-paced Python scope, roles one person holds, exercises, and checks |
| [05-tradeoffs-recommendations-sources.md](05-tradeoffs-recommendations-sources.md) | Deletions, tradeoffs, lessons to spawn, and the source list |

The core-versus-extension split with the instructional dossier is in `Idea_CrossCutting/06-instructional-design/05-core-versus-extension.md`. The audience pre-filter, the version pin, and the extractive citation open the next lesson. Reciprocal rank fusion is the extension.

Maturity labels used everywhere:

- **Proven.** A method with a stable primary description and a production or textbook use that matches the problem it claims to solve. Reciprocal rank fusion, BM25-style lexical rank, pre-filters, extractive citation, and row-level audience rules are in this class for a policy register.
- **Emerging.** A published method with a real evaluation, whose fit to this lesson’s store is partial or whose cost and failure modes are still moving. Anthropic’s contextual retrieval and Microsoft’s GraphRAG are in this class.
- **Experimental.** A method that can help a different task, and that would make this lesson’s citation guarantees weaker if it became the implementation. An open agent loop over the document store, and an LLM judge as the grade for this release, are in this class.

Vendor-reported retrieval rates are quoted only as the vendor stated them, with the metric name they used. This review invents no nDCG.

## Recommendation

Keep the case. Criteria v4 comes into force for endocrinology, ophthalmology, and cardiology only. An in-flight referral keeps the version it started on. `circ-ramadan-unauth` is unauthorized and mis-filed as public. A staff leaflet must not be cited to a patient. The change feed, not the markdown snapshot, is the update. Those facts are more realistic than a generic “embed the handbook” lab, and the grader already encodes them.

Change what the word hybrid means in the code. In `search.rank`, hybrid mode drops every chunk whose status is not `in_force` and adds 1 to a cosine score when a hyphenated code from the question is a key in the chunk vector. Vector mode keeps every status and adds nothing. `slice-hybrid` passes when vector mode ranks the unauthorized circular first and hybrid mode ranks the in-force hours circular first. That slice is a status filter wearing a fusion name. Industry hybrid search, as OpenSearch documents it and as Cormack, Clarke, and Büttcher defined reciprocal rank fusion in 2009, combines two ranked lists. It does not decide which documents are legal to cite.

Implement, in ordinary Python, on the existing snapshot and feed:

1. A pre-filter that runs before any score. The asker’s audience, the citable statuses for this question, and the specialty notice all apply here. Unauthorized documents never enter a candidate list. Drafts may be found by a separate search that cannot return a citation. **Proven.**
2. Version binding that reads the v4 specialty set from the notice, keeps a superseded v3 when the referral’s start day sits inside its window, and pins the citation to `content_hash` as well as version and clause id. The hash is already on the document rows. The citation fields the rag check compares today omit it. **Proven** as application logic.
3. An extractive citation. The returned text is the clause text. A refusal carries no clause. Faithfulness for this lesson is equality with the stored span, plus the audience, status, version, and hash. **Proven.**
4. Reciprocal rank fusion of two lists on the already-filtered set: a lexical score that rewards codes and rare tokens, and the existing token-share cosine. Use the constant from the 2009 paper’s pilot, k = 60, and grade top-1 on a planted pair where each list alone is wrong. Do not report nDCG on fifteen documents. **Proven** algorithm, toy retrievers.
5. A conflict record for the booking window: both document ids, the cluster document as winner, the answer text taken only from the winner’s clause. **Proven** policy.
6. The service-catalog lookup as a path that must not acquire a leaflet id. **Proven.**
7. The photo transcription gap as an ingestion rule: the sentence present only in `transcription` becomes a chunk with audience, status, and its own clause id. **Proven** ingestion. A vision model is not part of the implementation.

Name, in a short reading with the primary links, and do not build:

- Contextual retrieval as Anthropic published it on 19 September 2024. **Emerging.** Their metric is one minus recall at 20, not nDCG. The post also says a knowledge base under about 200,000 tokens can sit in the prompt. This pack is far smaller. The reason to retrieve is permission and version, which a stuffed prompt does not enforce.
- GraphRAG as Edge and colleagues describe it. **Emerging** for global questions over large private corpora. **Experimental** as the index for a criteria register that already has specialty, status, effective, and sunset fields.
- Agentic multi-hop in the sense of IRCoT. **Emerging** on HotpotQA-style benchmarks. **Experimental** as the citer for this store, because a free hop can surface the staff leaflet or the unauthorized circular. One scripted second lookup, criteria code then public leaflet, is enough code.
- RAGAS faithfulness as the grade. **Emerging** as a reference-free metric, with published limits. Lesson 4 already owns an uncalibrated judge. This lesson should hand that lesson a citation record a judge can get wrong.

## What to delete

Delete the facilitator syllabus line that this lab builds a vector-database pipeline and optimizes response generation. The student words page already says the folder does not start a database and does not train `local-embed`. The code matches the words page. The syllabus does not.

Delete the identification of hybrid search with “keep `in_force` and add one.” Keep a real fusion, and keep the status rule under the policy filter.

Delete the advanced chapter’s claim to vision. `vision.clause` removes the export string from the transcription. `slice-vision` in the design notes is an OCR or vision pass. The three finish checks do not read `vision.py`, `conflict.py`, or `catalog.py`. Either the photo clause enters the foundation index under an honest name, or the chapter stops using the vision brand.

Delete an open GraphRAG index, a contextualizer call to a hosted model, and an agent loop from the self-paced path. One person, no API key, and the existing unittest runner are the constraints that make the lesson finishable.

## The rule for implement versus name

A technique is implemented in this lesson when three conditions hold at once. The failure it prevents is already planted in `rel-m03-l03` or can be planted with one extra public, in-force pair. A correct behavior fits in a function the existing unittest style can call with dicts, with no network and no model file. A wrong behavior is visible as the wrong document id, the wrong version, a staff audience on a patient citation, or a string that is not the clause. Pre-filter, version window, extractive citation, a twenty-line fusion, the booking conflict, the catalog lookup, and the transcription gap meet that rule.

A technique is named when any of those conditions fail. Contextual retrieval needs a model call per chunk and a recall-at-20 corpus this pack is not. GraphRAG’s published target is global sensemaking over collections on the order of a million tokens, with an LLM building the graph. IRCoT’s published gains are on multi-hop Wikipedia sets, and the loop decides what to retrieve next. RAGAS faithfulness needs a second model to judge claims, which is the failure Lesson 4 is built to catch. Naming them, with the metric and the limit attached, is the advanced reading. Building them would either fake the method, as `vision.clause` fakes a vision pass, or make the finish checks depend on a service the self-paced reader does not have.

The student journey log for this lesson records fifteen pastes and zero failures after the paste fix, with `chk-m03-l03-rag`, `slice-hybrid`, and `slice-acl` passing on both the student work and the solution. That is evidence the current chapters are completable. It is also evidence that completion does not require choosing among the architectures in the research file. The redesign keeps the completable path and moves the choice into three functions the reader writes against failing tests: the pre-filter, the version bind, and the fusion. Chunking and the token vector stay provided, so the day still ends.

## What one person holds

The background chapter already assigns lead, index, application, product, and architect to the same reader. Keep that. The redesign does not add a second role for “the retrieval specialist” or “the security reviewer.” The same person writes the pre-filter, the bind, the refusal sentence, and the audience table, then runs the checks. The solution copy stays closed until the finish chapter, as it does now.

## Five sources to open first

1. Cormack, Clarke, and Büttcher, reciprocal rank fusion, SIGIR 2009: https://dl.acm.org/doi/10.1145/1571941.1572114
2. Anthropic, contextual retrieval, 19 September 2024: https://www.anthropic.com/engineering/contextual-retrieval
3. Edge et al., GraphRAG, arXiv:2404.16130: https://arxiv.org/abs/2404.16130
4. OpenSearch hybrid search and document-level security: https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/index/ and https://docs.opensearch.org/latest/security/access-control/document-level-security/
5. Es et al., RAGAS, EACL 2024 system demonstrations: https://aclanthology.org/2024.eacl-demo.16/

Liu et al. on long context, the pgvector hybrid section, and the IRCoT paper are cited in the research file and the source file. They support the “name, do not build” column. They are not a sixth implementation.
