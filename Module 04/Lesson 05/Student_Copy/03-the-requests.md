# 03 — The requests

[Chapter 02](02-the-role.md) named the five parts. This chapter opens twenty files, in order, and then you run one demo and two interviews. You do not paste a file on this page. There is no heading on this page that starts with Replace.

The blocks under Read these files are pictures. They replace nothing. Do not paste them. A picture belongs to the numbered item above it. The next item starts with the next number. Some items have no picture. Those items say so. Do not look for a block under them.

A jsonl row is one long line. Word wrap can make that line look like several lines. It is still one row. A json file is still one file when it wraps.

Open each link with Ctrl+click on Windows or Command+click on macOS, so the file opens in the editor. Do not double-click the file in File Explorer. A double-click can open Excel or a browser, and the search below will not match what you see. To search, Ctrl+F on Windows or Command+F on macOS, inside the file named in that item. A search inside this chapter does not count. Do not type in a packet file. Close it when the item is done.

Stay on the list until item 20. Then run the demo, then the two interviews. Finish one item before you open the next number. If you are lost, you are on the item you have open. Finish that item.

## Read these files

1. Open [README.md](packet/release/README.md). Search for `connected`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing.

```text
# rel-m04-l05

From: Enterprise Architect
Case date: 2027-02-04

The contact center, the warehouse feed, and HR asked to be connected. Staff sign-in and the event bus are confirmed after the drill. The lesson notes are [Module 4, Lesson 5](home.md).

Files:

- [bus/events.jsonl](bus/events.jsonl)
- [cc/handoff.jsonl](cc/handoff.jsonl)
- [connect/requests.json](connect/requests.json)
- [gates/stage-gate.md](gates/stage-gate.md)
- [hr/leave.jsonl](hr/leave.jsonl)
- [iam/staff.json](iam/staff.json)
- [personal/attack.json](personal/attack.json)
- [raci/assistant.json](raci/assistant.json)
- [steering/steer-m04-l05.md](steering/steer-m04-l05.md)
- [survey/readiness.json](survey/readiness.json)
- [templates/architecture-deploy.md](templates/architecture-deploy.md)
- [templates/knowledge.md](templates/knowledge.md)
- [templates/operations.md](templates/operations.md)
- [templates/proposal.md](templates/proposal.md)
- [templates/readout.md](templates/readout.md)
- [templates/retro.md](templates/retro.md)
- [templates/sprint.md](templates/sprint.md)
- [value/model.json](value/model.json)
- [warehouse/feed.jsonl](warehouse/feed.jsonl)
```

That was a picture. Do not paste it. The day-notes link in that file does not open. It points inside this student copy. You do not need it. This chapter is the lesson.

This file is done when the search finds `connected` and you have read that the contact center, the warehouse feed, and HR asked to be connected. Close the file. The next item is number 2.

2. Open [requests.json](packet/release/connect/requests.json). Search for `cc`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A json file is still one file when it wraps.

```text
{
  "confirm": [
    "bus",
    "iam"
  ],
  "requests": [
    {
      "id": "cc",
      "kind": "handoff"
    },
    {
      "id": "bi",
      "kind": "warehouse"
    },
    {
      "id": "hr",
      "kind": "leave"
    }
  ]
}
```

That was a picture. Do not paste it. This file is done when the search finds `cc` and you have seen `bi` and `hr`. Close the file. The next item is number 3.

3. Open [staff.json](packet/release/iam/staff.json). Search for `staff`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A json file is still one file when it wraps.

```text
{
  "actors": [
    {
      "id": "coord-1",
      "kind": "staff",
      "role": "coordinator"
    },
    {
      "id": "svc-integration",
      "kind": "service",
      "role": "admin"
    }
  ]
}
```

That was a picture. Do not paste it. This file is done when the search finds `staff` and you have seen a service actor beside it. Close the file. The next item is number 4.

4. Open [events.jsonl](packet/release/bus/events.jsonl). Search for `evt-extra`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A row is one long line. Word wrap can make a row look like several lines. It is still one row.

```text
{"disposition": "kept", "id": "evt-extra", "session": "ses-2", "topic": "session.cancelled"}
{"id": "evt-cancel", "session": "ses-1", "topic": "session.cancelled"}
```

That was a picture. Do not paste it. This file is done when the search finds `evt-extra` and you have seen `session.cancelled` on both rows. The first row has a field the consumer does not have to know. Close the file. The next item is number 5.

5. Open [handoff.jsonl](packet/release/cc/handoff.jsonl). Search for `call-empty`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A row is one long line. Word wrap can make a row look like several lines. It is still one row.

```text
{"agent": "cc-1", "id": "call-status", "summary": "Referral status, still pending."}
{"agent": "cc-1", "id": "call-empty", "summary": ""}
```

That was a picture. Do not paste it. This file is done when the search finds `call-empty` and you have seen one summary and one empty summary. Close the file. The next item is number 6.

6. Open [leave.jsonl](packet/release/hr/leave.jsonl). Search for `published`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A row is one long line. Word wrap can make a row look like several lines. It is still one row. Do not write a minute count beside this row.

```text
{"consultant": "con-1", "entered_at": "2027-02-04T11:00:00", "id": "lv-1", "published_at": "2027-02-04T08:00:00", "session": "ses-9", "status": "published"}
```

That was a picture. Do not paste it. This file is done when the search finds `published` and you have seen that the entered time is after the published time. Do not write a minute count. Close the file. The next item is number 7.

7. Open [feed.jsonl](packet/release/warehouse/feed.jsonl). Search for `referred_at`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A row is one long line. Word wrap can make a row look like several lines. It is still one row.

```text
{"booking_date": "2027-01-20", "id": "wh-1", "referred_at": "2027-01-02"}
{"booking_date": "2027-01-18", "id": "wh-2", "referred_at": "2026-12-11"}
```

That was a picture. Do not paste it. This file is done when the search finds `referred_at` and you have seen `booking_date` on the same row. Close the file. The next item is number 8.

8. Open [model.json](packet/release/value/model.json). Search for `p-triage`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A json file is still one file when it wraps.

```text
{
  "method": "value",
  "problems": [
    {
      "blockers": [
        "pol-clinical-safety"
      ],
      "depends_on": [],
      "id": "p-triage"
    },
    {
      "blockers": [],
      "depends_on": [],
      "id": "p-clock"
    },
    {
      "blockers": [],
      "depends_on": [
        "identity"
      ],
      "id": "p-waitlist"
    },
    {
      "blockers": [],
      "depends_on": [
        "identity"
      ],
      "id": "p-dna"
    },
    {
      "blockers": [],
      "depends_on": [
        "identity"
      ],
      "id": "p-status"
    },
    {
      "blockers": [],
      "depends_on": [
        "criteria"
      ],
      "id": "p-bounce"
    },
    {
      "blockers": [],
      "depends_on": [],
      "id": "p-slots"
    },
    {
      "blockers": [],
      "depends_on": [],
      "id": "p-info"
    },
    {
      "blockers": [],
      "depends_on": [],
      "id": "p-forecast"
    }
  ]
}
```

That was a picture. Do not paste it. This file is done when the search finds `p-triage` and you have seen that `p-triage` has a blocker and `p-clock` does not. Close the file. The next item is number 9.

9. Open [readiness.json](packet/release/survey/readiness.json). Search for `phone-only`.

   The next block is a picture of that file. Do not paste it. This block replaces nothing. A json file is still one file when it wraps. Do not copy a count. This file does not hold one.

```text
{
  "patient_groups": [
    "app",
    "caregiver",
    "phone-only"
  ],
  "roles": [
    "coordinators",
    "contact-center",
    "phc-clerks"
  ],
  "skew": {
    "group": "phone-only",
    "site": "phc-rim"
  }
}
```

That was a picture. Do not paste it. This file is done when the search finds `phone-only` and you have seen `phc-rim`. Close the file. The next item is number 10.

10. Open [assistant.json](packet/release/raci/assistant.json). Search for `clinical-safety`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. A json file is still one file when it wraps.

```text
{
  "cells": [
    {
      "id": "clinical-safety",
      "owner": "",
      "role": "clinical safety"
    }
  ],
  "gate": "G4",
  "id": "go-live"
}
```

That was a picture. Do not paste it. This file is done when the search finds `clinical-safety` and you have seen an empty owner and gate `G4`. Close the file. The next item is number 11.

11. Open [stage-gate.md](packet/release/gates/stage-gate.md). Search for `G4`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. The heading inside the picture is the file's heading. It is not the next step.

```text
# pol-stage-gate

Six gates:

- G0 intake
- G1 risk tier
- G2 DPIA
- G3 pilot approval
- G4 go-live
- G5 post-launch review

G4 is go-live. The clinical safety owner agrees at this gate.
```

That was a picture. Do not paste it. This file is done when the search finds `G4` and you have read that G4 is go-live. Close the file. The next item is number 12.

12. Open [steer-m04-l05.md](packet/release/steering/steer-m04-l05.md). Search for `twice`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. The heading inside the picture is the file's heading. It is not the next step. Do not answer the questions on this page.

```text
# steer-m04-l05

The steering committee asks these questions. The committee is cdo, med-dir, dpo, ciso, and finance.

1. Which problem is first, and what does it depend on?
2. What does a contact-center handoff contain?
3. Which event does consultant leave create?
4. Which benefit is counted twice?
5. What channel reaches phone-only patients?
```

That was a picture. Do not paste it. This file is done when the search finds `twice` and you have read the five questions. Close the file. The next item is number 13.

13. Open [attack.json](packet/release/personal/attack.json). Search for `atk-direct`.

    There is no picture of this file. There is no block under this item. A picture would copy the attack text.

    This file is done when the search finds `atk-direct`. Do not copy the text. Close the file. The next item is number 14.

14. Open [architecture-deploy.md](packet/release/templates/architecture-deploy.md). Search for `Zones`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. The headings inside the picture are the file's headings. They are not the next step. After the picture, the next item is number 15.

```text
# Deployment architecture

## Zones

## Flows

## Boundary
```

That was a picture. Do not paste it. This file is done when the search finds `Zones` and you have seen Flows and Boundary. Close the file. The next item is number 15.

15. Open [operations.md](packet/release/templates/operations.md). Search for `Owners`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. The headings inside the picture are the file's headings. They are not the next step.

```text
# Operations

## Owners

## RACI

## Gate

## Incident
```

That was a picture. Do not paste it. This file is done when the search finds `Owners` and you have seen RACI, Gate, and Incident. Close the file. The next item is number 16.

16. Open [proposal.md](packet/release/templates/proposal.md). Search for `Client`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. The headings inside the picture are the file's headings. They are not the next step.

```text
# Proposal

## Client

## Ranking

## Roadmap

## Plan

## Metrics

## Adoption
```

That was a picture. Do not paste it. This file is done when the search finds `Client` and you have seen Ranking, Roadmap, Plan, Metrics, and Adoption. Close the file. The next item is number 17.

17. Open [readout.md](packet/release/templates/readout.md). Search for `Ranking`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. The headings inside the picture are the file's headings. They are not the next step.

```text
# Readout

## Ranking

## Handoff

## Leave

## Benefit

## Channel

## Asks
```

That was a picture. Do not paste it. This file is done when the search finds `Ranking` and you have seen Handoff, Leave, Benefit, Channel, and Asks. Close the file. The next item is number 18.

18. Open [retro.md](packet/release/templates/retro.md). Search for `Keep`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. The headings inside the picture are the file's headings. They are not the next step.

```text
# Retro

## Keep

## Drop

## Open
```

That was a picture. Do not paste it. This file is done when the search finds `Keep` and you have seen Drop and Open. Close the file. The next item is number 19.

19. Open [sprint.md](packet/release/templates/sprint.md). Search for `Order`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. The heading inside the picture is the file's heading. It is not the next step.

```text
# Sprint

## Order
```

That was a picture. Do not paste it. This file is done when the search finds `Order`. Close the file. The next item is number 20.

20. Open [knowledge.md](packet/release/templates/knowledge.md). Search for `Knowledge`.

    The next block is a picture of that file. Do not paste it. This block replaces nothing. The heading inside the picture is the file's heading. It is not the next step.

```text
# Knowledge

1.

2.
```

That was a picture. Do not paste it. This file is done when the search finds `Knowledge` and you have seen two empty numbered lines. Close the file. The twenty files are done. The next heading is Run the demo. You still do not paste a file.

## Run the demo

The twenty files are done. You have not pasted a file. If you changed a file under `packet`, close it without saving. The files you change start in chapter 05.

The demo uses the window that is still inside `problem_simulation`. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line. If you closed that window, open a terminal in the course folder and run both lines.

```text
cd problem_simulation
python -m alwaha.demo.benefit --profile practice
```

You should see one line. The line is `Which benefit is counted twice?` It does not say which two lines count the same calls. It does not print a lag, a survey count, or the attack text. Do not copy a lag, a count, or the attack text into a file.

The prompt returns after that line. That is the command finishing. There is no error. Do not paste the line.

Stay on this page. The next heading is Interview the access manager.

## Interview the access manager

Stay in that same window, still inside `problem_simulation`. If you opened a new terminal in the course folder, run the `cd` line first. If you are already inside `problem_simulation`, skip the `cd` line.

```text
cd problem_simulation
python -m alwaha.interview --persona access-mgr --script "../Module 04/Lesson 05/Student_Copy/work/interviews/access-mgr.questions.txt"
```

You should see `Q1:`, `Q2:`, and `Q3:`, each followed by `A:`. The command prints no score. If the command says it cannot find the script, [chapter 01](01-setup.md) has not created `work/` yet. Run `prepare_work.py` from that chapter, then come back to this heading. The first answer says no-shows are what they feel in the clinic, and the ledger is a different story. The second answer says a large share of contact-center calls are people asking for the status of a referral. The third answer says a handoff with no summary is not a handoff. You paste the notes in [chapter 08](08-the-pages.md). Do not type into [access-mgr.notes.md](work/interviews/access-mgr.notes.md) on this page. The question file is not the graded note.

Stay on this page. The next heading is Interview the enterprise architect.

## Interview the enterprise architect

The same window. Skip the `cd` line if you are already inside `problem_simulation`.

```text
cd problem_simulation
python -m alwaha.interview --persona ea --script "../Module 04/Lesson 05/Student_Copy/work/interviews/ea.questions.txt"
```

You should see `Q1:`, `Q2:`, and `Q3:`, each followed by `A:`. The command prints no score. If the command says it cannot find the script, [chapter 01](01-setup.md) has not created `work/` yet. Run `prepare_work.py` from that chapter, then come back to this heading. The first answer says the strategy is real and the hospitals are not all on it. The second answer says leave is entered after the session is published, and that leave creates `session.cancelled`. The third answer says the warehouse feed is the bi mart. You paste the notes in [chapter 08](08-the-pages.md). Do not type into [ea.notes.md](work/interviews/ea.notes.md) on this page. The question file is not the graded note.

This page is done when you have finished all twenty items, the demo has printed one line, and both interviews have printed `Q1:`. You have not pasted a file.

Next: [04 — Words](04-words.md).
