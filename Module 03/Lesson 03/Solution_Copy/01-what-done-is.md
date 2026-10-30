# 01 — What done is

This page is the map. The day is finished by the sprint, the chunk split, the local embed, the index, the search, the audience filter, the criteria bind, the citation, the sync, the photo read, the booking conflict, the catalog lookup, the refusal, the audience table, and the knowledge file.

Open `work/` and find each row. The release pages those answers cite are in [sources](sources/README.md).

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Index, then filter, then cite, then sync. v4 is endo, ophth, and card, not all specialties. Explained in [chapter 02](02-the-sprint.md) |
| [app/chunk.py](work/app/chunk.py) | A blank line starts a clause, and the clause id stays. Explained in [chapter 03](03-the-index.md) |
| [app/embed.py](work/app/embed.py) | A token vector, including codes. Explained in chapter 03 |
| [app/index.py](work/app/index.py) | One vector stored on each clause. Explained in chapter 03 |
| [app/search.py](work/app/search.py) | Hybrid keeps `in_force` and adds a code boost. Vector does not. Explained in chapter 03 |
| [tests/test_chunk.py](work/tests/test_chunk.py) | Two clauses keep the clause id. The same bytes as the packet |
| [tests/test_embed.py](work/tests/test_embed.py) | A hyphenated code stays in the vector |
| [tests/test_index.py](work/tests/test_index.py) | The index stores a vector |
| [tests/test_search.py](work/tests/test_search.py) | Hybrid drops the unauthorized status. Vector does not |
| [app/filter.py](work/app/filter.py) | A patient sees public only. Explained in [chapter 04](04-the-citation.md) |
| [app/bind.py](work/app/bind.py) | v4 for three specialties. An in-flight referral keeps its start day. Explained in chapter 04 |
| [app/cite.py](work/app/cite.py) | Cite an in-force span the asker may see, or refuse. Explained in chapter 04 |
| [app/sync.py](work/app/sync.py) | Apply the change feed and touch the changed ids. Explained in chapter 04 |
| [tests/test_filter.py](work/tests/test_filter.py) | A patient sees public only. Staff do not see restricted |
| [tests/test_bind.py](work/tests/test_bind.py) | An early start stays on v3. Neuro stays on v3 |
| [tests/test_cite.py](work/tests/test_cite.py) | An in-flight referral keeps its start version. A patient does not receive the staff leaflet |
| [tests/test_sync.py](work/tests/test_sync.py) | The feed touches only the changed ids |
| [app/vision.py](work/app/vision.py) | The transcription with the export removed. Explained in [chapter 05](05-the-advanced.md). The three checks do not require it |
| [app/conflict.py](work/app/conflict.py) | The cluster booking window wins, and both documents are named. Explained in chapter 05. The three checks do not require it |
| [app/catalog.py](work/app/catalog.py) | Clinic and prep from the catalog. No document id. Explained in chapter 05. The three checks do not require it |
| [tests/test_vision.py](work/tests/test_vision.py) | The photo clause is not the export |
| [tests/test_conflict.py](work/tests/test_conflict.py) | The cluster window wins and both are named |
| [tests/test_catalog.py](work/tests/test_catalog.py) | The catalog answers without a leaflet |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | Runs the suite. Same bytes as the packet |
| [refusal.md](work/refusal.md) | No document binds, or the asker cannot see it. Explained in [chapter 06](06-the-pages.md) |
| [audience.md](work/audience.md) | Patient public, staff public and staff, records include restricted. Explained in chapter 06 |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 07](07-knowledge.md) |
| [phc-lead.notes.md](work/interviews/phc-lead.notes.md) | A trainer note. The morning did not ask for an interview. The checks do not read it |
| [phc-lead.questions.txt](work/interviews/phc-lead.questions.txt) | The questions that produced those notes. The checks do not read them |
| [coord-lead.notes.md](work/interviews/coord-lead.notes.md) | A trainer note. The morning did not ask for an interview. The checks do not read it |
| [coord-lead.questions.txt](work/interviews/coord-lead.questions.txt) | The questions that produced those notes. The checks do not read them |

The checks print `passed` when the index cites an in-force span the asker may see, an in-flight referral keeps the version it started on, a draft is not cited, the unauthorized circular is not cited, v4 stays inside endo, ophth, and card, a patient does not see a staff document, the change feed is applied, hybrid does not treat vector as the same path, the sprint sequences index then filter then cite then sync and limits v4 to three specialties, the refusal has both sentences, the audience table keeps the pipe characters, and both knowledge answers are present.

`slice-hybrid` and `slice-acl` do not read the four pages. A page miss fails only the rag check.

The checks do not read the interview notes.

Next: [02 — The sprint](02-the-sprint.md).
