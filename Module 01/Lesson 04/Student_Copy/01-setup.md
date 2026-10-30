# 01 — Setup

[Chapter 00](00-background.md) said what this release is. Python is already checked. Skip the installer and the download. Stay in the course folder you used for the earlier release today. This chapter prepares the grader for `rel-m01-l04` and creates this folder's `work/`. The earlier release's `work/` folder is a different folder. Leave it alone.

## How to open a terminal in the course folder

You will do this again in later chapters. The course folder is the one that contains `problem_simulation` and `Module 01`.

On Windows:

1. Open the course folder in File Explorer.
2. Click the address bar at the top.
3. Type `cmd` and press Enter.

A window opens, already inside the course folder. Later chapters call this "a terminal in the course folder." If your editor already has a terminal there, you can use that instead.

On macOS, open Terminal, type `cd ` with a space after it, drag the course folder onto the window, and press Enter. Use `ls` instead of `dir` in the next step. You are looking for the same two names.

## Step 1 — Check that you are in the right place

In that terminal:

```text
dir
```

You should see `problem_simulation` and `Module 01` in the list. If you do not, this window is not the course folder. Open a terminal in the folder that contains `problem_simulation` and `Module 01`.

Then check Python:

```text
python --version
```

You should see Python 3.12 or a newer 3.x.

## Step 2 — Prepare the grader

The terminal is still in the course folder.

```text
cd problem_simulation
python -m alwaha.build --profile practice --release rel-m01-l04
```

You should see four lines. The first is `Wrote rel-m01-l04 for practice`. Then a Pack line, a Truth line, and a Fingerprint line.

`practice` is the shared classroom world. `rel-m01-l04` is today's file drop, module 1 lesson 4. Leave the Truth folder closed. That folder is the grader's private files. The Pack line is another copy of files you already have in `packet/release`. Ignore it. Today you read this student copy.

## Step 3 — Create your workspace

The build used a terminal inside `problem_simulation`. Leave that window. Open a new terminal in the course folder, the same way as the top of this chapter. Then run:

```text
python "Module 01/Lesson 04/Student_Copy/prepare_work.py"
```

You should see `Created work/agent from the packet.`

`work/agent` now holds [run.py](packet/agent/run.py), [model.py](packet/agent/model.py), [schema.py](packet/agent/schema.py), [memory.py](packet/agent/memory.py), and [tools.py](packet/agent/tools.py). You will replace three of those copies in [chapter 06](06-the-agent.md). Leave the copies in `packet/agent` unchanged.

Run that command once before you edit. A second run with no extra word copies the starter scripts again and replaces `model.py`, `schema.py`, and `memory.py`.

## If a command fails

| What you see | What to do |
| --- | --- |
| `python` is not recognized | Run `py --version`. If that prints Python 3.12 or newer, use `py` instead of `python` for the rest of the lesson |
| `command not found: python` | On macOS or Linux, run `python3 --version`. If that prints Python 3.12 or newer, use `python3` instead of `python` for the rest of the lesson |
| You cannot see `problem_simulation` in `dir` | The window is not the course folder. Open a terminal there, using the steps at the top of this chapter |
| `No module named alwaha` | The terminal is not inside `problem_simulation`. Open a new terminal in the course folder, run `cd problem_simulation`, and then the build command again |
| The prepare script says it must stay next to `packet` | Run it as `python "Module 01/Lesson 04/Student_Copy/prepare_work.py"` from the course folder. Do not move the script |

Next: [02 — The role](02-the-role.md).
