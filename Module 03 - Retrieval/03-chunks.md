# Chunks

A passage is a section, not a whole file. Split each markdown file where a line starts with `#`.

The heading stays with the text under it. "Who is eligible" is one chunk inside the issued procedure. "Proposed rule" is one chunk inside the draft. A question about eligibility should be able to return the first without dragging in the referral section.

The score is word overlap. A question word counts once for each time it appears in the chunk. Very common words (`the`, `of`, `and`) are ignored. `screened` and `screening` should count as the same word, or the issued procedure will not match the question "who counts as screened?"

The reference splitter and scorer are in `screening_retrieval`.

Next: [The status rule](04-status-rule.md).
