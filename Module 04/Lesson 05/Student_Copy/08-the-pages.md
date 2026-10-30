# 08 — The pages

[Chapter 07](07-the-proposal.md) ran the suite. The suite does not read these pages. This chapter replaces seven files, in this order. Finish one before you start the next. If you are lost, stay on the Replace heading you have open. Finish it. Then do the next Replace heading.

1. [architecture-deploy.md](work/architecture-deploy.md), under Replace the deployment architecture
2. [operations.md](work/operations.md), under Replace the operations plan
3. [proposal.md](work/rcp/proposal.md), under Replace the proposal
4. [readout.md](work/readout.md), under Replace the readout
5. [retro.md](work/retro.md), under Replace the retro
6. [access-mgr.notes.md](work/interviews/access-mgr.notes.md), under Replace the access manager notes
7. [ea.notes.md](work/interviews/ea.notes.md), under Replace the enterprise architect notes

Scroll to the heading Replace the deployment architecture. That is the first paste on this page. There is no picture above it. Finish that heading, then the next heading that starts with Replace. Do not go back up the page.

There is no picture of a shell on this page. Chapter 01 copied the blanks. Do not type into the empty lines. Each block replaces the whole work file. It does not replace the template in `packet/templates`, and it does not replace the blank notes in `packet/interviews`. The packet path is the wrong file. The work path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`.

The two notes are tables. Keep the pipes. A preview can drop the pipe characters. Open this `.md` file before you copy. The other pages on this chapter are not pipe tables. The question files are not replaced.

The checks run in chapter 09. Do not run one from this page.

## Replace the deployment architecture

This block replaces [work/architecture-deploy.md](work/architecture-deploy.md). The full path is `Module 04/Lesson 05/Student_Copy/work/architecture-deploy.md`. It does not replace a Python file.

1. Open the work file named here, [work/architecture-deploy.md](work/architecture-deploy.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `zone-private`, then `cc`, then `clinician`.

The headings Zones, Flows, and Boundary inside the block are part of this file. Paste the whole block in one copy. They are not three more pastes.

```text
# Deployment architecture

## Zones

zone-private holds the assistant on site-a and site-b. zone-hospital holds int-engine. zone-public is the path to ext-large.

## Flows

cc receives the handoff. bi is the warehouse feed. hr sends leave. The bus carries session.cancelled.

## Boundary

A clinician assigns urgency. The assistant routes emergency wording to a human.
```

The headings Zones, Flows, and Boundary were inside the block. They are not the next step.

Open [work/architecture-deploy.md](work/architecture-deploy.md). Zones names zone-private, zone-hospital, and zone-public. Flows names cc, bi, hr, and the bus. Boundary names a clinician and urgency.

Stay on this page. The next heading is Replace the operations plan.

## Replace the operations plan

This block replaces [work/operations.md](work/operations.md). The full path is `Module 04/Lesson 05/Student_Copy/work/operations.md`. It does not replace [gates.py](work/app/gates.py).

1. Open the work file named here, [work/operations.md](work/operations.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `med-dir`, then `G4`, then `checklist`.

The headings Owners, RACI, Gate, and Incident inside the block are part of this file. They are not four more pastes.

```text
# Operations

## Owners

The architect owns the deployment architecture. The application engineer owns the handoff. The lead presents.

## RACI

The clinical safety owner is med-dir.

## Gate

G4 is go-live. The go-live checklist is the evidence.

## Incident

The Lesson 2 replay is the incident path. Dashboards cover latency, errors, and tool failures.
```

The headings Owners, RACI, Gate, and Incident were inside the block. They are not the next step.

Open [work/operations.md](work/operations.md). RACI names med-dir. Gate names G4 and the checklist. Owners and Incident each have a line.

Stay on this page. The next heading is Replace the proposal.

## Replace the proposal

This block replaces [work/rcp/proposal.md](work/rcp/proposal.md). The full path is `Module 04/Lesson 05/Student_Copy/work/rcp/proposal.md`. The file is inside the folder `rcp`. It is not `work/proposal.md`. If you see `proposal.md` next to `sprint.md`, that is the wrong file. Close it without saving. This block does not replace [rank.py](work/app/rank.py). The Metrics section does not contain the digits 70.

1. Open the work file named here, [work/rcp/proposal.md](work/rcp/proposal.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `Al-Waha`, then `not the value model`, then `p-clock`, then `same calls`, then `site-b`, then `phone-only`.

The headings Client, Ranking, Roadmap, Plan, Metrics, and Adoption inside the block are part of this file. They are not six more pastes.

```text
# Proposal

## Client

The client is Al-Waha.

## Ranking

The dot-vote ranks p-triage first. That ranking is not the value model. p-clock is a defensible first problem. p-waitlist depends on identity.

## Roadmap

The first build is p-clock. The route is rent.

## Plan

The vendor saving and the contact-center saving count the same calls. Procurement stays on the rent route.

## Metrics

site-b served after the drill. p-status is a measured contact-center demand.

## Adoption

The readiness survey names phone-only patients. phc-rim skews to that group. The channel is a phone callback.
```

The headings Client, Ranking, Roadmap, Plan, Metrics, and Adoption were inside the block. They are not the next step.

Open [work/rcp/proposal.md](work/rcp/proposal.md). The path contains `rcp`. Client names Al-Waha. Ranking says the dot-vote is not the value model. Roadmap starts with p-clock. Plan says the two savings count the same calls. Metrics names site-b. Adoption names phone-only and phc-rim.

Stay on this page. The next heading is Replace the readout.

## Replace the readout

This block replaces [work/readout.md](work/readout.md). The full path is `Module 04/Lesson 05/Student_Copy/work/readout.md`.

1. Open the work file named here, [work/readout.md](work/readout.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `p-clock`, then `summary`, then `session.cancelled`, then `same calls`, then `phone-only`, then `access-mgr`.

The headings Ranking, Handoff, Leave, Benefit, Channel, and Asks inside the block are part of this file. They are not six more pastes.

```text
# Readout

## Ranking

p-clock is first. p-waitlist depends on identity.

## Handoff

A handoff needs a summary.

## Leave

Consultant leave creates session.cancelled.

## Benefit

The vendor saving and the contact-center saving count the same calls.

## Channel

The readiness survey names phone-only patients. phc-rim skews phone-only.

## Asks

access-mgr holds the handoff. finance asks which benefit is counted twice. A clinician assigns clinical urgency. Patient data stays off ext-large.
```

The headings Ranking, Handoff, Leave, Benefit, Channel, and Asks were inside the block. They are not the next step.

Open [work/readout.md](work/readout.md). Ranking names p-clock. Handoff says a handoff needs a summary. Leave names session.cancelled. Benefit says the same calls. Channel names phone-only. Asks names access-mgr.

Stay on this page. The next heading is Replace the retro.

## Replace the retro

This block replaces [work/retro.md](work/retro.md). The full path is `Module 04/Lesson 05/Student_Copy/work/retro.md`.

1. Open the work file named here, [work/retro.md](work/retro.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `summary`, then `triage`, then `phone-only`.

The headings Keep, Drop, and Open inside the block are part of this file. They are not three more pastes.

```text
# Retro

## Keep

A summary on every handoff.

## Drop

A roadmap that starts with triage.

## Open

A phone callback for phone-only patients at phc-rim.
```

The headings Keep, Drop, and Open were inside the block. They are not the next step.

Open [work/retro.md](work/retro.md). Keep names a summary. Drop names triage. The Open section names phone-only.

Stay on this page. The next heading is Replace the access manager notes.

## Replace the access manager notes

This block replaces [work/interviews/access-mgr.notes.md](work/interviews/access-mgr.notes.md). The full path is `Module 04/Lesson 05/Student_Copy/work/interviews/access-mgr.notes.md`. It does not replace [access-mgr.questions.txt](work/interviews/access-mgr.questions.txt). The question file is not the graded note.

1. Open the work file named here, [work/interviews/access-mgr.notes.md](work/interviews/access-mgr.notes.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `summary`.

This note is a table. Keep the pipes. If the pipes are gone, you pasted from a preview. Paste this block again from the chapter file. The heading inside the block is part of the note. It is not the next step.

```text
# access-mgr

| Who | Their words | Kind |
| --- | --- | --- |
| access-mgr | A handoff with no summary is not a handoff. | fact |
```

Open [work/interviews/access-mgr.notes.md](work/interviews/access-mgr.notes.md). You should see the summary. The pipes are still there.

Stay on this page. The next heading is Replace the enterprise architect notes.

## Replace the enterprise architect notes

This block replaces [work/interviews/ea.notes.md](work/interviews/ea.notes.md). The full path is `Module 04/Lesson 05/Student_Copy/work/interviews/ea.notes.md`. It does not replace [ea.questions.txt](work/interviews/ea.questions.txt). The question file is not the graded note.

1. Open the work file named here, [work/interviews/ea.notes.md](work/interviews/ea.notes.md). The path contains `Student_Copy\work`. On macOS it shows as `Student_Copy/work`. If the path contains `packet`, close it and open the work copy.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy from this chapter file, not from a preview. A preview can drop indentation, and it can drop the pipe characters in a table. Open the `.md` file, then copy. To open it, Ctrl+click the link on Windows or Command+click it on macOS. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. If the editor offers a styled paste, use Paste Without Formatting.
4. Paste. Save. Search the saved work file, not this chapter. Ctrl+F on Windows, Command+F on macOS. Look for `leave`, then `session.cancelled`, then `bi`.

This note is a table. Keep the pipes. If the pipes are gone, you pasted from a preview. Paste this block again from the chapter file. The heading inside the block is part of the note. It is not the next step.

```text
# ea

| Who | Their words | Kind |
| --- | --- | --- |
| ea | Leave is entered after the session is published. That leave creates session.cancelled. | fact |
| ea | The warehouse feed is the bi mart. | fact |
```

Open [work/interviews/ea.notes.md](work/interviews/ea.notes.md). You should see leave, `session.cancelled`, and bi. The pipes are still there.

Stay on this page. That was the last paste on this page. The line that starts with Next is the end of this page.

This page is done when the deployment architecture has Zones, Flows, and Boundary, the operations plan has Owners, RACI, Gate, and Incident, the proposal has Client, Ranking, Roadmap, Plan, Metrics, and Adoption, the readout has Ranking, Handoff, Leave, Benefit, Channel, and Asks, the retro has Keep, Drop, and Open, and both notes keep their pipes. Do not run a check from this page.

Next: [09 — Finish](09-finish.md).
