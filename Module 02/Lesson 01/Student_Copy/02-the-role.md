# 02 — The role

[Chapter 00](00-background.md) said which release this is. This chapter is how you behave on the client's site for this release. Nothing is filed yet.

A forward deployed engineer works on the client's problem, inside the client's constraints, and leaves something the client can run and check. On this engagement the client is the Al-Waha Health Cluster. You are with the patient-access service. You hold all five parts yourself.

## The five parts today

| Part | What you will leave |
| --- | --- |
| Lead | The sprint, with the generated client before any booking |
| AI or data engineer | The Module 1 status tool still answering one status question |
| Application engineer | A patient on the chat, a coordinator on the console, and a session row in the application database |
| Product manager | The sign-in states |
| Architect | The token flow |

[Chapter 05](05-the-notice.md) is the notice and the sprint. [Chapter 06](06-the-sign-in.md) is the states and the token flow. [Chapter 07](07-the-status.md) is the client, the session row, and the status question. You do every part.

There is no interview today. The checks do not read an interview note.

## What the assistant may do

The assistant may sign in a patient and a coordinator. It may answer a status question by reading `his-wadi` and then calling the Module 1 status tool.

The assistant does not book today. Booking waits until the client is in place. A service token is not a patient token. The patient does not open the staff console. The coordinator does not open the patient chat.

## Where today sits

[Chapter 00](00-background.md) names this release. New files arrive on a schedule. You work from this folder. The grader's copy of the same pages is built in chapter 01. You read the copies in `packet/`.

Coding assistants are allowed on the scripts. [Chapter 07](07-the-status.md) says what may enter a prompt. The scenario file stays out. [status.json](packet/release/scenarios/status.json) carries a watermark. [pol-assistant-use.md](packet/kickoff/corpus/pol-assistant-use.md) says the watermark stays out of prompts, tickets, and the work you submit. Do not copy that scenario file into `work/`.

Next: [03 — The client](03-the-client.md).
