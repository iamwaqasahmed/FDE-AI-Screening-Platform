# Core path versus the retrieval extension

`Idea_Module_03_Lesson_03` says this lesson should implement a pre-filter, a version-and-hash pin, an extractive citation, and a small reciprocal-rank fusion. The instructional dossier says code on the core path is at most one completion in one file, and that the index is an extension. Both are describing a real defect. They are not describing the same gate.

The reference ranker drops every chunk that is not `in_force`, then adds 1 to the token cosine when a code matches. `slice-hybrid` passes when vector mode ranks the unauthorized circular first and hybrid mode ranks the in-force hours circular. That is a status filter. The audience check in the reference runs after rank, so a staff leaflet can still be scored for a patient.

**Core specification, which opens the next lesson.** One function. Candidates are filtered by audience and by status before any score. An in-flight referral keeps the criteria version it started on. The cited text equals the clause, and the stored `content_hash` is part of the citation. A status filter that still scores a staff leaflet, or a citation that survives a body edit under the same version id, fails. No vector database, no model, and no new lesson.

**Extension, which is not the door.** Reciprocal rank fusion of a lexical list and the token cosine, on a public in-force pair where each list alone fails, graded at top 1. Cormack, Clarke, and Büttcher (SIGIR 2009) are the citation. This is the lab that makes the word “hybrid” mean fusion. Skipping it leaves the next lesson open and forbids a capstone sentence that claims a fused index was built.

**Named, not graded.** Contextual retrieval, GraphRAG, and agentic multi-hop. Anthropic’s 19 September 2024 failure reductions are that post’s numbers. The same post says a store under about 200,000 tokens can sit in the prompt. This pack is smaller than that, and a prompt is not an access check. A contextual prefix may be a later extension only if the audience pre-filter still runs first. It does not replace the core specification.
