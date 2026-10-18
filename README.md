# Forward deployed engineering

Two tracks. Same fictional client: Hartland Regional Health Authority, a regional health service that reports to a Ministry of Health. Nothing here is a real patient's record, and nothing here is a protocol for care.

## Version 01 — self-paced introduction to FDE

About four days. A mixed cohort does the same case: software engineers, data scientists and data engineers, solution and enterprise architects, technical product managers, and technology consultants.

You read the reference, run the checkers, and explain the result. The work is one engagement: a vague platform request, a messy extract, a small agent, and a handoff that keeps the pilot stopped.

| | |
|---|---|
| Start here | [Version 01](<Version 01/README.md>) |
| Who it is for | [target_audience.md](<Version 01/target_audience.md>) |
| The practice | [FDE.md](<Version 01/FDE.md>) |

Run the checkers from `Version 01`. The commands are at the end of that guide.

## Version 02 — advanced track

For senior engineers who already put services in production: machine learning specialists, data engineers, software engineers, and solution architects.

Start at [Version 02/README.md](<Version 02/README.md>). Week 1 is [Week 01 — Problem discovery](<Version 02/Week 01 - Problem Discovery/README.md>). Week 2 is [Week 02 — Enterprise data](<Version 02/Week 02 - Enterprise Data/README.md>). Week 3 is [Week 03 — Retrieval and ML evidence](<Version 02/Week 03 - Retrieval and ML Evidence/README.md>). The data participants work from is described in [Version 02/data](<Version 02/data/README.md>). The generator, checks, eval, and mock APIs are in [Version 02/problem_simulation](<Version 02/problem_simulation/README.md>), and the design is [problem_simulation/PLAN.md](<Version 02/problem_simulation/PLAN.md>). The graph and the agent are not built yet.

The Hartland world in that plan is deep enough that a count, a citation, and a handoff depend on identity resolution, policy lineage, a care-path graph, and a workflow that can stop. LangGraph, retrieval, graph retrieval, and a solution architecture are how those questions come out right.
