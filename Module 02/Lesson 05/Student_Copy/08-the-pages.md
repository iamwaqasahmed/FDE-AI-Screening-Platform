# 08 — The pages

[Chapter 07](07-the-contract.md) left the suite green. This chapter replaces three pages. There is no picture to paste on this page. The blocks under Replace are the pastes.

You replace three files under `work/`, in this order:

1. [zones.md](work/zones.md), under Replace the zone page
2. [operators.md](work/operators.md), under Replace the operator steps
3. [deployment.md](work/deployment.md), under Replace the deployment note

Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the templates in `packet/templates` unchanged. Do not run a check from this page.

Scroll to the heading Replace the zone page. The block under it is the first paste. Two more Replace headings follow it. Use the four steps from [chapter 05](05-the-sprint.md) on each one. There is no picture on this page. Every fenced block is a paste, and each paste replaces the whole file.

The zone table uses pipe characters. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. After you paste, you should still see a `|` at the start and end of each row. A row that has lost its pipes is no longer a table. Select the whole file, delete it, and paste that block again.

## Replace the zone page

This block replaces [work/zones.md](work/zones.md). The full path is `Module 02/Lesson 05/Student_Copy/work/zones.md`. It does not replace [packet/templates/zones.md](packet/templates/zones.md). Open the work file. Select the whole file. Delete it. Copy the lines inside the block. Do not copy the backtick lines. Paste. Save.

```text
# Zones

| surface | zone |
| --- | --- |
| url | zone-private |
| sched-ain | zone-hospital |
```

The columns are `surface` and `zone`. The URL row is `url` and `zone-private`. The file row is `sched-ain` and `zone-hospital`. [guide.md](packet/m02-l04/endpoint/guide.md) puts the URL in `zone-private`. [sched-ain.md](packet/release/systems/sched-ain.md) puts the file in `zone-hospital`.

Read the file back. You should see both rows, with the pipes still in place. The blank template can still have an empty row. That file is in `packet/templates`. That is expected.

## Replace the operator steps

This block replaces [work/operators.md](work/operators.md). It does not replace [packet/templates/operators.md](packet/templates/operators.md). Use the same steps on the work file.

```text
# Operator steps

## Steps

Read the health probe. Use the prod credential for the private endpoint.
```

The page needs the words `health` and `prod`. [guide.md](packet/m02-l04/endpoint/guide.md) names the probe. [prod.json](packet/m02-l04/credentials/prod.json) is the prod credential. You do not type the credential value.

Read the file back. You should see `health` and `prod` under Steps.

## Replace the deployment note

This block replaces [work/deployment.md](work/deployment.md). The full path is `Module 02/Lesson 05/Student_Copy/work/deployment.md`. It does not replace [packet/templates/deployment.md](packet/templates/deployment.md). Use the same steps on the work file. The headings inside the block belong to the file. They are not new chapters.

```text
# Deployment

Cited from ciso and from endpoint/guide.md. The checklist is pol-deploy. The change is notices/cr-ain.md. The file path is systems/sched-ain.md.

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

## Ain

h-ain is included through sched-ain. The interface is a nightly file in zone-hospital. A booking stays queued until that file arrives.

## Change

cr-ain is accepted and sequenced after the smoke test.
```

The previous lesson's headings are still there: URL, Zone, Probe, Credentials, Monitoring, Boundary, and Operator steps. Ain names `h-ain`, `sched-ain`, nightly, and `zone-hospital`. Change names `cr-ain` and sequences it after the smoke test. The word `hash` is on the Probe line. The page does not store the hash value. Read that value in [models.json](packet/m02-l04/registry/models.json) if you want to see it. The quota number stays in [quota.json](packet/m02-l04/registry/quota.json).

The note cites `ciso`, `endpoint/guide.md`, `pol-deploy`, `notices/cr-ain.md`, and `systems/sched-ain.md`. Leave those names on the page.

Read the file back. You should see `## Ain` and `## Change`. The sentence under Ain says a booking stays queued. The sentence under Change says `cr-ain` is sequenced after the smoke test. Do not add a sentence that says Ain has a live slot. Do not add a sentence that says monitoring is complete.

This page is done when `work/zones.md` has the rows `url` / `zone-private` and `sched-ain` / `zone-hospital`, `work/operators.md` has `health` and `prod`, and `work/deployment.md` has Ain and Change. Do not run the check from this page.

Next: [09 — The readout](09-the-readout.md).
