# 09 — The pages

[Chapter 08](08-the-endpoint.md) ran the suite. This chapter writes the three pages the check reads besides the sprint and the knowledge file. The check runs in chapter 10. Do not run it from this page.

This page has three blocks to paste, in this order. Each heading starts with Replace. There is no picture to paste on this page. The headings inside a paste block belong to the file you are writing. They are not extra chapters.

1. [zones.md](work/zones.md), under Replace the zone page
2. [operators.md](work/operators.md), under Replace the operator steps
3. [deployment.md](work/deployment.md), under Replace the deployment note

The work path must contain `Student_Copy\work`. If the path contains `packet`, close it and open the work copy. For each of those three files, use the same four steps:

1. Open the work file named in that section. Do not open the template in `packet/templates` for the paste.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside that section's block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it.
4. Paste. Save. Keep every pipe character on a table. If the paste lands as one long line, or a column is missing, select the whole file, delete it, and paste again. Do not repair a table by hand.

## Why a section says what it says

Open these. You do not edit them, and you do not paste them into `work/`.

1. [guide.md](packet/release/endpoint/guide.md). The URL, the namespace `ns-team`, the model `local-small`, and `zone-private` are in that file. Chapter 09 cites `endpoint/guide.md`.
2. [pol-deploy.md](packet/release/standards/pol-deploy.md). Search for `non-root`. The deployment note uses that word. It does not say the container runs as root.
3. [starter.md](packet/release/dashboard/starter.md). Search for `request rate`. Search f. Monitoring at this stage is those three rates. The rest waits.
4. [zones.md](packet/kickoff/world/zones.md). Search for `zone-private`. The URL sits there. `ext-large` sits in `zone-public`.
5. [admit.py](work/app/admit.py). Search for `root`. You should see `rejected` on that line. That word stays in the admission code. That is expected. It does not go on the deployment page as a claim that the container runs as root.

The demo printed `root image: rejected` and `registered image: accepted`. Those lines did not say `non-root`. This page is where you label that result.

## Replace the zone page

Chapter 01 copied [zones.md](packet/templates/zones.md) to [work/zones.md](work/zones.md). The full path is `Module 02/Lesson 04/Student_Copy/work/zones.md`. Use the four steps at the top of this page on that work file. Do not type into the empty cells. This block replaces the whole file. It does not replace the template in `packet/templates`.

The columns are `surface` and `zone`. The surface cell is `url`. The zone cell is `zone-private`. Leave both pipes on each row.

```text
# Zones

| surface | zone |
| --- | --- |
| url | zone-private |
```

Read the file back. You should see a header row `surface` and `zone`, then one data row. The surface cell is `url`. The zone cell is `zone-private`. The check says the url is not in zone-private when that row is missing or the cells are swapped. It does not name a second surface.

## Replace the operator steps

This block replaces [work/operators.md](work/operators.md). It does not replace [packet/templates/operators.md](packet/templates/operators.md). Use the four steps at the top of this page. The full path is `Module 02/Lesson 04/Student_Copy/work/operators.md`.

The steps tell someone to read the health probe with the prod credential.

```text
# Operator steps

## Steps

Read the health probe. Use the prod credential for the private endpoint.
```

Read the file back. You should see `health`. You should see `prod`. The check says the operator steps are missing when either word is absent. It does not name a command.

## Replace the deployment note

This block replaces [work/deployment.md](work/deployment.md). It does not replace [packet/templates/deployment.md](packet/templates/deployment.md). Use the four steps at the top of this page. The full path is `Module 02/Lesson 04/Student_Copy/work/deployment.md`.

The headings are URL, Zone, Probe, Credentials, Monitoring, Boundary, and Operator steps. The URL is the address in the endpoint guide. The zone is `zone-private`. The probe reports the registered hash for `local-small`, and the container user is `non-root`. Dev and prod stay in their own files. Monitoring names request rate, error rate, and model latency, and it says the rest waits until Module 2. Boundary says a clinician assigns clinical urgency, and PHI stays off `ext-large`. The note cites `ciso` and `endpoint/guide.md`, and it names `pol-deploy`.

Do not add the sentence "The container runs as root." The admission code may still contain the word `root` on the line that rejects that account. That is expected. This page says `non-root`.

```text
# Deployment

Cited from ciso and from endpoint/guide.md. The checklist is pol-deploy.

## URL

https://assistant.site-a.alwaha.internal

## Zone

The URL is in zone-private.

## Probe

GET /v1/health reports the registered hash for local-small. The container user is non-root.

## Credentials

Dev and prod credentials differ. Dev stays in dev. Prod stays in prod.

## Monitoring

Request rate, error rate, and model latency. The rest of the operations stack waits until Module 2.

## Boundary

A clinician assigns clinical urgency. PHI stays off ext-large.

## Operator steps

Read the health probe with the prod credential.
```

Read the file back. You should see the seven headings. You should see the URL, `zone-private`, `local-small`, `hash`, `non-root`, `dev`, `prod`, `pol-deploy`, and `endpoint/guide.md`. Under Monitoring you should see `Module 2`. Under Boundary you should see `clinician`, `urgency`, and `ext-large`. You should not see the sentence "The container runs as root."

The check says the deployment note is missing a required fact when too many of those pieces are absent. It does not name which piece. The inputs are the URL, `zone-private`, `local-small`, the word hash, dev, prod, non-root, `pol-deploy`, a citation such as `endpoint/guide.md`, and Module 2 under Monitoring. It says the deployment note does not leave urgency with a clinician when Boundary is missing `clinician` or `urgency`. It says the deployment note does not keep patient data off the external model when Boundary is missing `ext-large`. It says the deployment note does not cite a source when `ciso`, `pol-deploy`, and `endpoint/guide.md` are all absent. It says the deployment note contains a banned sentence when the page says the container runs as root.

This page is done when `work/zones.md` has the row `url` and `zone-private`, `work/operators.md` has `health` and `prod`, and `work/deployment.md` has the seven headings. Do not run the check from this page.

Next: [10 — Finish](10-finish.md).
