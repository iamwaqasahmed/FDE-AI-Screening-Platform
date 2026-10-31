---
id: TECH-ASSISTANT
title: Operator guide for northline-assistant-2024
date: 2024-11-20
type: operator-note
author: Riley Chen
systems:
  - northline-assistant-2024
  - hospital
access: student
---

This note is for desk operators who run northline-assistant-2024. I am Riley Chen. I own this product. The guide below is the way the assistant is built to behave on a shift. Read it before you open a referral on the screen, and use it when a supervisor asks where a field on that screen came from.

The assistant is a reader. It does not append to the hospital log, the channel log, or the payer log. It does not file a slot, dispatch a handset, or decide coverage. It loads hospital rows for one referral and fills one screen. The product name on that screen is `northline-assistant-2024`. If the banner shows a different name, you are in a different tool and this note does not apply.

## Before you open a referral

Have the referral code from the desk session. The assistant looks up that code in the hospital extract. The extract is the JSON the local reader serves for the hospital, the same bundle you can open under the extracts folder. You need a mart row for the referral, a stored letter for the referral, and the hours documents the assistant walks. When the cache row is present, the screen also fills the coverage line from it. When a required row is missing, leave the screen and tell the supervisor which row you could not find. Do not type a value in by hand to complete the panel.

Confirm you are on the Vancouver desk session for that member before you read clinical text aloud. The letter the assistant scans is hospital text with a clinician audience. The screen shows the scan result. It does not replace the letter, and it does not copy the letter into the channel utterance.

## What the assistant reads

The assistant reads the mart. It finds the hospital mart row whose referral matches the one on the screen. From that row it copies `wait_days` onto the screen. The field you see is the figure stored on the mart. The assistant does not compute a second figure, and it does not read the channel log or the payer log to fill `wait_days`. If you need to show a colleague the source, open the mart row for the same referral and read `wait_days` there. The screen and that row match because the screen copied the row.

The assistant then finds the stored letter for the referral and scans the letter text. The scan does two jobs, and it does them only on that letter.

The first job looks for urgency words. The words it treats as urgency are `urgent` and `chest pain`. The match ignores letter case. When either word is present, the screen urgency is `urgent`. When neither word is present, the screen urgency is `routine`. The assistant does not read the tone of the rest of the sentence, and it does not ask a clinician to confirm the word. Your job is to know that the badge is the result of that word scan. Read the letter yourself when the member is on the phone. The badge is the product's scan, which you can point to when someone asks why the panel says urgent or routine.

The second job looks for an approval-shaped token. The shape is the letters `APR-` followed by digits. The first token of that shape in the letter is copied into `approval_accepted` on the screen. When the letter has no token of that shape, the field is empty. The assistant does not check the token against a payer row, a permit, or a second document. It records the token it found in the letter. When you quote the screen to a member, quote the token the field shows and say it came from the letter scan.

## Hours the assistant serves

The assistant serves the first hours document it finds. It collects hospital document changes whose document id is `hours-cedar`. It orders those documents by the `occurred_at` stored on the row and serves the earliest one. That document is the first hours document in the walk. The screen fields `hours_close_local` and `hours_version_served` are copied from the document it served. `hours_close_local` is the local close on that document. `hours_version_served` is the version on that document.

When you are asked which hours sheet the member was shown, answer with the version on the screen. Then open that same document in the hospital extract and read the close and the version there. They are the same values, because the assistant copied them. Later hours documents for `hours-cedar` remain in the extract. The product serves the first one in this walk. If a supervisor wants a different sheet read to the member, they use the document store. The assistant panel continues to show the first document it found.

The close on the served document is a local time. The document may also name a timezone. The assistant copies the close string. It does not convert that close into the Vancouver desk clock, and it does not compare it with a nightly file time. Tell the member the close the screen shows, and name the version, so the call notes match the panel.

## The rest of the panel

When an eligibility cache row exists for the referral, the assistant reads `eligible` on that row. A true value shows as `eligible` in `coverage_shown`. A false value shows as `not-eligible`. The panel uses that flag. It does not open the payer coverage document to fill this line. If you are explaining the line, open the cache row and read `eligible`.

A completed screen for a referral therefore shows the product name, the referral, `wait_days` from the mart, `urgency` from the word scan, `approval_accepted` from the token scan, `coverage_shown` from the cache flag, and the close and version from the first hours document. Those are the fields the 2024 assistant fills. A field that is empty means the scan or the row did not supply it.

## During the call

Open the referral after the desk session is up. Let the panel fill. Read the seven values back in a fixed order so the call recording matches the screen: product, referral, wait, urgency, approval token, coverage line, hours close and version. If the member asks you to change the wait or the close, tell them the panel is a reading of the hospital extract and that a change is a hospital append, which this product does not perform. Write the screen values into the desk note as they appear. Do not replace the approval token with a code you remember from another referral. Do not replace the hours version with a version you saw on a poster in the office.

At the end of the call, leave the panel as it rendered. The assistant does not store a second copy of the screen inside the logs. The extract rows remain the source you and the next operator can open. If the panel and the mart row disagree, stop and fetch the hospital extract again before you continue the call. A stale file on the workstation is handled by reloading the extract, then reading the panel once more.

## Handoff

Night shift inherits the same rules. The product does not switch sheets after 17:00 or after 21:00 local. It serves the first hours document on every shift. Weekend calls use the same walk. Cedar Ridge may file at night, and the assistant still reads the mart and the letter and the hours documents as described above. It does not read the nightly file id to choose hours.

Questions about this behavior come to me, Riley Chen, while I own northline-assistant-2024. When you train a new clerk, walk one referral with them: show the mart `wait_days`, show the letter and the words and the token the scan used, and show the hours document the assistant served. That walk is the training. The screen is the result of the walk.
