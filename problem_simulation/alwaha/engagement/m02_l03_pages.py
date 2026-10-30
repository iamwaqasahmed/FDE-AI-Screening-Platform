"""Participant pages for rel-m02-l03.
The old delay stays out of these strings.

These strings are the receipt-timing notice, the clock guide, the access clauses, and the interface documents for the clock and SMS. They tell a reader to pin the case clock and advance it. The fault switch is named so a receipt that stays pending can be recognized.
"""

from __future__ import annotations


def timing_note() -> str:
    return """# Receipt timing

The SMS partner has withdrawn the wall-clock wait. Waiting on the wall clock no longer makes a receipt due.

Pin the case clock. The interval is in this pack. The fault switch is receipt-late. While that switch is on, the receipt stays pending after the clock has moved.

The access clauses and the usability scripts are in this pack.
"""


def clock_guide() -> str:
    return """# Clock

`PUT /clock` with a JSON body `{"at": "<timestamp>"}` pins the case clock. `GET /clock` reads it back.

A receipt sent at the pinned time is due only after that clock moves by the minutes in [receipt.json](receipt.json). Advance the pinned time. Do not sleep.

`receipt-late` holds the receipt pending after that move.
"""


def access_note() -> str:
    return """# Access clauses

| Id | Clause |
| --- | --- |
| plain-language | The task uses short words. |
| caregiver-complete | A caregiver can finish the task. |
| named-control | A control has a name, not a color alone. |
| one-action | The task has one next step. |
"""


def clock_spec() -> str:
    return """openapi: 3.0.3
info:
  title: clock
  version: "1"
paths:
  /clock:
    get:
      operationId: readClock
      responses:
        "200":
          description: The pinned case clock.
    put:
      operationId: pinClock
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [at]
              properties:
                at:
                  type: string
      responses:
        "200":
          description: The clock is pinned at `at`.
"""


def sms_spec() -> str:
    return """openapi: 3.0.3
info:
  title: sms
  version: "2"
paths:
  /messages:
    post:
      operationId: sendMessage
      responses:
        "202":
          description: Accepted. The receipt follows the case clock.
  /receipts/{id}:
    get:
      operationId: readReceipt
      responses:
        "200":
          description: Due once the clock has moved by the published interval.
        "202":
          description: Still pending.
"""
