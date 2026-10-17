# Forward deployed engineer

This course trains you to do the work of a forward deployed engineer in a health authority. The work is the real shape of the job: understand who you are for, discover the problem inside a messy engagement, then build a system that can run there.

There is no real client and no real patient data. We simulated the engagement and generated the files.

The simulated client is Hartland Regional Health Authority, a fictional regional service that reports to a Ministry of Health. Their request is an AI Screening Platform. The generated world is a diabetic eye screening service: a registry of people with diabetes, retinal photos recorded as rows, a grader workbook, letters, referrals, a vendor score file, and the written rules for that service. How that world was built is in [problem_simulation/README.md](problem_simulation/README.md). What each generated file means, in ordinary language, is in [data/README.md](data/README.md).

The generated drop you will use is [data/handover](data/handover) and [data/corpus](data/corpus). `data/truth` and `data/eval`, when present, are the hidden copy and the answer key. Leave them closed until a module tells you to open them.

Read the documents in this order.

## 1. Who is an FDE

Start with [FDE.md](FDE.md).

That note is the skill set. A forward deployed engineer embeds with a customer, turns a vague operational problem into a working AI system, and leaves it running in production. The four parts are production engineering, applied AI, customer consulting, and ownership in the client's environment.

Keep this list nearby. Each module trains a piece of it.

## 2. Module 01 — Problem discovery

Then open [Module 01 — Problem Discovery](<Module 01 - Problem Discovery/README.md>).

No health background is required. The module starts with the words the case uses, then walks the engagement one note at a time.

You are embedded at the simulated authority. The only request you have been given is an AI Screening Platform. The module teaches you to find the problem underneath that sentence before you design a system, using the generated extract and rules. It tells you when to open them. Leave the grading files and the generator closed until the module says otherwise.

Write the two artifacts the module asks for: an ask log, then a problem brief. Read the debrief only after the brief exists.
