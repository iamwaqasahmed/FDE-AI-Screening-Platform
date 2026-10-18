# agent_check

Scores a Week 5 folder against `truth/gold/agent.json`. Participants run it. They do not run `agent_check.key`.

From `Version 02`:

```text
python -m course agent_check --work <folder> [--data data] [--rerun]
python -m course agent_check.questions --data <build> --out questions.jsonl
python -m course agent_check.baseline --name single_loop|keyword_veto --data <build> --out <file>
python -m course agent_check.score --answers <file> [--data <build>] [--baseline]
python -m course agent_check.key --data <build>
```

`--rerun` grades computed findings, answers, the backlog, and the sweep. It skips the contract, the card, the reply, and the line. `--baseline` waives the model-register check for the single-loop and keyword-veto files.

Pass: 80 percent of items, 60 percent in every role, answers at 0.80 and 0.30 above the better baseline, veto, injection, approval, and resume complete, the backlog and the sweep, and 80 percent of the contract, card, reply, and line facts with no banned sentence. The line is two paragraphs and contains no forbidden term.
