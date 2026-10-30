# 09 — The readout

[Chapter 08](08-the-pages.md) filed the zone row, the operator steps, and the deployment note. This chapter replaces the readout and the retro. There is no picture to paste on this page.

You replace two files under `work/`, in this order:

1. [readout.md](work/readout.md), under Replace the readout
2. [retro.md](work/retro.md), under Replace the retro

Each work path must contain `Student_Copy\work`. On macOS that folder shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy. Leave the templates in `packet/templates` unchanged. Do not run a check from this page.

Scroll to the heading Replace the readout. The block under it is the first paste. The next Replace heading is Replace the retro. Use the four steps from [chapter 05](05-the-sprint.md). There is no picture on this page. Each paste replaces the whole file, including every heading inside the block. Those headings belong to the file.

Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting.

## Replace the readout

This block replaces [work/readout.md](work/readout.md). The full path is `Module 02/Lesson 05/Student_Copy/work/readout.md`. It does not replace [packet/templates/readout.md](packet/templates/readout.md). Open the work file. Select the whole file. Delete it. Copy the lines inside the block. Do not copy the backtick lines. Paste. Save. The headings inside the block belong to the file.

```text
# Readout

## Smoke

GET /v1/health on https://assistant.site-a.alwaha.internal reports the registered hash. Citation: endpoint/guide.md.

## Change

cr-ain is accepted and sequenced after the smoke test. Citation: notices/cr-ain.md.

## File

sched-ain is a nightly file in zone-hospital. Citation: systems/sched-ain.md.

## Patients

A patient at h-ain sees a queued booking. A clinician assigns clinical urgency.

## Monitoring

The starter dashboard shows request rate, error rate, and model latency. Stage 2 adds the rest in Module 2.

## Model

The endpoint serves local-small. The quota is the number in registry/quota.json. Citation: registry/quota.json.

## Asks

The nightly file path stays open until the first file lands. Patient data stays off ext-large.
```

Smoke needs `health` and `hash`. Change needs `cr-ain` and a sequence word. The word on this page is `sequenced`. File needs `nightly`, `sched-ain`, and `zone-hospital`. Patients needs `queued`. Monitoring needs `latency`, and `Stage 2`. This page has both. Model needs `local-small` and `quota`. The quota number stays in [quota.json](packet/m02-l04/registry/quota.json). Asks is not empty, and it keeps patient data off `ext-large`.

The note cites `endpoint/guide.md`, `notices/cr-ain.md`, `systems/sched-ain.md`, and `registry/quota.json`. A clinician still assigns clinical urgency.

Read the file back. You should see all seven headings. Under Patients you should see `queued`. The word `booked` is not required on this page. If you add a sentence that says Ain has a live slot, the readout check fails.

## Replace the retro

This block replaces [work/retro.md](work/retro.md). It does not replace [packet/templates/retro.md](packet/templates/retro.md). Use the same steps on the work file.

```text
# Retro

## Keep

The health probe and the separate prod credential.

## Drop

A promise that Ain can confirm a slot today.

## Open

The nightly file for sched-ain, and the Module 2 operations stack.
```

Keep, Drop, and Open each have text. Drop names a promise you are putting down. It does not say Ain has a live slot.

Read the file back. You should see all three headings with a sentence under each.

This page is done when `work/readout.md` has the seven headings and `work/retro.md` has Keep, Drop, and Open. Do not run the check from this page.

Next: [10 — Finish](10-finish.md).
