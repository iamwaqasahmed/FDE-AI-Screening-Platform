# 05 — The pages

Five pages. The blanks are what the morning packet still holds. The filled copies are in this folder. The question files are not the graded notes.

## Timeline

A blank timeline makes the incident check say `the timeline does not match the replay`. The message does not print the timestamps.

[timeline.md](work/timeline.md) names `referral.status`, the first error, and the alert. Those two times are the `at` values in [spans.jsonl](sources/release/replay/spans.jsonl): `2027-02-01T09:12:00+03:00` on the first `referral.status` error, and `2027-02-01T09:15:00+03:00` on the alert.

## Dashboard page

A page that misses latency, errors, or tool failures makes the incident check say `the dashboard only has CPU`. That same line can also come from the shell module. The suite tells them apart. If the suite already passed, the page is the miss.

[dashboard.md](work/dashboard.md) names latency, errors, and tool failures, and it says CPU stays flat. That CPU sentence is expected on this page. The filled module does not say CPU.

## Runbook

An empty heading makes the incident check say `the runbook misses a required field`. The message does not name the field.

[runbook.md](work/runbook.md) keeps Detect, Scope, Impact, Timeline, Owner, Cache, and Shadow. Detect names the alert. Scope names `referral.status` and a flat CPU. Impact keeps the registered pending reply. Timeline uses the alert time. Owner is the lead. Cache names `document.changed` and `circ-ramadan-hours`. Shadow names `shadow-extract` and a comparison before promotion. The blank headings are in [runbook.md](sources/release/templates/runbook.md).

## Notes

Notes that miss the replay or the dashboard make the incident check say `the ciso notes miss the replay or the dashboard`. Notes that miss the evening close or the circular make it say `the patient-rep notes miss the old hours`.

[ciso.notes.md](work/interviews/ciso.notes.md) names the replay, the alert, CPU, and the dashboard. [patient-rep.notes.md](work/interviews/patient-rep.notes.md) names the evening close and the circular. Both files keep the pipes. [ciso.questions.txt](work/interviews/ciso.questions.txt) and [patient-rep.questions.txt](work/interviews/patient-rep.questions.txt) are not the graded notes.

A page miss fails only the incident check.

Next: [06 — Knowledge](06-knowledge.md).
