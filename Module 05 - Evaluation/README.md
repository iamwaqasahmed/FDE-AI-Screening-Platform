# Module 05 — Evaluation

Measure the agent. A demo is not a measurement.

You build a small labeled set from the engagement: coverage, the queue, draft versus issued policy, letters, and refusals. `data/eval` stays hidden. It is the instructor's set, not the one you write.

For each case you record whether the right tool was called, the right document was cited, the result matched, and the agent refused when it should have. Failures get a type: wrong join, draft treated as policy, a silent model treated as healthy, a letter that invents a diagnosis. You also record latency and how many model calls a case cost.

This module is ready when a change to a tool or a prompt can be accepted or rejected from your set, and the instructor set can be run without you having written it.

The lesson notes for this module are not written yet.
