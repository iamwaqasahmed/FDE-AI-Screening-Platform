# 09 — The pages

[Chapter 08](08-the-fair.md) ran the suite. This chapter replaces the pages. There is no picture of a shell on this page, and there is no Python. The packet templates stay blank. The question file is copied and not replaced.

You replace five files, in this order. Finish one before you start the next. If you are lost, stay on the Replace heading you have open. Finish it. Then do the next Replace heading.

1. [guardrails.json](work/guardrails.json), under Replace the guardrails
2. [dpia.md](work/dpia.md), under Replace the DPIA
3. [requests.md](work/requests.md), under Replace the requests
4. [breach.md](work/breach.md), under Replace the breach note
5. [ciso.notes.md](work/interviews/ciso.notes.md), under Replace the CISO notes

The checks run in chapter 10. Do not run them from this page. The question file is not on this list. Do not replace it.

`guardrails.json` is JSON. A styled paste can drop a comma or a quote. Copy from this chapter file, not from a preview. If a later command shows a JSON error, paste this chapter's guardrails block again. Do not repair the commas by hand. If you run `prepare_work.py` again, it puts the blank pages back, and it puts the shell tests back. You would then paste chapters 05 through 09 again.

The CISO notes are a table. Keep the pipes. A preview can drop them.

## Replace the guardrails

This block replaces [work/guardrails.json](work/guardrails.json). The full path is `Week 04/Day 01/Student_Copy/work/guardrails.json`. It does not replace the template in `packet/templates`. The dev file contains `atk-direct` and does not contain `atk-prompt`. This page is a different file. It lists `atk-prompt`. A families list that is only `atk-direct` misses a family.

1. Open the work file named here, [work/guardrails.json](work/guardrails.json). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `atk-prompt`.

```text
{
  "checklist": [
    "non-root",
    "health-probe",
    "resource-limits",
    "no-phi-in-logs",
    "image-provenance",
    "registered-model-hash"
  ],
  "families": [
    "atk-direct",
    "atk-indirect",
    "atk-disclose",
    "atk-supply",
    "atk-poison",
    "atk-output",
    "atk-agency",
    "atk-prompt",
    "atk-embed",
    "atk-misinfo",
    "atk-tokens",
    "atk-hoard"
  ]
}
```

Open [work/guardrails.json](work/guardrails.json). You should see `atk-prompt` and `non-root`. You should not see an empty families list. The checklist has six ids. The families list has twelve names. Stay on this page. The next heading is Replace the DPIA.

## Replace the DPIA

This block replaces [work/dpia.md](work/dpia.md). The full path is `Week 04/Day 01/Student_Copy/work/dpia.md`. It does not replace the template in `packet/templates`. Keep the headings. Purpose is the patient access assistant. Residency keeps PHI off `ext-large`. The risk tier is G1. Stores cover the row, memory, the index, and the logs. The breach clock starts at the notice, not at a model. This block has no pipe table.

1. Open the work file named here, [work/dpia.md](work/dpia.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `ext-large`.

```text
# tpl-dpia

## Purpose

The patient access assistant handles referrals and bookings. A clinician assigns urgency.

## Residency

PHI stays off ext-large. Training stays on the private cloud.

## Risk tier

G1 is the risk tier. G2 is this DPIA.

## Stores

Deletion covers the row, memory, the index, and the logs.

## Breach clock

The clock starts at the rel-w4d1 notice, 2027-01-31T08:00:00+03:00. The log is int-engine. The notice does not name a model.
```

Open [work/dpia.md](work/dpia.md). You should see `patient access assistant`, `ext-large`, `G1`, the four stores, and `int-engine`. The five headings are still there. Stay on this page. The next heading is Replace the requests.

## Replace the requests

This block replaces [work/requests.md](work/requests.md). The full path is `Week 04/Day 01/Student_Copy/work/requests.md`. It does not replace the template in `packet/templates`. Access and deletion name the same four stores. The reply says the records are removed and no slot was booked from the letter. This block has no pipe table.

1. Open the work file named here, [work/requests.md](work/requests.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `removed`.

```text
# Requests

## Access

person-access is in the row, memory, the index, and the logs.

## Deletion

person-access is removed from the row, memory, the index, and the logs.

## Reply

The records for this request are removed. No slot was booked from the letter.
```

Open [work/requests.md](work/requests.md). You should see `row`, `memory`, `index`, and `logs` under Access and again under Deletion. You should see `removed` and `letter` under Reply. Stay on this page. The next heading is Replace the breach note.

## Replace the breach note

This block replaces [work/breach.md](work/breach.md). The full path is `Week 04/Day 01/Student_Copy/work/breach.md`. It does not replace the template in `packet/templates`. It cites [phi-logs.md](packet/release/notices/phi-logs.md). Read the timestamp and the change id from that notice. Do not invent them. The clock starts at the notice, not at a model. This block has no pipe table.

1. Open the work file named here, [work/breach.md](work/breach.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `int-engine`.

```text
# Breach

The clock starts at 2027-01-31T08:00:00+03:00 on the rel-w4d1 notice. The log is int-engine since CHG-2025-118. The notice does not name a model. The report is due 72 hours after that timestamp.
```

Open [work/breach.md](work/breach.md). You should see the timestamp from the notice, `int-engine`, the change id from the notice, and `72`. You should not see a sentence that starts the clock at a model. Stay on this page. The next heading is Replace the CISO notes.

## Replace the CISO notes

This block replaces [work/interviews/ciso.notes.md](work/interviews/ciso.notes.md). The full path is `Week 04/Day 01/Student_Copy/work/interviews/ciso.notes.md`. It does not replace [ciso.questions.txt](work/interviews/ciso.questions.txt). The question file stays as chapter 01 copied it. The notes name the go-live checklist and the integration-engine log. Keep the pipes.

1. Open the work file named here, [work/interviews/ciso.notes.md](work/interviews/ciso.notes.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `integration-engine`.

```text
# ciso

| Who | Their words | Kind |
| --- | --- | --- |
| ciso | The go-live checklist is the list the security office will use at gate G4. | fact |
| ciso | Patient data has been in the integration-engine log since change CHG-2025-118. | fact |
```

Open [work/interviews/ciso.notes.md](work/interviews/ciso.notes.md). You should see `go-live checklist` and `integration-engine`. You should see the pipe characters in the header and in both fact rows. The question file is unchanged. That was the last paste on this page.

On Windows, a page sometimes saves with an extra `.txt`. In File Explorer, open View and tick File name extensions. If you see `.txt`, rename the file so the name ends in `.md` or `.json`.

This page is done when the guardrails list the families and the six checklist ids, the DPIA keeps the five headings and the sentences above, the requests name the four stores twice and the reply names the letter, the breach note cites the notice, and the CISO notes name the checklist and the integration-engine log. Do not run a check from this page.

Next: [10 — Finish](10-finish.md).
