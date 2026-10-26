# 08 — The advanced path

[Chapter 07](07-the-citation.md) cites an in-force span or refuses. This chapter replaces the photo read, the booking conflict, and the catalog lookup. Then you run the suite.

You replace three files under `work/`, in this order:

1. [vision.py](work/app/vision.py), under Replace the photo read
2. [conflict.py](work/app/conflict.py), under Replace the booking conflict
3. [catalog.py](work/app/catalog.py), under Replace the catalog lookup

Paste only those three blocks. The blocks under Read these files are pictures of the shell. Pasting a picture puts the shell back. Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the copies in `packet/` unchanged. Do not paste a test. The tests are copied and not replaced.

Scroll down to the heading Replace the photo read. It is the first heading on this page that starts with Replace. The code block directly under it is the first paste. Two more Replace headings follow it. The four steps are repeated above each paste. Everything above that first Replace heading is a picture. You do not paste it.

These files are Python. A styled paste can break the indentation. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. A `def` line starts at the left edge. The lines inside a function are indented four spaces. If the terminal later shows `SyntaxError` or `IndentationError`, run `prepare_work.py` from the course folder and paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand.

The three checks do not require these three files. You still replace them. You do not delete them. The suite imports them. A deleted file fails the suite.

Do not run a check on this page. The checks are only in [chapter 10](10-finish.md).

## Read these files

You are reading. You are not pasting yet. Open these in the packet. Read the comment at the top of each one. Do not edit them.

Open [prep.json](packet/release/photos/prep.json). Search for `export`. The export and the transcription are different fields. Open [pol-booking-cluster.md](packet/release/dms/pol-booking-cluster.md) and [pol-booking-h-safra.md](packet/release/dms/pol-booking-h-safra.md). Search for `site` in the facility file. Open [service-catalog.json](packet/release/catalog/service-catalog.json). Search for `clinic`.

1. [vision.py](packet/app/vision.py). Search for `skip the photo transcription`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/vision.py](work/app/vision.py) is under the Replace heading for this file.

```text
"""Read the text export and skip the photo transcription.

clause returns the export text. The transcription is not read.
A page with no export returns empty text.
"""

from __future__ import annotations


def clause(page: dict) -> str:
    """Return the export text from the page.

    page is the scanned page. The transcription field is not
    used. A page without an export returns an empty string.
    """
    return page.get("export", "")
```


2. [conflict.py](packet/app/conflict.py). Search for `Let the facility window replace`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/conflict.py](work/app/conflict.py) is under the Replace heading for this file.

```text
"""Let the facility window replace the cluster window.

booking returns the document for the given site as the winner.
The also field is empty, so the other document is not named.
"""

from __future__ import annotations


def booking(docs: list[dict], site: str) -> dict:
    """Name the site document as the only winner.

    docs is the policy list. site selects the document whose
    site matches. The winner is that document id. also is an
    empty string. A site with no matching document raises,
    because next() requires a match.
    """
    local = next(doc for doc in docs if doc.get("site") == site)
    # The site document wins. The other document is not named.
    return {"also": "", "winner": local["doc_id"]}
```


3. [catalog.py](packet/app/catalog.py). Search for `Cite the leaflet instead`. That sentence is the shell. The next block is a picture of that file. Do not paste it. This block replaces nothing. The paste that replaces [work/app/catalog.py](work/app/catalog.py) is under the Replace heading for this file.

```text
"""Cite the leaflet instead of the service catalog row.

lookup ignores the catalog rows. It returns the clinic that was
asked for, the leaflet document id, and an empty preparation
string.
"""

from __future__ import annotations


def lookup(rows: list[dict], clinic: str) -> dict:
    """Return a leaflet citation for the clinic.

    rows is discarded, so no catalog preparation text is used.
    clinic is copied into the result. The document id is the
    leaflet. prep is empty.
    """
    # The catalog rows are not searched.
    del rows
    return {"clinic": clinic, "doc_id": "leaflet-prep", "prep": ""}
```


The pictures end here. The next heading is the first paste.

## Replace the photo read

This block replaces [work/app/vision.py](work/app/vision.py). The full path is `Week 03/Day 03/Student_Copy/work/app/vision.py`. It does not replace the packet copy. A long block is still one file. This one is `vision.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Read the clause that exists only on the photo transcription.

clause takes the transcription and removes the export text, then
strips the ends. What remains is the text the export did not
already contain.
"""

from __future__ import annotations


def clause(page: dict) -> str:
    """Return the transcription text that is outside the export.

    page supplies export and transcription. A missing export is
    empty text. A missing transcription is empty text. The export
    string is removed from the transcription, and the ends are
    stripped.
    """
    export = page.get("export", "")
    # Remove the export from the transcription and keep what remains.
    return page.get("transcription", "").replace(export, "").strip()
```

Open [work/app/vision.py](work/app/vision.py). Search inside that file, not inside this chapter. You should see `Read the clause that exists only on the photo transcription.`. `export` is still in the file. That is expected. The function removes that field from the transcription. Do not copy the transcription out of prep.json onto a page. You should not see `skip the photo transcription`. If you see that text, you pasted the picture.

## Replace the booking conflict

This block replaces [work/app/conflict.py](work/app/conflict.py). The full path is `Week 03/Day 03/Student_Copy/work/app/conflict.py`. It does not replace the packet copy. A long block is still one file. This one is `conflict.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""The cluster booking window wins. Name both documents.

booking finds the document for the site and the cluster booking
document. The cluster document is the winner. The site document
is named in also.
"""

from __future__ import annotations


def booking(docs: list[dict], site: str) -> dict:
    """Name the site document and return the cluster window as the winner.

    docs must contain a document whose site matches and the
    cluster booking document. The site document id is also.
    The cluster document id is the winner. A missing match
    raises, because next() requires one.
    """
    # The document for this site, and the cluster window.
    local = next(doc for doc in docs if doc.get("site") == site)
    cluster = next(doc for doc in docs if doc.get("doc_id") == "pol-booking-cluster")
    # Name the site document. The cluster window is the winner.
    return {"also": local["doc_id"], "winner": cluster["doc_id"]}
```

Open [work/app/conflict.py](work/app/conflict.py). Search inside that file, not inside this chapter. You should see `The cluster booking window wins. Name both documents.`. `pol-booking-cluster` is the winner. The site document is still named. That is expected. You should not see `Let the facility window replace`. If you see that text, you pasted the picture.

## Replace the catalog lookup

This block replaces [work/app/catalog.py](work/app/catalog.py). The full path is `Week 03/Day 03/Student_Copy/work/app/catalog.py`. It does not replace the packet copy. A long block is still one file. This one is `catalog.py`.

1. Open the work file named under this heading. The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. The sentence under the block names what to search for. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS.

```text
"""Answer a preparation question from the service catalog.

lookup finds the catalog row whose clinic matches, and returns
that clinic with the row's preparation text. The result has no
document id.
"""

from __future__ import annotations


def lookup(rows: list[dict], clinic: str) -> dict:
    """Return the preparation text for this clinic.

    rows are catalog entries. clinic is the name to match. The
    first matching row supplies prep. The clinic in the result
    is the one that was asked for. A clinic with no row raises,
    because next() requires a match.
    """
    # The row whose clinic matches. The answer does not carry a document id.
    row = next(item for item in rows if item["clinic"] == clinic)
    return {"clinic": clinic, "prep": row["prep"]}
```

Open [work/app/catalog.py](work/app/catalog.py). Search inside that file, not inside this chapter. You should see `Answer a preparation question from the service catalog.`. The answer has `clinic` and `prep`. It does not carry a document id. You should not see `Cite the leaflet instead`. If you see that text, you pasted the picture.

## Search before the suite

These strings exist in the replaced work files. A pasted picture fails the search. Open the work file named in the row. A match in this chapter does not count. A match in `packet/` does not count.

| Work file | Search for this | You should find it |
| --- | --- | --- |
| [chunk.py](work/app/chunk.py) | `Split a document into clauses and keep the clause id.` | Yes. `clause_id` is still on the field list. That is expected. You should not see `Drop the clause id` |
| [embed.py](work/app/embed.py) | `local-embed: a token vector, including codes.` | Yes. You should not see `{"shell": 1.0}` |
| [index.py](work/app/index.py) | `Store one vector per clause.` | Yes. You should not see `Return an empty index` |
| [search.py](work/app/search.py) | `mode == "hybrid"` | Yes, on two `if` lines. You should not see `del mode`. Do not make vector follow the same path as hybrid |
| [filter.py](work/app/filter.py) | `A patient sees public documents. Staff do not see restricted ones.` | Yes. You should not see `return True` |
| [bind.py](work/app/bind.py) | `v4 binds for three specialties. An in-flight referral keeps its start version.` | Yes. `started` is still the argument name. That is expected. You should not see `del started` |
| [cite.py](work/app/cite.py) | `Cite an in-force span the asker may see, or refuse.` | Yes. `no-document` is still in the file. That is expected. You should not see `including a draft` |
| [sync.py](work/app/sync.py) | `Apply document.changed and touch only the changed ids.` | Yes. `feed` is still the argument name. That is expected. You should not see `del feed` |
| [vision.py](work/app/vision.py) | `Read the clause that exists only on the photo transcription.` | Yes. `export` is still in the file. That is expected. You should not see `skip the photo transcription` |
| [conflict.py](work/app/conflict.py) | `The cluster booking window wins. Name both documents.` | Yes. You should not see `Let the facility window replace` |
| [catalog.py](work/app/catalog.py) | `Answer a preparation question from the service catalog.` | Yes. You should not see `Cite the leaflet instead` |

If a row fails, you pasted a picture or you skipped that file. The chunk, embed, index, and search rows are the blocks in [chapter 06](06-the-index.md). The filter, bind, cite, and sync rows are the blocks in [chapter 07](07-the-citation.md). The photo, booking, and catalog rows are the blocks above. Paste the failed row's block again from that chapter. Search the work file, not the packet file.

## Run the suite

Leave the window you used for the demo. That window is inside `problem_simulation`, and this command is not. Open a new terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Week 03`. If chapter 01 told you to use `py`, use `py` here.

```text
cd "Week 03/Day 03/Student_Copy/work"
python -m unittest discover -s tests -q
```

If the `cd` line says the path cannot be found, this window is not the course folder. Open a new one and run both lines again. Do not chain `cd ..` to climb out of another folder.

If you run this command before the app files are replaced, it fails. That failure is the shell. The tests are already the shared tests. The app is still the shell. Finish the Replace headings on chapters 06, 07, and 08, then run it again.

You should see a line that starts with `Ran 14 tests`, then a blank line, then `OK`. A line of dashes can sit above the `Ran` line. The time on the `Ran` line can differ. There is no `FAIL` and no `ERROR`. The prompt returns after `OK`.

`Ran 14 tests` also appears when the suite fails. Read the line under it. That line has to be `OK`. If the line is `FAILED`, the shell is still in place. One test can pass while the others fail. That is still the shell. Do not stop at the `Ran` line.

A `FAIL` block names a file under `tests\`, such as `test_chunk.py`. The app file to replace is the same name without `test_`. `test_chunk.py` means [chunk.py](work/app/chunk.py). `test_embed.py` means [embed.py](work/app/embed.py). The same pattern holds for index, search, filter, bind, cite, sync, vision, conflict, and catalog. Do not edit the test. The tests are shared. Use the search table, then paste that app file again from the chapter that owns it.

If the terminal says `SyntaxError` or `IndentationError`, run this from the course folder:

```text
python "Week 03/Day 03/Student_Copy/prepare_work.py"
```

A second run erases the pasted files. Paste chapters 05 through 08 again from the chapter source. Do not repair the spaces by hand. Then run the suite again. Do not run `prepare_work.py` on this page unless the terminal shows `SyntaxError` or `IndentationError`.

A green suite can still fail chapter 10. The suite does not read the four pages. The rag check does. `slice-hybrid` and `slice-acl` do not read the four pages.

This page is done when the suite prints `Ran 14 tests` and `OK`, and the eleven searches above pass in the work files.

Next: [09 — The pages](09-the-pages.md).
