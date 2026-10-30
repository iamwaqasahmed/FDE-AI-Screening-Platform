# 04 — The status

[Chapter 03](03-the-sign-in.md) wrote the states and the token flow. This page is the client and the one status question.

## The two lines

The demo prints two lines and nothing else:

```text
v1 client: his-wadi read failed
v2 client: his-wadi read ok
```

The first line is the hand-written client. The second line is a client generated from [his-wadi.yaml](sources/release/openapi/his-wadi.yaml). The demo does not print a field name. It does not print a count. The label is: the hand-written client failed the read, and the generated client succeeded.

[work/app/client.py](work/app/client.py) is that generated file. The first line says `Generated his-wadi client. Leave this file as the generator wrote it.` [generate.py](work/app/generate.py) is what wrote it. Every other file under `work/app` matches the starter shell. You were not asked to edit them.

[his.py](work/app/his.py) is the dev stand-in. It accepts a body whose keys, aside from the referral id, are the names in the spec. A leftover name from the hand-written client fails the read. The journey check then says `his-wadi read failed`. It does not name a field or a count.

## The reply

[contract.py](work/app/contract.py) answers a successful read with the Module 1 status tool. `tool_trace` is `status`. On Module 1, Lesson 4 the catalog called this same read `referral.status`. Today's trace uses the short name. `citations` contains `his-wadi`. `booked` is false. The reply says the referral is still pending. Count, state, and facility come from the scenario row. A message that asks to book returns "Booking is a later day." and does not call the status tool. An approval stays `later`.

The journey check says `status count does not match`, `status state does not match`, or `facility does not match` when those copies are wrong. It does not print the count. It says `status tool is missing` when the tool list dropped `status`, and `a book call was made` when booking ran.

## The two pages

[chat.py](work/app/chat.py) is the patient page. The heading is Patient chat. [console.py](work/app/console.py) is the coordinator page. The heading is Staff console, and the page says booking is a later day. [server.py](work/app/server.py) serves both on one process. The home page has a patient button and a coordinator button.

[compose.yaml](work/compose.yaml) is the laptop stand-in for that one service. [namespace.yaml](work/deploy/namespace.yaml) lists `/chat` and `/console`. A live cluster deploy is a later day.

[zones.md](sources/kickoff/world/zones.md) places `h-wadi` in `zone-private`. `his-wadi` is that hospital's record. The assistant is not deployed there today.

The scenario file is not in this folder. [pol-assistant-use.md](sources/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts, tickets, and the work you submit. A copy of the scenario in `work/` fails the check. The message does not print the watermark.

## The path through the files

The morning chapter [07-the-status.md](../Student_Copy/07-the-status.md) has the section How the replacement works. That section is the path through the files this page compares. Read it beside the finished file. The notes above are the decisions the check names.

Next: [05 — Knowledge](05-knowledge.md).
