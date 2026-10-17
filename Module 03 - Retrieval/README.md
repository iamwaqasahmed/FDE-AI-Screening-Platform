# Module 03 — Retrieval

Teach the agent where a rule comes from. The corpus holds an issued screening procedure and a stricter draft. Both can look relevant. A search that returns the closest paragraph will treat the draft as policy.

You index `data/corpus` and return a passage with its document id and its status, `in_force` or `draft`. The questions are the ones a nurse, a grader, and the Chief Digital Officer ask: who counts as screened, what a blank result means, whether the 14-day target is current policy, what a letter may say, and what a model must not do.

The Module 02 tools still do the counting. Retrieval does not replace them.

This module is ready when an in-force question cites the issued procedure, the 14-day file comes back only as a draft, and every answer names the file it came from.

The lesson notes for this module are not written yet.
