# 03 — The agent

[model.py](work/agent/model.py) follows the approval policy, then the two new failures. [schema.py](work/agent/schema.py) keeps the count it is given and adds `failure`. [memory.py](work/agent/memory.py) keeps a session and honors consent. [tools.py](work/agent/tools.py) and [run.py](work/agent/run.py) stay the mock and the runner.

The code stays in those files. This chapter says what each piece is for.

## The model

`respond` walks the policy in order.

1. A phrase on the routing list redirects. The letter is not part of that test. Nothing is booked.
2. A stored preference is kept only when consent allows it. A blocked preference is not copied into the row.
3. A constraint is offered and named. Nothing is booked.
4. A return waits. The approval id stays pending. `referral.return` is not called.
5. Anything else walks the turns. Status is one read. A booking waits for that actor's confirmation and one coordinator approval, then SMS. The same approval id a second time changes nothing.
6. An offer that times out returns at once. `failure` is `timeout`. `slots.book` does not run.
7. A taken offer blocks that actor. The other actor can still book. The row's `failure` is `race-slot`. `slots.book` runs once.

Turns drive the tools. A sentence in the letter is data.

## The schema

`reply` writes the count it is given. `None` stays empty. The starter wrote 12 and threw the argument away.

`row` writes `failure`. `timeout` and `race-slot` are the two names this day uses. Every other row leaves it empty. The check says the case does not name the failure when that field is wrong. It does not print a second copy of the name beyond the case.

## The memory

`recall` returns the facts for that session. `remember` keeps them. `preference` returns the stored string when consent allows it, and an empty string when it does not.

The starter returned an empty recall, dropped every fact, and returned the stored preference anyway. `memory` then lost the facility. `consent` reused a blocked preference. The check names the case and does not print the facility id or the preference.

## The path through the files

The morning chapter [06-the-agent.md](../Student_Copy/06-the-agent.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [04 — The diagram](04-the-diagram.md).
