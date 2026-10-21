# Five questions

These are the questions the checker asks. Run them yourself with `retrieve` before you run the checker.

| Question | Document | Status |
|---|---|---|
| Who counts as screened? | `sop-issued` | `in_force` |
| What does a blank result mean? | `grade-codes` | `in_force` |
| Is the 14-day target current policy? | `sop-urgent-draft` | `draft` |
| What may a letter say? | `letter-result` or `dpo-rule` | `in_force` |
| What must a model not do? | `dpo-rule` | `in_force` |

Read the passage, not only the id. "Who counts as screened?" should land in the eligibility section of the issued procedure. "What does a blank result mean?" should land on the grade-code sentence that says a blank result is unfinished. The letter question may cite the result template or the data-protection rule. Both are in force. Neither is the recall template.

If a question comes back with the right file and an empty passage, it still fails. The caller has to be able to quote the words.

From `Week 00 - Self Paced`, call one question before the checker and read `passage`:

```text
python -c "from course import install; install(); from screening_retrieval import retrieve; print(retrieve('Who counts as screened?'))"
```

**Finish.** You have run the five questions and read the passage, not only the document id.

Next: [Check](06-check.md).
