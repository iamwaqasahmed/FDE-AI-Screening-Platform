# Documentation standards

These rules govern later edits to the self-paced pages. They describe the course that is already written. They are not a new template to paste onto every file.

## Voice

Write the way the lesson chapters already write.

- Short sentences. One fact per sentence when the fact is a rule.
- Name the file, the id, and the command. A reader who cannot find the file cannot do the lesson.
- Say what the check prints when it passes, and name the failure line when you tell the reader how to recover.
- Use the cluster's ids (`rel-m01-l01`, `h-wadi`, `p-info`) after the lesson's words chapter has given the everyday meaning.
- Do not add a second vocabulary for an idea the chapter already named. If an outside name helps (LoRA, RAG, leakage), say it once and then keep the chapter's word.

## What a chapter owes the reader

A numbered chapter already has a job: background, setup, role, client, words, the lesson's work, or finish. Do not force every file into the same outline.

Where a section is added, it should earn its place by answering one of these:

- Why this page exists inside the Al-Waha engagement.
- What the reader is supposed to hold at the end.
- What the earlier release already finished, in the words the next background already uses.
- What a term means, in everyday language, before the reader has to use it.
- Which file to open, which file to leave closed, and what a command prints.
- What to open next, after the finish conditions are true. That is the next lesson.

Skip the element that the surrounding chapter already answers.

## Code

Explain the script that is already in the chapter or in `packet/`. Say what the file is for, what it reads, what it refuses to do, and what it writes.

Do not change a fenced block that the reader is told to paste. The check looks for phrases inside those blocks. A clearer docstring belongs in the explanation around the block, not in a rewritten block.

Do not describe a library, a training loop, or a service the file does not call. Module 3, Lesson 2 selects a registered adapter row. It does not run a neural-network trainer. Say that.

## Exercises

Clarify the request that is already on the page. Do not add a deliverable, a file the check does not read, or a step that changes the pass line.

Optional questions live in [../learning/review.md](../learning/review.md). They are not filed. The finish chapter says so. Do not turn them into a `work/` file.

## Solutions

The solution copy is for after the attempt. Its chapters may say why the finished file satisfies the morning chapter. They may not replace `work/` with a different design.

Point forward with the result the day already states. Do not add the next day's failure trick.

## Links

Use a relative Markdown link. When the path contains a space, put it in angle brackets, as the root README does: [Module 1 Lesson 2](<../Module 01/Lesson 02/Student_Copy/README.md>). Percent-encoding the space also matches the release notes already in the course.

Every new link has to resolve to a file that exists. Do not invent a URL. The installer links already in chapter 01 stay as they are.

## What stays untouched

- `packet/` and `sources/` documents that are the client's files.
- Python, tests, CSV, JSON, YAML, and notebooks.
- The strings a check searches for.
- The release ids (`rel-m01-l01` through `rel-m04-l05`), the folder names those ids use, and the role names. The classroom calendar is ten days. Do not retitle a release folder to match a classroom day.
- Facilitator-only folders: `course_design/`, `problem_simulation/design`, `problem_simulation/build`.

If a page is wrong about a fact the code contradicts, record it in [remaining-issues.md](remaining-issues.md). Do not silently change the requirement.
