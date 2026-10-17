# What stays out

The run directory holds the access log and the result file. It must not hold:

- A retinal image. The handover names picture files and does not include the bytes. The service does not copy a `.jpg`, `.png`, or `.dcm` into the run.
- The API key. `.env` is gitignored. The log and the result file must not echo it.
- A training set. This service does not write a file of patient images or grades for a model to train on.
- `data/truth` and `data/eval`. Those are for grading, not for the authority's run.

A letter answer that adds a diagnosis fails the check.

Next: [The container](05-the-container.md).
