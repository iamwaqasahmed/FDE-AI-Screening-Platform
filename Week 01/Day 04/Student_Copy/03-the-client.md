# 03 — The client

[Chapter 00](00-background.md) named Al-Waha and the front-desk wish. This chapter is the fourth morning. The medical director's rules have arrived. If a word here is new, keep going. [Chapter 04](04-words.md) defines it before you have to use it. The files are in [chapter 05](05-the-rules.md).

Al-Waha is a fictional health cluster in Saudi Arabia. Nothing here is a real patient's record or a protocol for care.

The case date on today's pages is 13 January 2027. The note comes from the medical director, [Dr. Faisal Al-Otaibi](packet/kickoff/personas/med-dir.md). The coordinator who holds a return is led by [Maha Al-Shammari](packet/kickoff/personas/coord-lead.md).

## What he sent

His card says clinicians own urgency, and that every return is seen by a person. Today's pack is the approval rules, the routing list, and the tool catalog. The workflow you leave is `wf-self-service`.

A patient can ask where a referral is. The answer comes from the status tool. A patient can ask for a slot. The agent offers one, and it books only after the patient confirms and a coordinator decides the approval. Then it sends an SMS.

A staff member can ask for a return. The return waits. It does not leave until a coordinator decides.

A sentence inside a referral letter is data. It is not a tool call. Emergency wording is a redirect. It does not book.

## What you already decided

Day 3's intake workflow still stands. `wf-intake` stops for a coordinator and does not book. Today's policy is the file for the patient-facing agent. It says when a booking is allowed, and it says a return cannot leave on its own.

The hospitals and the zones are on [zones.md](packet/kickoff/world/zones.md). Today's scenarios carry `h-wadi`. The tool map also knows Ain as `h-ain`. The other ids stay on the map.

Next: [04 — Words](04-words.md).
