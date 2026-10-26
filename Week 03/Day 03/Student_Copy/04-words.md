# 04 — Words

Read this page once. You do not need to memorize it, and you do not need to open every link. Scan the tables, then go to [chapter 05](05-the-sprint.md). When a later chapter uses a word you want in the file's own sentence, come back to that row and open the link. You do not paste anything on this page, and you do not run a command. If you are lost on this page, scroll to the line that starts with Next. That line is the end of the reading.

These are the words this day uses. A definition here is the everyday meaning. When the rule lives in a file, the link is beside the word. Open that file when you need the sentence itself.

## Criteria and the store

| Word | Meaning |
| --- | --- |
| Criteria v4 | The notice in [criteria-v4.md](packet/release/notices/criteria-v4.md). In force for three specialties, not every specialty |
| endo | Endocrinology. One of the three specialties on the notice |
| ophth | Ophthalmology. One of the three specialties on the notice |
| card | Cardiology. One of the three specialties on the notice |
| neuro | Neurology. A specialty still in the store. The notice does not name it. Open [crit-neuro-v3.md](packet/release/dms/crit-neuro-v3.md) |
| in force | The document may be cited. The status word in the file is `in_force` |
| `in_force` | The status value on a document that may be cited. Search the snapshot for it |
| draft | Searchable, and not citable. On the snapshot, v4 is still draft |
| superseded | The older document after the feed moves the window. It can still cover a start day inside that window |
| unauthorized | Not citable. The circular with that status is on the [change feed](packet/release/feed/changes.jsonl), not on the snapshot page |
| circular | A short notice in the document store. The unauthorized one is not a citation |
| snapshot | [snapshot.jsonl](packet/release/dms/snapshot.jsonl). The store before the feed. A row is one long line |
| change feed | [changes.jsonl](packet/release/feed/changes.jsonl). The update. A row is one long line |
| `document.changed` | The feed event named in [dms.yaml](packet/release/openapi/dms.yaml) |
| effective | The day a document starts. A case date before it is outside the window |
| sunset | The day a document stops. A case date on or after it is outside the window |
| window | From effective up to, and not including, sunset |
| case date | `2027-01-26`, on the notice and on the release index |
| version | The criteria generation. v3 and v4 are both in the store. An in-flight referral keeps the version it started on |
| specialty | The service line on a criteria document: endo, ophth, card, or neuro |
| site | Where the document applies. `cluster` is cluster-wide. `h-safra` is one facility, in [pol-booking-h-safra.md](packet/release/dms/pol-booking-h-safra.md) |
| cluster | The whole health cluster. A cluster-wide document matches a cluster case |
| `h-safra` | One facility. Its booking window is the local document. The cluster window is the other document |
| referral | A request from a local clinic for a hospital appointment |
| in-flight | A referral that already started. It keeps the criteria version it started on |
| bind | Choose the criteria document that covers the start day. Chapter 07 replaces `bind.py` |

## Audience and refusal

| Word | Meaning |
| --- | --- |
| audience | Who a document is written for: `public`, `staff`, or `restricted` |
| asker | Who is asking: `patient`, `staff`, or `records`. The dev rows are in [retrieve.jsonl](packet/release/slices/retrieve.jsonl) |
| patient | Sees `public` only |
| staff | Sees `public` and `staff`. Does not see `restricted` |
| records | Sees `public`, `staff`, and `restricted` |
| public | An audience a patient may see. The hours circular is public |
| restricted | An audience for records. [pol-safety.md](packet/release/dms/pol-safety.md) is restricted |
| ACL | The allow rule. A patient does not see a staff document |
| refusal | What the answer says when nothing binds, or the asker cannot see the document |
| `no-document` | The refusal when nothing in force binds the answer |
| citation | The in-force span the asker may see. A search hit is not a citation |

## Index, search, and the pages

| Word | Meaning |
| --- | --- |
| chunk | One clause cut from a document body. A blank line starts the next clause |
| clause | That piece of the body |
| clause id | The id that stays on the clause. The citation calls it the span |
| span | The clause id on the citation. A failure does not print the span |
| embedding | A vector of tokens. This day uses `local-embed` |
| `local-embed` | The token vector, including codes. Chapter 06 replaces `embed.py` |
| vector | Similarity alone. It can rank a document that is not citable |
| hybrid | Vector similarity, plus a code boost, and it keeps `in_force` only |
| code | A token with a hyphen, such as the codes on the criteria pages |
| index | The stored clauses and their vectors. The sprint names it first |
| filter | The audience allow rule. The sprint names it second |
| cite | The citation or the refusal. The sprint names it third |
| sync | Apply the change feed and touch the changed ids. The sprint names it fourth |
| catalog | The service row in [service-catalog.json](packet/release/catalog/service-catalog.json). Clinic and prep. Not a leaflet |
| photo | [prep.json](packet/release/photos/prep.json). `export` is one field. `transcription` is the other |

## What the check will see

| Word | Meaning |
| --- | --- |
| `work/` | The folder you fill in. The checks read this copy |
| `packet/` | The drawer. The checks do not read the shell in the packet |
| The tests | Shared. They fail beside the shell and pass beside the filled app. You do not edit them |
| The workflow | [.github/workflows/ci.yml](packet/.github/workflows/ci.yml). On Windows, `.github` is hidden. Tick Hidden items. You do not edit the workflow |
| Watermark | A mark that must not be copied into `work/`. The failure line does not print the mark |
| Lead | Sequences the sprint and limits v4 to three specialties |
| AI or data engineer | Owns the index, and the three advanced files |
| Application engineer | Owns the filter, the bind, the cite, and the sync |
| Product manager | Writes the refusal |
| Architect | Sets the audience table and answers the two knowledge questions |

This page is done when you can find a word in the tables and open its file.

## A plain reading

This day is retrieval over the cluster's documents. You will also hear that job called RAG, retrieval-augmented generation: the answer has to come from a retrieved span, and the span has to be in force for the person who asked. The chapters say index, filter, and cite.

A chunk is one clause, cut at a blank line, with its clause id kept. An embedding, here, is the token vector `local-embed` writes. The text is split into tokens. A hyphenated code stays one token. Each token gets a weight equal to its share of the text. Nearness compares two of those maps. The replacement file calls that comparison cosine similarity. A vector score can still rank a document you are not allowed to cite. Hybrid search adds the code boost and keeps `in_force` only.

A patient sees `public` only. Staff also see `staff`. Records also see `restricted`. A draft can be found by search and still not be a citation.

This section adds no file and no command.

The [concept index](../../../learning/concept-index.md) lists words from the whole course and points back to the page that introduced each one. It is a lookup. It is not the next chapter.

Next: [05 — The sprint](05-the-sprint.md).
