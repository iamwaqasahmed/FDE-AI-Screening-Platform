# Access log

Every ask appends one JSON line. The fields are the time, who asked, the question, the tool, `document_id`, and whether the reply was refused.

The log does not include the API key, the rest of `.env`, or the full tool payload. Who asked is an argument, `--who`. A run without a name is rejected.

Default path: `runtime/access.log`. That directory is gitignored.

Next: [Result file](03-result-file.md).
