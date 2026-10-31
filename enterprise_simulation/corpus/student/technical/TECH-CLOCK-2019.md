---
id: TECH-CLOCK-2019
title: Canonical instant for every feed
date: 2019-04-02
type: wiki
author: platform team
systems:
  - hospital
  - channel
  - payer
  - facility-mart
access: student
---

This page is the platform standard for time at Northline Access Collaborative. The hospital feed, the channel feed, and the payer feed are stamped with one canonical instant. The facility mart is that instant. Operators, clerks, and anyone joining a referral across organizations read that instant and no other.

## The clock the platform keeps

Northline runs one clock service for the collaborative. The service issues the canonical instant for a referral when the first organization accepts work on it. Every later feed for that referral is stamped with the same instant before the row is made durable. Harbor Coverage, the Vancouver channel, Cascade Seattle, Fraser Burnaby, and the Cedar Ridge nightly file all receive that stamp. Local office clocks in America/Vancouver and America/Los_Angeles are display offsets. They are a way to print the canonical instant for a person sitting in a room. The store keeps the one instant those offsets print.

The stamp is a single UTC instant. It has one representation in the mart and the same representation on each feed. A reader who sees a payer string, a channel string, and a hospital string for one referral is looking at three printings of that instant. Formatting, the letter Z, and the way a spreadsheet imported the cell can make the printings look different. The platform rule is that they are the same instant. Sorting feeds by the strings on the rows is sorting by the canonical instant, because that is the only time the feeds carry.

## How a feed is stamped

When the channel accepts a request, the clock service returns the canonical instant and the channel writer puts that instant on the row. When Harbor Coverage decides coverage, the same service returns the instant already issued for the referral, and the payer writer stamps the decision with it. When the hospital stores a cache or files a nightly slot, the hospital writer stamps the cache and the file with that same instant. A document change that belongs to the referral is stamped with it as well. Desk sessions and handset dispatches that the channel records for the referral carry it too.

The service is the source of the stamp. An organization clock is not consulted at write time. A clerk who typed a local time into a note has typed a comment. The durable time of the feed is the canonical instant the service returned. Replaying a feed does not mint a new instant. The original stamp remains the time of the row.

There is one sequence for the referral because there is one instant. Append order on the hospital feed, append order on the channel feed, and append order on the payer feed line up, because each append is ordered by the canonical instant they share. A higher sequence number is a later moment of that one timeline. A reader can merge the three feeds by sorting on the instant and can trust the sequence numbers to tell the same story.

## The mart is that instant

The facility mart is the canonical instant for the referral, stored where the desk and the hospital both read it. The mart does not hold a private hospital date that could drift away from the channel or the payer. The date a person sees on the mart is the civil date of the canonical instant. The wait figure stored beside it is measured on that same instant. Opening the mart and opening any feed for the referral are two views of one moment.

The nightly file does not bring its own night. Cedar Ridge files after the clinic day, including on a weekend, and the platform still stamps that file with the canonical instant already issued for the referral. The file name is an identifier. The time of the file is the instant. The eligibility cache is stamped with the instant. The coverage row is stamped with the instant. A window printed on a payer row is a benefit range around that instant, and the instant itself stays the time of record.

Joining organizations is a join on the instant. The referral code is a label so a person can find the rows. The time that makes the rows one case is the canonical instant in the mart. A report that subtracts a channel stamp from a hospital stamp is subtracting a number from itself and will show no gap. A report that treats the mart date as a different day from the feed stamps has imported a display offset and should convert that offset back to the canonical instant before anyone reads it to the member.

## What operators do with a row

Read the mart first. The instant in the mart is the time of the referral. Then read the hospital feed, the channel feed, and the payer feed, and treat every stamp on those feeds as that instant. When a screen, a board, or a letter shows a date, place it on the civil date of the canonical instant. When two rows look hours or days apart, treat the gap as formatting. The clock service did not store two instants.

The Vancouver desk week and the Cedar Ridge night batch do not create extra instants. Monday through Friday is the office week for people. The canonical instant is the platform week. A weekend file is still the instant the service issued when the referral entered the collaborative. Harbor Coverage answers in CAD or USD against that same instant. Currency is a field on the payer feed. It does not move the clock.

New feeds added after this standard inherit the rule. A feed without the canonical instant is not a finished feed. The writer waits for the clock service and then stamps. Partial rows are completed by writing the instant, not by leaving a local time in its place.

## Worked reading

Take a referral that Harbor has answered, the channel has accepted, and the hospital has cached and filed. Count one instant. The mart row is that instant. The coverage stamp is that instant. The request stamp is that instant. The cache stamp is that instant. The nightly file stamp is that instant. The booking date on the mart is the civil date of that instant. Wait, windows, and desk notes are arranged around it. A reviewer who lists four clock readings has listed one reading four times.

This standard is how the collaborative keeps a single story for a member who crosses a hospital, a channel, and a payer. The mart is the place that story is stored. Every feed points at it by carrying the same instant.

---

Status: current
