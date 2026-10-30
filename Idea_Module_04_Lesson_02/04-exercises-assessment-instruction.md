# 04 — Exercises, assessment, and self-paced instruction

## Prerequisites

The student can already run `python -m alwaha.build --profile practice --release rel-m04-l02` and the demo `python -m alwaha.demo.trace --profile practice`. They have finished Module 4 Lesson 1’s logging rule: a patient identifier does not belong in a trace. They have seen Module 3’s citation fields (id, version, status, audience). They do not need an OpenTelemetry SDK, a collector, a GPU, or an account on Langfuse, Phoenix, or Braintrust.

Time: one sitting, about three to four hours if they write the functions themselves. The current paste path is shorter and does not meet this file’s outcomes.

## Outcomes

1. From `spans.jsonl`, state the first `referral.status` error time, the alert time, and whether the gap is inside five minutes, after excluding the alert span from the rates.
2. Show a CPU board and an SLI board on the same spans, and say which one matches the tool incident.
3. Show that those spans do not contain the circular, then make `document.changed` for `circ-ramadan-hours` replace the cached hours, and make the same topic for any other id leave them.
4. Name ramadan hours, criteria v4, and campaign clinic, and write one sentence each that uses the narrow meanings in file 02 (stale document, superseded retrieval version, data drift as covariate shift). Add one sentence that tool-schema drift is a different failure.
5. Return only the registered reply. Refuse to promote a hash unless `compared` and `matched` are both true. Name one write a discarded shadow response would still perform if the process kept production credentials.
6. Sum SAR by hospital, including a shadow row if present. Compute the stamped share. Say that the share is not a proof of quality until it sits beside a policy check.
7. Write a blameless timeline and a runbook whose Cache and Shadow sections record Failure H and the promotion gate, not only the tool error.

## The runnable replay

Save the program below as `replay_incident.py` anywhere outside the course tree, or inside this idea folder. Run it with no arguments. Then run it with `--pack` pointed at `Module 04/Lesson 02/Student_Copy/packet/release`. Then run `--break ttl` and `--break schema`. A clean run prints `replay ok`. A broken run prints `replay failed` and exits 1.

The program is the reference handler plus the probes. It is not the student’s graded `work/app`. After it runs, the student still writes `cache.py`, `dashboard.py`, `shadow.py`, and the markdown files so the existing checks have something to import. The script’s job is to make the blind board visible before those files are written.

```python
"""Local incident replay for rel-m04-l02. Stdlib only.

Usage:
  python replay_incident.py
  python replay_incident.py --pack path/to/packet/release
  python replay_incident.py --break ttl
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

SLO_MINUTES = 5
CIRCULAR = "circ-ramadan-hours"
OLD = "Code hrs-ramadan closes the evening clinics at 21:00."
NEW = "Evening clinics close at 01:00. Daytime slots are not offered."
REGISTERED = "Your referral is still pending."
SHADOW_TEXT = "Your referral was accepted by the shadow adapter."
LABELS = {"clinic": "campaign clinic", "criteria": "criteria v4", "hours": "ramadan hours"}
NEIGHBOR = {
    "hours": "stale document",
    "criteria": "superseded retrieval version",
    "clinic": "data drift (covariate shift)",
}


def p95(values: list[int]) -> int:
    ordered = sorted(values)
    if not ordered:
        return 0
    rank = (95 * len(ordered) + 99) // 100
    return ordered[rank - 1]


def sli_board(spans: list[dict]) -> dict:
    body = [span for span in spans if span.get("name") != "alert"]
    errors = [span for span in body if span.get("status") == "error"]
    tools = [span for span in errors if span.get("tool")]
    alert = next(span.get("at") for span in spans if span.get("name") == "alert")
    return {
        "alert_at": alert,
        "error_rate": (len(errors) / len(body)) if body else 0.0,
        "latency_p95": p95([int(span.get("latency_ms") or 0) for span in body]),
        "tool_failures": len(tools),
    }


def cpu_board(spans: list[dict]) -> dict:
    return {"cpu": spans[0]["cpu"] if spans else 0}


def answer(store: dict, event: dict, mode: str) -> str:
    if mode == "ttl":
        return str(store.get("hours") or "")
    if mode == "flush":
        if event.get("topic") == "document.changed":
            return str(event.get("body") or "")
        return str(store.get("hours") or "")
    if event.get("topic") == "document.changed" and event.get("doc_id") == CIRCULAR:
        return str(event.get("body") or "")
    return str(store.get("hours") or "")


def reply(turn: dict, mode: str) -> str:
    if mode == "shadow-reply":
        return str(turn.get("shadow_reply") or "")
    return str(turn.get("registered_reply") or "")


def promote(comparison: dict, mode: str) -> str:
    if mode == "promote":
        return str(comparison.get("candidate_hash") or "")
    if comparison.get("compared") and comparison.get("matched"):
        return str(comparison.get("candidate_hash") or "")
    return ""


def cost(rows: list[dict]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for row in rows:
        hospital = str(row["hospital"])
        totals[hospital] = totals.get(hospital, 0) + int(row["sar"])
    return totals


def embedded() -> dict:
    tool = "referral.status"
    base = {"cpu": 0.2, "hospital": "h-wadi", "trace_id": "tr-replay"}
    spans = [
        {**base, "at": "2027-02-01T09:00:00+03:00", "hash": "sha256:registered", "latency_ms": 180, "name": "model", "status": "ok", "tokens": 128, "tool": tool},
        {**base, "at": "2027-02-01T09:05:00+03:00", "hash": "", "latency_ms": 220, "name": "tool", "status": "ok", "tokens": 0, "tool": tool},
        {**base, "at": "2027-02-01T09:12:00+03:00", "hash": "", "latency_ms": 2400, "name": "tool", "status": "error", "tokens": 0, "tool": tool},
        {**base, "at": "2027-02-01T09:13:00+03:00", "hash": "", "latency_ms": 2600, "name": "tool", "status": "error", "tokens": 0, "tool": tool},
        {**base, "at": "2027-02-01T09:14:00+03:00", "hash": "", "latency_ms": 2800, "name": "tool", "status": "error", "tokens": 0, "tool": tool},
        {**base, "at": "2027-02-01T09:15:00+03:00", "hash": "", "latency_ms": 0, "name": "alert", "status": "error", "tokens": 0, "tool": ""},
    ]
    return {
        "spans": spans,
        "signals": [
            {"current": CIRCULAR, "id": "drift-hours", "kind": "hours", "seen": "circ-ramadan"},
            {"current": "crit-endo-v4", "id": "drift-criteria", "kind": "criteria", "seen": "crit-endo-v3"},
            {"current": "ophth-screen", "id": "drift-clinic", "kind": "clinic", "seen": "ophth-clinic"},
        ],
        "gateway": [
            {"hospital": "h-wadi", "path": "live", "sar": 11},
            {"hospital": "h-wadi", "path": "shadow", "sar": 1},
            {"hospital": "h-nakhl", "path": "live", "sar": 7},
            {"hospital": "h-safra", "path": "live", "sar": 4},
        ],
        "overrides": [{"stamped": True}, {"stamped": True}, {"stamped": False}],
        "turn": {
            "candidate_hash": "sha256:shadow",
            "effects": ["read"],
            "registered_reply": REGISTERED,
            "shadow_reply": SHADOW_TEXT,
        },
        "schema": {"latency_ms": 200, "seen": "schema-v2", "registered": "schema-v1", "status": "ok", "tool": tool},
    }


def load_pack(pack: Path) -> dict:
    data = embedded()

    def rows(path: Path) -> list[dict]:
        out = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                out.append(json.loads(line))
        return out

    data["spans"] = rows(pack / "replay" / "spans.jsonl")
    data["signals"] = rows(pack / "drifts" / "signals.jsonl")
    data["gateway"] = rows(pack / "meter" / "gateway.jsonl")
    data["overrides"] = rows(pack / "actions" / "overrides.jsonl")
    turn = json.loads((pack / "experiment" / "shadow-extract.json").read_text(encoding="utf-8"))
    turn.setdefault("effects", ["read"])
    data["turn"] = turn
    return data


def minutes_between(first: str, alert: str) -> float:
    return (datetime.fromisoformat(alert) - datetime.fromisoformat(first)).total_seconds() / 60


def run(data: dict, mode: str) -> list[str]:
    problems: list[str] = []
    spans = data["spans"]
    print("phase replay")
    cpus = {span.get("cpu") for span in spans}
    print("cpu values", sorted(cpus, key=lambda item: (item is None, item)))
    first = next(span["at"] for span in spans if span.get("status") == "error" and span.get("tool"))
    alert = next(span["at"] for span in spans if span.get("name") == "alert")
    gap = minutes_between(first, alert)
    print("first tool error", first)
    print("alert", alert, "gap_minutes", gap, "slo", SLO_MINUTES)
    if not 0 <= gap <= SLO_MINUTES:
        problems.append("alert outside slo")
    blob = json.dumps(spans)
    if "circ-ramadan" in blob or "doc_id" in blob:
        problems.append("trace already contains the circular")
    print("trace mentions the circular: no")

    print("phase dashboard")
    print("architecture A", cpu_board(spans))
    board = sli_board(spans)
    if mode == "cpu":
        board = cpu_board(spans)
    print("architecture B sli", board)
    if mode != "cpu":
        if "error_rate" not in board or "tool_failures" not in board:
            problems.append("sli board missing")
    else:
        if board != {"cpu": spans[0]["cpu"]}:
            problems.append("cpu break did not stick")
        problems.append("cpu board hides the tool incident")

    print("phase timeline skeleton")
    print("Write a blameless timeline that includes these facts:")
    print("- first referral.status error at", first)
    print("- alert at", alert, "inside", SLO_MINUTES, "minutes")
    print("- CPU stayed flat while the tool failed")
    print("- no span carries the hours document")
    print("Do not name a person as the cause.")

    print("phase cache")
    store = {"hours": OLD}
    other = {"topic": "document.changed", "doc_id": "circ-other", "body": "Unrelated text."}
    changed = {"topic": "document.changed", "doc_id": CIRCULAR, "body": NEW}
    cache_mode = "ttl" if mode == "ttl" else "flush" if mode == "flush" else "event"
    kept = answer(store, other, cache_mode)
    fresh = answer(store, changed, cache_mode)
    print("after other document:", kept)
    print("after hours circular:", fresh)
    if kept != OLD:
        problems.append("unrelated document changed the hours cache")
    if fresh != NEW or OLD in fresh or "21:00" in fresh:
        problems.append("old clinic hours are still served")

    print("phase drift")
    for row in data["signals"]:
        kind = str(row.get("kind"))
        print(LABELS[kind], "|", NEIGHBOR[kind], "| seen", row.get("seen"), "| current", row.get("current"))
    schema = data["schema"]
    schema_bad = schema["seen"] != schema["registered"]
    if mode == "schema":
        schema_bad = True
    print(
        "proposal tool-schema",
        schema["tool"],
        "status",
        schema["status"],
        "latency_ms",
        schema["latency_ms"],
        "definition",
        schema["seen"],
        "registered",
        schema["registered"],
    )
    if schema_bad and schema["status"] == "ok":
        print("schema pin: tool name is stable and the definition hash moved")
        if mode == "schema":
            problems.append("tool schema drifted while status stayed ok")

    print("phase shadow")
    turn = data["turn"]
    said = reply(turn, mode)
    print("patient reply:", said)
    if said != turn.get("registered_reply") or turn.get("shadow_reply", "\0") in str(said):
        problems.append("shadow traffic changes the patient reply")
    if "write" in turn.get("effects", []):
        problems.append("shadow process can write")
    bare = {"candidate_hash": turn.get("candidate_hash", ""), "compared": False, "matched": False}
    ready = {"candidate_hash": turn.get("candidate_hash", ""), "compared": True, "matched": True}
    blocked = promote(bare, mode)
    opened = promote(ready, mode)
    print("promote uncompared:", blocked or "(empty)")
    print("promote matched:", opened or "(empty)")
    if blocked:
        problems.append("a hash is promoted with no comparison")
    if mode != "promote" and opened != ready["candidate_hash"]:
        problems.append("a matched comparison did not promote")

    print("phase meter")
    totals = cost(data["gateway"])
    stamped = [row for row in data["overrides"] if row.get("stamped")]
    rate = (len(stamped) / len(data["overrides"])) if data["overrides"] else 0.0
    print("sar by hospital", totals)
    print("stamped share", rate)
    print("The stamped share is not quality until a policy check sits beside it.")
    if "h-nakhl" not in totals or "h-safra" not in totals:
        problems.append("cost is missing a hospital")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pack", type=Path)
    parser.add_argument(
        "--break",
        dest="mode",
        default="ok",
        choices=("ok", "cpu", "ttl", "flush", "shadow-reply", "promote", "schema"),
    )
    args = parser.parse_args()
    data = load_pack(args.pack) if args.pack else embedded()
    problems = run(data, args.mode)
    if problems:
        print("replay failed")
        for item in problems:
            print("-", item)
        return 1
    print("replay ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

What a clean run is asserting, so the student can check the screen without trusting a vibe:

- CPU is a single value while three tool spans are errors.
- The alert gap is inside five minutes.
- The span JSON does not contain the circular.
- An unrelated `document.changed` leaves the 21:00 text in place.
- The hours circular replaces it with the 01:00 body.
- The three graded phrases print beside a neighbor that is not a synonym.
- The schema fixture is status ok and latency 200 while the definition hash differs. On `--break schema` that fact fails the run. On the happy path it is printed and does not fail, because today’s check does not grade it. The print is the lesson.
- The patient line is the pending sentence. The uncompared hash prints empty.
- `h-nakhl` and `h-safra` are in the sum. The embedded shadow row of 1 SAR is inside `h-wadi`’s total, so dropping `path == shadow` would still show a total and the script would not catch the drop. The printout labels `path`. The written meter note has to say the shadow SAR was included. That is a deliberate small gap: a sum cannot prove the student noticed the label. The note can.

`--break cpu` is expected to fail. `--break ttl` fails on old hours. `--break flush` fails on the unrelated document. `--break shadow-reply` and `--break promote` fail the shadow gates. Use those runs as the lab, then implement the healthy handlers in `work/app`.

## Exercise sequence

Do these after the script’s happy path and at least two `--break` runs. Write into the lesson’s `work/` only when following the real course. In a dry run of this proposal, write into a scratch directory so the course files stay as they are.

**E1. Read the pack before any module.** Open `replay/note.md`, `spans.jsonl`, `circ-ramadan-hours.md`, `document-changed.json`, `signals.jsonl`, `shadow-extract.json`. Record the first error `at` and the alert `at` from the file, not from memory of this research note. Confirm the shadow file has no `compared` field.

**E2. Two boards.** Implement `board` so the packet’s CPU test fails and a new test expects `error_rate`, `latency_p95`, `tool_failures`, and `alert_at`. Keep the alert out of the denominator. State in `dashboard.md` that CPU stayed flat and that the SLI board is the tool incident, and that the hours incident is not on that board.

**E3. Attribute map, ungraded.** A table with one row per span name in the replay and the Development attributes it would carry (`gen_ai.operation.name`, `gen_ai.tool.name`, usage tokens, and, for a retrieval span that does not exist yet, `alwaha.doc.id`). Mark content attributes as opt-in and leave them blank. This is architecture B on paper.

**E4. Cache.** Replace the starter that deletes the event. Tests: the hours circular returns the new body; `circ-other` returns the stored 21:00 sentence; a topic that is not `document.changed` returns the store. This is the doc-id guard `slice-cache` alone does not prove.

**E5. Drift paragraph.** `knowledge.md` keeps two numbered lines the current checker can read: the three phrases, then `document.changed`. Add a third numbered line the current checker ignores: one sentence that hours are a stale document, criteria are a superseded version, the clinic row is covariate shift, and none of the three is embedding drift. Add a fourth line naming tool-schema drift as absent from `spans.jsonl`. If a future grader starts requiring exactly two numbered lines, merge the distinctions into line 1 after the three names rather than adding lines. Today `knowledge_problems` only inspects the first numbered line for the three names and the second for the event, and it only complains when there are fewer than two numbered lines.

**E6. Shadow.** `reply` returns the registered sentence. `promote` stays empty until both flags are true. In the runbook Shadow section, write the credential rule: the shadow path cannot book, stamp, or invalidate cache. The effects list in the replay is the concrete version.

**E7. Timeline and runbook.** Timeline includes both instants, `referral.status`, the flat CPU, and a clause that the hours document was not on the trace. Runbook sections stay Detect, Scope, Impact, Timeline, Owner, Cache, Shadow, so `runbook_problems` still passes. Cache names `document.changed` and `circ-ramadan-hours`. Shadow names `shadow-extract` and a comparison. Owner names the lead. Impact keeps the word `pending`, because the patient reply stays the registered pending sentence while the phone line may still be quoting old hours. Those two impacts are different. Write both in Impact if the section can hold two sentences. The checker only requires `pending`.

**E8. Interviews.** CISO notes: the replay already contains the alert, and a CPU dashboard misses the tool failures. Patient-rep notes: the evening close and the circular. Add one clause the checker does not require: the latency board also misses the evening close. The required words `evening` and `circular` stay.

## Assessment

**Keep, unchanged, until a course editor touches the grader:**

- `chk-m04-l02-incident` on spans, dashboard, meter, drift, override, shadow, and the notes.
- `slice-cache` on `cache.answer` for the real event.
- Miss text that does not reveal timestamps, hashes, rates, costs, or the old sentence.
- The demo’s three lines and the hidden error detail.

**Change in the student copy when this proposal is adopted:**

- Starter tests must expect the repaired behavior, or they must be clearly named `test_the_trap_fails_on_purpose` and excluded from the suite the student is told to turn green. A test named as the product that asserts `{"cpu": 0.2}` teaches the wrong definition of done.
- Chapters 05–09 stop pasting the solution. They paste nothing but a failing test, if anything. The replay script is the worked example of the incident, not of the student’s functions.
- `dashboard.md` must include a clause that the hours bug is off the latency board. That needs a one-line addition to `dashboard_problems` later. Until that edit, E2’s sentence is ungraded and still required by this proposal’s self-check: the student’s dashboard note contains `hours` or `circular`.

**Self-check before the official commands.** `python replay_incident.py` prints `replay ok`. `python replay_incident.py --break ttl` prints `replay failed`. The student’s `cache.answer` matches phase cache on all three inputs. The student’s `shadow.reply` and `shadow.promote` match phase shadow.

**Official commands, unchanged:**

```text
python -m alwaha.check incident --release rel-m04-l02 --work "../Module 04/Lesson 02/Student_Copy/work" --profile practice
python -m alwaha.check cache --release rel-m04-l02 --work "../Module 04/Lesson 02/Student_Copy/work" --profile practice
```

Pass lines remain `chk-m04-l02-incident passed.` and `slice-cache passed.`

**Rubric for the writing, beyond keyword presence.**

| Item | Pass | Fail |
| --- | --- | --- |
| Timeline | Both instants, the tool, CPU flat, hours absent from the trace, no person blamed | Only the two instants copied from a chapter |
| Drift | Three graded names plus the three neighbors, and embedding drift named as a different event | The three names alone, or all three called concept drift |
| Cache | Doc id and topic both required | TTL only, or every event body wins |
| Shadow | Registered reply, both flags, no write tools | Patient text changed, or a hash promoted from a trace |
| Board | SLIs, alert excluded, hours called out as off-board | CPU, or a latency board treated as the whole incident |

## Instruction notes for a solo student

Work in `Student_Copy`. Leave `Solution_Copy` closed. The replay script does not replace `prepare_work.py` or the build. When a check fails, the miss sentence is the spec. It will not show the number you got wrong. Re-open the pack file it names and recompute. Do not paste a hash, a SAR figure, or the error detail into markdown.

Skip architecture D. If a slide is added later, one line is enough: Langfuse, Phoenix, and Braintrust are examples of sinks for spans and scores, and OpenInference is not the OpenTelemetry GenAI document.

The trainer chapter can stay optional. A facilitator who has a room runs `--break ttl` on a projector, asks which board is green, then asks which document the patient would hear. That question is the lesson. The modules afterwards are the repair.
