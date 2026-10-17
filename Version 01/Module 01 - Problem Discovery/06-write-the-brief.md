# Write the brief

Write this before you open the [debrief](07-debrief.md). Two pages is enough. Where the files are thin, say so under open questions. Do not fill the gaps with a platform diagram.

1. **Ask, verbatim.**
2. **Client and sponsor.** Who can say yes, and what they are under pressure to show.
3. **Who feels the pain.** The people whose day changes if you succeed. One sentence each.
4. **Workflow as it is.** Use the path from the [health language](01-health-language.md) note: person with diabetes, photo, grade, letter, specialist. Mark the handoffs that break.
5. **Job to be done.** One paragraph. The request was a platform. The job is the outcome the eye-screening program cannot currently produce.
6. **Outcome and metrics.** One primary outcome. Three to five metrics you counted, or that the first slice would have to start counting.
7. **Constraints.** Clinical, data, integration, and political. Only constraints you can point to in an interview, a file, or a corpus document.
8. **First slice.** The sites, the users, what runs this quarter, and the decision a human still owns.
9. **Later work.** What you will not put in the first release. Each item needs a reason from the evidence.
10. **Open questions.** What would change the slice if the answer came back differently.
11. **Two conversations.** Five lines for the Chief Digital Officer. Five lines for the ophthalmology lead. Same slice, different sentences.

## What the first slice is

In this course the first slice is an **agent**: software that chooses a next step, retrieves a written rule, and calls a tool on the client files. It is not a person, and it is not a chat window that answers from memory.

- **Retrieval** reads `data/corpus`: which rule is in force, which letter template to use, what a grade code means, what the service must refuse.
- **Tools** read `data/handover`: who is on the registry, who has a photo, who has a result, who was referred.

A grader still signs every result that refers, recalls, or reassures a patient. The agent can prepare the queue and the letter. It does not invent a diagnosis from a retinal photo.

**Finish.** The brief is about two pages. This module has no checker. Open the debrief only after the brief exists.

When the brief exists, open [Debrief](07-debrief.md).
