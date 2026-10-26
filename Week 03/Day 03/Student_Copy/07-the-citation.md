# 07 — The citation

[Chapter 06](06-the-index.md) stored a vector on each clause. This chapter replaces the audience filter, the criteria bind, the citation, and the sync.

You replace four files under `work/`, in this order:

1. [filter.py](work/app/filter.py), under Replace the audience filter
2. [bind.py](work/app/bind.py), under Replace the criteria bind
3. [cite.py](work/app/cite.py), under Replace the citation
4. [sync.py](work/app/sync.py), under Replace the sync

Paste only those four blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the audience filter. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Three more Replace headings follow it. The four steps are repeated above each paste. The section How the replacement works sits above the first Replace heading. Read it. Do not paste it. Every code block above that Replace heading is a picture. You do not paste a picture.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 through 07 again from the chapter source. Do not repair the spaces by hand.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md).

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them.

Open [criteria-v4.md](packet/release/notices/criteria-v4.md) again. Search for `endo`. v4 binds for endo, ophth, and card. A referral that already started keeps the version it started with. Open [changes.jsonl](packet/release/feed/changes.jsonl). Search for `unauthorized`. The sync has to apply that feed. The shell ignores it.

1. [filter.py](packet/app/filter.py). Search for `Keep every audience`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/filter.py](work/app/filter.py) is under the Replace heading for this file.

```text
"""Keep every audience, including a staff document for a patient.

allow does not read the document or the asker. It returns true
for every pair, so each asker passes with each audience.
"""

from __future__ import annotations


def allow(doc: dict, asker: str) -> bool:
    """Allow the document for this asker.

    doc and asker are discarded. The audience is not compared
    with the asker.
    """
    del doc, asker
    return True
```


2. [bind.py](packet/app/bind.py). Search for `Restart in-flight work on v4`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/bind.py](work/app/bind.py) is under the Replace heading for this file.

```text
"""Restart in-flight work on v4, and treat every v4 as in force.

criteria ignores the start day. It returns the first document
for the specialty whose version is 4. Status is not read, so
any version 4 document is returned. When no document matches,
the result is an empty dict.
"""

from __future__ import annotations


def criteria(docs: list[dict], specialty: str, started: str) -> dict:
    """Return the first version 4 document for this specialty.

    docs is the document list. specialty must match the document
    specialty. started is discarded, so the start day does not
    choose the document. The first match is returned as it is.
    """
    # The start day is not part of this choice.
    del started
    for doc in docs:
        # Version 4 is enough. Status is not consulted.
        if doc.get("specialty") == specialty and doc.get("version") == 4:
            return doc
    # No version 4 for this specialty.
    return {}
```


3. [cite.py](packet/app/cite.py). Search for `including a draft`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/cite.py](work/app/cite.py) is under the Replace heading for this file.

```text
"""Return the nearest chunk, including a draft.

answer indexes the documents and ranks them in vector mode. An
empty ranking is a no-document refusal. Otherwise the first
ranked chunk is cited. Status is copied onto the citation, so
a draft is cited the same way as any other status. The asker
is not checked.
"""

from __future__ import annotations

from index import build
from search import rank


def answer(question: dict, docs: list[dict]) -> dict:
    """Cite the top vector hit, or refuse when nothing ranks.

    question supplies the text to rank. docs are indexed, then
    ranked in vector mode. The citation copies audience, document
    id, clause id as the span, status, and version from that hit.
    A missing text field becomes empty text. A missing version
    becomes zero.
    """
    ranked = rank(question["text"], build(docs), "vector")
    # No hit means there is nothing to cite.
    if not ranked:
        return {"refusal": "no-document"}
    top = ranked[0]
    # Status is passed through. This function does not drop a draft.
    return {
        "audience": top.get("audience", ""),
        "doc_id": top.get("doc_id", ""),
        "span": top.get("clause_id", ""),
        "status": top.get("status", ""),
        "version": top.get("version", 0),
    }
```


4. [sync.py](packet/app/sync.py). Search for `ignore the change feed`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/sync.py](work/app/sync.py) is under the Replace heading for this file.

```text
"""Rebuild from the snapshot and ignore the change feed.

apply copies the snapshot documents and returns an empty touched
list. Events in the feed are not applied.
"""

from __future__ import annotations


def apply(snapshot: list[dict], feed: list[dict]) -> dict:
    """Copy the snapshot and report that nothing was touched.

    Each snapshot document is copied, so a later edit to a result
    dict does not change the caller's dict. feed is discarded.
    touched is an empty list.
    """
    # The change feed is not applied.
    del feed
    return {"docs": [dict(doc) for doc in snapshot], "touched": []}
```


The pictures end here. The next heading is How the replacement works. Read it. It is not a paste. The first paste is the next heading that starts with Replace.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

A search hit is not yet a citation. Four functions turn it into one, or into a refusal.

`allow` is the audience rule. A patient sees `public` only. Staff see `public` and `staff`. Records also see `restricted`. Anyone else sees nothing. A missing audience matches nothing.

`criteria` binds one specialty at the referral's start day. Week 1 Day 3 already followed the document that was in force on that day. v4 was a draft then. Today's feed can mark v3 superseded when v4 becomes in force. A superseded v3 still covers a start day inside its window, which is why the kept statuses are `in_force` and `superseded`. For `card`, `endo`, and `ophth`, an in-force version 4 that covers that day wins. Otherwise a version 3 that is in force or superseded, and that covers the day, wins. `_covers` rejects a day before the effective date or on or after sunset. An in-flight referral keeps the version it started on. `dev-flight` started on `2027-01-20`, before the case date. Neuro is not in the v4 set. This function does not read site. Site is the booking conflict in chapter 08.

`answer` cites a span the asker may see, or refuses. Nothing bound is `no-document`. A bound document the asker cannot see is an audience refusal. With no specialty, `_visible` keeps in-force spans this asker may see that carry a question code. `_cite` puts the clause id on the span.

`apply` copies the snapshot and plays the change feed. An add inserts the document. Any other op writes the event fields onto the stored id. Only the touched ids are listed, so you do not rebuild the world for one change.

The unauthorized circular can be in the feed and still not be a citation. It is not in force, or the asker cannot see it, or both.

Before you paste, say who may see a staff document, and which date chooses between v3 and v4.

This section adds no file and no command.

## Replace the audience filter

This block replaces [work/app/filter.py](work/app/filter.py). The full path is `Week 03/Day 03/Student_Copy/work/app/filter.py`. It does not replace the packet copy. A long block is still one file. This one is `filter.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""A patient sees public documents. Staff do not see restricted ones.

allow compares the document audience with the asker. A patient
sees a public document only. Staff see a public or staff
document. Records see a public, staff, or restricted document.
Any other asker sees nothing.
"""

from __future__ import annotations


def allow(doc: dict, asker: str) -> bool:
    """Return whether this asker may see the document.

    doc supplies the audience. A missing audience is empty text,
    which matches none of the allowed sets. asker selects the
    set. patient, staff, and records are the askers that can
    pass.
    """
    audience = doc.get("audience", "")
    # A patient sees public only. Staff and restricted stay off this path.
    if asker == "patient":
        return audience == "public"
    # Staff see public and staff. Restricted stays off this path.
    if asker == "staff":
        return audience in {"public", "staff"}
    # Records see public, staff, and restricted.
    if asker == "records":
        return audience in {"public", "staff", "restricted"}
    # Any other asker sees nothing.
    return False
```

Open [work/app/filter.py](work/app/filter.py). Search inside that file, not inside this chapter. You should see `A patient sees public documents. Staff do not see restricted ones.`. A patient returns true only for `public`. `staff` is still in the staff branch. That is expected. `restricted` is only in the records branch. You should not see `return True`. If you see that text, you pasted the picture.

## Replace the criteria bind

This block replaces [work/app/bind.py](work/app/bind.py). The full path is `Week 03/Day 03/Student_Copy/work/app/bind.py`. It does not replace the packet copy. A long block is still one file. This one is `bind.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""v4 binds for three specialties. An in-flight referral keeps its start version.

criteria keeps the rows for one specialty. For card, endo, and ophth,
an in-force version 4 that covers the start day wins. Otherwise a
version 3 that is in force or superseded, and that covers the start
day, wins. A document whose window misses the start day is skipped.
When nothing covers that day, criteria returns an empty mapping.
"""

from __future__ import annotations

# A superseded v3 can still cover a start day inside its window.
_KEPT = {"in_force", "superseded"}
# v4 is in force for these three specialties, not for every specialty.
_V4 = {"card", "endo", "ophth"}


def _covers(doc: dict, day: str) -> bool:
    """Return whether the day sits inside the document window.

    A day before the effective date is outside. A day on or after sunset is outside. An empty bound does not close that side.
    """
    effective = doc.get("effective") or ""
    sunset = doc.get("sunset") or ""
    # A day before the effective date is outside the window.
    if effective and day < effective:
        return False
    # A day on or after sunset is outside the window.
    if sunset and day >= sunset:
        return False
    return True


def criteria(docs: list[dict], specialty: str, started: str) -> dict:
    """Return the criteria document that covers this start day.

    For a specialty in the v4 set, an in-force v4 that covers the day wins. Otherwise a v3 that is in force or superseded, and that covers the day, wins. Nothing that covers the day returns an empty mapping so the caller can refuse.
    """
    rows = [doc for doc in docs if doc.get("specialty") == specialty]
    # For the three specialties, an in-force v4 that covers the start day wins.
    if specialty in _V4:
        for doc in rows:
            if doc.get("version") == 4 and doc.get("status") == "in_force" and _covers(doc, started):
                return doc
    # Otherwise a v3 that is in force or superseded, and that covers the start day, wins.
    for doc in rows:
        if doc.get("version") == 3 and doc.get("status") in _KEPT and _covers(doc, started):
            return doc
    # Nothing covers that start day.
    return {}
```

Open [work/app/bind.py](work/app/bind.py). Search inside that file, not inside this chapter. You should see `v4 binds for three specialties. An in-flight referral keeps its start version.`. `started` is still the name of the day argument. That is expected. The shell deletes that day. This file uses it. You should not see `del started`. If you see that text, you pasted the picture.

## Replace the citation

This block replaces [work/app/cite.py](work/app/cite.py). The full path is `Week 03/Day 03/Student_Copy/work/app/cite.py`. It does not replace the packet copy. A long block is still one file. This one is `cite.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Cite an in-force span the asker may see, or refuse.

A specialty question binds the criteria for the start day, or the
case date when that start day is absent. Nothing bound is a
no-document refusal. A bound document the asker cannot see is an
audience refusal. With no specialty, the first in-force span the
asker may see that carries a code from the question is cited. When
none remains, the result is the same no-document refusal.
"""

from __future__ import annotations

from bind import criteria
from embed import codes
from filter import allow
from index import build
from search import rank


def answer(question: dict, docs: list[dict]) -> dict:
    """Return a citation the asker may see, or a refusal.

    A specialty question binds criteria for the start day, or the case date when the start day is absent. Nothing bound returns a no-document refusal. A bound document the asker cannot see returns an audience refusal. With no specialty, the first in-force span the asker may see is cited, or the same no-document refusal when none remains.
    """
    # A specialty question binds the criteria for the start day, or the case date.
    if question.get("specialty"):
        chosen = criteria(docs, question["specialty"], question.get("started") or question["case_date"])
        # Nothing binds.
        if not chosen:
            return {"refusal": "no-document"}
        # The asker cannot see the document that bound.
        if not allow(chosen, question["asker"]):
            return {"refusal": "audience"}
        return _cite(chosen)
    # No specialty: hybrid rank, then keep an in-force span the asker may see.
    visible = _visible(question, docs)
    if not visible:
        return {"refusal": "no-document"}
    return _cite(visible[0])


def _visible(question: dict, docs: list[dict]) -> list[dict]:
    """Return in-force spans this asker may see that carry a question code.

    Hybrid rank supplies the order. A span that is not in force, or that this asker cannot see, is dropped. A span whose vector contains none of the question codes is dropped.
    """
    query_codes = codes(question["text"])
    kept = []
    for chunk in rank(question["text"], build(docs), "hybrid"):
        # Drop a span that is not in force, or that this asker cannot see.
        if chunk.get("status") != "in_force" or not allow(chunk, question["asker"]):
            continue
        vector = chunk.get("vector") or {}
        # Keep a span whose vector contains a code from the question.
        if any(code in vector for code in query_codes):
            kept.append(chunk)
    return kept


def _cite(doc: dict) -> dict:
    """Return the citation fields for one document.

    The span is the clause id. Audience, document id, status, and version travel with it so the citation can be checked without the rest of the document. A missing text field is empty, and a missing version is zero.
    """
    # The span is the clause id. The other fields travel with the citation.
    return {
        "audience": doc.get("audience", ""),
        "doc_id": doc.get("doc_id", ""),
        "span": doc.get("clause_id", ""),
        "status": doc.get("status", ""),
        "version": doc.get("version", 0),
    }
```

Open [work/app/cite.py](work/app/cite.py). Search inside that file, not inside this chapter. You should see `Cite an in-force span the asker may see, or refuse.`. `no-document` is still in the file. That is expected. It is the refusal when nothing binds. `audience` is the other refusal, when the asker cannot see the document. You should not see `including a draft`. If you see that text, you pasted the picture.

## Replace the sync

This block replaces [work/app/sync.py](work/app/sync.py). The full path is `Week 03/Day 03/Student_Copy/work/app/sync.py`. It does not replace the packet copy. A long block is still one file. This one is `sync.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Apply document.changed and touch only the changed ids.

apply starts from a copy of the snapshot. Each feed event appends
its document id to touched. An add inserts the event document.
Any other op writes the event fields onto the stored document
with that id.
"""

from __future__ import annotations


def apply(snapshot: list[dict], feed: list[dict]) -> dict:
    """Copy the snapshot, apply each event, and list the touched ids.

    snapshot is copied one document at a time, so the caller's
    dicts stay as they were. feed is walked in order. An add
    appends a copy of the event document and indexes it by
    document id. Any other op writes the event fields onto the
    document already stored under that id. touched gains one id
    per event.
    """
    # Start from a copy of the snapshot. The snapshot list itself stays unchanged.
    docs = [dict(doc) for doc in snapshot]
    by_id = {doc["doc_id"]: doc for doc in docs}
    touched = []
    for event in feed:
        # Every event id is touched, whether the op adds or updates.
        touched.append(event["doc_id"])
        if event["op"] == "add":
            # An add inserts the new document.
            added = dict(event["doc"])
            docs.append(added)
            by_id[added["doc_id"]] = added
        else:
            # Any other op writes the event fields onto that id.
            by_id[event["doc_id"]].update(event["fields"])
    return {"docs": docs, "touched": touched}
```

Open [work/app/sync.py](work/app/sync.py). Search inside that file, not inside this chapter. You should see `Apply document.changed and touch only the changed ids.`. `feed` is still the name of the second argument. That is expected. The shell deletes the feed. This file applies it. You should not see `del feed`. If you see that text, you pasted the picture.

This page is done when those four searches pass in the work files. The packet copies are still the shells. Do not run a check from this page.

Next: [08 — The advanced path](08-the-advanced.md).
