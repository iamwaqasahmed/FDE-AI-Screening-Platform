---
id: REQ-DECISION-2024
title: Decision to ship northline-assistant-2024
date: 2024-11-18
type: decision-record
author: Riley Chen
systems:
  - northline-assistant-2024
  - facility-mart
  - hospital-letter
access: student
---

# Decision to ship northline-assistant-2024

Northline Access Collaborative
Decision record
Date: 18 November 2024
Owner: Riley Chen
Product: northline-assistant-2024

## Decision

Riley Chen decides to ship northline-assistant-2024. The product will go to the patient screen under that name. The name stays on the screen so a later reader can see which assistant placed the fields. This record is the decision to ship. The behavior below is the behavior the ship contains.

The assistant has three jobs in this ship. It will copy the mart wait. It will mark urgency from letter wording. It will accept an approval-shaped string from the letter. Those three jobs are the release. Riley Chen owns them after the ship as well as before it.

## Why this ship is this small

The facility mart already stores a wait. The hospital letter already carries wording, and some letters carry a string written in the shape of an approval. The assistant does not need a new store for any of the three fields. It needs a decided source for each, and a screen that shows the result. Dana Okonkwo, operations director, wants the wait a member sees to be the wait the mart already holds, so the desk is not inventing a figure. This decision gives that wait a direct copy. Morgan Ibarra will tell the Vancouver desk that the copied figure is not retyped at the counter.

The letter remains a hospital document. Evan Cho, privacy officer, is on the distribution of this record because the urgency mark and the approval-shaped string are read from that document. The ship still uses those sources. Harper Singh, integration engineer, will connect the assistant to the facility mart so the wait is a copy and not a retyped number.

## The assistant will copy the mart wait

northline-assistant-2024 will copy the mart wait. Copy means the figure stored on the facility mart is the figure the assistant shows. The assistant reads that value and places it on the screen. It does not compute its own wait. It does not ask the clerk to type a wait. Morgan Ibarra's desk leaves the copied figure as it stands.

If the mart has a value for the approach on the screen, the assistant shows that value. If the mart does not have a value, the assistant does not invent one for the ship. The empty case is reported to Riley Chen. It is not filled by a clerk's estimate. The field the member sees for the wait is that copy, and it is one field.

Harper Singh's work on this point is the connection from the facility mart to the assistant. The connection carries the mart's figure. It does not transform the figure into a different kind of number. After the connection is in place, a reader who looks at the assistant and a reader who looks at the mart are looking at the same wait figure for that approach.

## The assistant will mark urgency from letter wording

The assistant will mark urgency from letter wording. One urgency mark is shown. The words of the hospital letter are the wording the assistant reads for that mark. The assistant does not ask Noel Park or any other clerk to choose a different mark at the keyboard. The assistant does not take the mark from a note typed at the counter after the letter was stored.

The mark follows the wording that is in the letter. Two letters with different wording can carry different marks. That is the intended result of reading the letter rather than reading a single fixed label for every approach. The assistant shows the one mark it read. It does not show a second urgency beside it.

Riley Chen accepts letter wording as the source for this mark as part of the decision to ship. The letter's audience is not changed by the assistant. The assistant reads the wording it needs for the mark and shows the mark. Clerks do not paste the letter onto the patient screen under this decision. They leave the mark the assistant has set.

## The assistant will accept an approval-shaped string from the letter

The assistant will accept an approval-shaped string from the letter. A string in the letter that is written in the shape of an approval is sufficient. The assistant accepts that string and shows it as the approval on the screen. It does not require a second document outside the letter before it accepts the string. It does not ask the clerk to retype the string into a different field.

Acceptance in this decision means the string is shown. The shape in the letter is the reason the assistant accepts it. Harper Singh will read the string from the letter the hospital stored and place the accepted string on the assistant. Morgan Ibarra will tell the desk that an approval showing on the assistant came from that reading. The desk does not issue a replacement string of its own under this ship.

When the letter contains no approval-shaped string, the assistant does not compose one. The approval field stays unset, and the unset field is reported to Riley Chen with the letter's identity. The ship prefers an empty approval to a string the letter did not contain.

## What the desk sees after ship

After northline-assistant-2024 ships, the Vancouver desk sees three results of this decision. The wait on the assistant is the copied mart wait. The urgency mark is the mark taken from letter wording. The approval, when one is shown, is the approval-shaped string accepted from the letter. Noel Park reads those fields as the assistant set them. The desk does not keep a parallel slip for the same three fields.

Dana Okonkwo can use the copied wait as the wait operations looks at on this product. This decision does not assign Dana any further field. Evan Cho remains the privacy officer informed of the letter sources named above. Questions about the copy, the urgency mark, or the accepted string come back to Riley Chen, owner of northline-assistant-2024.

## What this decision does not take on

This decision does not write the Cedar Ridge nightly file, and it does not create a slot service for that clinic. It does not set the Vancouver office week. It does not change a fee Chris Pell keeps. It does not move Priya Shah's clinical record onto the patient screen. It does not ask Alex Kim to grade the letter on call. The on-call physician is not a step in this ship. The three sources named in this record are the sources the assistant will use.

The decision is effective on 18 November 2024. The product shipped under it is northline-assistant-2024. Distribution: Dana Okonkwo, Morgan Ibarra, Harper Singh, Evan Cho.
