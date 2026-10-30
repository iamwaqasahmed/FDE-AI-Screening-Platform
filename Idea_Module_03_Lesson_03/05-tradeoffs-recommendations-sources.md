# Tradeoffs, recommendations, and sources

## Recommendation

Implement permission-aware retrieval, version binding with a content hash, extractive citation, and a small reciprocal-rank fusion on the filtered candidate list. Name contextual retrieval, GraphRAG, and an open multi-hop agent. Keep the Al-Waha pack. Delete the claim that the current hybrid branch is hybrid search, and delete the vision brand on a string replace.

That is the whole decision. The rest of this file is the tradeoff table, the deletion list, the lessons that should stay unborn, and the sources the other files quote.

## Tradeoffs

**Pre-filter before fusion, versus fusion on the full store and a check on the winner.** Pre-filter is **Proven** in the OpenSearch hybrid pre-filter documentation and in document-level security as a query that decides what a role may read. It costs a second path for in-flight rows: the superseded v3 must remain bindable while staying out of the default candidate list. The current code pays that cost by skipping `rank` on specialty questions and then forgetting to say so. A winner-only check is shorter and is what `slice-acl` grades today. It leaves the staff chunk inside `rank`’s return value. The tradeoff favors the pre-filter because the leak the course cares about is a document shown, logged, or stuffed into a later prompt, not only a wrong final id. OpenSearch issue 1303 is the warning that an engine’s hybrid query and its DLS rule can fail as a pair. Application-level `candidates` is the version a self-paced lab can test.

**RRF with k = 60, versus the +1 code boost, versus a tuned weight.** RRF is **Proven**, needs no labeled ranks, and matches the default OpenSearch documents. The +1 boost passes the current hours test and collapses two mechanisms into one flag. A weight fitted on this pack would be an invented hyperparameter. The tradeoff favors k = 60 taken from the paper’s pilot, where they say the choice was not critical, and a top-1 test on a three-chunk fixture. Nobody reports nDCG.

**Sparse token cosine as the second list, versus a neural embedding.** The sparse map is what Lesson 2 registered and what this folder can run offline. It is correlated with the lexical list, so the parking fixture has to be written until the two rankings disagree. A neural model would separate paraphrase from overlap more cleanly and would dominate the day with a download, a hash, and the residency rule Lesson 2 just closed. The tradeoff favors the stand-in, described honestly, with pgvector and OpenSearch named as the place a dense vector goes later. **Proven** infrastructure, deferred.

**Extractive equality, versus RAGAS faithfulness.** Equality catches a blend, a paraphrase, and a swapped body under the same version, and it cannot score a legitimate summary. RAGAS can score a summary and will accept an accurate quotation of the unauthorized circular, because the metric asks whether the context supports the claim. WikiEval’s 0.95 pairwise agreement on faithfulness is real and is about Wikipedia answers, fifty pages, one judge setup. The telecom preprint’s caution about claim splitting is real and is about another domain. Neither number is a license to grade `rel-m03-l03` with the library. The tradeoff favors equality here and a canned judge in Lesson 4, where the uncalibrated judge is already the trap. RAGAS stays **Emerging**.

**Single clause in the answer, versus Anthropic’s top 20.** Their post found 20 chunks better than 10 or 5 on one-minus-recall-at-20, and Liu et al. found middle position worse than closed-book for GPT-3.5-Turbo on multi-document QA, with the closed-book figure they state at 56.1 percent. This pack’s answers are legal citations, not essays. One clause, plus `also` when two policies conflict, is the record. The tradeoff is that a question whose answer truly spans two clauses must return two records or refuse. The booking conflict is that case, and it returns two ids and one text. **Proven** for policy. **Emerging** only if a later product wants a paragraph.

**Scripted second hop, versus IRCoT.** The scripted hop teaches that the second query is determined by a code in the first clause and is still filtered. IRCoT’s reported gains, up to 21 retrieval points and up to 15 QA points on four multi-hop sets, are about questions where the second query is not known in advance. The Al-Waha hop is known. An open loop is **Experimental** here because a generated query can overlap `circ-ramadan-unauth`. The tradeoff favors one extra test and a naming paragraph.

**GraphRAG versus the change feed.** Community summaries help global theme questions in the paper’s evaluation, at the win rates they report, after a model has read the corpus. The feed already lists which ids changed and the notice already lists which specialties moved. A graph index of this pack would be **Experimental** and would spend model calls the getting-started page warns about. The tradeoff favors the feed.

**Contextual retrieval versus a title line copied by the chunker.** Prepending “Endocrinology criteria v4, in force for endo” is something `chunk.py` can do from fields the document already has, with no model. That is a deterministic context line. It is not Anthropic’s method. Their method is a model reading the whole document, **Emerging**, and they say stores under about 200,000 tokens can skip retrieval entirely. A deterministic header is a reasonable one-line addition if the parking fixture is too artificial without it. It should be labeled as a field copy. Calling it contextual retrieval would repeat the vision mistake.

**Reading the notice, versus a constant set.** A constant `{card, endo, ophth}` can drift from `criteria-v4.md`. Reading the notice couples the sprint sentence to the bind. The cost is a parser for three tokens. The tradeoff favors the parser. **Proven.**

**Hash pin, versus version integer.** Version integers express the v3/v4 policy. They do not survive an in-place body edit. The hash does. Keeping both is cheap because the hash is already computed in `m03_l03_corpus.py`. The tradeoff favors storing both on the citation. A full document-management product would also freeze the bytes shown to the reader. The lab freezes the clause string next to the hash. That is enough.

**Promoting conflict and catalog into the foundation, versus leaving them unread.** They are each smaller than `fuse`. Leaving them in an advanced chapter that the checks ignore teaches that conflicts and structured data are optional color. The design notes say the opposite: the cluster window wins, and the catalog is where lookup beats retrieval. The tradeoff favors grading them. If the day overflows, the scripted hop moves to the reading, not these two.

**Paste, versus a blank function.** Full-file pastes produce the green journey log and skip the decision. Blank modules strand readers on syntax. Three small functions, with the current pedantic docstrings and a solution folder that opens after the finish chapter, is the compromise. **Proven** as a teaching pattern only in the weak sense that the course has already shown pastes work. The narrower blank is a recommendation, not a published pedagogy result.

## Deletions

Delete from the facilitator syllabus the sentence that this lesson builds RAG with vector databases and optimizes response generation. Replace it with the purpose line the curriculum map already uses, plus fusion and the hash.

Delete the hybrid mode whose meaning is “status is `in_force`, and add 1 for a code.” Replace it with `candidates` and `fuse`.

Delete the requirement that `sprint.md` contain the words index, filter, cite, and sync in that order as evidence of design. Keep the specialty limit and “not all.”

Delete the name vision from `vision.py`, and delete a solution that does not put the transcription remainder into the index. Either ingest it under an honest name and cite it, or remove the module from the suite.

Delete any plan to grade this lesson with RAGAS, nDCG, recall at 20, or a live judge model.

Delete GraphRAG, a contextualizer API call, an agent loop, OpenSearch, and Postgres from the implementation. They remain links.

Delete the knowledge-answer claim that bind checks site, unless conflict’s site rule is what that sentence points at. Today the solution’s first knowledge answer mentions site, and `bind.criteria` does not read it. The checker accepts the sentence anyway.

Delete nothing of the case: unauthorized public misfile, staff leaflet, in-flight window, three-specialty notice, feed versus snapshot, near-duplicate superseded leaflet, restricted safety policy, catalog row, photo gap.

## Lessons to spawn, and lessons to refuse

Spawn no new module. Extend Lesson 4 with one fixture: a fluent quotation of the wrong version beside a high “supported by context” verdict, and the hash that shows the version. That fixture is the critique of faithfulness, taught where judges are already in scope.

Add a paragraph to Module 4 Lesson 2 that the cache key for hours includes the content hash from this lesson. The incident lesson already drops a cache on `document.changed`. The hash says which body was cached.

Refuse a GraphRAG week, a contextual-retrieval week, and an agentic-RAG week inside this program. The comparison page is the spawn. A post-course elective may move `fuse` into SQL. It starts only after `candidates` is the `WHERE`.

## Unverified, and left unverified

This review did not re-execute OpenSearch 3.2.0 to confirm the comment on issue 1303. The citation is the issue, not a reproduction.

This review did not recompute Anthropic’s 5.7, 3.7, 2.9, and 1.9 percent failure rates. They are quoted from the 19 September 2024 post, as one minus recall at 20, on their domains, with the embedding and reranker they name.

This review did not recompute GraphRAG’s win rates. They are quoted from the paper’s v2 text as LLM-judge win rates on comprehensiveness and diversity, with the claim-count agreement they also report.

This review did not treat the telecom paper’s page header as proof of an ICML proceedings slot. The arXiv id is the handle.

No nDCG, no latency, and no cost for the Al-Waha pack is stated, because none was measured. Anthropic’s $1.02 per million document tokens is their worked example under their token assumptions. It is not a course budget.

## Sources

Cormack, G. V., Clarke, C. L. A., and Büttcher, S. Reciprocal rank fusion outperforms Condorcet and individual rank learning methods. SIGIR 2009. https://dl.acm.org/doi/10.1145/1571941.1572114 and the author PDF https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf.

OpenSearch. Hybrid search. https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/index/. Reciprocal rank fusion, introduced 2.19. https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/rrf/. Pre-filtering, introduced 3.0. https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/pre-filtering/. Hybrid query. https://docs.opensearch.org/latest/query-dsl/compound/hybrid/. Document-level security. https://docs.opensearch.org/latest/security/access-control/document-level-security/.

OpenSearch issue 1303, hybrid search with document-level security. https://github.com/opensearch-project/neural-search/issues/1303.

pgvector README, hybrid search section, including the pointer to the RRF example. https://github.com/pgvector/pgvector/blob/master/README.md. Postgres text search, as that section links it. https://www.postgresql.org/docs/current/textsearch-intro.html. RRF example. https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/rrf.py.

Anthropic. Introducing Contextual Retrieval. 19 September 2024. https://www.anthropic.com/engineering/contextual-retrieval. Cookbook. https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide.

Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., and Liang, P. Lost in the Middle: How Language Models Use Long Contexts. TACL 12, 157–173, 2024. https://aclanthology.org/2024.tacl-1.9/ and https://arxiv.org/abs/2307.03172.

Edge, D., et al. From Local to Global: A Graph RAG Approach to Query-Focused Summarization. arXiv:2404.16130. https://arxiv.org/abs/2404.16130. Docs. https://microsoft.github.io/graphrag/get_started/. Project page. https://www.microsoft.com/en-us/research/project/graphrag/publications/.

Trivedi, H., Balasubramanian, N., Khot, T., and Sabharwal, A. Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions. ACL 2023. https://aclanthology.org/2023.acl-long.557/ and https://arxiv.org/abs/2212.10509.

Es, S., James, J., Espinosa-Anke, L., and Schockaert, S. RAGAS: Automated Evaluation of Retrieval Augmented Generation. EACL 2024 System Demonstrations, 150–158. https://aclanthology.org/2024.eacl-demo.16/. Faithfulness metric. https://docs.ragas.io/en/latest/concepts/metrics/available_metrics/faithfulness/.

Alan Turing Institute, TEA techniques, retrieval-augmented generation evaluation, on the currency limit of faithfulness. https://alan-turing-institute.github.io/tea-techniques/techniques/retrieval-augmented-generation-evaluation/.

Roychowdhury, S., Soman, S., Ranjani, H. G., Gunda, N., Chhabra, V., and Bala, S. K. Evaluation of RAG Metrics for Question Answering in the Telecom Domain. arXiv:2407.12873. https://arxiv.org/abs/2407.12873.

## Course files this review used

The judgment is about these, and they were not modified. Curriculum map, Lesson 3. `course_design/module-03.md` Lesson 3 and `course_design/slides/module-03-lesson-03.md`. Student chapters `00` through `10`, especially `04-words`, `06-the-index`, `07-the-citation`, and `08-the-advanced`. Solution `01-what-done-is`, `05-the-advanced`, and `work/app` through `search`, `filter`, `bind`, `cite`, `sync`, `vision`, `conflict`, `catalog`, plus the unit tests. Checks `rag_m03_l03.py`, `hybrid_m03_l03.py`, `acl_m03_l03.py`, `notes_m03_l03.py`. Design `05-corpus.md`, `11-eval-and-hardness.md`, and `traceability/module-03-trace.md`. Journey log `instructional/student-journey/lessons/m03_l03.md`.

## Maturity, one list

**Proven, implement:** audience and status pre-filter; half-open version window; notice as the specialty authority; content hash on the citation; extractive clause text; RRF of a lexical list and the existing token vector; feed apply that keeps superseded rows; cluster-over-site with both ids; catalog lookup without a document id; photo remainder ingested as a clause.

**Emerging, name:** Anthropic contextual retrieval; GraphRAG for global sensemaking; IRCoT-style multi-hop on benchmarks where the next query is unknown; RAGAS as a reference-free score with the limits above.

**Experimental, do not build here:** an open agent over this store; a community graph of the criteria register; a vision model standing in for `str.replace`; a live LLM judge as the grade for `chk-m03-l03-rag`; any nDCG target for this pack.
