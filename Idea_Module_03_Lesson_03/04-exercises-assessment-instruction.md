# Exercises, assessment, and self-paced instruction

One person holds every part. The background chapter already says so: lead, index, application, product, and architect. The redesign keeps that table. It does not add a pair exercise, a facilitated red team, or a requirement that someone else own the audience rules. Lesson 4 owns the workshop. This lesson ends when the same reader can show a citation, a refusal, and a candidate list.

## Prerequisites

From Module 1, the reader knows `p-info` is the retrieval family, and that a referral keeps the criteria document that was in force on the day it started. From Module 3 Lesson 2, hours questions stayed on retrieval, `local-embed` is a registered name, and the file that wears that name is not a training loop. From Module 2, a change feed is a sequence of events the store applies in order. The reader can open JSONL, run `python -m unittest`, and read a failing assertion. The reader does not need linear algebra beyond the words page’s account of cosine, does not need a vector database, and does not need an API key. A neural embedding model is out of scope on purpose. Installing one would spend the day on weights and would hide the policy bugs under a download.

The words page stays. In force, draft, superseded, unauthorized, window, audience, asker, span, and refusal are the vocabulary. Add four words and no more: candidate list, lexical rank, reciprocal rank fusion, content hash. Define fusion as the 2009 sum of 1 / (k + rank) with k = 60, and point at the paper. Define the content hash as the field the snapshot already stores.

## What the reader writes, and what is provided

Provided, as now, and pasted or copied once: `chunk.py` and `embed.py`. Blank-line clauses, hyphenated codes, token shares, cosine. The reading beside them says this vector is a sparse stand-in registered as `local-embed`. A later system may store the same map, or a neural map, in Postgres or OpenSearch. This folder does not start either. The pgvector hybrid section and the OpenSearch hybrid page are a reading, after the tests pass, not a lab.

The reader writes three functions against tests that fail on the shell:

- `candidates(docs, question)` in `filter.py`. Audience, citable status for this question, and the window. Unauthorized never. Patient lists contain no staff or restricted id.
- `criteria(docs, notice, specialty, started)` in `bind.py`. The notice supplies the three specialties. The window logic stays the logic the solution already uses. The result includes the hash.
- `fuse(lexical, vector, k=60)` in `search.py`. Two ranked lists of the same candidate ids. The function returns ids and fused scores. It does not look at status. Status was decided before the lists were built.

`cite.answer` is provided as a thin wrapper once those three exist, so the reader sees the order and does not spend the day on dictionary keys. The wrapper’s contract is the assessment. A reader who wants to rewrite the wrapper may. The tests do not care which file contains the branch, as long as the public functions behave.

`sync.apply` stays a guided replacement, as today, with one new assertion: an unknown id is a skip recorded on the result, and a body change refreshes the hash. `conflict.booking` and `catalog.lookup` move into the foundation suite. They are each a single function with the tests that already exist, plus the equality check that the booking answer text is the cluster clause. The photo gap becomes `ingest.photo_clause`, called from the index builder. The old `vision.py` name is deleted so the suite does not import a fiction.

The scripted second hop is one test in `test_cite.py`: staff-visible criteria text contains `prep-endo`, the asker is a patient, the cited id is `leaflet-prep`, and `leaflet-staff` is absent from the candidate list of the second hop. The reader fills a function `next_lookup(citation, docs, asker)` that searches codes in the cited text and calls `candidates` again. An empty code list returns the citation unchanged. That is the whole agent. There is no loop bound to write, because the hop count is one.

## Chapter order for a self-paced day

The current order is right: case, words, sprint, index primitives, citation policy, pages, checks, then a short reading. The redesign changes the middle.

Chapters 00–04 stay. The demo stays. The twenty-three-file walk is long and is also the only place the reader sees that the markdown is the snapshot. Keep it. Cut nothing from the notice, the feed, or the unauthorized row.

Chapter 05, the sprint, stops being a paragraph the checker scans for word order. The sprint file still exists, because the lead role should say the order in a sentence a person can read: sync the feed, build candidates, rank only those candidates, cite or refuse, and limit v4 to the notice. The check looks for the behavior in tests. It may still require the three specialty names and “not all” in the sprint, since that sentence is the scope decision and it is easy to get wrong. It should stop requiring the tokens “index” before “filter” as a proxy for learning.

Chapter 06 provides chunk and embed and asks the reader to implement `fuse` and to show, on the parking fixture, that cosine’s first id and the lexical rank’s first id differ, and that fusion’s first id is the hours clause. The shell’s `fuse` returns the cosine list unchanged, so the test fails until ranks are combined. This is the slice that replaces today’s `slice-hybrid`.

Chapter 07 is the pre-filter, the bind, the hash pin, and the citation wrapper. The shell’s `candidates` returns every document. `slice-acl` fails because the patient list contains the staff leaflet. A second test fails because the unauthorized id is in the list even when it is not the final citation. A third test fails because the in-flight bind returns v4. The reader is not handed the finished `allow` and `criteria` as a paste of the whole file. They are handed the docstrings and the tests the solution already satisfies. A worked solution remains in `Solution_Copy` for after the finish chapter, which is the course’s existing rule.

Chapter 08, after a green finish, is the four-source reading and the five knowledge sentences in the redesign file. It is not required for the foundation checks. If the day ends, the reader leaves with the foundation and opens Lesson 4. That matches the current finish chapter’s instruction, with the content of the advanced path replaced.

Chapter 09’s refusal and audience table stay. The product sentences are still “no document binds” and “the asker cannot see it.” The audience table is still the three rows. Those pages are how a non-code role discharges the same person’s job. Keep the pipe characters. The current checker’s bug, a patient cell that mentions staff as a forbidden word inside a longer sentence, can be ignored here. The table is the contract.

## Assessment

Foundation checks, still pass or fail, still silent about the gold ids in the failure text:

| Check | Pass means | Simpler method that fails |
| --- | --- | --- |
| `chk-m03-l03-rag` | Citation text equals the clause; id, span, status, version, audience, and hash match; refusals match; touched ids match; v4 stays inside the notice | A paraphrase, a draft, a mutated body under the same version, an in-flight restart onto v4 |
| `slice-acl` | The patient candidate list contains no staff or restricted id, and the cited leaflet is the public one | A ranker that sees every audience and then hopes the winner is public |
| `slice-hybrid` | On the filtered public in-force set, fusion’s top-1 beats lexical-only on one planted question and cosine-only on the other | Cosine alone, lexical alone, or a `+ 1` boost that was tuned on the old unauthorized pair |
| `slice-bind` | Start day 2027-01-20 stays on the original endo v3 hash; the case-date start uses v4; neuro stays on v3 | “Latest in force” for every specialty |

`slice-conflict` can be foundation or the first advanced credit. Pass means winner is the cluster id, also is the site id, and the answer text equals the cluster clause. The current unit test already has the ids. Add the text equality so a blend fails.

The suite remains `unittest`. Fourteen tests become about eighteen. Still seconds, still no model. The journey log’s standard, a scratch run that pastes and passes, should be repeated on the new chapters before anyone calls the redesign teachable. The current lesson met that bar. The new one is not done until it does too.

Do not grade with RAGAS. Do not report nDCG, recall at 20, or a faithfulness fraction. Those metrics belong to the papers in the reading. Publishing a number for this pack would be an invented score. Lesson 4 may show a canned judge output next to the hash mismatch and ask the reader which one they believe. The belief the course wants is the hash.

## Solution approach

The reference solution is the current solution plus a small delta, not a new framework.

`candidates` is `allow` plus a status set chosen by whether the question is an in-flight specialty bind or a fresh lookup, plus the window test already in `_covers`. Unauthorized is a hard exclusion before the status set.

`fuse` builds a dict of id to 0, adds `1 / (60 + rank)` for each list, and sorts. Ranks start at 1, as OpenSearch’s formula states and as the usual reading of Cormack’s sum states. Ids missing from a list add nothing. Tests use three chunks so the arithmetic is inspectable. The reader can print the three fused scores. The check asserts the top id only.

The hash pin stores the clause text beside the hash on the citation. When the feed mutates the live row, `cite` for an in-flight question reads the stored snapshot of that hash, which `apply` saved before the mutation. A dozen lines of dict bookkeeping. No merkle tree.

`next_lookup` tokenizes the cited text with the existing `codes` helper, finds `prep-endo`, and runs `candidates` with the patient asker and no specialty. The staff leaflet shares the code and fails `allow`, so it never enters the second list. That is the demonstration that a second hop without a pre-filter is how the staff leaflet returns.

The solution copy’s interview notes stay trainer-only. The morning still does not require an interview. `phc-lead` and `coord-lead` already said, in the design schedule, that v4 is three specialties. The notice is that statement in the participant pack. Another interview would repeat it.

## Instructional risks

The paste chapters exist because a self-paced reader on a clock can otherwise stall on syntax. The journey log shows the paste path works. Replacing every paste with a blank function will strand a reader who can follow a policy and cannot debug a sort. The compromise is narrow blanks: `fuse` is ten lines, `candidates` is a loop and three predicates, `criteria` is the loop the current solution already comments. Docstrings stay as pedantic as the current solution’s, because that voice is the course’s. The failure table in chapter 10 stays, and it gains rows for “the staff id is in the candidate list,” “the hash moved,” and “fusion returned the parking notice,” still without printing the id. The current messages already avoid printing ids. Keep that discipline.

A reader who implements the pre-filter and skips fusion should fail `slice-hybrid` and pass `slice-acl` and `slice-bind`. The finish chapter should say that pattern in the failure table, so the reader sees the thesis as a test result: the filter was necessary, and the hours paraphrase is still wrong. A reader who implements fusion on the unfiltered store should fail `slice-acl` or the unauthorized candidate test even if the top-1 happens to be legal. That split is the assessment’s whole point.

Out-of-time rule: foundation checks green, advanced reading skipped, next folder opened. Same rule as today. The photo ingestion is foundation, so it cannot be skipped by skipping chapter 08. If that makes the day too heavy, drop the scripted hop to the advanced reading and keep the photo clause, because the corpus design already planted the transcription gap and the current lesson never cites it.

## New lesson opportunities, only where the work does not fit

Lesson 4 should inherit the citation record and run one judge fixture against a fluent quotation of the wrong version. That is an extension, not a new lesson. The uncalibrated-judge trap is already scheduled there.

Module 4 Lesson 2 already invalidates a cache on `document.changed` for `circ-ramadan-hours`. The extension worth a paragraph in that lesson, not a new lesson, is that the cache key includes the content hash from this lesson. A changed body under a familiar id is the incident, which that lesson already reconstructs for hours.

A later elective, after the course, can install pgvector or OpenSearch and move `fuse` behind SQL, with a `WHERE` that matches `candidates`. That elective is **Proven** infrastructure and is not a module. Contextual retrieval becomes reasonable in that elective only after the store is large enough that the authors’ 200,000-token note no longer says to skip retrieval, and only after the pre-filter runs before any contextualizer sees a staff body. GraphRAG and an open agent loop do not get a lesson in this program. They get the naming page.

## Roles, restated as tasks the same person finishes

Lead: write the sprint sentence that limits v4, and decide the out-of-time cut is the hop, not the pre-filter.

Index: implement fusion and the photo-clause ingestion, and leave `embed.py` as the provided stand-in.

Application: implement candidates, bind, hash history, and sync’s unknown-id skip.

Product: write the two refusal sentences, unchanged in meaning.

Architect: write the audience table and the knowledge answers, including the answer that a staff document is visible to staff and withheld from a patient, and the answer that in force for a new question means status, window, and audience together, while an in-flight question additionally keeps the hash it started with.

No task waits on another person. The checks are the other person.
