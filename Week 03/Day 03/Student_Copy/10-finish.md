# 10 — Finish

Two actions. Replace `knowledge.md`. Run three commands. You are done when each command prints `passed`.

The suite in chapter 08 does not read these pages. `slice-hybrid` and `slice-acl` do not read them either. A page miss fails only the rag check. Use the failure table at the bottom only when a check fails. It is not more work.

The checks do not read an interview note. You do not write one.

## Do this

Chapter 01 copied [knowledge.md](packet/templates/knowledge.md) to [work/knowledge.md](work/knowledge.md). The full path is `Week 03/Day 03/Student_Copy/work/knowledge.md`. The copy has two empty numbers. Do not type into the empty lines. This block replaces the whole file. It does not replace the template in `packet/templates`.

1. Open the work file named here, [work/knowledge.md](work/knowledge.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. To open the chapter file, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `in_force` and `patient`.

```text
# Knowledge

1. A document is in force when its status is in_force, the case date is inside the effective window, and the site matches or is cluster-wide.
2. A staff document may be seen by staff, and a patient may not see it.
```

On Windows, the file sometimes saves as `knowledge.md.txt`. In File Explorer, open View and tick File name extensions. If you see `.txt`, rename the file so the name ends in `.md`.

## You should now see

Open [work/knowledge.md](work/knowledge.md). Two numbered lines. The first says a document is in force when its status is `in_force`, the case date is inside the effective window, and the site matches or is cluster-wide. The second says a staff document may be seen by staff, and a patient may not see it. A second sentence on the next line, without a number, does not count as the second answer.

Then run the checks. Open a terminal in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines. `--work` is required. The path is the work folder you filled in.

```text
cd problem_simulation
python -m alwaha.check rag --release rel-w3d3 --work "../Week 03/Day 03/Student_Copy/work" --profile practice
python -m alwaha.check hybrid --release rel-w3d3 --work "../Week 03/Day 03/Student_Copy/work" --profile practice
python -m alwaha.check acl --release rel-w3d3 --work "../Week 03/Day 03/Student_Copy/work" --profile practice
```

Each command prints its own line. Wait for one line before you start the next command. You need all three. You should see:

```text
chk-w3-rag passed.
slice-hybrid passed.
slice-acl passed.
```

`work/knowledge.md` has both answers. The first says a document is in force when its status is `in_force`, the case date is inside the effective window, and the site matches or is cluster-wide. The second says a staff document may be seen by staff, and a patient may not see it.

If you see those three `passed` lines, skip the table below and go to Done.

## If a check fails

A failed check prints `failed`, then one or more lines that start with a dash. The words after the dash are what you look up in the left column below. Do what the right column says. Then run the command again. A failure does not print a doc id, a span, or a clause. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

`slice-hybrid` and `slice-acl` do not read the four pages. A page miss fails only the rag check.

| What it prints | Where to go |
| --- | --- |
| `Build rel-w3d3 first.` | The pack or the grader's gold file is missing. From the course folder, run `cd problem_simulation` and then `python -m alwaha.build --profile practice --release rel-w3d3`. If you are already inside `problem_simulation`, skip the `cd` line. Then run the three checks again |
| `the citation is not the in-force span` | The message does not name a document or a span. Open [snapshot.jsonl](packet/release/dms/snapshot.jsonl) and [changes.jsonl](packet/release/feed/changes.jsonl). A document is in force when its status is `in_force`, the case date `2027-01-26` sits inside the effective window, and the site matches or is cluster-wide. Label the row you opened: its status, and whether the case date sits inside the window. Then match the other dash lines. Only rag failed: paste [chunk.py](work/app/chunk.py) again from [chapter 06](06-the-index.md). You should see `Split a document into clauses and keep the clause id.` You should not see `Drop the clause id`. Rag and acl failed, and hybrid says vector search alone clears the slice: paste [embed.py](work/app/embed.py) again from chapter 06. You should see `local-embed: a token vector, including codes.` You should not see `{"shell": 1.0}`. All three checks failed with this line: paste [index.py](work/app/index.py) again from chapter 06. You should see `Store one vector per clause.` You should not see `Return an empty index`. Rag also says the index ignores the change feed: paste [sync.py](work/app/sync.py) again from [chapter 07](07-the-citation.md). You should see `Apply document.changed and touch only the changed ids.` `feed` is still the argument name. That is expected. You should not see `del feed` |
| `a draft is cited` | The message does not name the draft. Open [bind.py](work/app/bind.py). A draft stays searchable and is not citable. For endo, ophth, and card, an in-force v4 that covers the start day wins. Otherwise a v3 that covers the start day wins. [Chapter 07](07-the-citation.md). Paste `bind.py` again. You should see `v4 binds for three specialties. An in-flight referral keeps its start version.` `started` is still the argument name. That is expected. You should not see `del started`. Open [retrieve.jsonl](packet/release/slices/retrieve.jsonl) and find `dev-flight`. Its `started` value is `2027-01-20`. Label that start day against the window on the criteria row |
| `the unauthorized circular is cited` | The message does not name the circular. Open [changes.jsonl](packet/release/feed/changes.jsonl) and find the row whose status is `unauthorized`. Label that row: it is not a citation. If only hybrid failed, paste [search.py](work/app/search.py) again from [chapter 06](06-the-index.md). You should see `mode == "hybrid"` on two `if` lines. You should not see `del mode`. Hybrid keeps `in_force` only. Vector mode is the other path. That is expected. Do not make vector follow the same path as hybrid. If rag also lists the restarted referral, the draft, the v4 scope, the staff document, and the answer does not refuse, paste [cite.py](work/app/cite.py) again from [chapter 07](07-the-citation.md). You should see `Cite an in-force span the asker may see, or refuse.` `no-document` is still in the file. That is expected. You should not see `including a draft` |
| `an in-flight referral is restarted on v4` | The message does not name the version it kept. Open [bind.py](work/app/bind.py) and the `dev-flight` row in [retrieve.jsonl](packet/release/slices/retrieve.jsonl). `started` is `2027-01-20`. That referral keeps the version that covers that day. [Chapter 07](07-the-citation.md). Paste `bind.py` again. You should see `An in-flight referral keeps its start version.` You should not see `del started`. If cite.py is also the shell, paste `cite.py` again from the same chapter. Label the start day: the referral is not restarted |
| `v4 is applied outside its specialties` | The message does not name the specialty. Open [criteria-v4.md](packet/release/notices/criteria-v4.md). v4 is endo, ophth, and card, not all. Open [crit-neuro-v3.md](packet/release/dms/crit-neuro-v3.md). Search for `neuro`. The notice does not name it. [Chapter 07](07-the-citation.md). Paste `bind.py` again. You should see `_V4`. It names card, endo, and ophth. Label the neuro page: its in-force row is v3 |
| `the answer does not refuse` | The message does not name the missing refusal. Open [cite.py](work/app/cite.py). When nothing binds, the refusal is `no-document`. When the asker cannot see the document, the refusal is `audience`. [Chapter 07](07-the-citation.md). Paste `cite.py` again. You should see `Cite an in-force span the asker may see, or refuse.` You should not see `including a draft`. The dev rows are in [retrieve.jsonl](packet/release/slices/retrieve.jsonl). Label a question that has no matching code: the answer refuses |
| `a staff document is shown to a patient` | The message does not name the document. Open [leaflet-staff.md](packet/release/dms/leaflet-staff.md). Search for `staff`. A patient sees public only. If rag and acl failed and hybrid passed, paste [filter.py](work/app/filter.py) again from [chapter 07](07-the-citation.md). You should see `A patient sees public documents. Staff do not see restricted ones.` You should not see `return True`. If rag also lists the circular, the restarted referral, the draft, the v4 scope, and the answer does not refuse, paste [cite.py](work/app/cite.py) again from the same chapter. Then open [audience.md](work/audience.md). The patient line starts with `| patient |` and the next cell is `public` only. That line must not contain `staff` or `restricted`. Keep the pipe characters. [Chapter 09](09-the-pages.md). Label the patient row: public only |
| `the index ignores the change feed` | The message does not name the event. Open [changes.jsonl](packet/release/feed/changes.jsonl). Search for `in_force`. The snapshot is the store before that feed. [Chapter 07](07-the-citation.md). Paste `sync.py` again. You should see `Apply document.changed and touch only the changed ids.` You should not see `del feed`. Label one feed row: which id it touches |
| `the index did not run` | The message does not name the line. A work module is missing, or the paste broke the indentation, or a name the check calls is missing. Run `prepare_work.py` from the course folder, then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand. Do not delete `vision.py`, `conflict.py`, or `catalog.py` |
| `vector search alone clears the slice` | This line is from `slice-hybrid`. The message does not name the document. Open [search.py](work/app/search.py). Hybrid is not the same path as vector. [Chapter 06](06-the-index.md). Paste `search.py` again. You should see `mode == "hybrid"` on two `if` lines. You should not see `del mode`. If embed.py is still the shell, the same line can come with a span miss on rag and acl. Paste `embed.py` again from chapter 06. You should see `local-embed: a token vector, including codes.` Label the two modes: vector can rank a document that is not citable, and hybrid keeps `in_force` |
| `sprint.md does not sequence the index` | The message does not print the four words. [Chapter 05](05-the-sprint.md). The page needs index, then filter, then cite, then sync. Paste `sprint.md` again |
| `sprint.md does not limit v4 to three specialties` | The message does not print the specialties. [Chapter 05](05-the-sprint.md). The page needs `endo`, `ophth`, `card`, and `not all`. Paste `sprint.md` again. Open [criteria-v4.md](packet/release/notices/criteria-v4.md) and label the three names |
| `the refusal copy is missing` | [Chapter 09](09-the-pages.md). `refusal.md` needs `no document` and `cannot see`. Paste `refusal.md` again |
| `the audience note lets a patient see a staff document` | [Chapter 09](09-the-pages.md). The table header is `asker` and `audiences`. Keep the pipe characters. The patient row is `public` only. The staff row is `public, staff` and must not contain `restricted`. The records row contains `restricted`. Paste `audience.md` again. Label the patient row |
| `knowledge.md needs two answers` | Paste the block above again. Two numbered lines, each with words after the number. A second sentence on the next line does not count |
| `knowledge.md does not say what makes a document in force` | The message does not name the missing fact. Line 1 of the block above says a document is in force when its status is `in_force`, the case date is inside the effective window, and the site matches or is cluster-wide |
| `knowledge.md does not say who may see a staff document` | Line 2 of the block above says a staff document may be seen by staff, and a patient may not see it |
| `a watermarked sample is in the work directory` | A file that carries the mark is under `work/`. Delete that copy. The message does not print the watermark. Do not delete `vision.py`, `conflict.py`, or `catalog.py` |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python lines |
| `SyntaxError` or `IndentationError` | Run `python "Week 03/Day 03/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand |

## Done

The three checks print `passed`, and `knowledge.md` answers both questions. The first says a document is in force when its status is `in_force`, the case date is inside the effective window, and the site matches or is cluster-wide. The second says a staff document may be seen by staff, and a patient may not see it.
