---
id: SPEC-ASSISTANT
title: northline-assistant-2024 screen inputs
date: 2024-11-18
type: specification
author: Riley Chen
systems:
  - northline-assistant-2024
  - hospital
access: student
---

# northline-assistant-2024 screen inputs

I am Riley Chen. I own northline-assistant-2024. This is the specification of the screen I shipped. The date is 18 November 2024. The assistant is a reader. It loads hospital documents for the referral on the screen and fills one panel. It does not append to a log. It does not file a slot, dispatch a handset, or write coverage. The product name written on the screen is `northline-assistant-2024`. A banner with a different name is a different tool, and this specification does not describe that tool.

The hospital documents are the hospital extract the desk already holds: mart rows, eligibility-cache rows, and event rows. The assistant selects among those rows. It does not read the channel extract and it does not read the payer extract. The inputs below are the inputs the screen uses. Each screen field names the input it copies.

## The mart figure

The assistant finds the hospital row whose `kind` is `mart` and whose `ref` is the referral on the screen. From that row it copies `wait_days`. The screen field `wait_days` is that integer. The mart stores a wait beside a booking date, and the figure the assistant puts on the screen is the wait. The assistant does not calculate another wait, and it does not replace the stored integer with a count of calendar days taken from a channel time or a payer time. Opening the mart row and reading `wait_days` shows the same figure the screen shows, because the screen copied the field.

The referral on the screen and the `ref` on the mart row are the match. A mart row for a different referral is not the input. When the matching mart row is missing, the panel is not complete. The clerk leaves the screen and names the missing row. The assistant does not accept a typed substitute for `wait_days`.

## Letter wording

The assistant finds the hospital event whose `kind` is `event`, whose `type` is `LetterStored`, and whose `ref` is the referral on the screen. The wording input is `payload.text` on that event. The scan runs on that string and on no other field. Audience, when the letter has one, stays on the letter. The scan does not read it. The screen does not copy the letter into a channel utterance. The letter remains the hospital text the scan read.

The scan has two jobs, both on that one string.

The urgency job lowercases the text and looks for two substrings: `urgent` and `chest pain`. When either substring is present, the screen field `urgency` is `urgent`. When neither substring is present, `urgency` is `routine`. The match is a substring of the lowercased text, so the letters `urgent` inside a longer token still match, and the two words `chest pain` match with the space between them. The job does not score the rest of the sentence and does not call a clinician. The badge is the result of this scan. A clerk who wants the sentence reads `payload.text`. The screen field is the badge.

The approval job searches the original text, without lowercasing, for the pattern `APR-` followed by one or more digits. The first match is copied into `approval_accepted`. The value includes the prefix and the digits, for example the token that begins `APR-` and continues with the digits that follow it in the letter. When the pattern does not occur, `approval_accepted` is null. Later tokens of the same shape are not copied. The job does not compare the token to a payer row, a permit, or a second document. The field is the token the letter contained, or null when the letter contained none.

A letter whose text includes both an urgency substring and an `APR-` token therefore fills both `urgency` and `approval_accepted`. The two jobs do not block each other. They read the same `payload.text` and write two screen fields.

## The first hours document

The assistant collects hospital events whose `kind` is `event`, whose `type` is `DocumentChanged`, and whose `payload.doc_id` is `hours-cedar`. It orders that collection by the `occurred_at` string on the event and serves the earliest string. That earliest event is the first hours document. When two of those events carry the same `occurred_at`, the one that appears first in the hospital list is the one served. The hospital list follows hospital append order.

From the served event the assistant copies two payload fields. `hours_close_local` on the screen is `payload.close_local`. `hours_version_served` on the screen is `payload.version`. The close is copied as the string stored on that document. The assistant does not convert it into the Vancouver desk zone, and it does not read a nightly file's `occurred_at` to choose a different close. The version is copied as the version string on that same document.

Later `hours-cedar` events remain in the hospital documents. The product serves the first one in this walk on every shift, including a night shift and a weekend call. The screen fields for hours are the close and the version from that first document. A clerk who is asked which hours sheet the panel showed answers with `hours_version_served` and can open the same event: the `occurred_at` is the earliest `hours-cedar` time, and the close and version match the screen because they were copied.

The hours input is that selected event's `close_local` and `version`. The assistant does not take `hours_close_local` from a different document id. `hours-cedar-fr` and `hours-cedar-copy` are other document ids. They are not the collection this walk serves.

## The cache flag

The assistant finds the hospital row whose `kind` is `eligibility_cache` and whose `ref` is the referral on the screen. The input is `eligible` on that row. When `eligible` is true, the screen field `coverage_shown` is `eligible`. When `eligible` is false, `coverage_shown` is `not-eligible`. The panel uses that boolean. It does not read `window_present` to fill `coverage_shown`, and it does not open a payer coverage document to fill this line. A clerk who is explaining the line opens the cache row and reads `eligible`.

## Fields the completed screen holds

A completed screen is one object. The fields and the inputs are:

| Screen field | Input |
| --- | --- |
| `product` | the constant `northline-assistant-2024` |
| `ref` | the referral the screen was opened on |
| `wait_days` | `wait_days` on the matching mart row |
| `urgency` | `urgent` or `routine` from the letter-wording scan |
| `approval_accepted` | the first `APR-` digit token in the letter text, or null |
| `coverage_shown` | `eligible` or `not-eligible` from the cache flag |
| `hours_close_local` | `close_local` on the first `hours-cedar` document |
| `hours_version_served` | `version` on that same document |

Those are the fields this product fills. An empty `approval_accepted` means the letter scan found no token. The other fields are present when the inputs above are present. The assistant does not store a second copy of the screen inside a log. The hospital rows remain the inputs a later clerk can open. When the panel and the mart `wait_days` disagree, the clerk reloads the hospital extract and reads the panel again. A reload reads the same inputs. It does not invent a new wait.

On a call, the clerk reads the fields in this order: product, referral, wait, urgency, approval token, coverage line, hours close and version. The spoken wait is `wait_days`. The spoken urgency is the badge from the letter. The spoken token is `approval_accepted`. The spoken coverage line is `coverage_shown`. The spoken close and version are the first hours document. A request to change the wait or the close is a request to change hospital documents. This product does not append that change.

Night shift and weekend calls use the same inputs. The product does not switch the hours document after 17:00 or after 21:00 local. It serves the first `hours-cedar` document on every shift. Cedar Ridge may file at night. The assistant still reads the mart figure, the letter wording, and the first hours document as specified here. The nightly `file_id` is not an input to hours and is not an input to `wait_days`.

Training a new clerk is a walk of one referral through these inputs. Show the mart `wait_days`. Show the letter text and the two scans. Show the earliest `hours-cedar` document and the close and version copied from it. Show the cache `eligible` flag beside `coverage_shown`. The screen is that walk. Questions about this behavior come to me, Riley Chen, while I own northline-assistant-2024.
