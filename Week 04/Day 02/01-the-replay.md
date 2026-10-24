# The replay

The morning is a stand-up. You have the Week 4 Day 1 pack, and nothing from later this week.

Open the release readme, [data/rel-w4d2/README.md](../../data/rel-w4d2/README.md). Then read:

1. [replay/note.md](../../data/rel-w4d2/replay/note.md)
2. [replay/spans.jsonl](../../data/rel-w4d2/replay/spans.jsonl)
3. [dms/circ-ramadan-hours.md](../../data/rel-w4d2/dms/circ-ramadan-hours.md)

From `problem_simulation`:

```text
python -m alwaha.interview --persona ciso --script "..\Week 04\Day 02\work\interviews\ciso.questions.txt"
python -m alwaha.interview --persona patient-rep --script "..\Week 04\Day 02\work\interviews\patient-rep.questions.txt"
```

Ask the CISO about the incident replay, then about a CPU dashboard. Ask the patient representative about the phone line, then about the clinic hours she is still offered after the circular. Write what you hear.

The lead copies [templates/sprint.md](templates/sprint.md) to `work/sprint.md`. Sequence the replay, then the dashboard, then the timeline, then the cache, then shadow traffic.

Copy [templates/timeline.md](templates/timeline.md) to `work/timeline.md`. The alert is already in the replay. The alert time is the alert span. The SLO is on the replay note. The circular id is on the release note.
