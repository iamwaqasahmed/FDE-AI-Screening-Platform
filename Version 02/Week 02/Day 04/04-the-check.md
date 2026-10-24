# The check

From `problem_simulation`, with your work directory filled in:

```text
python -m alwaha.check deploy --release rel-w2d4 --work "..\Week 02\Day 04\work"
```

`chk-w2-deploy` scores the health probe, the image user, the deploy log, the credentials, the router, and the deployment note. A miss says the probe does not report the registered hash, the image runs as root, a national id is in the deploy log, prod uses the dev credential, the router leaves the private endpoint, or the deployment note is missing a required fact. It does not name a hash, a token, the quota, or a national id.

A watermarked fixture copied into `work/` fails the check. The message does not print the watermark.

On `practice`, the instructor can show the rejection:

```text
python -m alwaha.demo.deploy --profile practice
```

Then write `work/knowledge.md` with two short answers:

1. Which zone is this URL in?
2. What does a rollback change?

The day is done when the check prints `passed` and the knowledge file has both answers. Booking from chat still waits.
