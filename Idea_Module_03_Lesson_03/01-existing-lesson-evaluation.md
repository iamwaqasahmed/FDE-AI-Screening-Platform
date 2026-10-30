# Existing lesson evaluation

Module 3, Lesson 3 is the release `rel-m03-l03`. The student folder calls it Cite. The facilitator syllabus calls it Retrieval and asks for embeddings, vector databases, enterprise knowledge, retrieval quality, grounding, and response generation. The curriculum map’s purpose line is narrower and more accurate: answers cite an in-force document the asker is allowed to see; an in-flight referral keeps the criteria version it started on; the unauthorized circular is not a citation. The Python and the three checks follow the purpose line. They do not follow the syllabus line. That gap is the evaluation.

## What the reader actually does

Chapters 00 through 04 are reading and one demo. `python -m alwaha.demo.duplicate` prints two titles and `one is superseded`. Chapter 03 walks the notice, the snapshot, the feed, the dev slice, the catalog, the photo JSON, and the markdown documents. The notice limits v4 to endo, ophth, and card, keeps a started referral on its version, and says a draft is searchable and not citable, and an unauthorized document is not citable. The snapshot still has v4 as draft. The feed is the update. That opening is the lesson’s real case.

Chapters 05 through 07 and 09 paste the sprint, eight Python modules, and three pages. Chapter 10 runs the checks. Chapter 08 is after a green finish. The checks do not read `vision.py`, `conflict.py`, or `catalog.py`. The suite still imports them, so the shells stay.

The journey log records fifteen pastes and zero failures after the paste fix. Student work and solution both print the three pass lines. The day is completable by pasting the fenced blocks. Completion does not show that the reader can separate a status filter from rank fusion, or a metadata match from a grounded sentence.

## The pipeline the solution implements

`chunk.clauses` splits `body` on a blank line and copies a fixed field list onto every piece, including `clause_id`. The shell dropped the clause id and kept the whole body as one row. The replacement restores the id. The id is the document’s id, copied onto each piece. The corpus helpers in `m03_l03_corpus.py` and `m03_l03_docs.py` mint one clause id per document (`endo-v3-c1`, `hrs-ramadan-c1`, `prep-endo-staff-c1`). A blank-line split therefore does not create a new span identity. The citation “span” is a document-level clause id. That is enough for this pack, because the planted bodies are single clauses. It will mis-cite the day a body has two clauses and one id.

`embed` lower-cases text, keeps letter and digit tokens with internal hyphens, and maps each token to its share of the count. `nearness` is cosine. An empty side scores 0. `codes` returns hyphenated tokens. The words page says `local-embed` is Lesson 2’s register row, that this file does not train, and that no vector database is started. The object is a normalized bag of tokens. It prefers a chunk that repeats the question. The `+ 1` code boost assumes that cosine lives in a small range, which is true of this map and of a neural cosine alike, so the boost would still dominate a later model swap.

`index.build` embeds every clause of every document on each call. `cite.answer` calls `build` inside the non-specialty path. There is no persistent index.

`search.rank` has two modes. Vector mode scores every chunk, whatever its status. Hybrid mode skips a chunk unless `status == "in_force"` and adds 1 when any question code is a key in the chunk vector. Ties break by document id. The unit test plants the question “evening clinic hours in the fasting month code hrs-ramadan” against two chunks. The unauthorized chunk repeats the hours wording and the code. The in-force chunk says the code closes evening clinics. Vector mode returns `circ-ramadan-unauth` first. Hybrid mode returns `circ-ramadan` first. Both the status skip and the +1 can produce that result. The test does not separate them.

`filter.allow` is a three-row rule. A patient sees `public`. Staff see `public` and `staff`. Records see `public`, `staff`, and `restricted`. Any other asker sees nothing. A missing audience matches nothing.

`bind.criteria` is the best function in the lesson. For a specialty in `{card, endo, ophth}`, an in-force version 4 whose window covers the start day wins. Otherwise a version 3 that is `in_force` or `superseded` and covers the day wins. The window is half-open: the day must be on or after `effective` and before `sunset`. Neurology is outside the set, so a draft neuro v4 does not bind, and neuro v3 does. An endocrinology referral started on 2027-01-20 stays on v3 even when the case date is 2027-01-26 and v4 is in force. The unit test locks those three outcomes. The specialty set is a Python constant. The notice file says the same three names. The two can drift.

`cite.answer` forks. A question with a specialty calls `criteria`, returns `no-document` when nothing binds, returns `audience` when the bound document fails `allow`, and otherwise cites that document. A question without a specialty hybrid-ranks the full index, then keeps chunks that are in force, allowed for the asker, and whose vector contains a question code. The first survivor is the citation. If none survive, the refusal is `no-document`. `_cite` returns audience, doc id, clause id as span, status, and version. It does not return the clause text, the content hash, the effective date, or the sunset.

`sync.apply` copies the snapshot, appends every event’s document id to `touched`, inserts on `add`, and `update`s fields on any other op. The rag check compares the touched set with gold. It does not check that only those ids were re-embedded, because nothing re-embeds incrementally. Chapter 07’s reading says the touched list means you do not rebuild the world for one change. `index.build`, called from `cite`, rebuilds every vector from the post-feed documents. The check and the sentence grade different things.

## What the three checks grade

`chk-m03-l03-rag` loads bind, cite, embed, filter, index, search, and sync. It applies the feed. The touched set must equal gold. Each held question is passed to `cite.answer`. If the gold expects a refusal, the refusal string must match. Otherwise the check collects specific leaks: document id `circ-ramadan-unauth`, an in-flight question answered with version 4, status `draft`, version 4 on a specialty outside the gold v4 list, or a patient citation whose audience is `staff` or `restricted`. A span miss, meaning disagreement on audience, doc id, span, status, or version, is reported only when none of those leaks fired. Notes are graded even when the index crashes. A canary returns only the watermark. The failure text does not print a document id, a span, or a clause. That is good grading hygiene for a class that shares a room.

`slice-hybrid` ranks one gold question as vector and as hybrid. If the vector-only document is in the index and vector mode still puts the hybrid document first, the slice says vector search alone cleared it. If hybrid mode puts the vector-only document first, the slice says the unauthorized circular was cited. Any other hybrid top is a span miss. The design note in `11-eval-and-hardness.md` describes the slice as “vector search alone” failing and “hybrid search plus version filters” passing. The code path under test is status filtering inside `rank`. Version windows live in `bind.py`, which this slice does not call.

`slice-acl` asks `cite.answer` the patient question and asks `filter.allow` whether the blocked staff document is allowed for a patient. A staff leak is any of: the filter allows it, the citation audience is staff or restricted, or the citation is the blocked id. A wrong document is a span miss only when the leak was not already recorded. The design note calls the failing method “retrieval with no audience filter” and the passing method “permission-aware retrieval.” The implementation filters after ranking, inside `cite._visible`, and again by the specialty fork’s `allow` check. The staff document is still embedded and still scored. Permission-aware retrieval, in the sense OpenSearch documents as document-level security and as a hybrid pre-filter, removes the document from the candidate set before scores exist. Post-checking the winner catches the planted leaflet. It does not catch a log, a trace, or a later prompt that still contains the staff chunk because the ranker returned it and a caller forgot to call `allow`.

The written-note checker is lexical. The sprint must contain the four words in order and “not all” plus the three specialty names. The refusal must contain “no document” and “cannot see.” The audience table must give the patient public only, staff public and staff, and records the restricted row. Knowledge needs two numbered answers. The first must say in force or `in_force` and must contain date, window, or effective. The second must contain staff and patient. The solution’s first answer also says the site matches or is cluster-wide. `bind.criteria` does not read site. Chapter 07 says so, and points site at the booking conflict in chapter 08. The knowledge checker does not require the site sentence, and it does not reject it. A reader can pass with a sentence the bind function does not implement.

## The advanced chapter

The design trace lists phone photos, conflicts, multi-hop questions, the catalog, and the unauthorized circular. The advanced chapter implements three tiny functions. Audiences, touched ids, and the unauthorized trap are graded elsewhere.

`vision.clause` returns `transcription` with the `export` substring removed and the ends stripped. The test page has export “Bring your card.” and transcription “Bring your card. Bring the fasting slip.” The result is “Bring the fasting slip.” The shell returned the export and ignored the transcription. That teaches a real ingestion fact from `05-corpus.md`: a text-only read of the export misses the clause that exists only on the page. It does not teach OCR, a vision model, or `slice-vision` as the hardness table defines it (“Text-only extraction” fails; “OCR or a vision pass on phone photos” passes). The photo clause is not inserted into the index. A citation question cannot retrieve it. The function is disconnected from `cite.answer`.

`conflict.booking` finds the document whose site matches the argument and the document whose id is `pol-booking-cluster`. It returns the site id as `also` and the cluster id as `winner`. The shell let the site window win and left `also` empty. The rule matches the planted conflict: the facility override at `h-safra` shortens a window, and the cluster policy wins, with both ids named. The function does not read the two bodies, does not detect a contradiction, and does not attach the winner’s clause to a citation. The cluster id is a constant.

`catalog.lookup` returns clinic and prep from the first matching catalog row and does not set `doc_id`. The shell ignored the rows and returned `leaflet-prep` with an empty prep. The design note is right that a structured clinic table is a place where lookup beats retrieval. The function is the right decision. It is not wired to `cite.answer`, so a patient question about preparation still goes through the leaflet index, which is the path `test_cite` grades.

Multi-hop and unanswerable questions appear in the trace and barely appear in the code. Unanswerable is the `no-document` refusal when no code matches, which `test_cite` covers with `aero-x9`. There is no second hop. There is no case where the criteria clause names a prep code and the leaflet must be fetched under the patient’s audience. There is no generator that could answer from memory when the store refuses.

## Traps that are doing real work

Two traps are well planted and should survive any redesign.

The unauthorized circular is public in audience and unauthorized in status, and its body is a near copy of the hours question. A similarity ranker that ignores status cites it. A patient-audience filter that ignores status also cites it, because the audience is public. Both gates are required. The feed is where the row appears, so a reader who indexes the snapshot markdown and skips `sync.apply` never sees the trap, and the touched-set check fails for a different reason. That coupling is good.

The staff leaflet shares a preparation code with the public leaflet and repeats the preparation wording, so a pure similarity rank puts it first for a patient. `test_cite` and `slice-acl` both lock the public id. The near-duplicate leaflets, one of which the feed supersedes, are the same idea for time: similarity does not know sunset.

The in-flight rule is the third trap, and it is the one hybrid mode cannot pass. Hybrid `rank` drops every status other than `in_force`. A superseded v3 is exactly the document an early endocrinology referral must cite. `cite.answer` therefore does not use hybrid rank on specialty questions. It uses `bind`. The architecture already admits that a citable-status filter inside the ranker is the wrong tool for version binding. The lesson never says that sentence. The sprint sequence “index, then filter, then cite” describes the non-specialty path. The specialty path is bind, then allow, then cite, and the historical row must remain in the store after the filter used for new questions has dropped it.

## Syllabus claims the lab does not meet

`answer` returns a citation record or a refusal code. There is no drafted sentence and no check that a sentence is supported by a span. RAGAS faithfulness, in Es et al., is a relation between generated claims and retrieved context. This lab grades metadata against gold. That is the right first check for a policy store. Lesson 4 is where a fluent wrong citation is supposed to be named. This lesson emits ids, not the text a judge would score.

Quality is a top-1 assertion on planted pairs. A ranked-list metric on this pack would be theatre. The missing fixture is a pair in which both documents are in force and public, so fusion is graded apart from the status filter.

Chapter 04 already says the maps stay in the files the reader opens. The syllabus header still says vector databases. The facilitator slide lists chunking, embeddings, filters, citations, and audiences, and does not say that the vector is a token share or that hybrid mode is a status predicate.

## What is already worth keeping

The corpus design in `05-corpus.md` is the asset. Criteria v3 in force at open, v4 draft and staff, v4 promoted for three specialties, unauthorized circular mis-filed as public, facility override, near-duplicate leaflets, catalog as the SQL slice, photo transcription longer than the export. The release note and the dev slice make those facts readable before any paste.

The refusal split is worth keeping. `no-document` and `audience` are different outcomes. A patient who cannot see a staff criteria row is not in the same state as a question no document covers. The product page has to say both. The checker’s substring test is crude and still forces both sentences to exist.

The self-paced role table is worth keeping. One person sequences the work, writes the index path, writes the filter and the bind, writes the refusal, and answers who may see a staff document. Nothing in the lesson requires a second account or a facilitated workshop. Lesson 4 owns the workshop. This lesson should stay a single-reader lab.

The decision to leave chapter 08 unread by the foundation checks is half right. A day that cannot finish should still pass a coherent foundation. The half that is wrong is the content of chapter 08: three functions that look like the trace’s advanced topics and do not participate in retrieval. A reader who finishes only chapter 10 has done the real policy work and has been told the photo, the conflict, and the catalog are optional. A reader who finishes chapter 08 has still not put the photo clause or the conflict into a citation.

## Failure modes the current checks miss

A citation can name the right document id and the wrong body, if `sync` mutates that id’s fields in place and the citation stores no hash. The documents already carry `content_hash`. The compared fields omit it.

A staff chunk can be the top hybrid hit for a patient and still pass `slice-acl` if `allow` is applied only at the end and happens to flip the result to the public leaflet. The slice does not inspect the candidate list. A later caller that prints `rank(...)[0]` leaks.

An in-flight citation can be right on version and wrong on the clause if v3’s body is edited by a `replace` event that does not change `version`. The bind function keys off version and window, not hash.

Hybrid mode can pass `slice-hybrid` with the status filter alone, with the +1 alone, or with both. The lesson cannot tell a reader which mechanism they implemented, because the paste provides both and the slice accepts the combination.

The knowledge answer can claim a site rule the bind function does not apply. The booking conflict, which is the site rule, is outside the checks.

A draft remains searchable in the narrative and is excluded from hybrid rank by the same predicate that excludes unauthorized and superseded rows. The narrative says drafts are searchable and not citable. The code has no search path that returns a draft. The distinction is taught in the notice and dropped in `rank`.

## Judgment

**Proven** parts of the current lesson, worth carrying forward as behavior: the unauthorized-public misfile, the staff leaflet, the in-flight window, the three-specialty limit, the feed as the source of status, separate refusals, and the catalog’s refusal to wear a document id.

**Emerging** only as vocabulary the chapters mention and do not run: multi-hop, unanswerable questions beyond a code miss, and “vector database” as a later home for the same maps.

**Experimental** relative to the claims on the syllabus: treating `local-embed` as an embedding model, treating the hybrid branch as hybrid search, treating `vision.clause` as a vision pass, and treating a metadata match as grounded generation.

The lesson is a policy-citation lab with a retrieval costume. The costume is what a redesign should remove. The policy lab is what it should finish.
