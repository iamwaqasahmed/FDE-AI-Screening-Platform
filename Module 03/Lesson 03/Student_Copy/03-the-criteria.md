# 03 — The criteria

[Chapter 02](02-the-role.md) named the five parts. This chapter is the file drop. You read. You run one demo. You do not paste a file.

To open a link, Ctrl+click it on Windows or Command+click it on macOS. To search, Ctrl+F or Command+F inside the file that item names, not inside this chapter.

The blocks under Read these files are pictures. They replace nothing. Do not paste them.

## Read these files

Open these in order. Stay on the list until item 23. Then run the demo. You do not paste any of these files. You do not open `data/` or `case/`.

Each item tells you when you are done with that file. Finish that item before you open the next number. A jsonl row is one long line. Word wrap can make that line look like several lines. It is still one row.

1. [release/README.md](packet/release/README.md). Search for `2027-01-26`. You are done with this file when that case date is on the page.
2. [criteria-v4.md](packet/release/notices/criteria-v4.md). Search for `endo`. You should also see `ophth` and `card`, and a sentence that v4 is not in force for every specialty. A referral that already started keeps the version it started with. A draft can be searched. A draft is not citable. An unauthorized document is not citable. The notice does not name neuro. You are done with this file when you have seen those three specialty names.
3. [snapshot.jsonl](packet/release/dms/snapshot.jsonl). Search for `draft`. You are done with this file when a v4 row is still `draft`. The snapshot is the store before the feed. The next block is a picture of the first row. Do not paste it. This block replaces nothing. That row's fields are audience, body, clause_id, code, content_hash, doc_id, effective, family, site, specialty, status, sunset, supersedes, title, and version.

```text
{"audience": "staff", "body": "Code endo-v3 is the criteria in force for endocrinology.", "clause_id": "endo-v3-c1", "code": "endo-v3", "content_hash": "sha256:ead296d6cef7ab93", "doc_id": "crit-endo-v3", "effective": "2026-01-01", "family": "criteria", "site": "cluster", "specialty": "endo", "status": "in_force", "sunset": "", "supersedes": "", "title": "Endocrinology criteria v3", "version": 3}
```

4. [changes.jsonl](packet/release/feed/changes.jsonl). Search for `unauthorized`. You are done with this file when one row sets a status and one row is unauthorized. The feed is the update. The next block is a picture of the first row. Do not paste it. That row's fields are doc_id, fields, and op. A later row adds a document. Read that row in the file. Do not copy it onto a page.

```text
{"doc_id": "crit-endo-v4", "fields": {"effective": "2027-01-26", "status": "in_force", "supersedes": "crit-endo-v3"}, "op": "replace"}
```

5. [retrieve.jsonl](packet/release/slices/retrieve.jsonl). Search for `dev-hours`. You are done with this file when you see three question rows and none of them has an answer. The next block is a picture of the first row. Do not paste it. That row's fields are asker, case_date, question_id, site, and text. A later row can also have specialty and started.

```text
{"asker": "patient", "case_date": "2027-01-26", "question_id": "dev-hours", "site": "cluster", "text": "When do the public evening clinics close?"}
```

6. [dms.yaml](packet/release/openapi/dms.yaml). Search for `searchDocuments`. You are done with this file when the page says a hit is not a citation. Drafts are searchable. `readChangeFeed` reads `document.changed` events since the snapshot.
7. [service-catalog.json](packet/release/catalog/service-catalog.json). Search for `clinic`. You are done with this file when the endo row is visible. The fields on that row are clinic, code, and prep.
8. [prep.json](packet/release/photos/prep.json). Search for `export`. You are done with this file when `export` and `transcription` are both fields. Do not copy the transcription onto a page. The demo does not print it.
9. [circ-ramadan.md](packet/release/dms/circ-ramadan.md). Search for `public`. You are done with this file when audience is `public` and status is `in_force`.
10. [crit-endo-v3.md](packet/release/dms/crit-endo-v3.md). Search for `in_force`. You are done with this file when status is `in_force`.
11. [crit-endo-v4.md](packet/release/dms/crit-endo-v4.md). Search for `draft`. You are done with this file when status is `draft`. This page is the snapshot. The feed is what changes it.
12. [crit-ophth-v3.md](packet/release/dms/crit-ophth-v3.md). Search for `in_force`. You are done with this file when status is `in_force`.
13. [crit-ophth-v4.md](packet/release/dms/crit-ophth-v4.md). Search for `draft`. You are done with this file when status is `draft`.
14. [crit-card-v3.md](packet/release/dms/crit-card-v3.md). Search for `in_force`. You are done with this file when status is `in_force`.
15. [crit-card-v4.md](packet/release/dms/crit-card-v4.md). Search for `draft`. You are done with this file when status is `draft`.
16. [crit-neuro-v3.md](packet/release/dms/crit-neuro-v3.md). Search for `neuro`. You are done with this file when status is `in_force`. The notice in item 2 does not name this specialty.
17. [crit-neuro-v4.md](packet/release/dms/crit-neuro-v4.md). Search for `draft`. You are done with this file when status is `draft`. The feed does not have to promote every v4.
18. [leaflet-prep.md](packet/release/dms/leaflet-prep.md). Search for `in_force`. You are done with this file when status is `in_force` and audience is `public`.
19. [leaflet-prep-old.md](packet/release/dms/leaflet-prep-old.md). Search for `in_force`. You are done with this file when status is `in_force`. This page and the snapshot are the store before the feed. Both leaflets are in force there. Open [changes.jsonl](packet/release/feed/changes.jsonl) and search for `leaflet-prep-old`. That row sets status `superseded` and sunset `2027-01-26`. The demo's last line is that result. The two titles are the pair. Do not copy them.
20. [leaflet-staff.md](packet/release/dms/leaflet-staff.md). Search for `staff`. You are done with this file when audience is `staff`.
21. [pol-booking-cluster.md](packet/release/dms/pol-booking-cluster.md). Search for `cluster`. You are done with this file when site is `cluster`.
22. [pol-booking-h-safra.md](packet/release/dms/pol-booking-h-safra.md). Search for `h-safra`. You are done with this file when site is `h-safra`.
23. [pol-safety.md](packet/release/dms/pol-safety.md). Search for `restricted`. You are done with this file when audience is `restricted`.

On items 18 and 19, read status and audience. Do not copy a title or a body line from those two files onto a page. The demo prints the titles.

## Run the demo

The build in chapter 01 left a terminal inside `problem_simulation`. Stay in that window for this command. If you closed it, open a terminal in the course folder, run `cd problem_simulation`, and then the python line. If that window is already inside `problem_simulation`, skip the `cd` line.

```text
cd problem_simulation
python -m alwaha.demo.duplicate --profile practice
```

That block is a command, not a picture.

## You should now see

Two titles, then this line:

```text
one is superseded
```

You should see two titles, then the line above. The demo does not print the watermark. It does not print the clause that tells the two leaflets apart. Do not copy the titles onto a page. If the command says `Build rel-m03-l03 first.`, go back to chapter 01 and run the build, then run the demo again.

## What you are deciding

The index has to cite an in-force document the asker is allowed to see. Module 1, Lesson 3 already used the criteria that was in force on the referral's start day. v4 was a draft then. Today's feed promotes v4 for endo, ophth, and card. A referral whose start day is before that window keeps v3. Neuro is not on the notice. The unauthorized circular is not a citation. A patient does not see a staff document. The markdown status is the snapshot. The feed is the update. Those decisions are the sprint, the code, and the pages in the later chapters. You do not run a check from this page.

This page is done when item 23 is done and the demo printed two titles and then `one is superseded`.

Next: [04 — Words](04-words.md).
