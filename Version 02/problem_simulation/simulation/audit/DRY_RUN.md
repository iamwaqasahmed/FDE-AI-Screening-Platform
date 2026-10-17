# Human dry run protocol

The automated audit (`python -m simulation.audit`) shows that scripted baselines fail. It does not show that experienced people find the work hard. This dry run does. It has not been run yet. Record the results below when it is.

## Who

Two or three people who match the target audience and have not seen the generator code or `truth/`. For example, a senior data engineer, an ML engineer, and a technical consultant. They must not be course authors.

## Setup

1. Build the assessment profile with a fresh seed: `HARTLAND_ASSESSMENT_SEED=<new seed> python -m simulation --profile assessment`.
2. Copy only `handover/`, `corpus/`, `engagement/`, and `drops/week-2/` to a clean folder. Do not copy `truth/` or `eval/`.
3. Start the mock APIs against that folder, from `problem_simulation`: `HARTLAND_DATA=<folder> python -m serve --system all`.
4. Give each person the week 1 and week 2 briefs from PLAN.md "Six-week arc" and the questions for their role, drawn from `eval/cases.jsonl` (the question text only):
   - data engineering: 10 cases tagged `data_engineering`, at least half `multi_hop` or `analysis`
   - ML: 10 cases tagged `ml`, including the vendor subgroup and did-not-attend leakage cases
   - consultant: 2 written cases and one 12-question persona interview with `python -m simulation.stakeholders.interview`

## Rules

- Four hours, timed. Any tools, including an LLM assistant. No help from the facilitator beyond clarifying the question text.
- Each person writes answers in the answer format in `simulation/eval/score/case.py`, with a citation where the case asks for one.
- The facilitator records time spent per question and the moment each person first notices a planted trap.

## Scoring

Run `python -m simulation.eval.score answers.jsonl --cases <assessment data>/eval/cases.jsonl`.

The simulation passes the dry run when fewer than half of the participants solve their slice unaided. "Solved" means a pass rate of at least 0.5 on their role slice. If more than half solve it, find which traps they saw through quickly and deepen those, then repeat with new people.

## Results

| Date | Seed | Role | Years of experience | Pass rate | Time used | Traps found unaided | Notes |
|---|---|---|---|---|---|---|---|
| not yet run | | | | | | | |
