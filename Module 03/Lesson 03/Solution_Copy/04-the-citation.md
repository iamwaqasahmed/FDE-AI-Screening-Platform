# 04 — The citation

Open the finished files and put them beside yours.

## Filter

[filter.py](work/app/filter.py). The shell returns true for every asker, so a staff document is shown to a patient on rag and acl. Hybrid still passes. The filled file lets a patient see public only, staff see public and staff, and records see public, staff, and restricted. Any other asker sees nothing. You should not see `return True`.

[leaflet-staff.md](sources/release/dms/leaflet-staff.md) is the staff audience. A patient row that also contains staff or restricted fails the audience page. That page is chapter 06.

## Bind

[bind.py](work/app/bind.py). The shell ignores the start day and returns the first v4 for the specialty. Rag then says an in-flight referral is restarted on v4, a draft is cited, and v4 is applied outside its specialties. Hybrid and acl still pass. The filled file uses the start day. Module 1 stopped on the document in force at the start. After the feed, v3 can be superseded and still cover an earlier start day. For card, endo, and ophth, an in-force v4 that covers that day wins. Otherwise a v3 that is in force or superseded, and that covers that day, wins. The function does not read site. A day before effective, or on or after sunset, is outside the window. `started` is still the argument name. That is expected. You should not see `del started`.

The `dev-flight` row in [retrieve.jsonl](sources/release/slices/retrieve.jsonl) has `started` of `2027-01-20`. Label that day against the window. The notice is [criteria-v4.md](sources/release/notices/criteria-v4.md).

## Cite

[cite.py](work/app/cite.py). The shell returns the nearest chunk, including a draft. Rag then reports the unauthorized circular, the restarted referral, the draft, the v4 scope, the staff document, and that the answer does not refuse. Acl reports the staff document. Hybrid still passes. The filled file binds a specialty question on the start day, or the case date, then checks the audience. Nothing bound is `no-document`. The asker cannot see it is `audience`. A question with no specialty uses hybrid rank and keeps an in-force span the asker may see that contains a question code. `no-document` is still in the file. That is expected.

## Sync

[sync.py](work/app/sync.py). The shell ignores the feed, so rag says the index ignores the change feed and misses the span, and acl misses the span. Hybrid still passes. The filled file copies the snapshot, applies each event, and touches every changed id. An add inserts the document. Any other op updates the fields. `feed` is still the argument name. That is expected. You should not see `del feed`.

The feed is [changes.jsonl](sources/release/feed/changes.jsonl). The snapshot is the store before that feed. A row is one long line.

## The path through the files

The morning chapter [07-the-citation.md](../Student_Copy/07-the-citation.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [05 — The advanced path](05-the-advanced.md).
