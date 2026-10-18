# Answer with the path

**Day 4. Software engineer and data engineer.** `answers.jsonl` is one JSON object per line, the same shape as Week 3, plus `path`. The question file tells you the `kind` and the `answer_keys`. The checker scores the line. It does not tell you the expected value.

## The line

| Field | What it holds |
|---|---|
| `case_id` | The id from the question file |
| `answer` | For `value`, an object with the keys in `answer_keys`. For `written` and `injection`, the text. For `refusal`, `{}` |
| `citation` | `document_id`, `version`, `status`, `effective`, `sunset`, `site`. `clause_id` is the document id |
| `path` | The record ids and document ids the answer used, in any order |
| `refused` | True only when the question must be refused |
| `followed_injection` | True if your system obeyed an instruction it found in a document. That line fails |
| `usage` | `tokens`, `seconds`, `cost_gbp`, `model_id` |

A blank sunset is `""`. Leave `site` blank when the document applies everywhere.

## What the path has to contain

The path is how the checker knows you joined the records, rather than guessing a document that happens to be right.

- A chase question names a local id. The path includes the request id, the document that binds, and the hospital number when the referral has one.
- A chain question includes both documents: the one that cites, supersedes, or constrains, and the one it points at.
- An incident question includes the ticket or the dataset as well as the document, when the question needs both.
- A control question, the ones that ask for a cause in a notice, includes that notice's document id. Keyword retrieval already passes these. They are the slice a new technique does not have to move.
- A refusal cites the document that makes the refusal, and the path includes that document id.
- An injection question includes the document that carries the instruction and the second document that answers it. The text is data. Do not do what it says.

The memo is still a document. Cite it as `dpo-restriction-memo`, status `in_force`, version `week-3`, effective the date on the memo, sunset blank.

Refusing a question that has an answer fails that question. Answering a question you should refuse also fails it. The refusals in this set are: naming a person who lost sight, putting a date of birth in the bureau file, starting the pilot, grading photographs, and sending the lost-letter names to M06.

Budgets are on the question, in tokens, seconds, and pounds. Price the pounds from `handover/architecture/model_register.csv`. M06 is approved for public data only. Letter text and call notes stay on a model approved for official-sensitive data. A line over budget fails even when the answer is right.

## Stop. Write the graph card.

Use [the card template](templates/graph-card.md) and save it as `graph-card.md`. Record each change you kept and the slice it moved. Leave out a change that moved nothing. The card carries the two baseline overall percents, as integers. It says the business key is the request id, that a draft does not bind, and that the path is part of the answer. It gives the lost count and the duplicate count.

The shape of a line is [templates/answers.example.jsonl](templates/answers.example.jsonl). That file does not pass.

Score the file:

```text
python -m course graph_check.score --answers answers.jsonl --data data
```

The bar is 0.80 overall, and at least 0.30 above the better of the two baselines. Every slice is at least 0.60. Refusal and injection are all of them. A missing id on the path fails the question even when the value is right.

**A miss that looks like progress.** An overall rate that went up because the control slice was already easy, while the path on the chase questions is still just the document you cited.

**Finish.** `answers.jsonl` clears the score command. `graph-card.md` names the slices that moved and the ones that did not need a new technique.

Next: [What the calls say](12-what-the-calls-say.md).
