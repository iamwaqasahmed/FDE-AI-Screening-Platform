# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check repo --work "..\Week 01\Day 01\work"
python -m alwaha.check interview --work "..\Week 01\Day 01\work"
```

`chk-w1-repo` passes when the health test in [starter/tests/test_health.py](starter/tests/test_health.py) passes, [starter/policy/pol-assistant-use.md](starter/policy/pol-assistant-use.md) is still the cluster document, [starter/scan.py](starter/scan.py) is clean, the credentials match this profile, and the access request names the requester, the data, the purpose, and the classification.

`chk-w1-interview` passes when exactly two scripts were run, each of those conversations reached what that person will say when asked, and each notes file marks statements as a claim, a request, or a fact. A failed interview says that it is incomplete. It does not name the missing fact. Go back to the questions.

Then write `work/knowledge.md` with two short answers:

1. What must be true to pass gate G0?
2. What may a coding assistant be shown on this engagement?

The day is done when both checks print `passed` and the knowledge file has both answers. The architect's zone sketch can live at the bottom of that file: three zones, and the hospital in each.
