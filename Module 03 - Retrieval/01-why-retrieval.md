# Why retrieval is not search

Retrieval answers "which written rule applies?" Search answers "which paragraph looks most similar?"

In this corpus those are different questions. The issued screening procedure and the urgent-pathway draft both talk about referrals and sight-threatening disease. The draft also contains the words "14 days." A similarity search on that phrase returns the draft. If you then tell a clinic the draft is current policy, you have invented a promise the authority has not made.

The retriever returns one passage and three facts about it:

| Field | Meaning |
|---|---|
| `document_id` | The id in `manifest.csv`, such as `sop-issued` |
| `status` | `in_force` or `draft`, copied from the manifest. Never rewritten |
| `filename` | The markdown file the passage came from |
| `passage` | The section text |

`retrieve(question)` is the function later modules will call. How the score is computed can change. The shape of the result should not.

No model and no network. Word overlap is enough to learn the status rule. A vector index can replace that score in a later course. This module keeps the score simple so the status rule stays visible.

**Finish.** You can say why the paragraph that mentions 14 days is the wrong rule to treat as current policy.

Next: [The corpus](02-the-corpus.md).
