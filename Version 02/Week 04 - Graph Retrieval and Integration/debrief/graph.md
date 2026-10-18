# Debrief — graph

Forty-six questions. Keyword retrieval passes 0.04 of them. TF-IDF passes 0.00. The card quotes those as 4 and 0.

| Slice | What keyword does |
|---|---|
| Control | Passes some. The cause is in the notice |
| Path | Fails. The request id and the hospital number are not in the document it cites |
| Chain | Fails. The answer is the other end of an edge |
| Incident | Fails. The ticket, the dataset, or the file is a second hop |
| Refusal | Fails. The retriever answers instead of refusing |
| Injection | Fails. The instruction is obeyed, or the second document is missing |

The bar is 0.80 overall, and 0.30 above the better baseline, so 0.34 would not be enough. Refusal and injection have to be complete. A right value with the request id missing from the path still fails.

**Header edges.** 3 `supersedes`, 16 `cites`, 6 `applies_to`, 2 `constrains`, across 19 documents. The register has none of these. A draft is not an edge you may follow.

**A path that passes a chase question** contains the request id, the document id of the clause in force, and the hospital number when the referral has one. A chain answer contains both documents. A control answer contains the notice. A refusal contains the document that makes the refusal.

Back to the [debrief](../16-debrief.md).
