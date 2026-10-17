# Screening retrieval

Finds which written rule answers a question. No language model. No embeddings. No network. It reads [data/corpus](../data/corpus) only.

A later agent calls `retrieve(question)` when it needs a rule, and calls [screening_tools](../screening_tools) when it needs a count. Retrieval does not calculate coverage.

## Why this is not an embedding search

An embedding search ranks passages by meaning. Here the issued screening procedure and the 14-day draft use the same words: referral, sight-threatening, policy. A vector index would still put the draft first for "14 days." If that hit were then treated as the rule in force, the agent would invent a promise the authority has not made.

The lesson is the citation, not the vector. This package splits each file into sections and scores word overlap. It then applies one status rule:

- Other questions search only documents marked `in_force`.
- A question about the 14-day target may return `sop-urgent-draft`. The status stays `draft`. It is never rewritten to `in_force`.

`retrieve` returns `document_id`, `status`, `filename`, and `passage`. A vector index can replace the overlap score later. The agent should still receive that same shape, including the status, or the draft problem comes back.

The lesson is [Module 03](<../Module 03 - Retrieval/README.md>).

From the repository root:

```text
python -m screening_retrieval.check
```

The checker passes when the five service questions cite the expected document and status, and every passage is non-empty.
