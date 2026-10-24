# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check deploy --release rel-w2d5 --work "..\Week 02\Day 05\work"
python -m alwaha.check journey --release rel-w2d5 --work "..\Week 02\Day 05\work"
python -m alwaha.check readout --release rel-w2d5 --work "..\Week 02\Day 05\work"
python -m alwaha.check individual --release rel-w2d5 --work "..\Week 02\Day 05\work"
```

`chk-w2-deploy` scores the Day 4 smoke test and the updated deployment note. A miss says the probe does not report the registered hash, the image runs as root, a national id is in the deploy log, prod uses the dev credential, the router leaves the private endpoint, or the deployment note is missing a required fact. It does not name a hash, a token, the quota, a national id, or a clinic code.

`chk-w2-journey` scores `queue.py`, `file_ain.py`, and `notify.py` when those files are present. A miss says a live slot was promised, a missed night cleared the slots, or a failed notice confirmed a slot.

`chk-readout` scores [readout.md](templates/readout.md) and [retro.md](templates/retro.md). `chk-individual-w2` scores [app/contract.py](app/contract.py) and [tests/test_contract.py](tests/test_contract.py). The contract test stays green on a queued booking and goes red on the live-slot fault.

The Day 2 journey still has to pass:

```text
python -m alwaha.check journey --release rel-w2d2 --work "..\Week 02\Day 02\work"
```

A watermarked fixture copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can show the steering card:

```text
python -m alwaha.demo.ain --profile practice
```

Then write `work/knowledge.md` with two short answers:

1. Why can Ain not confirm a slot today?
2. What will Stage 2 add to monitoring?

The day is done when the four checks print `passed` and the knowledge file has both answers.
