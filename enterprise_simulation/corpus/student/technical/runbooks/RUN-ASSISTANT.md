---
id: RUN-ASSISTANT
title: When the assistant and the hours page disagree
date: 2025-01-08
type: runbook
author: Riley Chen
systems:
  - northline-assistant-2024
  - hospital
  - local-read-api
access: student
---

# RUN-ASSISTANT

I am Riley Chen. I own northline-assistant-2024. This note is dated 8 January 2025. It is for desk clerks and the supervisor on the Vancouver desk when the assistant panel and the hours page disagree. The operator guide I wrote on 20 November 2024 still describes how the panel is filled. This note says what I want done on the shift when the close on that panel and the close on the hours page are not the same words.

The assistant is a reader. It does not append to the hospital log, the channel log, or the payer log. It does not file a slot, dispatch a handset, or write coverage. It loads hospital rows for one referral and fills one screen. The product name on that screen is `northline-assistant-2024`. If the banner shows a different name, you are in a different tool and this note does not apply. The three logs remain three append-only tables in `var/log.sqlite`. Update on those tables is rejected. Delete is rejected. A command that tries to install one shared clock is rejected. The assistant does not write a shared instant across hospital, channel, and payer, because the assistant does not write the logs at all.

No account is open. The desk app, the assistant panel, the hours page, and the host panel are on the desk machine in Vancouver. There is no remote host in another account to restart, because that account was not opened and nothing in this note was deployed. When I say restart, I mean the desk app on this machine. When I say the host, I mean the host panel for that local desk app.

## What the two screens are

The assistant serves the first hours document it finds. It collects hospital document changes whose document id is `hours-cedar`. It orders those documents by the `occurred_at` stored on the row and serves the earliest one. The screen fields `hours_close_local` and `hours_version_served` are copied from the document it served. `hours_close_local` is the local close on that document. `hours_version_served` is the version on that document. Later hours documents for `hours-cedar` remain in the extract. The product serves the first one in this walk. The close on the served document is a local time. The document may also name a timezone. The assistant copies the close string. It does not convert that close into the Vancouver desk clock, and it does not compare it with a nightly file time.

The hours page is the other display a clerk can open for Cedar Ridge hours. It has its own status line and its own close. Cedar Ridge is the rural clinic in Washington. It has no slot API. Its hours documents live with the hospital documents the local reader can serve. A clerk can have the assistant panel on one side of the desk app and the hours page on the other. The panel can show the close and version from the earliest `hours-cedar` document in the walk. The hours page can show a different version, a different status line, and a different close. That split is the disagreement this note is about. Both displays can be open at the same time. Both can be reading hospital document rows. They do not become one display because the clerk is in a hurry.

The assistant also fills other fields from hospital rows: wait from the mart row, urgency from a word scan of the stored letter, an approval-shaped token from that same letter, and a coverage line from the eligibility cache flag when that cache row is present. Those fields are described in the operator guide. This note is about the hours close and the hours version when they disagree with the hours page. I am not, on this page, assigning those other fields to a board, and I am not telling anyone which clock a board is allowed to use. The logs do not share a clock. The assistant copies strings that are already stored.

The desk reads extracts through a local HTTP process on this machine. `python -m access serve` binds `127.0.0.1` and port 8088 unless another port is given. It reads every JSON file under `student_pack/extracts`. `GET /extracts` returns the bundle. `GET /extracts/<name>` returns one file. `GET /ref/<ref>` returns the rows whose ref matches. The assistant looks up the referral in the hospital extract that reader serves. It does not append, and the reader does not append. Restarting the desk app does not delete a log row. Delete would be rejected if something tried.

## The steps I wrote

When the assistant and the hours page disagree, these are the steps I wrote for the bay.

First, restart the desk app. Quit the desk app on the Vancouver workstation and open it again. Let it load against the local reader. The reader is the HTTP process on `127.0.0.1`. The extracts it serves are the JSON files under `student_pack/extracts`. After the app is open again, bring the referral back up on the assistant panel and open the hours page again so you are looking at this session of the app, not at a window left from earlier in the shift. The restart is a restart of that local app. It is not a change to `log_hospital`, `log_channel`, or `log_payer`. It does not rewrite an hours document. It does not insert a shared clock.

Second, trust the assistant if the host is green. The host panel for the desk app shows the host name, a cpu percent, a latency figure, and a status. The host I mean on this desk is desk-app-3. Read the status on that panel after the restart. If the host is green, trust the assistant. Read the member the close on the assistant panel, and write the assistant's close and the assistant's version into the call note. The hours page can still be open beside it. Under this step, the words you speak and the words you write down are the assistant's `hours_close_local` and `hours_version_served`.

Those are the steps. Restart the desk app, then trust the assistant if the host is green. I wrote them in that order. The second step has a condition. The condition is the status word green on the host panel. I have not written a further step on this page for a host whose status is some other word. I have not written a step that edits the hours page, and I have not written a step that appends a new hours document. The assistant remains a reader after the restart, the same way it was a reader before the restart.

## What trusting the assistant means on this page

Trusting the assistant, in the second step, means using the hours fields the panel is showing after the restart. Quote the version on the screen when a supervisor asks which hours sheet the member was shown from the assistant. The operator guide already says the panel copies the earliest `hours-cedar` document in the walk. Later documents stay in the extract. The hours page is a separate display. I am telling the clerk, when the host is green, to take the assistant's close and version for the call. I am recording that as the step. The hours page continues to show whatever close and status it shows.

Read the seven assistant values back in the order the operator guide already uses, so the call recording matches the screen: product, referral, wait, urgency, approval token, coverage line, hours close and version. The hours close and version in that list are the ones on the assistant after the restart, when the host is green. Do not replace the hours version with a version you saw on a poster in the office. Do not type a close in by hand to make the panel match the hours page. The panel is a reading of the hospital extract. A change to a stored hours document is a hospital append, which this product does not perform.

If the banner is not `northline-assistant-2024`, stop and say so. This note does not apply to a different tool. If the referral's hospital rows are missing, leave the screen and tell the supervisor which row you could not find. Do not type a value in by hand to complete the panel. The restart is not a way to invent a missing row. If the row is absent after the app is open again, it is absent in the extract the local reader is serving.

## What the host panel is

The host panel is local. Status green is a word on that panel. The panel also shows a cpu percent and a latency figure. The second step I wrote uses the status word. I am not writing a threshold for the cpu percent, and I am not writing a threshold for the latency figure. Clerks sometimes want me to turn those numbers into a rule about the hours document. I am not doing that here. The condition in the second step is: the host is green. The host name on this desk is desk-app-3.

The office week is Monday through Friday. Night shift and weekend calls use the same two steps when the assistant and the hours page disagree. The product does not switch sheets after a particular local hour. It serves the first hours document on every shift. Cedar Ridge may file at night, including on a weekend, and the assistant still reads the hospital extract as the operator guide describes. The nightly file is not how this product chooses hours. The restart does not become a different restart on Saturday. The host panel is the same panel.

## Who keeps which machine

I own the assistant. Bobbi Tran keeps the three logs. If a clerk thinks the log itself should be edited so the hours page and the assistant show one close, that edit is a delete or an update, and both are rejected. A later hours document is a new append if an authority sends one. This note does not send that append. The local HTTP process only reads extracts. `GET /health` returns status up when the reader is up. That health word is the reader. The host status I named in the second step is the desk-app panel. They are two readings on the same machine. Neither one is a cloud account. An account is not open.

Questions about the assistant's walk come to me while I own northline-assistant-2024. Questions about why a log row cannot be deleted go to Bobbi. When you train a new clerk on this disagreement, walk the two steps with them on one referral: restart the desk app, then, if the host is green, trust the assistant and read the close and version the panel shows. That walk is the training I am leaving on this page.
