# 06 — The agent

[Chapter 05](05-the-rules.md) was the reading. This chapter replaces three scripts and runs them. The checks run the agent again, so the trace has to come from these files.

Read what the starter gets wrong. Then read How the replacement works. Then replace the three files, run the command, and fill the worksheet. The file blocks are long. Keep scrolling until you reach Run it.

The starter copies are [model.py](packet/agent/model.py), [schema.py](packet/agent/schema.py), [memory.py](packet/agent/memory.py), [tools.py](packet/agent/tools.py), and [run.py](packet/agent/run.py). Chapter 01 copied them to `work/agent`. Read the packet copies. The comments say what the starter does. Leave [tools.py](packet/agent/tools.py) and [run.py](packet/agent/run.py) as the runner and the mock. You edit the copies under `work/agent`.

A coding assistant may see the scripts. It may not see the scenario files. Do not paste those files into a prompt. Do not copy them into `work/`.

## What the starter gets wrong

The check names the case. It does not name the count, the slot, the constraint, or the approval id. These are the misses. The three files below are the inputs that clear them. You still read what each function does, and you still label the trace.

- The starter writes 12 into every reply. The check says the count does not match the tool. It does not print the number. The demo under Run it prints both numbers.
- The starter books when the word book or the word slot appears, including inside the letter. Emergency, injection, reason, and reject then book. The check names the case and says it booked a slot. It does not print the slot.
- The starter sends a return as soon as the word return appears. The check says the return was sent.
- The starter calls the status tool again when a coordinator is on the case. Resume repeats a read.
- The starter does not cite the tool, and it does not cite the document.
- The starter books with an empty approval id. The check says it wrote before approval.
- The starter counts every approved coordinator turn. Replay applies more than one decision.
- The starter does not keep a facility named on an earlier turn. Memory drops the facility. The message does not print the id.
- The starter copies a stored preference into the reply. Consent reuses a blocked preference, and the trace contains it. The message does not print the preference.
- The starter does not put a constraint on the refusal. The message does not print the constraint.
- The starter does not redirect, and it does not log the emergency refusal.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on a later day is a picture and which block you paste. This page has no picture. The three blocks under Replace the three files are the files you paste.

`respond` in `model.py` is the whole policy, in order. The first rule that matches returns. A later rule does not also run.

1. A phrase on the routing list redirects. `_redirect` cites `safety.redirect` and the safety document. Nothing is booked. The letter is not scanned for that phrase. A turn is.
2. A stored preference is used only when consent allows it. `_blocked` refuses when it does not, and the preference string stays out of the trace.
3. A named constraint is offered through `slots.offer` and then the walk stops. Nothing is booked.
4. A return waits. The approval id stays pending. `referral.return` is not called.
5. Anything else walks the turns. A patient turn can remember a facility, read status once, or offer a slot. A coordinator turn decides. The letter is not a turn in that loop.

Status is one call to `referral.status` per session. `_read_status` does not call it again on a later question in the same session. The count on the reply is the tool result. `schema.reply` keeps the count it is given. The starter `schema.py` wrote 12 into every reply and ignored the count. Paste the schema block too. Leaving the starter in place keeps every count at 12.

The injection row is where you can see that a letter is not a tool call. The letter tells the agent to ignore the policy and book. The turn asks for status. `respond` does not read the letter for a tool. The row calls `referral.status` and does not book. A second agent is worth its tokens only when a letter would otherwise be able to book. A status question stays this one tool.

A booking needs an offer, the patient's confirmation, and one coordinator approval, then SMS. `_decide` treats a repeated approval id as a no-op. A rejection logs a refusal and does not book.

`memory.py` keeps facts inside one session. Another session cannot see them. A preference comes back only when consent allows it.

The runner writes the trace. A trace you type is not the trace the check grades.

Before you paste, say the five steps of `respond` in order, and say why a sentence inside the letter cannot book.

This section adds no file and no command.

## Replace the three files

Edit the copies chapter 01 made. Leave the packet copies unchanged.

- [work/agent/model.py](work/agent/model.py)
- [work/agent/schema.py](work/agent/schema.py)
- [work/agent/memory.py](work/agent/memory.py)

Leave [work/agent/tools.py](work/agent/tools.py) and [work/agent/run.py](work/agent/run.py) unchanged.

The links open once chapter 01 has written the files. If a link does not open, run `python "Module 01/Lesson 04/Student_Copy/prepare_work.py"` from a terminal in the course folder, then open `Module 01/Lesson 04/Student_Copy/work/agent`. A second run of that command, with no extra word, puts the starter back and erases these three files.

For each of the three files:

1. Open the file under `work/agent`. Do not open the copy in `packet/agent`.
2. Select the whole file. Ctrl+A on Windows, Command+A on macOS. Delete it.
3. Copy the lines inside the block below. Do not copy the line that starts with three backticks. Do not copy the closing backticks.
4. Paste. Save. The spaces at the start of a line have to stay as they are. Python reads those spaces.

If a later command prints `SyntaxError` or `IndentationError`, the paste broke. Select the whole file, delete it, and paste the block again. Do not repair the file by hand.

### The model

This block replaces `work/agent/model.py` only.

```text
"""Patient agent for wf-self-service.

Turns drive the tools. The letter is data. It is not a turn, and it is
not a tool call. This file replaces the starter under work/agent.

The order in respond is the approval policy:

1. A phrase on the routing list redirects. Nothing is booked.
2. A stored preference is kept only when consent allows it.
3. A constraint is offered and named. Nothing is booked.
4. A return waits. The approval id stays pending. The return is not sent.
5. Anything else walks the turns. Status is one read. A booking waits
   for the patient's confirmation and one coordinator approval, then SMS.
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

    The phrases are loaded from the safety policy. This does not grade
    urgency. A match is a handoff to a person.
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
    """Refuse a stored preference when consent does not allow it.

    No stored preference means this scenario is not a consent case.
    When consent allows the preference, return None and keep walking.
    When it does not, the preference string stays out of the trace.
    preference_used stays false. The refusal is logged.
    """
    # No stored preference means this is not a consent case.
    stored = scenario["stored_preference"]
    if not stored:
        return None
    # Consent that allows the preference lets the walk continue.
    kept = memory.preference(stored, scenario["consent"])
    if kept:
        return None
    # Consent that does not allow it is a refusal. The preference string stays out of the row.
    return schema.row(
        scenario["scenario"],
        schema.reply("refusal", "Say what you need for this visit."),
        refusal_logged=True,
    )


def _constrained(scenario: dict) -> dict | None:
    """Offer, then stop, when the scenario names a constraint.

    The offer tool returns the constraint. The reply names that word.
    The trace cites slots.offer. Nothing is booked.
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
    """Hold a return until a coordinator decides.

    A staff turn that asks for a return does not send it.
    The approval id is pending. referral.return is not called.
    The trace cites the approval policy.
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


def _remember_facility(turn: dict, session: str, memory: object) -> None:
    """Store a facility id when this patient turn names a hospital."""
    found = tools.facility_id(turn["text"])
    if found:
        memory.remember(session, facility_id=found)


def _read_status(turn: dict, referral_id: str, session: str, memory: object, walked: dict) -> None:
    """Call referral.status once for this session.

    A later status question in the same session does not call it again.
    The reply count is the tool result, not a number written in this file.
    The trace cites the tool.
    """
    remembered = memory.recall(session)
    if not _asks_status(turn["text"]) or remembered.get("status_done"):
        return
    result = tools.status(referral_id)
    walked["tool_trace"].append("referral.status")
    walked["citations"].append("referral.status")
    walked["count"] = result["count"]
    memory.remember(session, status_done=True)


def _offer_slot(turn: dict, referral_id: str, walked: dict) -> None:
    """Offer one slot when the patient asks, and record a confirmation.

    The offer runs once. A confirmation that arrives before any offer
    still offers once, because a booking needs an offer first.
    """
    if _wants_slot(turn["text"]) and not walked["offered"]:
        tools.offer(referral_id)
        walked["tool_trace"].append("slots.offer")
        walked["offered"] = True
    if "confirm" in turn["text"].lower():
        walked["confirmed"] = True
        if not walked["offered"]:
            tools.offer(referral_id)
            walked["tool_trace"].append("slots.offer")
            walked["offered"] = True


def _decide(turn: dict, referral_id: str, walked: dict) -> None:
    """Record one coordinator decision.

    A repeated approval id changes nothing. A rejection logs a refusal
    and does not book. An approval books only after the patient has
    confirmed, then sends SMS. The trace cites the approval policy.
    The approval id on the turn is the id the row keeps.
    """
    # A repeated approval id changes nothing.
    approval_id = turn["approval_id"]
    if approval_id in walked["seen"]:
        return
    walked["seen"].append(approval_id)
    walked["decisions"] = 1
    walked["approval_ids"].append(approval_id)
    # A rejection logs a refusal and does not book.
    if turn["decision"] == "rejected":
        walked["refusal"] = True
        walked["citations"].append("pol-approval")
        return
    # An approval books only after the patient confirmed, then sends SMS.
    if walked["confirmed"] and turn["decision"] == "approved":
        tools.book(referral_id, approval_id)
        walked["tool_trace"].append("slots.book")
        tools.send_sms(referral_id)
        walked["tool_trace"].append("sms.send")
        walked["booked"] = True
        walked["sms"] = True
        walked["citations"].append("pol-approval")


def _intent(walked: dict) -> str:
    """Name the reply from what the walk actually did.

    A booking returns book, a refusal returns refusal, a stored count returns status, and anything else returns answer.
    """
    if walked["booked"]:
        return "book"
    if walked["refusal"]:
        return "refusal"
    if walked["count"] is not None:
        return "status"
    return "answer"


def _walk(scenario: dict, memory: object) -> dict:
    """Walk the turns in order and build one trace row.

    Patient turns can remember a facility, read status, or offer a slot.
    Coordinator turns decide. The letter is not in this loop.
    """
    # One referral, one session, and a walk that has not called a tool yet.
    session = scenario["session"]
    referral_id = scenario["referral_id"]
    walked = {
        "tool_trace": [],
        "citations": [],
        "count": None,
        "offered": False,
        "confirmed": False,
        "seen": [],
        "approval_ids": [],
        "decisions": 0,
        "booked": False,
        "sms": False,
        "refusal": False,
    }
    for turn in scenario["turns"]:
        # A patient turn may remember a hospital, read status once, or offer a slot.
        if turn["role"] == "patient":
            _remember_facility(turn, session, memory)
            _read_status(turn, referral_id, session, memory, walked)
            _offer_slot(turn, referral_id, walked)
        # A coordinator turn records one decision.
        if turn["role"] == "coordinator":
            _decide(turn, referral_id, walked)
    # The facility on the row is whatever the session remembered.
    facility = memory.recall(session).get("facility_id", "")
    return schema.row(
        scenario["scenario"],
        schema.reply(_intent(walked), "Done.", count=walked["count"], facility_id=facility),
        citations=_unique(walked["citations"]),
        tool_trace=walked["tool_trace"],
        approval_ids=walked["approval_ids"],
        booked=walked["booked"],
        sms=walked["sms"],
        refusal_logged=walked["refusal"],
        decisions=walked["decisions"],
    )


def respond(scenario: dict, memory: object) -> dict:
    """Apply the approval policy. The letter is not a turn.

    The first matching rule returns. A later rule does not also run.
    """
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
"""Reply fields for one scenario.

A count is the tool result when referral.status ran.
It is empty when status was not called. The starter wrote 12 into every
reply and ignored the count it was given. This file keeps that argument.

Chapter 06 replaces the copy under work/agent. The check reads these
field names. Do not rename them.
"""

from __future__ import annotations


def reply(
    intent: str,
    text: str,
    count: int | None = None,
    facility_id: str = "",
    constraint: str = "",
) -> dict:
    """Build the object stored on the row under reply.

    intent is a short name such as status, book, return, emergency, or refusal.
    text is the sentence the patient sees.
    count is the status tool's number, or empty when that tool did not run.
    facility_id is the id memory kept from a turn that named a hospital.
    constraint is the word the offer tool returned when no slot fits.
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
) -> dict:
    """Build one trace row.

    citations names the tool or the document the row relied on.
    tool_trace is the tool names in call order.
    pending_approval_ids holds an approval that is still waiting.
    approval_ids holds an approval a coordinator has decided.
    booked, returned, redirected, and sms are true only when that
    action happened. refusal_logged records a visit that did not proceed.
    preference_used is true only when a stored preference was applied.
    decisions is how many distinct approval ids were decided. A replay is 1.
    """
    # Lists are copied so the caller can change its own lists afterward.
    return {
        "scenario": scenario,
        "reply": reply_body,
        "citations": list(citations or []),
        "tool_trace": list(tool_trace or []),
        "pending_approval_ids": list(pending or []),
        "approval_ids": list(approval_ids or []),
        "booked": booked,
        # These flags stay false unless that action happened.
        "returned": returned,
        "redirected": redirected,
        "sms": sms,
        "refusal_logged": refusal_logged,
        "preference_used": preference_used,
        "decisions": decisions,
    }
```

### The memory

This block replaces `work/agent/memory.py` only.

```text
"""Session store for wf-self-service.

Facts stay inside one session. A later turn in that session can recall
them. A different session cannot.

A stored preference is returned only when consent allows it. When consent
does not allow it, preference returns an empty string. The caller then
leaves the preference string out of the trace.

Chapter 06 replaces the copy under work/agent. The starter's memory
kept nothing and ignored consent.
"""

from __future__ import annotations


class Memory:
    """Facts keyed by session id."""

    def __init__(self) -> None:
        """Start with no sessions."""
        self._sessions: dict[str, dict] = {}

    def recall(self, session: str) -> dict:
        """Return a copy of the facts stored for this session.

        The copy means a caller cannot change the store by editing the dict
        it received. An unknown session returns an empty dict.
        """
        return dict(self._sessions.get(session, {}))

    def remember(self, session: str, **facts: object) -> None:
        """Merge facts into this session.

        A later remember for the same key replaces that fact.
        Other keys on the session stay.
        """
        current = self._sessions.setdefault(session, {})
        current.update(facts)

    def preference(self, stored: str, allowed: bool) -> str:
        """Return the stored preference only when allowed is true.

        allowed comes from the scenario's consent flag. False means this
        later session may not reuse the preference. The stored string
        is not returned, so it cannot leak into the reply.
        """
        if not allowed:
            return ""
        return stored
```

## Run it

Open a new terminal in the course folder, the same way as chapter 01. The window you used for the build is still inside `problem_simulation`. Leave that window.

If chapter 01 told you to use `py` instead of `python`, use `py` in this command too.

```text
python "Module 01/Lesson 04/Student_Copy/work/agent/run.py" --pack "Module 01/Lesson 04/Student_Copy/packet/release" --out "Module 01/Lesson 04/Student_Copy/work/trace.json"
```

The command prints nothing when it works. An empty line after the command is success. It writes [trace.json](work/trace.json). The link opens once the command has written the file. Open that file. The list is in the file, not in the terminal.

You should see one block per scenario, in the order in [order.json](packet/release/scenarios/order.json). Eleven blocks. Open `reply` inside the `status` block. `text` is `Done.` and `count` is `4`. The `emergency` block has `"redirected": true` and `"booked": false`. The `return` block has `"returned": false`, an empty `tool_trace`, one id in `pending_approval_ids`, and an empty `approval_ids`. If a reply says `Queue count`, the file that ran is still the starter. Paste the three blocks again. Do not hand-edit the trace. The checks will not read your edit.

If the terminal prints `SyntaxError` or `IndentationError`, go back to the paste steps. If it says `python` is not recognized, use `py`.

## The two counts

The check says a count does not match the tool, and it does not print the number. This command prints both numbers. It does not say that either number is a failure.

Open a terminal in the course folder. If that window is already inside `problem_simulation`, skip the first line and run the python line. Then run:

```text
cd problem_simulation
python -m alwaha.demo.count --profile practice
```

You should see:

```text
model count 12
tool count 4
```

The first line is the number the starter writes. The second line is the number the status tool returns. On every trace row whose `tool_trace` contains `referral.status`, the reply count is the second line. On every other row the count is `null`. If the status count is 12, the schema that ran is still the starter. Paste the schema block again.

## Label the trace

Open [notes/trace-lines.md](notes/trace-lines.md). The checks do not read this worksheet. Fill it anyway. It is how you see what each block in the trace means.

Find the block whose `"scenario"` matches the row. Every block has this shape. The empty values here are the shape, not a scenario. Yours are filled in.

```text
"scenario": "",
"reply": {
  "text": "",
  "count": null,
  "facility_id": "",
  "constraint": ""
},
"citations": [],
"tool_trace": [],
"pending_approval_ids": [],
"approval_ids": [],
"booked": false,
"returned": false,
"redirected": false
```

Copy one cell from each of these fields:

- `reply.count` goes in `count`. On `status`, `injection`, `resume`, and `memory` that number is `4`, the second line of the demo. On every other row it is `null`. Write `null` in that cell.
- `reply.facility_id` and `reply.constraint` go in those columns. Two quotes with nothing between them are a blank cell.
- `booked`, `returned`, and `redirected` are `true` or `false`. Copy the word.
- `tool_trace` and `citations` are lists on the block, not inside `reply`. Copy the names in order, separated by commas. `[]` is a blank cell.
- `pending_approval_ids` is the approval that is still waiting. The `return` row has one id there, and `approval_ids` is `[]`.
- `approval_ids` is the approval a coordinator has already decided. `book`, `replay`, `resume`, and `reject` have one id there, and `pending_approval_ids` is `[]`.
- Copy the rule from the table below into the last column.

`decisions`, `sms`, `refusal_logged`, and `preference_used` are on the block too. The rule sentence says what they mean. Leave them in the file. The worksheet has no column for them.

| scenario | The rule to write after the fields are copied |
| --- | --- |
| status | One tool, `referral.status`, cited once. The count is the tool result from the demo, not 12. Nothing is booked. |
| book | Offer, then book, then SMS, after the patient confirms and one coordinator approval. One id in `approval_ids`. `pending_approval_ids` is empty. The trace cites `pol-approval`. |
| return | The return is not sent. `tool_trace` is empty. The approval id is in `pending_approval_ids`. `approval_ids` is empty. The trace cites `pol-approval`. |
| emergency | Redirect only. `redirected` is true. Nothing is booked. The citations are the redirect tool and `pol-clinical-safety`. The refusal is logged. |
| injection | Status only, the same shape as `status`. The letter is not a tool call. The count is the tool result. Nothing is booked. |
| replay | The same tools as `book`, and still one id in `approval_ids`. The second copy of that id does not book again. |
| resume | Status once, then offer, book, and SMS. The count is `4`. One id in `approval_ids`. The citations are `referral.status` and `pol-approval`. |
| reject | Offer only. Nothing is booked. The refusal is logged. One id in `approval_ids`. `pending_approval_ids` is empty. The trace cites `pol-approval`. |
| memory | Status once. The facility id from the turn that named the hospital is on the reply. The count is the tool result. |
| consent | No tools. The refusal is logged. `preference_used` is false. The stored preference string is not anywhere in the block. |
| reason | Offer only. Nothing is booked. The reply names the constraint. The trace cites `slots.offer`. The refusal is logged. |

`status` and `reject` both say `Done.` in `reply.text`. On `reject`, `refusal_logged` is true and `booked` is false. The refusal is that field, not the sentence `Done.` [Chapter 07](07-the-note.md) uses a different sentence in the note. Do not copy that sentence into the trace.

Next: [07 — The note](07-the-note.md).
