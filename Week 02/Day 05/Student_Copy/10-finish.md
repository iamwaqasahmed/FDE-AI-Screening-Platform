# 10 — Finish

Two actions. Replace `knowledge.md`. Run four commands. You are done when each command prints `passed`.

The checks grade the smoke test, the deployment note, the zone rows, the operator steps, the sprint, the booking, the file, the notice, the readout, the retro, the contract, and the shape of `knowledge.md`. The sentences in `knowledge.md` are still part of done.

Use the failure table at the bottom only when a check fails. It is not more work. Do not run `prepare_work.py` on this page unless a row in that table tells you to. A second run erases the files you pasted.

## Do this

1. Open [work/knowledge.md](work/knowledge.md). The full path is `Week 02/Day 05/Student_Copy/work/knowledge.md`. It sits beside `sprint.md`. It does not go inside `work/app`, and it does not go inside `packet/`. If the file is missing, create it in that `work` folder. On Windows the name sometimes becomes `knowledge.md.txt`. Click the name and remove `.txt`. If you cannot see `.txt`, in File Explorer open View and tick File name extensions, then rename the file so the name ends in `.md` only.

   Select the whole file and delete it. Copy from this chapter file, not from a preview. If the editor offers a styled paste, use Paste Without Formatting. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. These are the finished sentences.

```text
# Knowledge

1. Ain cannot confirm a slot today because sched-ain publishes a nightly file, and a booking stays queued.
2. Stage 2 adds the operations stack beyond request rate, error rate, and model latency, in Week 4.
```

2. Open a terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Week 02`. If chapter 01 told you to use `py`, use `py` here. If that window is already inside `problem_simulation`, skip the `cd` line and run the python lines.

```text
cd problem_simulation
python -m alwaha.check deploy --release rel-w2d5 --work "../Week 02/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check journey --release rel-w2d5 --work "../Week 02/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check readout --release rel-w2d5 --work "../Week 02/Day 05/Student_Copy/work" --profile practice
python -m alwaha.check individual --release rel-w2d5 --work "../Week 02/Day 05/Student_Copy/work" --profile practice
```

## You should now see

```text
chk-w2-deploy passed.
chk-w2-journey passed.
chk-readout passed.
chk-individual-w2 passed.
```

Each command prints its own line. Wait for one line before you start the next command. You need all four. `work/knowledge.md` has both answers. The first says Ain cannot confirm a slot today because `sched-ain` publishes a nightly file, and a booking stays queued. The second says Stage 2 adds the operations stack beyond request rate, error rate, and model latency, in Week 4.

If you see those four `passed` lines, skip the table below and go to Done.

## If a check fails

A failed check prints `failed`, then one or more lines that start with a dash. The words after the dash are what you look up in the left column below. Do what the right column says. Then run the command again. A line can say the probe does not report the registered hash, the image runs as root, a national id is in the deploy log, prod uses the dev credential, the router leaves the private endpoint, or the deployment note is missing a required fact. It can also say a live slot was promised, a missed night cleared the slots, or the contract test accepted the live-slot fault. It does not name a hash, a token, the quota, a national id, or a clinic code. A watermark message does not print the watermark. Where a line does not name the missing fact, the row gives the file to open and the inputs that make the check pass. Then you paste the block from that chapter again, and you label what you see.

| What it prints | Where to go |
| --- | --- |
| `the health probe does not report the registered hash` | The message does not name the hash. Open [models.json](packet/day4/registry/models.json). The row you want has id `local-small` and status `approved`. Open [work/app/health.py](work/app/health.py) and search for `approved["hash"]`. You should find it. That file is a smoke file. It was copied and not replaced. If the search fails, run `prepare_work.py` from the course folder, then paste chapters 05 through 10 again |
| `the image runs as root` | Open [work/deploy/Dockerfile](work/deploy/Dockerfile) and search for `USER 1000`. Open [work/app/admit.py](work/app/admit.py) and search for `return "rejected"`. Open [work/deploy/deployment.yaml](work/deploy/deployment.yaml) and search for `runAsNonRoot`. Those files are smoke files. If a search fails, run `prepare_work.py`, then paste chapters 05 through 10 again |
| `a national id is in the deploy log` | The message does not name the id. Open [work/app/admit.py](work/app/admit.py) and search for `emitted_log`. That function removes the id from the line. Leave the deploy log out of `work/` |
| `the deploy rejected a registered image` | A clean account `1000` with the line `started` must be accepted. Open [work/tests/test_admit.py](work/tests/test_admit.py) and search for `test_clean_user_is_accepted`. If it is missing, run `prepare_work.py` and paste chapters 05 through 10 again |
| `prod uses the dev credential` | The message does not name a token. Open [dev.json](packet/day4/credentials/dev.json) and [prod.json](packet/day4/credentials/prod.json). Open [work/app/secrets.py](work/app/secrets.py) and search for `prod.json`. Prod must read that file. If the search fails, run `prepare_work.py` and paste chapters 05 through 10 again |
| `the router leaves the private endpoint` | Open [work/app/router.py](work/app/router.py) and search for `ep-local-small`. The route is `ep-local-small`, `local-small`, and `zone-private`. If the search fails, run `prepare_work.py` and paste chapters 05 through 10 again |
| `the manifest is not in the team namespace` | [guide.md](packet/day4/endpoint/guide.md) names `ns-team`. Open [work/deploy/deployment.yaml](work/deploy/deployment.yaml) and search for `ns-team` |
| `the health probe is missing` | Readiness must call `/v1/health`. Open [work/deploy/deployment.yaml](work/deploy/deployment.yaml) and search for `/v1/health` |
| `the pipeline is not in CI` | Open [work/.github/workflows/ci.yml](work/.github/workflows/ci.yml) and search for `unittest`. The work copy and the packet copy both run the suite. If the search fails, run `prepare_work.py` and paste chapters 05 through 10 again |
| `the deployment note promises a live slot` | [Chapter 08](08-the-pages.md). Remove any line that says Ain has a live slot, that `h-ain` is out of scope, that every hospital has a live slot API, or that monitoring is complete. Paste `deployment.md` again |
| `the deployment note contains a banned sentence` | [Chapter 08](08-the-pages.md). The Boundary section leaves urgency with a clinician and keeps patient data off `ext-large`. Paste `deployment.md` again |
| `the deployment note does not leave urgency with a clinician` | [Chapter 08](08-the-pages.md). Boundary needs `clinician` and `urgency`. Paste `deployment.md` again |
| `the deployment note does not keep patient data off the external model` | [Chapter 08](08-the-pages.md). Boundary needs `ext-large`. Paste `deployment.md` again |
| `the deployment note is missing a required fact` | [Chapter 08](08-the-pages.md). The message does not name the fact. The page needs the URL, `zone-private`, `local-small`, the word hash, dev, prod, `non-root`, `pol-deploy`, a citation such as `endpoint/guide.md`, and `Week 4` under Monitoring. Ain needs `h-ain`, `sched-ain`, nightly, and `zone-hospital`. Change needs `cr-ain` and a sequence word. Paste `deployment.md` again, then label each of those on the page |
| `the deployment note does not cite a source` | [Chapter 08](08-the-pages.md). The message does not name the source. The page cites `ciso`, `endpoint/guide.md`, `notices/cr-ain.md`, and `systems/sched-ain.md`, and it names `pol-deploy`. Paste `deployment.md` again |
| `the url is not in zone-private` | [Chapter 08](08-the-pages.md). The zone table needs columns `surface` and `zone`, and the row `url` / `zone-private`. Keep the pipes. Paste `zones.md` again |
| `the file path is not in zone-hospital` | [Chapter 08](08-the-pages.md). The same table needs the row `sched-ain` / `zone-hospital`. Keep the pipes. Paste `zones.md` again |
| `the operator steps are missing` | [Chapter 08](08-the-pages.md). `operators.md` needs the words health and prod. Paste it again |
| `sprint.md does not sequence the change before the readout` | [Chapter 05](05-the-sprint.md). The message does not print the four words. The sentence needs smoke, then change, then readout, then retro. Paste `sprint.md` again |
| `a live slot was promised` | [Chapter 06](06-the-booking.md). The message does not name the return value. Open [queued.json](packet/release/fixtures/queued.json). The status is `queued`. Paste `queue.py` again. You should see `return "queued"`. `return "booked"` remains on the live-slot line and on the line for a facility that is not `h-ain`. That is expected |
| `a missed night cleared the slots` | [Chapter 06](06-the-booking.md). Open [missed.json](packet/release/fixtures/missed.json) and read the clinic code there. Do not type it. Paste `file_ain.py` again. You should see `return previous`. The type line can still say `None`. That is expected |
| `the nightly file did not replace yesterday` | [Chapter 06](06-the-booking.md). Open [nightly.json](packet/release/fixtures/nightly.json). A file that arrives replaces yesterday. Paste `file_ain.py` again. You should see `return arrived` on the line after the missed-night line |
| `a failed notice confirmed a slot` | [Chapter 06](06-the-booking.md). Paste `notify.py` again. You should see `return "queued"` when the status is `queued`. A failed notice leaves that status in place |
| `the booking did not run` | The terminal showed `SyntaxError` or `IndentationError`. Run `prepare_work.py` and paste the Python blocks from chapters 06 and 07 again from the chapter source |
| `the readout promises a live slot` | [Chapter 09](09-the-readout.md). Remove any line that says Ain has a live slot. Paste `readout.md` again |
| `the readout does not leave urgency with a clinician` | [Chapter 09](09-the-readout.md). The page needs `clinician` and `urgency`. Paste `readout.md` again |
| `the readout does not keep patient data off the external model` | [Chapter 09](09-the-readout.md). The page needs `ext-large`. Paste `readout.md` again |
| `the readout does not answer the smoke test` | [Chapter 09](09-the-readout.md). The message does not name the words. Open [guide.md](packet/day4/endpoint/guide.md). Smoke needs `health` and `hash`. Paste `readout.md` again, then label those two words under Smoke |
| `the readout does not sequence the change` | [Chapter 09](09-the-readout.md). The message does not name the words. Change needs `cr-ain` and a sequence word. Paste `readout.md` again |
| `the readout does not name the file path` | [Chapter 09](09-the-readout.md). File needs `nightly`, `sched-ain`, and `zone-hospital`. Paste `readout.md` again |
| `the readout does not say what patients will see` | [Chapter 09](09-the-readout.md). Patients needs `queued`. Paste `readout.md` again |
| `the readout does not name the monitoring limit` | [Chapter 09](09-the-readout.md). Open [starter.md](packet/day4/dashboard/starter.md). Monitoring needs `latency`, and either `Stage 2` or `Week 4`. Paste `readout.md` again |
| `the readout does not state the model limit` | [Chapter 09](09-the-readout.md). The message does not name the number. Open [quota.json](packet/day4/registry/quota.json) and read the number there. Do not type it. Model needs `local-small` and `quota`. Paste `readout.md` again |
| `the ask log is missing` | [Chapter 09](09-the-readout.md). Asks must have text. Paste `readout.md` again |
| `the readout does not cite a source` | [Chapter 09](09-the-readout.md). The message does not name the source. Cite `cr-ain`, `sched-ain`, `ea`, `ciso`, or a file such as `endpoint/guide.md`. Paste `readout.md` again |
| `readout.md is missing` | [Chapter 09](09-the-readout.md). Paste `readout.md` into `work/`. If `work/` is missing, run `prepare_work.py` first, then paste chapters 05 through 10 again |
| `retro.md is missing` | [Chapter 09](09-the-readout.md). Paste `retro.md` into `work/` |
| `the retro promises a live slot` | [Chapter 09](09-the-readout.md). Remove any line that says Ain has a live slot. Paste `retro.md` again |
| `the retro note is missing a heading` | [Chapter 09](09-the-readout.md). Keep, Drop, and Open each need text. Paste `retro.md` again |
| `the contract test is missing` | [Chapter 07](07-the-contract.md). `work/tests/test_contract.py` has to exist, and it has to contain `holds`. Paste the test again |
| `the contract test accepted the live-slot fault` | [Chapter 07](07-the-contract.md). The shell returns true for every status, including `booked`. Paste `contract.py` again. You should see `status == "queued"`. The test still contains `booked` inside `assertFalse(holds("booked"))`. That is expected. A queued booking stays green. The live-slot fault goes red |
| `the contract test rejected the queued booking` | [Chapter 07](07-the-contract.md). Open [queued.json](packet/release/fixtures/queued.json). The status is `queued`. `holds` has to accept that status. Paste `contract.py` again |
| `the contract test did not run` | The terminal showed `SyntaxError` or `IndentationError`. Run `prepare_work.py` and paste the Python blocks from chapters 06 and 07 again from the chapter source |
| `the deploy is missing` | A graded file is not in `work/`. Run `prepare_work.py`, then paste chapters 05 through 10 again |
| `the deploy did not run` | The terminal showed `SyntaxError` or `IndentationError`. Run `prepare_work.py` and paste the Python blocks again from the chapter source |
| `knowledge.md needs two answers` | Paste the block above again. Two numbered lines, each with words after the number |
| `knowledge.md does not say why ain waits` | The message does not name the file. Line 1 of the block above says `sched-ain` publishes a nightly file, and a booking stays queued |
| `knowledge.md does not say what stage 2 adds` | Line 2 of the block above says Stage 2 adds the operations stack, in Week 4 |
| `a watermarked sample is in the work directory` | A copy of `live-slot.json` is in `work/`. Delete that copy. Leave the file in `packet/release`. The message does not print the watermark |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | This window is already inside `problem_simulation`. Skip the `cd` line and run the python lines |
| `SyntaxError` or `IndentationError` | Run `python "Week 02/Day 05/Student_Copy/prepare_work.py"` from the course folder. Then paste chapters 05 through 10 again from the chapter source. Do not repair the spaces by hand |

## Done

The day is done when the four checks print `passed` and `work/knowledge.md` answers both questions.

Keep `work/`. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.
