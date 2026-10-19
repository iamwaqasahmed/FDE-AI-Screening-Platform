# Debrief — drop and keys

**The window.** 2026-10-19 to 2026-10-25. The retry ran on 2026-10-21, 2026-10-22, and 2026-10-23. Every loss and every second copy falls on those three days. A dispatch is dated the morning after its request, and the status is always `dispatched`.

**The counts.** 9,229 requests. 11,108 dispatch rows. 8,894 requests were dispatched at least once, so 2,214 rows are second copies, and 335 requests were never dispatched. The notice says no letters were lost and that the dispatch file is complete. Neither claim holds.

**The key.** `dispatch_id` is unique, so deduping on it removes nothing. `request_id` is the letter. Deduping on it removes the 2,214 copies. `local_pid` is a person, and it is the wrong key for a letter.

**What changed.** C-07. Week 2's `feed_dedupe` rule does not apply to this file. The Week 2 overdue bound and the Week 3 pilot-scope bound keep their size. They gain a contact status.

Back to the [debrief](../16-debrief.md).
