# 07 — The status

[Chapter 06](06-the-sign-in.md) wrote the states and the token flow. This chapter replaces one script and runs the shell. The checks run the shell again, so the client they see has to come from the generator. The checks themselves run in chapter 08. Do not run them from this page.

You do not paste into a Python file. [generate.py](packet/app/generate.py) writes `client.py`. If a paste into a Python file was a mistake, and the terminal shows `SyntaxError` or `IndentationError`, do not repair the spaces by hand. Go to "If the shell was edited" at the bottom of this chapter.

## How the replacement works

Read [how to read a replacement chapter](../../../learning/how-to-read-a-chapter.md) if you are not sure which block on this page is a picture and which block you paste.

You do not paste a client on this page. `generate.py` writes `work/app/client.py` from today's OpenAPI file. The hand-written client still speaks the previous spec. The demo's first line is that client failing the read. The second line is a generated client succeeding. The demo does not print the field name that was removed.

After the generator runs, search the work copy for `Generated his-wadi client`. If you still see the hand-written sentence, the command did not write the file.

The session row is the table `session.py` names: session id, subject, role, and assurance level. It lives in the application database, not in `his-wadi`.

`contract.py` is the boundary for today. A status question uses the Module 1 status tool and cites `his-wadi`. On the trace, `tool_trace` contains `status`. That short name is this week's record of the same read. On Module 1, Lesson 4 the catalog called it `referral.status`. A message that asks to book does not book. The reply says booking is a later day.

Before you generate, name the hand-written client. It is [packet/app/client.py](packet/app/client.py). That file still speaks the previous spec. There is no older spec file in this folder. Today's spec is [his-wadi.yaml](packet/release/openapi/his-wadi.yaml). The command under Replace the client is what replaces only `work/app/client.py`.

This section adds no file and no command.

## Read four files

Open these in the packet. Read the comment at the top of each one. Do not edit them. Do not edit the copies under `work/app` except by the generate command later on this page.

1. [client.py](packet/app/client.py). Search for `previous spec`. This is the hand-written client. The demo's first line comes from this file.
2. [generate.py](packet/app/generate.py). Search for `beside this file`. The generate command on this page runs the copy under `work/app`, and that copy writes a new `client.py` in the same folder.
3. [session.py](packet/app/session.py). Search for `COLUMNS`. Four names. The session row lives in that table.
4. [contract.py](packet/app/contract.py). Search for `Booking waits`. A status question uses the status tool. A message that asks to book does not book.

The other files under `packet/app` are commented the same way. Open one when a later message names it.

## See the two lines

This command is the only one on this page that starts inside `problem_simulation`. Open a terminal in the course folder, the same way as chapter 01. If that window is already inside `problem_simulation`, skip the `cd` line and run the python line.

```text
cd problem_simulation
python -m alwaha.demo.fhir --profile practice
```

You should see exactly these two lines, and nothing else:

```text
v1 client: his-wadi read failed
v2 client: his-wadi read ok
```

The first line is the hand-written client in [packet/app/client.py](packet/app/client.py). The second line is a client generated from [his-wadi.yaml](packet/release/openapi/his-wadi.yaml). The demo does not print a field name. It does not print a count.

Open [notes/client-lines.md](notes/client-lines.md). In the v1 cell, write `v1 client: his-wadi read failed`. In the v2 cell, write `v2 client: his-wadi read ok`. Leave the pipe characters. The checks do not read that worksheet. The label is yours: the hand-written client failed the read, and the generated client succeeded.

Leave the packet copy of `client.py` unchanged. The next command replaces the copy under `work/app`.

## Replace the client

The heading starts with Replace. This one is the exception. The block under it is a command. Do not paste the command into `client.py`.

The demo window is inside `problem_simulation`. Do not run the next command there. Close it, or leave it and open a new terminal in the course folder, the same way as chapter 01. In the new window, run `dir`. You should see `problem_simulation` and `Module 02`. If you see `alwaha` and `tests` instead, this window is still inside `problem_simulation`. Close it and open the terminal from the course folder.

This command does not use `cd`. It runs the generator that chapter 01 copied into `work/app`, and it points `--spec` at the packet. The generator writes `client.py` beside itself. That is `work/app/client.py`. This block is the command, not a file you paste.

```text
python "Module 02/Lesson 01/Student_Copy/work/app/generate.py" --spec "Module 02/Lesson 01/Student_Copy/packet/release/openapi/his-wadi.yaml"
```

A successful run prints no line of its own. The prompt comes back, and there is no error. Open [work/app/client.py](work/app/client.py). The full path is `Module 02/Lesson 01/Student_Copy/work/app/client.py`. Search for `Generated his-wadi client`. That docstring is the first line. If you still see `Hand-written his-wadi client`, this command did not write the file. Run it again from a terminal in the course folder.

If the terminal says `can't open file` or `No such file or directory`, the window is not the course folder, or chapter 01 has not created `work/` yet. Open a terminal in the course folder. If `Module 02/Lesson 01/Student_Copy/work` is missing, run the prepare command from chapter 01, paste the three pages again from chapters 05 and 06, then run this command again.

Leave every other file under `work/app` as the copy from the packet. The checks import those modules and run them. They do not compare the file bytes with the packet. A comment you add can still pass. A broken helper in one of those files can still fail. [his.py](packet/app/his.py) accepts the generated body. [contract.py](packet/app/contract.py) answers with the status tool and refuses a book call. [session.py](packet/app/session.py) writes the row. [auth.py](packet/app/auth.py) chooses chat or console.

## Write the trace

Same terminal, still in the course folder. This command replaces nothing you typed. It writes [work/trace.json](work/trace.json) and [work/sessions.db](work/sessions.db).

```text
python "Module 02/Lesson 01/Student_Copy/work/app/run.py" --pack "Module 02/Lesson 01/Student_Copy/packet/release" --db "Module 02/Lesson 01/Student_Copy/work/sessions.db" --out "Module 02/Lesson 01/Student_Copy/work/trace.json"
```

A successful run prints no line of its own. The prompt comes back, and there is no error. Open `work/trace.json` as text. The full path is `Module 02/Lesson 01/Student_Copy/work/trace.json`. Search for `"opened"`. You should find three keys:

- `opened`. The patient value is `chat`. The coordinator value is `console`.
- `sessions`. Two rows. Each row has `session_id`, `subject`, `role`, and `loa`.
- `chat`. `tool_trace` contains `status`. `booked` is false. `citations` contains `his-wadi`. `reply` is `Your referral is still pending.`

If `reply` is `The hospital record could not be read.`, the generated client is not the file that ran. Run the generate command again, then this command again.

Do not copy [status.json](packet/release/scenarios/status.json) into `work/`. The runner reads it from the packet. A copy inside `work/` fails the check. The message does not print the watermark. A coding assistant may see your script. It may not see that scenario file.

## Open the two pages

Same terminal, still in the course folder. `dir` still shows `problem_simulation` and `Module 02`. This command starts the server. The window stays open and prints nothing. That is the server waiting. You cannot type another command in that window until you stop it. Leave it open while you use the browser.

```text
python "Module 02/Lesson 01/Student_Copy/work/app/server.py" --pack "Module 02/Lesson 01/Student_Copy/packet/release" --db "Module 02/Lesson 01/Student_Copy/work/sessions.db"
```

If Windows asks whether to allow Python to talk on private networks, click Allow. If you click Cancel, the browser cannot open the page. Click the server window, press Ctrl+C, run the command again, and click Allow.

Open a web browser. Click the address bar. Type `http://127.0.0.1:8080/` and press Enter. Use `http`, not `https`. You should see the heading Patient Access Assistant, a button labeled Patient sign-in, and a button labeled Coordinator sign-in.

Click Patient sign-in. The address becomes `/chat`. The heading is Patient chat. The page says you are signed in.

Click the address bar again, type `http://127.0.0.1:8080/`, and press Enter. Do not use the Back button. Click Coordinator sign-in. The address becomes `/console`. The heading is Staff console. The page says `Booking is a later day. The queue is empty.`

Click the server window and press Ctrl+C. The prompt comes back. That is the server stopped. On macOS the same key stops it. If the window asks `Terminate batch job (Y/N)?`, type `Y` and press Enter. The checks do not need the server to stay running. Stop it before chapter 08.

If the browser says it cannot connect, look at the server window. An empty window means the server is waiting: check the address, then refresh the browser. If the window shows the address is already in use, port 8080 is taken. Close the other program, or a server you started earlier, and run the command again.

## Read the stand-in

Open [work/compose.yaml](work/compose.yaml). It is the laptop stand-in. One service publishes port 8080. You do not start it with a cluster tool today.

Open [work/deploy/namespace.yaml](work/deploy/namespace.yaml). Search for `/chat`, then `/console`. Both routes sit on one service. The comment at the top says a live cluster deploy is a later day.

## If the shell was edited

From a terminal in the course folder:

```text
python "Module 02/Lesson 01/Student_Copy/prepare_work.py"
```

That puts the starter shell back and replaces `sprint.md`, `states.md`, and `token-flow.md` with the empty sections. Paste those three files again from [chapter 05](05-the-notice.md) and [chapter 06](06-the-sign-in.md). Then run the generate command on this page again. Do not repair a Python file by hand. Do not run the checks until those three pages and the generated client are back.

Next: [08 — Finish](08-finish.md).
