# 08 — The pages

[Chapter 07](07-the-hours.md) ran the suite. The suite does not read these pages. This chapter replaces five files, in this order. Finish one before you start the next. If you are lost, stay on the Replace heading you have open. Finish it. Then do the next Replace heading.

1. [timeline.md](work/timeline.md), under Replace the timeline
2. [dashboard.md](work/dashboard.md), under Replace the dashboard page
3. [runbook.md](work/runbook.md), under Replace the runbook
4. [ciso.notes.md](work/interviews/ciso.notes.md), under Replace the CISO notes
5. [patient-rep.notes.md](work/interviews/patient-rep.notes.md), under Replace the patient-rep notes

Scroll to the heading Replace the timeline. That is the first paste on this page. There is no picture above it. Finish that heading, then the next heading that starts with Replace. Do not go back up the page.

There is no picture of a shell on this page. Chapter 01 copied the blanks. Do not type into the empty lines. Each block replaces the whole work file. It does not replace the template in `packet/templates`, and it does not replace the blank notes in `packet/interviews`. The packet path is the wrong file. The work path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`.

The two notes are tables. Keep the pipes. A preview can drop the pipe characters. Open this `.md` file before you copy.

## Replace the timeline

This block replaces [work/timeline.md](work/timeline.md). The full path is `Module 04/Lesson 02/Student_Copy/work/timeline.md`. The two times are the ones you found in [spans.jsonl](packet/release/replay/spans.jsonl): the first `referral.status` error, and the alert.

1. Open the work file named here, [work/timeline.md](work/timeline.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `referral.status`.

```text
# Timeline

The replay's first referral.status error is at 2027-02-01T09:12:00+03:00.
The alert fires at 2027-02-01T09:15:00+03:00.
```

Open [work/timeline.md](work/timeline.md). You should see `referral.status` and both times. Stay on this page. The next heading is Replace the dashboard page.

## Replace the dashboard page

This block replaces [work/dashboard.md](work/dashboard.md). The full path is `Module 04/Lesson 02/Student_Copy/work/dashboard.md`. It does not replace [dashboard.py](work/app/dashboard.py). That module was pasted in chapter 06. This page is the note the incident check reads.

1. Open the work file named here, [work/dashboard.md](work/dashboard.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Latency`.

```text
# Dashboard

Latency, errors, and tool failures. CPU stays flat through the replay.
```

Open [work/dashboard.md](work/dashboard.md). You should see `Latency`, `errors`, and `tool failures`. You should also see `CPU stays flat`. That sentence is expected on this page. It records that CPU stayed flat while the board itself is latency, errors, and tool failures. The shell sentence `A board that only has CPU` belongs in the old `dashboard.py`, and that sentence must already be gone from the module. Stay on this page. The next heading is Replace the runbook.

## Replace the runbook

This block replaces [work/runbook.md](work/runbook.md). The full path is `Module 04/Lesson 02/Student_Copy/work/runbook.md`. Keep the seven headings. It does not replace the blank template in `packet/templates`.

1. Open the work file named here, [work/runbook.md](work/runbook.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Detect`.

```text
# tpl-runbook

## Detect

The alert span in the replay is the detection.

## Scope

referral.status failed while CPU stayed flat.

## Impact

The patient reply stays the registered pending reply.

## Timeline

The alert fires at 2027-02-01T09:15:00+03:00.

## Owner

The lead owns the timeline.

## Cache

document.changed for circ-ramadan-hours drops the cached hours.

## Shadow

shadow-extract needs a comparison before promotion.
```

Open [work/runbook.md](work/runbook.md). You should see `Detect`, `Scope`, `Impact`, `Timeline`, `Owner`, `Cache`, and `Shadow`, each with a sentence under it. Detect names the alert. Scope names `referral.status` and a flat CPU. Impact keeps the registered pending reply. Timeline uses the alert time. Owner is the lead. Cache names `document.changed` and `circ-ramadan-hours`. Shadow names `shadow-extract` and a comparison before promotion. Stay on this page. The next heading is Replace the CISO notes.

## Replace the CISO notes

This block replaces [work/interviews/ciso.notes.md](work/interviews/ciso.notes.md). The full path is `Module 04/Lesson 02/Student_Copy/work/interviews/ciso.notes.md`. It does not replace [ciso.questions.txt](work/interviews/ciso.questions.txt). The question file is not the graded note. Keep the pipes.

1. Open the work file named here, [work/interviews/ciso.notes.md](work/interviews/ciso.notes.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `replay`.

```text
# ciso

| Who | Their words | Kind |
| --- | --- | --- |
| ciso | The incident replay already contains the alert. Do not add a new bug. | fact |
| ciso | A CPU dashboard misses the tool failures. | fact |
```

Open [work/interviews/ciso.notes.md](work/interviews/ciso.notes.md). You should see `replay`, `alert`, `CPU`, and `dashboard`. You should see the pipe characters. If the pipes are missing, you copied from a preview. Paste this block again from this chapter file. Stay on this page. The next heading is Replace the patient-rep notes.

## Replace the patient-rep notes

This block replaces [work/interviews/patient-rep.notes.md](work/interviews/patient-rep.notes.md). The full path is `Module 04/Lesson 02/Student_Copy/work/interviews/patient-rep.notes.md`. It does not replace [patient-rep.questions.txt](work/interviews/patient-rep.questions.txt). The question file is not the graded note. Keep the pipes.

1. Open the work file named here, [work/interviews/patient-rep.notes.md](work/interviews/patient-rep.notes.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `evening`.

```text
# patient-rep

| Who | Their words | Kind |
| --- | --- | --- |
| patient-rep | The phone line is the door most families still use. | fact |
| patient-rep | She is still offered the old evening close after the circular. | fact |
```

Open [work/interviews/patient-rep.notes.md](work/interviews/patient-rep.notes.md). You should see `evening` and `circular`. You should see the pipe characters. If the pipes are missing, paste this block again from this chapter file. That was the last paste on this page.

This page is done when the timeline names `referral.status` and both times, the dashboard page names latency, errors, and tool failures, the runbook has all seven headings filled, and both notes keep their pipes. Do not run a check from this page.

Next: [09 — Finish](09-finish.md).
