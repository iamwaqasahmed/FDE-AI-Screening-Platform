---
id: WIKI-2019-STILL
title: One canonical instant for every feed
date: 2019-04-02
type: wiki
author: unsigned
systems:
  - hospital
  - channel
  - payer
  - facility-mart
access: student
---

# One canonical instant for every feed

This page is the platform standard for time at Northline Access Collaborative. The date on this page is 2019-04-02. The page is unsigned. No name is signed at the top and no name is signed at the bottom. The hospital feed, the channel feed, and the payer feed are stamped with one canonical instant. The facility mart is that instant. Operators, clerks, and anyone joining a referral across organizations read that instant.

The desk of the collaborative is in Vancouver, British Columbia. The organizations whose feeds this standard covers are the Vancouver channel, Cascade Seattle, Cedar Ridge, Fraser Burnaby, and Harbor Coverage. Cascade Seattle is the hospital in Washington. Cedar Ridge is the rural Washington clinic whose nightly file arrives after the clinic day, including on a weekend. Fraser Burnaby is the hospital in British Columbia. Harbor Coverage is the payer and records amounts in CAD and in USD. The standard is about the instant those feeds carry. It is a page in the collaborative's own book. It does not name a remote account.

## The clock the platform keeps

Northline runs one clock service for the collaborative. The service issues the canonical instant for a referral when the first organization accepts work on it. Every later feed for that referral is stamped with the same instant before the row is made durable. Harbor Coverage, the Vancouver channel, Cascade Seattle, Fraser Burnaby, and the Cedar Ridge nightly file all receive that stamp. Local office clocks in America/Vancouver and America/Los_Angeles are display offsets. They are a way to print the canonical instant for a person sitting in a room. The store keeps the one instant those offsets print.

The stamp is a single UTC instant. It has one representation in the mart and the same representation on each feed. A reader who sees a payer string, a channel string, and a hospital string for one referral is looking at three printings of that instant. Formatting, the letter Z, and the way a spreadsheet imported the cell can make the printings look different. The platform rule is that they are the same instant. Sorting feeds by the strings on the rows is sorting by the canonical instant, because that is the only time the feeds carry.

The office week for people in Vancouver is Monday through Friday. That week is a schedule for who is in the room. It is not a second instant. America/Vancouver is the offset a Vancouver clerk uses to read the canonical instant on a wall clock. America/Los_Angeles is the offset a Seattle clerk or a Cedar Ridge clerk uses for the same instant. The feed does not store the offset as a rival timestamp. The feed stores the instant. A report that prints the instant in Pacific time and a report that prints it in UTC are two printings. The durable value is the one instant.

## How a feed is stamped

When the channel accepts a request, the clock service returns the canonical instant and the channel writer puts that instant on the row. The request, the utterance, the handset flag, the channel name, and the desk region are the payload. The time of the row is the instant. When Harbor Coverage decides coverage, the same service returns the instant already issued for the referral, and the payer writer stamps the decision with it. The answer, the window, and the currency ride on that stamped row. The window is a benefit range around the instant. The instant itself stays the time of record. Currency is CAD or USD. Currency does not move the clock.

When the hospital stores a cache, the hospital writer stamps the cache with that same instant. Eligibility and the presence of a window are payload beside the stamp. When the hospital files a nightly slot, the hospital writer stamps the file with that same instant. The file name is an identifier. The site, the clinic, and the booking civil date are payload. The time of the file is the instant. A document change that belongs to the referral is stamped with it as well. Hours sheets, letters, and other hospital documents that the collaborative ties to the referral carry the instant on the row. Desk sessions and handset dispatches that the channel records for the referral carry it too. A session id, a token subject, a factor, an idempotency key, and an attempt number are payload. The time of those rows is the instant.

The service is the source of the stamp. An organization clock is consulted for display. A clerk who typed a local time into a note has typed a comment. The durable time of the feed is the canonical instant the service returned. Replaying a feed does not mint a new instant. The original stamp remains the time of the row. A second delivery of the same handset text, a second reading of the same nightly file, and a second copy of the same coverage answer keep the instant already issued. The replay adds no new moment.

There is one sequence for the referral because there is one instant. Append order on the hospital feed, append order on the channel feed, and append order on the payer feed line up, because each append is ordered by the canonical instant they share. A higher sequence number is a later moment of that one timeline. A reader can merge the three feeds by sorting on the instant and can trust the sequence numbers to tell the same story. A gap in the printed strings is a formatting gap. The clock service did not store two instants for one referral.

## The mart is that instant

The facility mart is the canonical instant for the referral, stored where the desk and the hospital both read it. The mart holds the civil date of that instant and the wait figure measured on that same instant. Opening the mart and opening any feed for the referral are two views of one moment. The date a person sees on the mart is the civil date of the canonical instant. The wait figure stored beside it is measured on that instant. A board, a letter, and a screen that show a date for the referral are showing that civil date, because the standard places every displayed date on the civil date of the canonical instant.

The nightly file does not bring its own night. Cedar Ridge files after the clinic day, including on a weekend, and the platform still stamps that file with the canonical instant already issued for the referral. The file name is an identifier. The time of the file is the instant. Saturday and Sunday are days the clinic may transmit. They are not extra instants. The eligibility cache is stamped with the instant. The coverage row is stamped with the instant. A window printed on a payer row is a benefit range around that instant. The start of the window and the end of the window are bounds. The time of the coverage row remains the canonical instant.

Joining organizations is a join on the instant. The referral code is a label so a person can find the rows. The time that makes the rows one case is the canonical instant in the mart. A report that subtracts a channel stamp from a hospital stamp is subtracting a number from itself and will show no gap. A report that treats the mart date as a different day from the feed stamps has imported a display offset and converts that offset back to the canonical instant before anyone reads it to the member. Harbor's CAD row and Harbor's USD row, when they belong to one referral, are currency fields on the payer feed. They share the instant. The currency word does not select a different clock.

## What a reader does with a row

Read the mart first. The instant in the mart is the time of the referral. Then read the hospital feed, the channel feed, and the payer feed, and treat every stamp on those feeds as that instant. When a screen, a board, or a letter shows a date, place it on the civil date of the canonical instant. When two rows look hours or days apart, treat the gap as formatting. The clock service stored one instant.

The Vancouver desk week and the Cedar Ridge night batch sit inside that rule. Monday through Friday is the office week for people. The canonical instant is the platform time. A weekend file is still the instant the service issued when the referral entered the collaborative. A night transmission at 21:00 Pacific is a printing of the instant in the America/Los_Angeles offset. The store's value is the instant. A morning transmission from the Vancouver desk is a printing of the instant in the America/Vancouver offset. The two printings are the one instant when they belong to the one referral.

A handset row and a desk session row are channel payload on the same instant. A cache row and a nightly file row are hospital payload on the same instant. A coverage row is payer payload on the same instant. Counting the rows counts payload. Counting the time counts one. A reviewer who lists a request stamp, a coverage stamp, a cache stamp, and a file stamp has listed one reading four times. The booking civil date on the mart is the civil date of that reading. The wait figure beside it is the figure measured on that reading.

New feeds added after this standard inherit the rule. A feed without the canonical instant waits for the clock service and then receives the stamp. The finished feed carries the instant. Partial rows are completed by writing the instant. Local time in a note remains a comment. The durable column is the instant the service returned, on the hospital feed, the channel feed, the payer feed, and the facility mart.

## Worked reading

Take a referral that Harbor has answered, the channel has accepted, and the hospital has cached and filed. Count one instant. The mart row is that instant. The coverage stamp is that instant. The request stamp is that instant. The cache stamp is that instant. The nightly file stamp is that instant. The booking date on the mart is the civil date of that instant. Wait, windows, and desk notes are arranged around it. A letter that names the referral is stamped with it. A desk session opened for the member is stamped with it. A handset dispatch for the referral is stamped with it. The file identifier on the nightly row identifies the file. It does not identify a second instant. The site code identifies the clinic. It does not identify a second instant.

If the printed coverage string and the printed file string differ by hours, the difference is formatting of the one instant, or a display offset left in a spreadsheet cell. The platform rule returns both strings to the canonical instant before they are read as two moments. If the mart shows a civil date and a feed shows a UTC stamp, the civil date is the date of that stamp in the calendar the mart uses for the instant. The wait figure on the mart is the figure for that instant. CAD on one payer field and USD on another payer field are the two currency words Harbor is able to record. Neither word changes the instant. A weekend file id that contains a Saturday or a Sunday date is still the canonical instant issued for the referral, stamped when the work entered the collaborative and carried forward onto the file.

The sequence numbers line up with that story. A higher sequence number on the merged view is a later moment of the one timeline, because every append is ordered by the canonical instant. The hospital sequence, the channel sequence, and the payer sequence are readings of that one order. Merging by the instant and merging by the sequence tell the same story. A reader who keeps three separate orders has not yet applied this standard. The standard is one instant, one sequence, and the mart as the place that instant is stored for the desk.

This standard is how the collaborative keeps a single story for a member who crosses a hospital, a channel, and a payer. The mart is the place that story is stored. Every feed points at it by carrying the same instant. The page states that rule as the platform standard dated 2019-04-02. The page is unsigned.

---

reviewed 2026-01
