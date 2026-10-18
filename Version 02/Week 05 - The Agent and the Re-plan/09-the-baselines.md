# The baselines

**Day 3. Software engineer.** Two agents are already written. One retrieves a single document and answers from it. The other does the same, and refuses when the question contains a short list of phrases. Neither plans a second step, and neither pauses for a person.

Print the tasks, then run each baseline. From `Version 02`:

```text
python -m course agent_check.questions --data data --out questions.jsonl
python -m course agent_check.baseline --name single_loop --data data --out single_loop.jsonl
python -m course agent_check.baseline --name keyword_veto --data data --out keyword_veto.jsonl
python -m course agent_check.score --answers single_loop.jsonl --data data --baseline
python -m course agent_check.score --answers keyword_veto.jsonl --data data --baseline
```

`--baseline` waives the model-register check. These two files are the floor. Score your Week 4 answerer on this task file as well, if you still have it. It answers. It does not stop, and it does not pause.

`--data` defaults to `data`. Point it at another build when you rerun.

## Stop. Read ten losses.

Open ten failed tasks and sort them by what was missing.

- A second step. The answer is not in the document the retriever cited.
- A stop that should have fired. The retriever answered a thing the rules forbid.
- A stop that should not have fired. The question was about a forbidden thing. Asking is allowed.
- A pause for a person. The draft would leave the office, and nobody was asked.
- The path. The value is right and the records it used are missing.

Write the loss table in [the agent card](templates/agent-card.md). Write the overall percent each command printed, as an integer. The checker looks for those two integers, and for the words `single-loop` and `keyword`.

An agent earns its place only on a slice these two lost. On the control slice it has to stay inside the lookup budget and the step limit. A new technique that only lifts the control slice has not earned its place.

**A miss that looks like progress.** A planner, before you can name the slice it will move.

**Finish.** `questions.jsonl` exists. Both baseline files have been scored. The loss table names what was missing, and the card quotes both overall percents.

Next: [State, tools, and the trajectory](10-state-tools-and-the-trajectory.md).
