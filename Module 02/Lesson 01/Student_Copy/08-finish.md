# 08 — Finish

The checks grade the sprint, the states, the token flow, the session row, the two pages, and one status question. They also grade the shape of `knowledge.md`. They run the shell again. A trace you typed by hand is not what they grade. The sentences in `knowledge.md` are still part of done.

Use the failure table at the bottom only when a check fails. It is not more work.

## Do this

1. The server window from chapter 07 must already be stopped. If that window is still open and you cannot type in it, click it and press Ctrl+C. Then make `knowledge.md`. It sits in the same folder as `sprint.md`, `states.md`, and `token-flow.md`. The full path is `Module 02/Lesson 01/Student_Copy/work/knowledge.md`. It does not go inside `work/app`, and it does not go inside `packet/`.

   In the editor, open the `work` folder and create a new file named `knowledge.md`. If you use File Explorer instead, open that folder, right-click, choose New, then Text Document, and name it `knowledge.md`. On Windows the name sometimes becomes `knowledge.md.txt`. Click the name and remove `.txt`. If you cannot see `.txt`, in File Explorer open View and tick File name extensions, then rename the file so the name ends in `.md` only.

   Open the file. If anything is already in it, select the whole file and delete it. Copy the lines inside the block below. Do not copy the line of three backticks that opens the block, and do not copy the line of three backticks that closes it. Paste. Save. These are the finished sentences. Line 1 is the booking sentence from [loa.md](packet/release/identity/loa.md). Line 2 says where the session row lives.

```text
# Knowledge

1. Booking and cancellation require loa-2.
2. The session row lives in the application database.
```

2. Open a terminal in the course folder, the same way as chapter 01. `dir` should list `problem_simulation` and `Module 02`. If that window is already inside `problem_simulation`, skip the `cd` line and run the two python lines. Run both python lines in the block. The first can pass while the second still fails. Do not stop after the first.

```text
cd problem_simulation
python -m alwaha.check auth --release rel-m02-l01 --work "../Module 02/Lesson 01/Student_Copy/work" --profile practice
python -m alwaha.check journey --release rel-m02-l01 --work "../Module 02/Lesson 01/Student_Copy/work" --profile practice
```

## You should now see

```text
chk-auth passed.
chk-journey passed.
```

`work/knowledge.md` has both answers. The first says booking and cancellation require the level named in the identity note. The second says the session row lives in the application database.

## If a check fails

A failed auth check does not print the role list or the assurance level. A failed journey check says the his-wadi read failed when the client is still the hand-written one. It does not name a field or a count. A watermark message does not print the watermark. Where a check fails without naming the missing fact, use the row below. The row sends you back to the chapter that has the inputs. Then you write the label yourself.

| What it prints | Where to go |
| --- | --- |
| `python` is not recognized | [Chapter 01](01-setup.md). Use `py` instead of `python` in the command |
| `SyntaxError` or `IndentationError` | A Python file lost its spaces. Do not repair it by hand. From the course folder, run `python "Module 02/Lesson 01/Student_Copy/prepare_work.py"`, paste the three pages again from chapters 05 and 06, then run the generate command in [chapter 07](07-the-status.md) |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and run the check again |
| `The system cannot find the path specified` or `No such file or directory` on the `cd` line | Run `dir`. If the list shows `alwaha`, you are already inside `problem_simulation`. Skip the `cd` line. If the list shows `app` and `tests`, this window is inside `work/`. Open a new terminal in the course folder, the one whose `dir` lists `problem_simulation` and `Module 02`, and run the block from the `cd` line |
| `can't open file` or `No such file or directory` on `generate.py`, `run.py`, or `server.py` | That window is not the course folder. [Chapter 07](07-the-status.md). Run `dir`. You should see `problem_simulation` and `Module 02` |
| `Build rel-m02-l01 first.` | [Chapter 01](01-setup.md). Run the build again with `--profile practice` and `--release rel-m02-l01` |
| `auth needs --release rel-m02-l01.` | Add `--release rel-m02-l01` to the auth command above |
| `journey needs --release rel-m02-l01, rel-m02-l02, or rel-m02-l05.` | Add `--release rel-m02-l01` to the journey command above |
| `a watermarked sample is in the work directory` | Delete the scenario file from `work/`. It stays in [packet/release/scenarios](packet/release/scenarios/status.json). The message does not print the watermark |
| `the shell is missing` | [Chapter 01](01-setup.md). Run `prepare_work.py` again, then repeat chapters 05, 06, and 07 |
| `the shell did not run` | [Chapter 07](07-the-status.md). Restore the shell with `prepare_work.py`, paste the three pages again, and run generate again |
| `session row is missing` or `session row has an extra column` or `session row does not match` | [session.py](packet/app/session.py) was changed. The four columns are the whole row. Restore the shell as in the SyntaxError row. The message does not print the role or the assurance level |
| `patient did not open the chat` or `coordinator did not open the console` or `patient opened the staff console` or `coordinator opened the patient chat` | [chat.py](packet/app/chat.py) or [console.py](packet/app/console.py) was changed. Restore the shell. The patient page is Patient chat. The coordinator page is Staff console |
| `a listed staff role did not open the console` or `a foreign role was accepted` or `a service token was accepted as the patient` | [auth.py](packet/app/auth.py) was changed. The list is the staff heading in [loa.md](packet/release/identity/loa.md). The message does not print the list. Restore the shell, then generate again |
| `states.md is missing a sign-in state` | [Chapter 06](06-the-sign-in.md). Paste the states block again. Keep the pipe characters. The message does not print the role list or the assurance level |
| `token-flow.md does not say where the session row is written` or `token-flow.md does not keep a service token off the patient` | [Chapter 06](06-the-sign-in.md). Paste the token-flow block again |
| `sprint.md does not sequence the client before booking` | [Chapter 05](05-the-notice.md). Paste the sprint block again. The generate sentence stays above the booking sentence |
| `his-wadi read failed` | [Chapter 07](07-the-status.md). Run the demo. The first line is the hand-written client. The second line is the generated client. Then run generate.py. The message does not name a field or a count |
| `status tool is missing` or `a book call was made` or `the status reply has no citation` | [contract.py](packet/app/contract.py) was changed. A status question uses the status tool and does not book. Restore the shell and generate again |
| `status count does not match` or `status state does not match` or `facility does not match` | The shell copies those from the scenario row. The message does not print the count. Restore the shell and generate again. Do not type a number into the reply |
| `an approval was left open` or `approval is not held for a later day` or `health does not report the model` | [contract.py](packet/app/contract.py) was changed. An approval stays held. Restore the shell and generate again |
| `knowledge.md needs two answers` | Two lines that start with `1.` and `2.` and then a word. Use the block above |
| `knowledge.md does not name the booking assurance level` | The message does not print the level. Paste the block above. Line 1 is the booking sentence from the identity note |
| `knowledge.md does not say where the session row lives` | Line 2 of the block above names the application database |

## Done

This lesson is done when both checks print `passed` and `work/knowledge.md` answers both questions.

Keep `work/` and the client worksheet. The solution copy, when you receive it, is how you compare your pages with a finished set. Leave `problem_simulation/build` closed.

## What you open next

The Done section above is the gate. `knowledge.md` is part of that gate. The [optional review](../../../learning/review.md) is not filed. The checks do not read it.

If `Solution_Copy` is already on disk beside this folder, this is the moment it is for. Open [the solution README](../Solution_Copy/README.md) only after Done is true. Do not start in its `work/` folder. The trainer chapter there is optional.

This lesson is done. The next day is the feeds, then the receipt. `eref` pushes `referral.submitted`, and a cancelled clinic session arrives as its own event.

Open [the next lesson](<../../Lesson 02/Student_Copy/README.md>) and read `00-background.md` before any command.
