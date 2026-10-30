# 08 — Trainer session

Students can skip this page. The answers are in chapters 01 through 07.

Use this page after the attempt. Teach one block, then the next. Have their `work/` folder and this solution open.

## Before you start

Leave `problem_simulation/build` closed. Do not paste a watermark into a slide or a prompt.

[phc-lead.notes.md](work/interviews/phc-lead.notes.md), [phc-lead.questions.txt](work/interviews/phc-lead.questions.txt), [coord-lead.notes.md](work/interviews/coord-lead.notes.md), and [coord-lead.questions.txt](work/interviews/coord-lead.questions.txt) are for you. The checks do not read them. Students were not asked to run an interview. The PHC note says hospitals return a referral with a short reason on the page, and the templates still generate criteria v3. The coordinator note says the queue is long because each referral takes a second reading, and criteria v4 was circulated as a draft and is not the version the templates use.

The demo, from `problem_simulation`, prints two titles and then one line:

```text
cd problem_simulation
python -m alwaha.demo.duplicate --profile practice
```

The line after the titles is `one is superseded`. It does not print the watermark. It does not print the clause that tells the two leaflets apart. Do not type the titles on a slide.

`vision.py`, `conflict.py`, and `catalog.py` are the advanced path. The three checks pass if those files are absent. Do not tell a student to delete them. When the files are present, they have to keep the photo read, the cluster booking window, and the catalog lookup. The packet copies are the shells. The work copies are the replacements. The eleven test files match the packet byte for byte. Do not add a comment to only one side. `.github/workflows/ci.yml` matches the packet.

From the course folder, the three checks print `passed`:

```text
cd problem_simulation
python -m alwaha.check rag --release rel-m03-l03 --work "../Module 03/Lesson 03/Solution_Copy/work" --profile practice
python -m alwaha.check hybrid --release rel-m03-l03 --work "../Module 03/Lesson 03/Solution_Copy/work" --profile practice
python -m alwaha.check acl --release rel-m03-l03 --work "../Module 03/Lesson 03/Solution_Copy/work" --profile practice
```

## Block 1 — The sprint

Open their `sprint.md` beside [sprint.md](work/sprint.md). Ask which word comes first. The answer is index, then filter, then cite, then sync. v4 is endo, ophth, and card, not all specialties. [criteria-v4.md](sources/release/notices/criteria-v4.md) is the sentence they are repeating. The notice does not name neuro.

## Block 2 — The index

Open their `chunk.py`, `embed.py`, `index.py`, and `search.py` beside the files in this folder. The shell chunk drops the clause id. The filled chunk keeps it. The shell embed gives every text the same vector. The filled embed keeps codes. The shell index is empty. The filled index stores a vector. The shell search deletes `mode`. The filled search keeps `mode == "hybrid"` on two `if` lines. Vector mode is the other path. That is expected. Do not let them make vector follow the same path as hybrid.

## Block 3 — The citation

Open their `filter.py`, `bind.py`, `cite.py`, and `sync.py`. The shell filter returns true for every asker. The filled filter keeps a patient on public. The shell bind ignores the start day. The filled bind uses it. `started` remains the argument name. That is expected. The shell cite returns the nearest chunk, including a draft. The filled cite refuses with `no-document` or `audience`. `no-document` remains. That is expected. The shell sync ignores the feed. The filled sync applies it. `feed` remains the argument name. That is expected.

## Block 4 — The advanced path

Open their `vision.py`, `conflict.py`, and `catalog.py` only if they replaced them. The suite is `Ran 14 tests` and `OK` when all eleven filled modules are in place. The three checks do not call these three files. If a student deleted them, the checks can still pass and the suite cannot. Ask them to paste the three files back. Do not treat deletion as the fix.

## Block 5 — The pages

Open their `refusal.md` and `audience.md`. The refusal needs `no document` and `cannot see`. The audience table needs the pipe characters. Patient is public only. Staff is public and staff, and that row must not contain restricted. Records includes restricted.

## Block 6 — Knowledge

The first sentence says a document is in force when its status is `in_force`, the case date is inside the effective window, and the site matches or is cluster-wide. The second sentence says a staff document may be seen by staff, and a patient may not see it. Both sentences are numbered lines. A wrapped second line does not count.

## Close

A pass is three lines: `chk-m03-l03-rag passed.`, `slice-hybrid passed.`, and `slice-acl passed.`. If those three lines are on the screen, the failure table is not more work. Leave `problem_simulation/build` closed.
