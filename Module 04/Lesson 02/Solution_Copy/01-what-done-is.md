# 01 — What done is

This page is the map. The day is finished by the sprint, the trace, the board, the meter, the hours cache, the drift names, the override rate, the shadow hold, the timeline, the dashboard page, the runbook, the CISO notes, the patient-rep notes, and the knowledge file.

Open `work/` and find each row. The release pages those answers cite are in [sources](sources/README.md).

| In this folder | What it is for |
| --- | --- |
| [sprint.md](work/sprint.md) | Replay, then dashboard, then timeline, then cache, then shadow. Explained in [chapter 02](02-the-sprint.md) |
| [app/spans.py](work/app/spans.py) | Keep the tool, the hash, and the token count. Explained in [chapter 03](03-the-board.md) |
| [app/dashboard.py](work/app/dashboard.py) | Latency, errors, tool failures, and the alert span. Explained in chapter 03 |
| [app/meter.py](work/app/meter.py) | Sum gateway cost by hospital. Explained in chapter 03 |
| [tests/test_spans.py](work/tests/test_spans.py) | A span keeps the tool, the hash, and the tokens. The shell test says the trace fields are dropped. The two files are not the same |
| [tests/test_dashboard.py](work/tests/test_dashboard.py) | The board names latency, errors, tool failures, and the alert. The shell test reports CPU only |
| [tests/test_meter.py](work/tests/test_meter.py) | Every hospital is summed. The shell test costs one hospital |
| [app/cache.py](work/app/cache.py) | Drop cached hours when the Ramadan circular changes. Explained in [chapter 04](04-the-hours.md) |
| [app/drift.py](work/app/drift.py) | Name the three drifts. Explained in chapter 04 |
| [app/override.py](work/app/override.py) | The override rate is the stamped share. Explained in chapter 04 |
| [app/shadow.py](work/app/shadow.py) | Keep the registered reply. Promote only after a comparison. Explained in chapter 04 |
| [tests/test_cache.py](work/tests/test_cache.py) | The circular replaces the cached hours. Another document leaves the hours cache. The shell test keeps the old hours |
| [tests/test_drift.py](work/tests/test_drift.py) | Each kind has its name. The shell test names every row hours |
| [tests/test_override.py](work/tests/test_override.py) | The rate is the stamped share. The shell test keeps the rate at zero |
| [tests/test_shadow.py](work/tests/test_shadow.py) | The patient reply stays registered. Promotion waits for a comparison. The shell test shows the shadow reply and promotes a hash with no comparison |
| [timeline.md](work/timeline.md) | The first `referral.status` error and the alert. Explained in [chapter 05](05-the-pages.md) |
| [dashboard.md](work/dashboard.md) | Latency, errors, and tool failures. CPU stays flat. Explained in chapter 05 |
| [runbook.md](work/runbook.md) | Detect, Scope, Impact, Timeline, Owner, Cache, and Shadow. Explained in chapter 05 |
| [ciso.notes.md](work/interviews/ciso.notes.md) | The replay, the alert, CPU, and the dashboard. The incident check reads this file |
| [patient-rep.notes.md](work/interviews/patient-rep.notes.md) | The evening close and the circular. The incident check reads this file |
| [ciso.questions.txt](work/interviews/ciso.questions.txt) | The questions the interview command reads. The check does not read this file |
| [patient-rep.questions.txt](work/interviews/patient-rep.questions.txt) | The questions the interview command reads. The check does not read this file |
| [knowledge.md](work/knowledge.md) | The two answers. Explained in [chapter 06](06-knowledge.md) |
| [.github/workflows/ci.yml](work/.github/workflows/ci.yml) | The test job. This day does not replace it. The packet copy is the same file |

The checks print `passed` when a span keeps the tool, the hash, and the token count, the board names latency, errors, and tool failures, the alert sits inside the SLO, every hospital is in the cost, each drift has its name, the override rate is the stamped share, the patient reply stays registered, promotion waits for a comparison, the sprint opens the replay first, the timeline matches the replay, the runbook has the required fields, both knowledge answers are present, the CISO notes name the replay and the dashboard, the patient-rep notes name the evening close and the circular, and the cached hours drop when the Ramadan circular changes.

A spans, dashboard, meter, drift, override, shadow, sprint, dashboard-page, timeline, runbook, knowledge, CISO-note, or patient-rep-note miss fails only the incident check. A cache miss fails only the cache check.

The suite imports all seven app modules. None of them is optional.

Next: [02 — The sprint](02-the-sprint.md).
