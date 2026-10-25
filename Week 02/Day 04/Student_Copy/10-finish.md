# 10 — Finish

Two actions. Create `knowledge.md`. Run one command. You are done when that command prints `chk-w2-deploy passed.`

The check grades the health probe, the image account, the deploy log, the credentials, the router, the manifest, the pipeline, the deployment note, the zone row, the operator steps, the sprint, and the shape of `knowledge.md`. The sentences in `knowledge.md` are still part of done.

Use the failure table at the bottom only when a check fails. It is not more work. Do not run `prepare_work.py` on this page unless a row in that table tells you to. A second run erases the files you pasted.

## Do this

1. Make `knowledge.md`. It sits in the same folder as `sprint.md`, `deployment.md`, `zones.md`, and `operators.md`. The full path is `Week 02/Day 04/Student_Copy/work/knowledge.md`. It does not go inside `work/app`, and it does not go inside `packet/`.

   In the editor, open the `work` folder and create a new file named `knowledge.md`. If you use File Explorer instead, open that folder, right-click, choose New, then Text Document, and name it `knowledge.md`. On Windows the name sometimes becomes `knowledge.md.txt`. Click the name and remove `.txt`. If you cannot see `.txt`, in File Explorer open View and tick File name extensions, then rename the file so the name ends in `.md` only.

   Open the file. If anything is already in it, select the whole file and delete it. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. These are the finished sentences. Line 1 names `zone-private`. Line 2 says a rollback changes the model hash.

```text
# Knowledge

1. The URL is in zone-private.
2. A rollback changes the model hash.
```

2. Open a terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Week 02`. If chapter 01 told you to use `py`, use `py` here. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.check deploy --release rel-w2d4 --work "../Week 02/Day 04/Student_Copy/work" --profile practice
```

## You should now see

```text
chk-w2-deploy passed.
```

`work/knowledge.md` has both answers. The first names `zone-private`. The second says a rollback changes the model hash.

## If the check fails

A failed check prints `failed`, then one or more lines that start with a dash. The words after the dash are what you look up in the left column below. Do what the right column says. Then run the command again. A line says the probe does not report the registered hash, the image runs as root, a national id is in the deploy log, prod uses the dev credential, the router leaves the private endpoint, or the deployment note is missing a required fact. It can also say the manifest is not in the team namespace, the health probe is missing, the pipeline is not in CI, the url is not in zone-private, the operator steps are missing, or the sprint does not book the readout after the deploy. It does not name a hash, a token, the quota, or a national id. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the inputs. Then you paste the block from that chapter again.

| What it prints | Where to go |
| --- | --- |
| `the health probe does not report the registered hash` | [Chapter 07](07-the-probe.md). The message does not name the hash. Open `models.json`. The row you want has id `local-small` and status `approved`. The previous row stays in the file. Paste `health.py` and `test_health.py` again. The candidate argument can remain on the function line |
| `the image runs as root` | [Chapter 06](06-the-image.md) and [chapter 07](07-the-probe.md). The Dockerfile must end on `USER 1000`. Admission must reject `root` and `0`. The manifest must set `runAsNonRoot`. The demo's first line is `root image: rejected` |
| `a national id is in the deploy log` | [Chapter 06](06-the-image.md). The message does not name the id. Paste `admit.py` again. `emitted_log` removes the id. Leave `log.json` in the packet |
| `the deploy rejected a registered image` | [Chapter 06](06-the-image.md). A clean account `1000` with the line `started` must be accepted. The demo's second line is `registered image: accepted` |
| `prod uses the dev credential` | [Chapter 08](08-the-endpoint.md). The message does not name a token. Open `dev.json` and `prod.json`. Prod must read `prod.json`. Paste `secrets.py` again |
| `the router leaves the private endpoint` | [Chapter 08](08-the-endpoint.md). The route is `ep-local-small`, `local-small`, and `zone-private`. Paste `router.py` again |
| `the manifest is not in the team namespace` | [Chapter 07](07-the-probe.md). The guide names `ns-team`. Paste `deployment.yaml` again |
| `the health probe is missing` | [Chapter 07](07-the-probe.md). Readiness must call `/v1/health`. Paste `deployment.yaml` again |
| `the pipeline is not in CI` | [Chapter 08](08-the-endpoint.md). The work `ci.yml` must run `unittest` on `tests`. The packet copy stays without that step. Paste the work workflow again |
| `the url is not in zone-private` | [Chapter 09](09-the-pages.md). The zone table needs columns `surface` and `zone`, and the row `url` / `zone-private`. Keep the pipes. Paste `zones.md` again |
| `the operator steps are missing` | [Chapter 09](09-the-pages.md). `operators.md` needs the words health and prod. Paste it again |
| `sprint.md does not book the readout after the deploy` | [Chapter 05](05-the-sprint.md). The deploy sentence has to sit above the readout sentence. Paste `sprint.md` again |
| `the deployment note does not leave urgency with a clinician` | [Chapter 09](09-the-pages.md). Boundary needs `clinician` and `urgency`. Paste `deployment.md` again |
| `the deployment note does not keep patient data off the external model` | [Chapter 09](09-the-pages.md). Boundary needs `ext-large`. Paste `deployment.md` again |
| `the deployment note is missing a required fact` | [Chapter 09](09-the-pages.md). The message does not name the fact. The page needs the URL, `zone-private`, `local-small`, the word hash, dev, prod, `non-root`, `pol-deploy`, a citation such as `endpoint/guide.md`, and `Week 4` under Monitoring. Paste `deployment.md` again |
| `the deployment note does not cite a source` | [Chapter 09](09-the-pages.md). The message does not name the source. The page cites `ciso` and `endpoint/guide.md`, and it names `pol-deploy`. Paste `deployment.md` again |
| `the deployment note contains a banned sentence` | [Chapter 09](09-the-pages.md). Remove any line that says the container runs as root. The admission file may still say `root` on the rejection line. That is expected. Paste `deployment.md` again |
| `the deploy is missing` | A graded file is not in `work/`. Run `prepare_work.py`, then paste chapters 05 through 09 again, and paste the knowledge block above |
| `the deploy did not run` | The terminal showed `SyntaxError` or `IndentationError`. Run `prepare_work.py` and paste the Python blocks again from the chapter source |
| `knowledge.md needs two answers` | Paste the block above again. Two numbered lines |
| `knowledge.md does not name the zone` | Line 1 of the block above names `zone-private` |
| `knowledge.md does not say what a rollback changes` | Line 2 of the block above says a rollback changes the model hash |
| `a watermarked sample is in the work directory` | A copy of `log.json` is in `work/`. Delete that copy. The message does not print the watermark |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python line |
| `SyntaxError` or `IndentationError` | Run `python "Week 02/Day 04/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 09 again from the chapter source. Do not repair the spaces by hand |

## Done

The day is done when the check prints `passed` and `work/knowledge.md` answers both questions.

Keep `work/`. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.
