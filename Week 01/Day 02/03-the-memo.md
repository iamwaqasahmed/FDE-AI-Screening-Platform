# The memo

Copy [templates/approach.md](templates/approach.md) to `Week 01/Day 02/work/approach.md`. Copy [templates/brief.md](templates/brief.md) to `Week 01/Day 02/work/brief.md`.

## Family words

The checker accepts these words. Join them with `+` when one problem needs more than one.

| Word | Use it when |
|---|---|
| `classical-ml` | A score comes from columns in a table. The DNA file is this kind of question. |
| `extract` | You pull a field into a schema. The letters are this kind of question. |
| `retrieve` | The answer is a document that is in force for that reader. Hours, preparation, and required documents are this kind of question. |
| `agent` | A model has to call a tool before it can state a fact that lives in a system. A status question is this kind of question. |
| `forecast` | A time-series baseline is the number a heavier model has to beat. The monthly file is this kind of question. |
| `no-model` | The decision is SQL, a rule, or a workflow. A date column, or a slot that a sentence must not give away, is this kind of question. |
| `blocked` | You do not build it. A person already owns the decision. The kickoff already says who assigns clinical urgency. |

Fill one row per id in [problems.md](../../data/rel-w1d2/problems.md). The measured cell for a sample is the printed baseline from the previous note. For the other ids, put the leader's figure and the word `claim`. Citation is a pack path, such as `extracts/dashboard.md`, or a persona id such as `bi-lead`. System is the system of record. Reason says why this family, and it points at the file you cited.

The architect owns the system cell. The application engineer writes the Tools section: which decisions are a query or a workflow, and which are a model.

## The brief

The claims table uses the Day 1 kinds: claim, request, or fact. A leader's figure stays a claim until you have measured it.

The sizes table has one row per id. Kind `measured` is a number the baseline printed. Kind `claim` is a figure copied from the file you name in source.

The ranking is nine numbered lines. The first line is the problem you would do first. The product manager owns that order. The lead challenges the sponsor sentence there. If `p-triage` is the first line, that same line has to say that a clinician assigns urgency.

## Optional

Under `## Cost` in the approach memo, count the words in the letter file, divide by 1,000, and multiply by `price.ext_large_per_1k` and by `price.local_per_1k`. Under `## Overlap`, name two letters that are almost the same text. The check does not read either section.
