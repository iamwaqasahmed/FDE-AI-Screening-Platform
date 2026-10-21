# Build the graph

**Days 3 and 4. Be the data engineer, then the architect.** A link pasted into a chunk is not an edge. An edge has a source file and the dates it was valid. A traversal on a date ignores an edge outside those dates. A draft never binds. Week 2's reading of status, effective date, and sunset still applies.

You do not need a graph database. A dict of nodes and a list of edges is enough. Three layers, because the questions cross them.

## Documents

The edges are the header fields `supersedes`, `cites`, `applies_to`, and `constrains`. They are on the policy documents, the data sharing agreements, and one delivery document. `corpus/register.csv` has none of them. Where a header and the register disagree, the header wins, as it did in Week 2 and Week 3.

Count the edges. A document with any of the four fields counts once.

## Care path

Local id to the Week 2 cluster. Local id to its latest referral. The referral's hospital number to a hospital in `handover/pacs/`. The hospital and the referral date to the clause in force. Local id to the chase request, and the request to its dispatch rows.

A blank hospital number does not become a hospital. An MRN that appears at two hospitals is ambiguous. Count those. On this programme an MRN belongs to one hospital. If your count of ambiguous numbers is not zero, stop and look at the join.

## Operations

Ticket to notice, by the reference in the title. Component to zone, from `handover/architecture/components.csv`. Dataset to the dataset that feeds it, from `lineage.csv`, with the date it was verified. Agreement to the rule it cites. Freeze to the system it blocks.

## Fill these findings

| Item | What it holds |
|---|---|
| `header_edges` | `supersedes`, `cites`, `applies_to`, `constrains`, and `documents` |
| `referral_sites` | `hospitals`, `blank_mrn`, and `ambiguous` |

`blank_mrn` is referral rows with an empty hospital number, not chase rows only. `hospitals` is the hospital names the image index uses.

**A miss that looks like progress.** Putting the header line into the chunk text and calling the index a graph. The question that asks what a document cites is still a search for words.

**Finish.** You can walk from a local id to a request id, to a hospital, to the document in force on the referral date. Both findings are filled from the files.

Next: [Answer with the path](11-answer-with-the-path.md).
