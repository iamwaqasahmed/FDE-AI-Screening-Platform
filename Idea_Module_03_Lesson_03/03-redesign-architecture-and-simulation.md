# Redesign, architecture, and simulation

The redesigned lesson stays on `rel-m03-l03`. The snapshot, the change feed, the v4 notice, the unauthorized circular, the staff leaflet, the in-flight endocrinology referral, neurology left on v3, the `h-safra` booking pair, the service catalog, and the photo whose transcription is longer than its export are the simulation. They are already synthetic, already fictional, and already the right size for one person to read. A public IR benchmark would teach a different task and would bring licensing and scoring habits this pack does not need.

## The pipeline to build

One Python package, still dicts and JSONL, still no network. The stages are ordered so that a later stage cannot see a row an earlier stage dropped.

1. **Sync.** `apply(snapshot, feed)` copies the snapshot and plays `document.changed`. Adds insert. Other ops update fields and recompute `content_hash` when `body` changes. Superseded rows stay in the store. The return value is the document list plus the touched ids. **Proven** pattern, same shape as today’s `sync.py`.

2. **Policy pre-filter.** `candidates(docs, question)` returns the rows a ranker may score. Unauthorized is always out. A draft is out of the citable set. For a question with no specialty, the citable status is `in_force`, the audience must pass `allow`, and the case date must sit in the window. For a specialty question, `bind` chooses the one criteria row using the notice’s specialty set and the start day, and `allow` still applies. A superseded v3 can be that one row. It is not in the default citable set for a new question. **Proven.**

3. **Two ranks, then fusion, only on the candidate list.** Lexical rank: a small BM25 over the same tokens `embed` already produces, so a hyphenated code is one term. Vector rank: the existing token-share cosine, kept under the name `local-embed` and described as a sparse stand-in. Fusion: reciprocal rank fusion with k = 60. **Proven** fusion, toy retrievers. The database versions of the same idea are named from the pgvector README and the OpenSearch hybrid docs. They are not installed.

4. **Citation.** The winner’s clause text is the answer text. The record also carries doc id, clause id, status, version, audience, and `content_hash`. A refusal is `{refusal: no-document}` or `{refusal: audience}` and has no text. **Proven.**

5. **Conflict overlay.** When the question is the booking window and two in-force documents match, the record adds `winner` and `also`. The text is the winner’s clause only. The cluster document wins. **Proven** policy, promoted out of the unread chapter.

6. **Catalog short-circuit.** A preparation question whose clinic key hits `service-catalog.json` returns clinic and prep and does not take a doc id. **Proven.**

7. **Ingestion of the photo gap.** Before chunking, if `transcription` contains text that `export` does not, that remainder becomes its own clause with its own id, audience, and status, and it enters the store the ranker sees. **Proven** ingestion. The module should be named for the gap, not for vision.

A scripted second hop sits beside step 4 for one dev question: the bound criteria clause contains a code, and the next lookup is the public in-force leaflet with that code. The hop uses `candidates` again. It does not call a model. **Proven** as ordinary code. The IRCoT loop that would invent the second query is named in the reading and is **Experimental** here.

## Four architectures, compared

| Architecture | What it optimizes | What this pack needs from it | Maturity for this lesson | Decision |
| --- | --- | --- | --- | --- |
| Lexical rank plus sparse vector, fused with RRF, after a policy pre-filter | Exact codes and repeated wording, without putting those scores on one scale; legality decided before scores | The hours circular versus its unauthorized copy; the public leaflet versus the staff leaflet; v3 versus v4 by window | **Proven** | Implement |
| Contextual retrieval (Anthropic, 2024) | Chunks that are locally ambiguous because the document title and the date were stripped | A short clause that does not repeat its document’s title | **Emerging** | Name. The authors’ own size note says a store this small can sit in a prompt. A prompt still cannot be the permission boundary |
| GraphRAG (Edge et al.) | Global theme questions over a large private corpus, via an entity graph and community summaries | A feed question about which specialties moved, which the notice and the touched ids already answer | **Emerging** on the paper’s task, **Experimental** as this index | Name |
| Agentic multi-hop (IRCoT and the same shape of loop) | Questions whose second query is unknown until the first passage is read | One known second hop: criteria code, then public leaflet | **Emerging** on HotpotQA-style sets, **Experimental** as an open loop over this store | Implement the scripted hop. Name the open loop |

A fifth option is the one the current chapter calls hybrid: cosine, plus one if a code matches, and drop any status other than `in_force`. It is a policy predicate mixed with a score boost. It passes today’s `slice-hybrid` and it cannot return the superseded v3 an in-flight referral requires, which is why `cite.answer` bypasses it for specialty questions. The redesign deletes that mixture. The status rule moves to the pre-filter. The code preference moves to the lexical list. RRF replaces the `+ 1`.

## Why the pre-filter is not optional once fusion exists

RRF will happily fuse a list that contains `circ-ramadan-unauth`. If that circular ranks first on cosine, because it repeats the question, and first or second on BM25, because it contains `hrs-ramadan`, fusion promotes it. The current hybrid mode hides this by deleting non-`in_force` rows inside `rank`. The redesign makes the deletion visible and earlier, and it makes the deletion depend on the question. New hours questions exclude unauthorized, draft, and superseded. In-flight specialty questions include the superseded row whose window covers `started`, and still exclude unauthorized. Audience is applied in the same function, so a patient candidate list has no staff id and no restricted id for a ranker to leak into a log.

OpenSearch’s split between a hybrid pre-filter and document-level security, and issue 1303’s report that those features can fail together, is the production story the chapter should tell in a paragraph. The lab then does the simple thing the issue says not to take for granted: one candidate function, tested by asserting the forbidden id is absent from the list, not only absent from the final citation.

## Version binding

`bind` already implements the window. The redesign changes three details.

The specialty set is read from `notices/criteria-v4.md` (the three names, and the sentence that it is not every specialty). A hardcoded set that drifts from the notice is the bug the sprint page is trying to prevent with the words “not all.” **Proven.**

The citation stores `content_hash`. Documents already have the field. A later `replace` that edits a body under the same id and version changes the hash, and an in-flight record that stored the old hash still displays the old clause. The store keeps the previous body under the hash. The simplest simulation is a feed event that rewrites `crit-endo-v3`’s body without bumping `version`, and a gold citation for the early referral that still carries the original hash. Today’s check would pass that rewrite, because version stays 3. **Proven** as a pin. The full content-addressed store can be one dict keyed by hash. It does not need a new service.

Neurology stays off the notice. A neuro question on the case date binds v3. A v4 row for neuro, even if a faulty feed marks it `in_force`, does not bind, because the notice is the authority. That is the scope leak `V4_SCOPE` already names. Keep it.

## Citation faithfulness without a judge

The answer text is the clause string. The test is equality. A paraphrase the reader typed fails. A sentence that mixes the cluster window with the `h-safra` window fails, because the text must equal the winner’s clause while `also` carries the other id. This is the faithfulness check the lesson can grade. It is stricter than RAGAS on wording and weaker on summary. The product refusal pages stay human sentences, and they are not claims about clinic hours, so they are not put through the equality check.

Lesson 4 receives a record that includes the text, the hash, and the version. An exercise there can show a judge model, or a canned judge fixture, marking a fluent paraphrase of the unauthorized circular as supported. The fixture is **Experimental** as a grader and **Proven** as a demonstration of the metric’s blind spot, which both the RAGAS definition and the Turing Institute note already describe. This lesson does not call the judge.

Lost in the middle is the reason the prompt, when a later lesson adds a model, receives that one clause and the citation header, not the top 20. Anthropic’s post found 20 chunks best on their recall-at-20 setup and also warned that extra chunks distract. Liu et al. measured the distraction. The lesson quotes both and implements the single clause.

## Simulation: what stays, what is added, what is deleted

Stay, unchanged in spirit:

- The snapshot is before the feed. Markdown status is the snapshot. Readers who cite a file they opened without applying the feed are wrong, and the touched-set check remains.
- `circ-ramadan-unauth` is unauthorized and public, and its body repeats the hours wording and the code.
- `leaflet-staff` shares the preparation code with `leaflet-prep` and is more repetitive, so an unfiltered cosine prefers it for a patient.
- The old leaflet is in force on the snapshot and superseded on the feed, with a sunset. The demo line `one is superseded` stays.
- In-flight endo started 2027-01-20. Case date 2027-01-26. v4 effective that morning for the three specialties.
- Neuro v4 remains draft, and remains off the notice even if someone edits the feed in a negative test.
- `pol-safety` is restricted. Records may see it. Staff and patients may not.
- The catalog row for endo prep is the structured answer.
- The photo JSON keeps export and transcription.

Add three fixtures, still a few lines of JSONL, generated the way `m03_l03_corpus.py` already builds rows:

1. A public, in-force parking notice that repeats “evening clinic hours” and does not contain `hrs-ramadan`, and the short public in-force hours clause that does contain the code. After the policy filter has removed the unauthorized circular, cosine prefers the parking notice and the lexical rank prefers the hours clause. RRF’s top-1 is the hours clause. Lexical-only fails a paraphrase that omits the code and overlaps the parking notice less than a third in-force clause written for that paraphrase. Two questions, two failing single lists, one fusion that passes both. Grade top-1. Do not compute nDCG.
2. A feed event that changes the body of `crit-endo-v3` and therefore the hash, without changing version. The in-flight citation gold keeps the original hash and the original clause text.
3. One scripted two-hop question whose criteria clause contains `prep-endo` and whose patient-visible target is `leaflet-prep`.

Delete from the graded path:

- The hybrid mode flag that means “drop non-`in_force` and add 1.”
- The vision brand on the string replace. The behavior moves into ingestion and is graded by a citation of the fasting-slip clause, with audience and status, or it is cut. Leaving it as an ungraded function named vision teaches a false method. **Experimental** labeling of a fake vision model is worse than deleting the name.
- Any requirement to stand up OpenSearch, Postgres, or a graph library. The README links are the lab’s “where this lives in production” reading, assigned as a page, not as an install.

## Edge cases the simulation should fail closed

A document with audience `public` and status `unauthorized` is the hours trap. Closed means absent from every candidate list.

A document with audience `staff` and status `in_force` is the leaflet trap. Closed means absent from a patient candidate list and present in a staff list.

A superseded v3 inside the start-day window is the in-flight trap. Closed means absent from a new-question candidate list and present as the bind result for that referral.

A v4 row for a specialty the notice does not name is the scope trap. Closed means bind returns v3 or refuses.

A draft v4 that the feed has not promoted is searchable only through a debug function that is not `cite`. The notice’s sentence survives. Today’s `rank` has no such function, so the sentence is unread by the code.

Two in-force booking documents are the conflict trap. Closed means one text, two ids, cluster wins. A blend sentence fails the equality check.

A catalog hit is the non-retrieval trap. Closed means no doc id. Citing `leaflet-prep` for a column that lives in the catalog fails.

An empty asker, an unknown asker, or a missing audience fails closed to no rows.

A feed `replace` aimed at an unknown id fails the sync test. Today’s `apply` would raise on a missing key or would write through. The gold touched set hides that. The unit test should include one unknown id and expect a recorded skip, not a new document invented from the fields.

A question with no surviving candidate returns `no-document`, including the `aero-x9` case already in `test_cite`.

The photo remainder inherits the page’s audience. If the page is staff, a patient does not receive the fasting-slip sentence. Ingestion does not bypass `allow`.

## Production failures this simulation is allowed to omit

Shard routing, hybrid pagination depth, HNSW recall, embedding drift, and multilingual BM25 are real and absent. Naming them in a paragraph is enough. Measuring them on this pack would invent precision. The OpenSearch docs already separate pre-filter from post-filter and set a pagination depth on the hybrid query. A reader who later installs OpenSearch has those pages. This lesson’s failure is a wrong document shown to a patient, which a shard does not cause and a missing pre-filter does.

Graph community summaries, contextualizer prompt drift, and agent loops that call tools are omitted as running systems. They appear as a one-page comparison so a reader who has seen a product diagram can place it. The comparison says what question each diagram answers. The lab answers the citation question.

## Datasets

The participant pack is the dataset. Facilitator gold stays on the grading service, as `11-eval-and-hardness.md` already requires. The new fixtures are generated in `m03_l03_corpus.py` style, with hashes, so a hand-edited body cannot keep a stale hash. No Wikipedia dump, no HotpotQA download, no BEIR subset. Those sets are how the cited papers measured their own claims. Importing them would turn a policy lab into a retrieval contest and would pressure the course to publish an nDCG the redesign refuses to invent.

Synthetic text from Lesson 1 stays in Lesson 1. This lesson does not generate more leaflets with a model. The planted pairs are written by the course author so the failure is known. That is the same method the current unauthorized circular uses, and it is the right method.

## What the advanced reading contains

After the checks pass, the reader opens four primary pages and writes five sentences in `knowledge.md`, extending the two answers that already exist:

- What entered the candidate list, and what the unauthorized circular’s audience was.
- Which list, lexical or cosine, the parking fixture fooled, and that the fusion constant was 60 because that is the published default, not because this pack was tuned.
- Why the in-flight hash differs from the current body of the same version.
- Which named method, contextual retrieval, GraphRAG, or an agent loop, would still cite the staff leaflet if it ran before the pre-filter.
- Why a faithfulness score of the RAGAS kind would accept a perfect quotation of the superseded hours if that circular were the retrieved context.

Those sentences are the advanced chapter. They replace a vision function the checks ignore. A reader who is out of time still has a green foundation, and the shells they were told not to delete are either gone from the suite or are the ingestion function the foundation already ran.
