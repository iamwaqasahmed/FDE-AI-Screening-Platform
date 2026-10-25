# 06 — The agent

[Chapter 05](05-the-reading.md) was the reading. This chapter replaces three scripts and runs them. The checks run the agent again, so the trace has to come from these files.

Do these four things, in this order. The file blocks are long. Keep scrolling until you reach Run it.

1. Read what the starter gets wrong.
2. Replace `model.py`, save it, then `schema.py`, save it, then `memory.py`, and save it. One file at a time.
3. Run the command under Run it.
4. Fill the worksheet with three rows from the trace.

The starter copies are [model.py](packet/agent/model.py), [schema.py](packet/agent/schema.py), [memory.py](packet/agent/memory.py), [tools.py](packet/agent/tools.py), and [run.py](packet/agent/run.py). Chapter 01 copied them to `work/agent`. Read the packet copies. The comments say what the starter does. Leave [tools.py](packet/agent/tools.py) and [run.py](packet/agent/run.py) as the runner and the mock. You edit the copies under `work/agent`.

A coding assistant may see the scripts. It may not see the scenario files. Do not paste those files into a prompt. Do not copy them into `work/`.

## What the starter gets wrong

The check names the case. It does not name the count, the slot, or an interview sentence. These are the misses. The three files below are the inputs that clear them. You still read what each function does, and you still label the trace.

- The starter writes 12 into every reply. The check says the count does not match the tool. It does not print the number. The demo under Run it prints both numbers.
- The starter books when the word book or the word slot appears, including inside the letter. Emergency, injection, reason, reject, and timeout then book. The check names the case and says it booked a slot. It does not print the slot.
- The starter sends a return as soon as the word return appears. The check says the return was sent.
- The starter calls the status tool again when a coordinator is on the case. Resume repeats a read.
- The starter does not cite the tool, and it does not cite the document.
- The starter books with an empty approval id. The check says it wrote before approval.
- The starter counts every approved coordinator turn. Replay applies more than one decision.
- The starter does not keep a facility named on an earlier turn. Memory drops the facility. The message does not print the id.
- The starter copies a stored preference into the reply. Consent reuses a blocked preference, and the trace contains it. The message does not print the preference.
- The starter does not put a constraint on the refusal. The message does not print the constraint.
- The starter does not redirect, and it does not log the emergency refusal.
- The starter has no `failure` field, so timeout and race-slot do not name the failure. The check says the case does not name the failure.
- The starter books once as soon as the word book appears, including on race-slot, and it does not offer first. The finished row offers, books once, and names race-slot. A second `slots.book` on that case is what the check calls booked twice. It does not print the slot.

## Replace the three files

Edit the copies chapter 01 made. Leave the packet copies unchanged.

- [work/agent/model.py](work/agent/model.py)
- [work/agent/schema.py](work/agent/schema.py)
- [work/agent/memory.py](work/agent/memory.py)

Leave [work/agent/tools.py](work/agent/tools.py) and [work/agent/run.py](work/agent/run.py) unchanged.

The links open once chapter 01 has written the files. If a link does not open, run `python "Week 01/Day 05/Student_Copy/prepare_work.py"` from a terminal in the course folder, then open `Week 01/Day 05/Student_Copy/work/agent`. A second run of that command, with no extra word, puts the starter back and erases these three files.

For each of the three files:

1. Open the file under `work/agent`. Do not open the copy in `packet/agent`.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy the lines inside the block below. Do not copy the line that starts with three backticks. Do not copy the closing backticks.
4. Paste. Save. The spaces at the start of a line have to stay as they are. Python reads those spaces.

Paste one file, save it, and only then open the next file. Copy the lines inside the block. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it.

If a later command prints `SyntaxError` or `IndentationError`, the paste broke. Select the whole file, delete it, and paste the block again. Do not repair the file by hand. If the spaces disappear again as soon as you paste, the editor is changing them. Undo with Ctrl+Z. Paste once more. In Cursor and VS Code, a second paste that still slides the lines to the left means Format On Paste is on. Turn that off for this paste, or use Paste Without Formatting, then save. Do not type the spaces back in yourself.

### The model

This block replaces `work/agent/model.py` only.

```text
"""Patient agent for the proof of concept, including a timeout and a slot race.

Turns drive the tools. The letter is data. It is not a turn, and it is
not a tool call. This file replaces the starter under work/agent.

The order in respond is the approval policy, then the two new failures:

1. A phrase on the routing list redirects. Nothing is booked.
2. A stored preference is kept only when consent allows it.
3. A constraint is offered and named. Nothing is booked.
4. A return waits. The approval id stays pending. The return is not sent.
5. Anything else walks the turns. Status is one read. A booking waits
   for the patient's confirmation and one coordinator approval, then SMS.
6. An offer that times out does not book. The row names timeout.
7. Two patients offered one slot produce one booking. The row names race-slot.
"""

from __future__ import annotations

import schema
import tools


def _unique(items: list[str]) -> list[str]:
    """Keep the first copy of each citation.

    A tool or a document is cited once. A later copy of the same name
    adds nothing to the trace.
    """
    seen: list[str] = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen


def _asks_status(text: str) -> bool:
    """True when this turn asks where the referral is, or asks for status."""
    lowered = text.lower()
    return "where" in lowered or "status" in lowered


def _wants_slot(text: str) -> bool:
    """True when this turn asks to book, and it is not the confirmation.

    A confirmation line can also contain the word slot. That line records
    the confirmation. It is not a new request to offer a slot.
    """
    lowered = text.lower()
    return "confirm" not in lowered and ("book" in lowered or "slot" in lowered)


def _emergency(scenario: dict) -> bool:
    """True when any turn matches a phrase on the routing list.

    The phrases are loaded from the safety policy. The letter is not
    included. A match is a handoff to a person, not an urgency grade.
    """
    blob = " ".join(turn["text"] for turn in scenario["turns"]).lower()
    return any(phrase.lower() in blob for phrase in tools.phrases())


def _redirect(scenario: dict) -> dict:
    """Hand the visit to a person. Do not offer and do not book.

    The trace cites the redirect tool and the routing document.
    The refusal is logged so the visit is recorded as not booked.
    """
    tools.redirect(scenario["referral_id"])
    return schema.row(
        scenario["scenario"],
        schema.reply("emergency", "A person will take this from here."),
        citations=["safety.redirect", "pol-clinical-safety"],
        tool_trace=["safety.redirect"],
        redirected=True,
        refusal_logged=True,
    )


def _blocked(scenario: dict, memory: object) -> dict | None:
    """Refuse when a stored preference is present and consent does not allow it.

    No preference means this check does not apply. A preference that
    consent keeps is also left for the rest of respond. A blocked
    preference returns a refusal and does not copy the string into the row.
    """
    stored = scenario["stored_preference"]
    if not stored:
        return None
    kept = memory.preference(stored, scenario["consent"])
    if kept:
        return None
    return schema.row(
        scenario["scenario"],
        schema.reply("refusal", "Say what you need for this visit."),
        refusal_logged=True,
    )


def _constrained(scenario: dict) -> dict | None:
    """Offer once when the scenario names a constraint, then stop.

    The reply names the constraint the offer tool returned. Nothing is booked.
    """
    if not scenario["constraint"]:
        return None
    offered = tools.offer(scenario["referral_id"])
    return schema.row(
        scenario["scenario"],
        schema.reply("refusal", "No slot meets the constraint.", constraint=offered["constraint"]),
        citations=["slots.offer"],
        tool_trace=["slots.offer"],
        refusal_logged=True,
    )


def _waiting_return(scenario: dict) -> dict | None:
    """Hold a return that a staff turn asked for and a coordinator has not decided.

    The approval id stays pending. referral.return is not called.
    """
    waiting = any(turn["role"] == "staff" and "return" in turn["text"].lower() for turn in scenario["turns"])
    if not waiting:
        return None
    return schema.row(
        scenario["scenario"],
        schema.reply("return", "A coordinator has to see this return."),
        citations=["pol-approval"],
        pending=[f"apr-{scenario['scenario']}"],
    )


def _timeout(scenario: dict, tool_trace: list[str]) -> dict:
    """Stop when the offer did not return. Do not book and do not send SMS.

    failure is timeout. The citations and the tool list are the offer only,
    plus any tool already recorded on this walk.
    """
    return schema.row(
        scenario["scenario"],
        schema.reply("refusal", "The offer did not return."),
        citations=["slots.offer"],
        tool_trace=list(tool_trace),
        refusal_logged=True,
        failure="timeout",
    )


def _offer(
    scenario: dict,
    actor: str,
    offered: dict[str, dict],
    blocked: set[str],
    tool_trace: list[str],
    citations: list[str],
) -> dict | None:
    """Offer once for this actor.

    A second request from the same actor does not offer again.
    A timeout ends the walk. A taken slot blocks that actor and lets
    the walk continue so the other actor can still book.
    """
    if actor in offered:
        return None
    result = tools.offer(scenario["referral_id"])
    tool_trace.append("slots.offer")
    citations.append("slots.offer")
    offered[actor] = result
    error = result.get("error", "")
    if error == "timeout":
        return _timeout(scenario, tool_trace)
    if error == "taken":
        blocked.add(actor)
    return None


def _patient(scenario: dict, turn: dict, memory: object, walk: dict) -> dict | None:
    """Apply one patient turn.

    A hospital name is remembered for the session. Status is one read.
    A request to book offers a slot. A confirmation offers if this actor
    has not offered yet, and records the confirmation.
    A timeout row is returned immediately. Anything else returns None
    so the walk can continue.
    """
    actor = str(turn.get("actor", ""))
    session = scenario["session"]
    found = tools.facility_id(turn["text"])
    if found:
        memory.remember(session, facility_id=found)
    remembered = memory.recall(session)
    if _asks_status(turn["text"]) and not remembered.get("status_done"):
        result = tools.status(scenario["referral_id"])
        walk["tool_trace"].append("referral.status")
        walk["citations"].append("referral.status")
        walk["count"] = result["count"]
        memory.remember(session, status_done=True)
    if _wants_slot(turn["text"]):
        failed = _offer(scenario, actor, walk["offered"], walk["blocked"], walk["tool_trace"], walk["citations"])
        if failed is not None:
            return failed
    if "confirm" in turn["text"].lower():
        walk["confirmed"].add(actor)
        return _offer(scenario, actor, walk["offered"], walk["blocked"], walk["tool_trace"], walk["citations"])
    return None


def _coordinator(scenario: dict, turn: dict, walk: dict) -> None:
    """Apply one coordinator turn.

    The same approval id a second time changes nothing.
    A rejected decision, or an actor whose offer was taken, logs a refusal
    and does not book. A taken offer names race-slot.
    An approved decision books only after that actor has confirmed.
    If the book tool says the slot is taken, the row names race-slot
    and does not send SMS.
    A booking that succeeds sends SMS and cites pol-approval.
    """
    if turn["role"] != "coordinator":
        return
    approval_id = turn["approval_id"]
    if approval_id in walk["seen"]:
        return
    walk["seen"].append(approval_id)
    walk["decisions"] += 1
    walk["approval_ids"].append(approval_id)
    actor = str(turn.get("actor", ""))
    if actor in walk["blocked"] or turn["decision"] == "rejected":
        walk["refusal"] = True
        walk["citations"].append("pol-approval")
        if actor in walk["blocked"]:
            walk["failure"] = "race-slot"
        return
    if actor not in walk["confirmed"] or turn["decision"] != "approved":
        return
    result = tools.book(scenario["referral_id"], approval_id)
    if result.get("status") == "taken":
        walk["refusal"] = True
        walk["failure"] = "race-slot"
        walk["citations"].append("pol-approval")
        return
    walk["tool_trace"].append("slots.book")
    tools.send_sms(scenario["referral_id"])
    walk["tool_trace"].append("sms.send")
    walk["booked"] = True
    walk["sms"] = True
    walk["citations"].append("pol-approval")


def _finish(scenario: dict, memory: object, walk: dict) -> dict:
    """Build the row after every turn has been walked.

    A booking is intent book. A refusal is intent refusal. A status read
    with no booking is intent status. The facility comes from the session.
    The reply text on this path is Done. failure is whatever the walk set.
    """
    if walk["booked"]:
        intent = "book"
    elif walk["refusal"]:
        intent = "refusal"
    elif walk["count"] is not None:
        intent = "status"
    else:
        intent = "answer"
    facility = memory.recall(scenario["session"]).get("facility_id", "")
    return schema.row(
        scenario["scenario"],
        schema.reply(intent, "Done.", count=walk["count"], facility_id=facility),
        citations=_unique(walk["citations"]),
        tool_trace=walk["tool_trace"],
        approval_ids=walk["approval_ids"],
        booked=walk["booked"],
        sms=walk["sms"],
        refusal_logged=walk["refusal"],
        decisions=walk["decisions"],
        failure=walk["failure"],
    )


def _walk(scenario: dict, memory: object) -> dict:
    """Walk the turns in order.

    A patient turn can end the walk early, which is how a timeout returns
    before a later turn can book. Any other role is treated as a
    coordinator turn. Staff turns that are not coordinators do nothing here.
    """
    walk = {
        "tool_trace": [],
        "citations": [],
        "offered": {},
        "blocked": set(),
        "confirmed": set(),
        "seen": [],
        "approval_ids": [],
        "count": None,
        "decisions": 0,
        "booked": False,
        "sms": False,
        "refusal": False,
        "failure": "",
    }
    for turn in scenario["turns"]:
        if turn["role"] == "patient":
            failed = _patient(scenario, turn, memory, walk)
            if failed is not None:
                return failed
        else:
            _coordinator(scenario, turn, walk)
    return _finish(scenario, memory, walk)


def respond(scenario: dict, memory: object) -> dict:
    """Turns drive tools. The letter is not a turn."""
    if _emergency(scenario):
        return _redirect(scenario)
    blocked = _blocked(scenario, memory)
    if blocked is not None:
        return blocked
    constrained = _constrained(scenario)
    if constrained is not None:
        return constrained
    waiting = _waiting_return(scenario)
    if waiting is not None:
        return waiting
    return _walk(scenario, memory)
```

### The schema

This block replaces `work/agent/schema.py` only.

```text
"""Reply fields. A count is the tool result, or empty when status was not called.

This file replaces the starter under work/agent. Leave the packet copy unchanged.

reply writes the count it is given. None stays None. The starter wrote 12
and threw the argument away.

row adds failure. The starter had no such field. timeout and race-slot
are the two names this day writes there. An empty string means the row
is not one of those two failures.
"""

from __future__ import annotations


def reply(
    intent: str,
    text: str,
    count: int | None = None,
    facility_id: str = "",
    constraint: str = "",
) -> dict:
    """Return the reply object the trace stores under reply.

    Every argument is kept. count is the status tool's number, or None
    when status was not called.
    """
    return {
        "intent": intent,
        "text": text,
        "count": count,
        "facility_id": facility_id,
        "constraint": constraint,
    }


def row(
    scenario: str,
    reply_body: dict,
    citations: list[str] | None = None,
    tool_trace: list[str] | None = None,
    pending: list[str] | None = None,
    approval_ids: list[str] | None = None,
    booked: bool = False,
    returned: bool = False,
    redirected: bool = False,
    sms: bool = False,
    refusal_logged: bool = False,
    preference_used: bool = False,
    decisions: int = 0,
    failure: str = "",
) -> dict:
    """Return one trace row.

    Empty lists are written when the caller passes nothing.
    failure is the scenario's failure name, or an empty string.
    """
    return {
        "scenario": scenario,
        "reply": reply_body,
        "citations": list(citations or []),
        "tool_trace": list(tool_trace or []),
        "pending_approval_ids": list(pending or []),
        "approval_ids": list(approval_ids or []),
        "booked": booked,
        "returned": returned,
        "redirected": redirected,
        "sms": sms,
        "refusal_logged": refusal_logged,
        "preference_used": preference_used,
        "decisions": decisions,
        "failure": failure,
    }
```

### The memory

This block replaces `work/agent/memory.py` only.

`recall` returns the facts stored for that session, or an empty dict. `remember` keeps the facts on that session. `preference` returns the stored string when consent allows it, and returns an empty string when consent does not. The block below is the file the check runs. The packet copy of `memory.py` explains the starter, which keeps nothing.

The first line of the block mentions Day 4 tests. Leave that line in. It is part of the file.

```text
"""Session store that keeps a session and honors consent. The Day 4 tests copy this over the skeleton."""

from __future__ import annotations


class Memory:
    def __init__(self) -> None:
        self._sessions: dict[str, dict] = {}

    def recall(self, session: str) -> dict:
        return dict(self._sessions.get(session, {}))

    def remember(self, session: str, **facts: object) -> None:
        current = self._sessions.setdefault(session, {})
        current.update(facts)

    def preference(self, stored: str, allowed: bool) -> str:
        if not allowed:
            return ""
        return stored
```

## Run it

Before you run, open the three files you just saved and check the first line of each.

- `work/agent/model.py` starts with `Patient agent for the proof of concept`.
- `work/agent/schema.py` starts with `Reply fields. A count is the tool result`.
- `work/agent/memory.py` starts with `Session store that keeps a session and honors consent`.

`tools.py` and `run.py` stay the copies from chapter 01. If one of the three first lines is still the starter, paste that block again and save.

Open a terminal in the course folder, the same way as chapter 01. Copy the whole command below. It is one line. Then run:

```text
python "Week 01/Day 05/Student_Copy/work/agent/run.py" --pack "Week 01/Day 05/Student_Copy/packet/day4" --failures "Week 01/Day 05/Student_Copy/packet/release" --out "Week 01/Day 05/Student_Copy/work/trace.json"
```

The command prints nothing when it works. An empty line is success. It writes [trace.json](work/trace.json). Do not hand-edit the trace. The checks run the agent again. A trace you typed by hand is not the trace they grade.

If `python` is not recognized, use `py` in that command.

## The two counts

The starter writes 12. The status tool returns a different number. The check says the count does not match the tool. It does not print the number.

Open a terminal in the course folder. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.demo.count --profile practice
```

You should see:

```text
model count 12
tool count 4
```

`model count` is what the starter writes. `tool count` is what the status tool returns. The reply count on `status`, `injection`, `resume`, and `memory` has to be the tool count. The message does not print the number. Use the tool result.

## Label the trace

Open [trace.json](work/trace.json). It is a list. Each object starts with `"scenario"`. Use Ctrl+F, or Command+F on macOS. Search `"timeout"`, then `"race-slot"`, then `"emergency"`. Stay on the object that starts with that scenario. Do not use a later copy of the same word.

On that object, read `failure`, `booked`, `tool_trace`, `citations`, and `refusal_logged`. The other fields can stay unread for now.

For `timeout`, `failure` is `timeout`, `booked` is false, and `tool_trace` is `slots.offer`. `slots.book` is not in that list.

For `race-slot`, `failure` is `race-slot`, `booked` is true, `slots.book` appears once, and `sms.send` appears once.

For `emergency`, `tool_trace` is `safety.redirect`, `citations` includes `pol-clinical-safety`, `redirected` is true, `refusal_logged` is true, and `booked` is false.

If those three do not match, the paste in this chapter is not the file that ran. Go back to the first-line check under Run it, fix the file that is still the starter, and run the command again. Do not edit `trace.json`.

Write those three rows on [notes/trace-lines.md](notes/trace-lines.md). The checks do not read that worksheet. [Chapter 08](08-the-readout.md) uses the emergency row for the trace note.

Next: [07 — The diagram](07-the-diagram.md).
