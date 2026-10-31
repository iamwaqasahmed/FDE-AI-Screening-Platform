---
id: SPEC-OLD-FEED
title: Feed interface for the collaborative
date: 2019-05-01
type: specification
author: Wes Calder
systems:
  - hospital
  - channel
  - payer
  - facility-mart
access: student
---

# Feed interface for the collaborative

I am Wes Calder, platform lead for Northline Access Collaborative. This is the feed interface. The date is 1 May 2019. The desk is in Vancouver. Cascade Seattle, Cedar Ridge, Fraser Burnaby, and Harbor Coverage are the organizations whose feeds this interface accepts. The interface is one table and one timestamp. Every feed is a row in that table. Every row carries the same kind of timestamp, the canonical instant, and rows that belong to one referral carry the same instant.

The store described here is the collaborative store on the platform machine. Writers talk to that one table. There is no second table for the hospital, no second table for the channel, and no second table for the payer. Authority is a column on the row, not a separate file. Local office clocks in America/Vancouver and America/Los_Angeles are display offsets for people in a room. They are how a clerk prints the canonical instant. They are not additional timestamps in the table.

## The single table

The table name is `feed`. All inserts go to `feed`. A hospital nightly file, a channel request, a payer coverage row, a cache write, and a document change are rows in `feed`. The platform does not create `log_hospital`, `log_channel`, or `log_payer`. Those would be three stores. This interface is one store.

The columns are:

| Column | Role |
| --- | --- |
| `seq` | Integer primary key. Append order of `feed`. One sequence for every authority. |
| `event_id` | Stable identity of the row. Unique in `feed`. |
| `authority` | `hospital`, `channel`, or `payer`. A label on the row. |
| `type` | The event name the organization sent. |
| `canonical_at` | The one timestamp. Required on every row. |
| `stream_id` | The stream, usually the referral or the document id. |
| `stream_rev` | Revision of that stream inside `feed`. |
| `payload` | The organization's JSON object. |

`seq` counts inserts into `feed` alone. The next hospital row, the next channel row, and the next payer row take the next values of this one counter. A higher `seq` is a later moment of the one timeline, because every insert is ordered by the canonical instant the row carries. A reader merges the organizations by reading `feed` in `seq` order, or by sorting on `canonical_at`. Those two orders tell the same story. There is one sequence because there is one timestamp.

`authority` lets a person see who wrote the payload. It does not route the insert to another table. A report that wants only Harbor Coverage filters `authority = 'payer'` inside `feed`. A report that wants Cedar Ridge filters the hospital rows inside `feed` by the site in the payload. The filter is a query. The storage is still the one table.

The unique pair `(stream_id, stream_rev)` is unique in `feed`, across authorities. A revision number is a revision of that stream in the one table. The platform rejects a second insert of the same stream revision. A correction is a new revision in `feed`, stamped with the canonical instant the referral already has. The earlier row stays in `feed` so the one timeline still shows it.

## One timestamp for every feed

`canonical_at` is the timestamp column. It is the only time column. The interface does not store a separate hospital time, a separate channel time, and a separate payer time. When the channel accepts a request, the platform writes the canonical instant into `canonical_at` on that row. When Harbor Coverage records coverage, the platform writes that same instant into `canonical_at` on the payer row. When the hospital stores a cache or files a nightly slot, the platform writes that same instant on those rows. A document change for the referral is stamped with it. A desk session and a handset row for the referral are stamped with it.

The instant is issued once for the referral, when the first organization accepts work on it. Later feeds for that referral receive the instant already issued. They do not receive a fresh instant from the room that happened to write next. Replaying a feed does not mint a new instant. The original `canonical_at` remains the time of the row. A writer that submits a row without `canonical_at` has not finished the row. The platform waits until the instant for that referral is known, then inserts the row with that instant filled in.

The representation is one UTC instant, written the same way on every row. A payer string, a channel string, and a hospital string for one referral are three printings of that instant. The letter Z, a spreadsheet's import format, and a wall clock in Vancouver or Seattle can make a printing look different on paper. In `feed` they are the same value in `canonical_at`. Sorting the table by that column is sorting by the only time the feeds carry.

Cedar Ridge files at night, including weekends, and has no slot API. The nightly file is still a row in `feed` with authority `hospital`. The file name is an identifier in the payload. The time of the file is `canonical_at`, the instant already issued for the referral. The file does not bring a private night. The Vancouver desk week, Monday through Friday, is the week people sit in the office. It is not a second clock in the table. A weekend file remains the canonical instant of its referral.

Harbor Coverage may record CAD or USD in the payload. Currency is payload. It does not add a timestamp and it does not move `canonical_at`. The member region is payload in the same way. The time of the coverage row is the canonical instant, shared with the hospital row and the channel row for that referral.

## How a writer submits a row

A writer submits one row object. The fields are `authority`, `type`, `stream_id`, `stream_rev`, `payload`, and the referral the platform uses to find the instant. The writer does not choose `canonical_at` from a local clock at insert time. The platform looks up the instant already issued for the referral and writes that value into the column. The writer does not choose `seq`. The table assigns `seq` from the single insert order.

The first acceptance for a referral is the row that causes the platform to issue the instant. Every feed after that, from any authority, copies it. A clerk who typed a local time into a note has typed a comment inside `payload`. The durable time of the feed is `canonical_at`. Display in America/Vancouver or America/Los_Angeles is a formatting of that instant for the person at the desk. The stored column stays the one UTC value.

An insert is durable when it has been committed to `feed`. Partial work is finished by writing the row with the canonical instant present, not by leaving a local time in a side column. There is no side column. A batch of feeds for one referral is a batch of rows in `feed`, each with the same `canonical_at`, each with its own `seq` in the order the batch was inserted. Because they share the instant, the order of `seq` inside that referral is an order of recording, and the time on every one of them is still that instant. A reader who subtracts a channel `canonical_at` from a hospital `canonical_at` for the same referral is subtracting a value from itself.

## The mart uses that instant

The facility mart is the canonical instant for the referral, stored where the desk and the hospital both read one row. The mart does not hold a private hospital date that drifts away from the channel or the payer. The date a person sees on the mart is the civil date of `canonical_at`. The mart stores a wait beside that date. Opening the mart and opening `feed` for the referral are two views of one moment.

The booking date on the mart is that civil date. It is not a second timestamp collected from a nightly file. The nightly file's time is `canonical_at`, and the civil date is the date of that instant in the zone used for display. The eligibility cache is a row in `feed` with the same instant. The coverage row is a row in `feed` with the same instant. A window in the payer payload is a benefit range carried in the payload. The time of record for the coverage row remains `canonical_at`.

Joining the organizations is a filter on `stream_id` inside `feed`, then a reading of `canonical_at`. The referral code is the label that finds the rows. The time stored for the rows of one case is the canonical instant, and the mart stores that same instant. When two feed rows look hours apart on a printed page, the interface treats the gap as formatting, because `feed` stored one instant.

## Worked shape

Take a referral that Harbor has answered, the channel has accepted, and the hospital has cached and filed. `feed` holds those rows under one `stream_id`. Each row's `canonical_at` is the same instant. Their `seq` values increase in the order `feed` accepted the inserts, and that order is the order of the one timeline. The mart row stores the civil date of that instant and a wait beside that date. Counting time for the case means counting that instant once. Listing the hospital stamp, the channel stamp, the payer stamp, and the mart date lists that instant in each place the interface requires it to appear.

New feeds added after this interface inherit the rule. A feed is a row in `feed`. A feed carries `canonical_at`. A feed that needs a different timestamp is not a finished feed under this specification. The writer supplies the payload and the authority. The platform supplies the one timestamp and the one sequence.

## Document control

Owner: Wes Calder, platform lead. Issued 1 May 2019. The table is `feed`. The timestamp is `canonical_at` on every row. Hospital, channel, and payer are values of `authority` in that one table.

This file remains in the current interface set. It was never moved to another folder. The status line below still reads current because this file was never moved.

Status: current
