# 03 — The image

Open the finished [admit.py](work/app/admit.py), [test_admit.py](work/tests/test_admit.py), and [Dockerfile](work/deploy/Dockerfile) and put them beside yours.

[root.json](sources/release/fixtures/root.json) names the account `root`. [pol-deploy.md](sources/release/standards/pol-deploy.md) says the container user is not root, and that a log line has no national id. [deploy.md](sources/release/notices/deploy.md) says a container running as root is rejected, and a log line that carries a national id is rejected.

`admit` rejects `root` and `0`. It rejects a log line that still contains the national id. A clean account with a clean line is accepted. `emitted_log` removes the id from the line. The word `root` stays on the line that rejects that account. The deployment note does not say the container runs as root.

The test uses the stand-in `NID-sample`. That stand-in is not the id in the pack log. The pack log stays out of `work/`. `parents[1]` is the folder that contains `app`, because this file sits in `work/tests`.

The Dockerfile ends on `USER 1000`. The comment still mentions that the shell ends on root. The last `USER` line is the one that counts. `1000` is not root.

The shell accepts every account and returns the log line unchanged. The shell image ends on `USER root`. While that shell is the file that runs, the check says `the image runs as root` and `a national id is in the deploy log`. The messages do not name the id. A clean account that is rejected produces `the deploy rejected a registered image`.

The demo prints `root image: rejected`, then `registered image: accepted`. Those lines do not print a hash or a national id.

Next: [04 — The probe](04-the-probe.md).
