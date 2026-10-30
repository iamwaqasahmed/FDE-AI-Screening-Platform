# Enterprise simulation research

Research note only. It does not change `problem_simulation/`, the release packs, or any student lesson. The Al-Waha world stays the course: one seed, closed truth, twenty releases (`rel-m01-l01` through `rel-m04-l05`), personas, and a reference Patient Access Assistant that facilitators hold back.

This folder asks how to thicken six frictions students already meet in pieces, while checks stay deterministic:

- versioned, conflicting policies
- unreliable partners
- bilingual content
- identity ambiguity
- procurement delay
- partial observability

## How to read these notes

| Note | Question it answers |
|---|---|
| [01 Current simulator critique](01-current-simulator-critique.md) | What `python -m alwaha.worldbuild`, `alwaha.serve`, and `alwaha.check` already do well, and where those six frictions are still thin |
| [02 Reference simulators](02-reference-simulators.md) | What Synthea, HAPI FHIR, LocalStack, Testcontainers, Toxiproxy, PaySim, Bank of Anthos, the MIT beer game, and Contoso Coffee actually simulate |
| [03 Proposed architecture](03-proposed-simulation-architecture.md) | How to evolve this world, what stays hidden, what students generate, and why the grader should not call a live model |
| [04 Sources](04-sources.md) | URLs behind the claims |

## Stance

Keep the narrative. Nakhl, Safra, Wadi, Ain, the Ramadan calendar, Layla Al-Harbi's deadline, and the scripted interviews are the teaching surface. Population generators and protocol servers are patterns for the generator and the mocks. They are not a replacement case.

Adversary-emulation ranges, including MITRE Caldera, are out of scope. This note does not design an offensive cyber range. Existing scripted threat traffic in the Al-Waha design stays a scripted population with gold labels held in `truth/`.

## Grading claim, in short

A second build with the same seed matches. The grading service returns pass or fail and withholds the missing fact. A live language model on that path breaks both properties. Models may phrase frozen corpus text before a pack is published. They do not score the pack.
