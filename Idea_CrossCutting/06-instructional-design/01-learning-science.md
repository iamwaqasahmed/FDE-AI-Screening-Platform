# Learning science for this course

The course is already a case with traps, checks, and a withheld solution. Those devices are worth keeping. The load problem is elsewhere. From Module 1, Lesson 3, a chapter often hands over a finished file. Module 3 lessons replace on the order of nine to eleven modules and run to chapter 10. A person working alone holds the lead, the model work, the application, the product note, and the architecture on every lesson. Intrinsic load is the number of elements that must be held at once. For a reader who has not yet chunked the cluster, a lesson that is itself a distributed system is a high-interactivity task. [Sweller, van Merriënboer, and Paas (2019)](https://doi.org/10.1007/s10648-019-09465-5) treat that interactivity as a property of the material and of what the learner already knows. The same page is a different task for an engineer who already has the schema.

Extraneous load is added by the paste ritual itself: a picture of the shell, a block that must be pasted whole, spaces that must not move, `packet/` left untouched, `work/` as the only folder the check reads. Some of that split is necessary so the grader has a stable file. It is not instructional content. The [chapter-reading note](../../learning/how-to-read-a-chapter.md) already names the path that matters: what arrives, which function decides, what it refuses, and what it writes. That path is the right grain. The surrounding system is not.

## Worked examples, then a completion

A worked example is a full solution the learner studies, so attention goes to states and steps rather than to a search for any move that reduces the gap. The effect was first shown in algebra by Sweller and Cooper (1985), and [Sweller, van Merriënboer, and Paas (2019)](https://link.springer.com/content/pdf/10.1007/s10648-019-09465-5.pdf) restate it: studying examples can beat solving the equivalent problems, provided the example is actually studied. Scanning it and moving on does nothing. The same review describes the completion-problem effect, from van Merriënboer and Krammer's work on introductory programming: a partial program forces the study, because the learner cannot finish it without understanding the part that is given. A completion sits between a full example and a conventional problem.

The paste chapters are product-oriented examples that the check then executes. They do not require study. "Before you paste, say" is a question answered in the head. [Chi, Bassok, Lewis, Reimann, and Glaser (1989)](https://doi.org/10.1016/0364-0213(89)90002-5), as used in the 2019 review, showed that the explanations learners generate while studying examples are part of why examples work. A self-explanation that leaves no trace cannot be practiced, compared, or repaired.

Guidance should fade as expertise grows. [Kalyuga, Ayres, Chandler, and Sweller (2003)](https://doi.org/10.1207/s15326985ep3801_4) call this the expertise reversal effect: methods that help novices, including full examples, lose their benefit and can add load once the learner already has the schema. The 2019 review treats guidance fading as the curriculum-length version of that fact. An engineer who can already name what a function refuses should start at the completion or the problem. A non-engineer meeting the same function for the first time needs the worked decision in words. One required paste for both groups misfires twice.

For novices facing material whose elements interact, [Pollock, Chandler, and Sweller (2002)](https://doi.org/10.1016/S0959-4752(01)00016-0) found an advantage for a two-phase sequence: isolated elements first, the interacting whole second. The advantage showed up for low prior knowledge and disappeared when prior knowledge was higher. Phase two is obligatory. Isolation is not the end state. In this course, phase two is the module readout and the capstone, where decisions made earlier have to sit in one proposal. It is not every Tuesday's lesson.

## Productive failure, in bounds

[Sinha and Kapur (2021)](https://doi.org/10.3102/00346543211019105) meta-analyzed 53 studies and 166 comparisons of problem solving before instruction against instruction before problem solving. The primary result favors problem-solving-first for conceptual knowledge and transfer: Hedge's g = 0.36, 95% CI [0.20, 0.51]. Designs closer to productive failure were stronger, in the range g = 0.37 to 0.58. The authors' publication-bias adjustment (g = 0.87) is a sensitivity estimate, not the primary result.

The bounds matter more than the headline.

- Procedural knowledge showed no reliable difference: g = −0.03, 95% CI [−0.20, 0.15], 51 comparisons.
- Effects were estimated mostly on school and undergraduate mathematics, with thinner evidence for professional samples. A wide interval on a small "other / professional" subgroup is not a finding about government staff learning a cluster.
- High fidelity includes a generation phase on a problem that affords more than one approach, then instruction that builds on the solutions learners actually produced. Instruction that builds on student solutions was one of the stronger moderators (g = 0.56 against g = 0.20). Group generation also moderated the effect. A solo, self-paced lesson cannot meet that fidelity. A pre-written consolidation can answer the wrong forks the author already planted. It cannot respond to an unanticipated solution.
- Domain-general skills and younger pupils favored instruction first. Reading a trace, writing a requirement, and following a terminal command are closer to that category than to a single new mathematical concept.
- Productive failure is not minimal guidance continued to the end. [Kirschner, Sweller, and Clark (2006)](https://doi.org/10.1207/s15326985ep4102_1) argue that unguided discovery is a poor bet for novices, and that the advantage of guidance shrinks when prior knowledge can supply the guidance. The two papers disagree about the opening move for concepts. They agree that a novice left alone in a large problem space is not the design.

The traps already in the author record are the right opening move when they are conceptual and the consolidation is written: Friday is not a working day, Ain has no live slot, the mart's wait number is a claim, triage stays with a clinician, the unauthorized circular is not a citation. The learner commits a short prediction. The next chapter names that class of error and the case consequence. That is a bounded, low-fidelity form of problem-solving-first. It is the form this course can actually run.

It is the wrong opening move for procedures. Replacing a worker, a client, an index, or a manifest should begin with a worked example or a completion. Holding the gold file until the check is green, after the learner has been told to paste it, is neither failure nor study.

## Four components, not twenty systems

[Four-component instructional design](https://www.4cid.org/about/) is the curriculum-scale pair of cognitive load theory, summarized for long programs in [Sweller, van Merriënboer, and Paas (2019)](https://doi.org/10.1007/s10648-019-09465-5). A program is built from four pieces.

| Component | Role in this course |
| --- | --- |
| Learning tasks | The backbone. Authentic work in task classes, simple before complex, with variability inside a class. Early tasks are simplified versions of the professional decision, not the whole cluster. |
| Supportive information | The case, the terms, and how this kind of decision is made. High interactivity, available for the whole task class. |
| Procedural information | Just-in-time how-to: which block is a picture, which block is pasted, which command to run. It fades on later lessons. |
| Part-task practice | Only for a recurrent skill that must become automatic and that whole tasks will not repeat enough. A calendar count or a schema can qualify. A new subsystem every lesson does not. |

Part-task practice is the exception. The about page is explicit that whole tasks usually give enough practice on routines, and that drill is for automaticity. LoRA rank, hybrid search, and replica failover are not drills. They are separate task classes. Putting them inside the core lesson raises element interactivity for everyone and, by the expertise-reversal result, adds redundant guidance for readers who already live in that layer.

The completion strategy named in the 2019 review is the fade inside a technical lab: full example, then completion, then a conventional problem. It is not the shape of the core path. The core path's non-routine work is the decision, supported by the case, with procedural hints only for the command that runs the check.

## How long a lesson can be

There is no minute limit in this literature that can be copied onto these chapters. Three neighboring results are easy to misuse. They are cited here with the measurement attached.

**Video watch time is not lesson mastery.** [Guo, Kim, and Rubin (2014)](https://doi.org/10.1145/2556325.2566239) analyzed 6.9 million edX video sessions across four courses. Median engagement time was at most six minutes regardless of video length. Videos longer than nine minutes were often watched less than halfway. The share of sessions followed by a problem attempt fell from 56% after the shortest bucket to 31% after the longest. The authors recommend video chunks under six minutes, and they note that shorter videos may also be better planned. This course is text, a terminal, and a case. A six-minute rule would be a change of construct.

**Segmenting is about learner-paced steps in complex, fast material.** Mayer's segmenting principle, in *[Multimedia Learning](https://doi.org/10.1017/cbo9780511811678.013)* (2nd ed., 2009), says people learn better when a multimedia message is presented in user-paced segments than as one continuous unit. The reported effect, d = 0.98 on transfer, comes from narrated animations (a lightning sequence broken into sixteen short segments). The stated boundary is complex, fast-paced material and learners new to it. These chapters are already self-paced. The usable implication is one decision beat per chapter when the reader is new to that beat. It is not a duration.

**Long open courses lose people, and self-paced mastery can too.** [Jordan (2015)](https://doi.org/10.19173/irrodl.v16i3.2112) assembled 221 MOOCs. Completion, on mixed definitions and for the 129 courses that reported it, ranged from 0.7% to 52.1%, median 12.6%. In a regression with start date and peer grading, longer courses (measured in weeks) had lower completion; courses that used peer grading had lower completion than auto-graded courses. Jordan's own design conclusion is shorter, modular courses with signposting between them. Jordan also notes that Perna and colleagues (2014) did not find a length relationship, and the week-by-week curves are dominated by four-week Open2Study courses. [Reich and Ruipérez-Valiente (2019)](https://doi.org/10.1126/science.aav7958) found that HarvardX and MITx completion did not improve over six years: in 2017–18, 3.13% of participants, 15.42% of those who intended to complete, and 46.02% of verified-track learners. Those figures describe open, voluntary enrolments. They are not a forecast for a selected professional cohort. They are a warning that length and assessments which wait on another person are associated with attrition, and that auto-grading is associated with finishing a credential. Finishing is not the same claim as judgment. [Kane (2013)](https://doi.org/10.1111/jedm.12000) is the brake on that leap: a score interpretation has to be argued. "Completed" does not mean "can defend a boundary."

[Kulik, Kulik, and Bangert-Drowns (1990)](https://doi.org/10.3102/00346543060002265) reviewed 108 mastery-learning evaluations. Mastery programs raised examination performance, with stronger effects for weaker students, and they often raised time on task. Self-paced mastery programs often reduced completion in college classes. Gates help the people who stay and can shrink the number who finish, if each gate is large. The design response is small gates and revision, not fewer decisions and not a clock.

## One artifact, two productions

[Star and Griesemer (1989)](https://doi.org/10.1177/030631289019003001) describe boundary objects: things that are plastic enough for different groups to use and stable enough to keep a common identity. The case, the decision record, and the check ids can be that object. A clinician-side manager and an engineer can both point at "Ain stays on the nightly file" and mean the same constraint. They do not need to produce the same files.

The shared production on every core lesson is the decision record: the refusal, the boundary, and the id it traces to. The engineer's additional production is the extension lab. A non-engineer still reads the four beats in words, so the function's refusal is visible. They are not asked to paste the subsystem.

Expertise reversal is why a pretest sits on the lab rather than on the core lesson. A reader who can already state the refusal starts the lab at the completion. A reader who cannot starts at the worked example. The core gate does not depend on that choice. Scaffolding, in the four-component sense, is procedural information and examples that are withdrawn as the specification starts being met. The gold paste is not scaffolding. It is the performance, done by the chapter.

## Rules the progression uses

1. One core lesson carries one trap and one decision. Other subsystems appear as facts already decided.
2. Conceptual traps open with a short written prediction, then a consolidation written against that fork.
3. Procedures open with a worked example or a completion. Study is a written four-beat note.
4. Full examples fade when a pretest shows the schema is already there.
5. Isolated elements come back together at the module gate and the capstone.
6. Extension labs are task classes of their own. They are not chapters inside the core lesson.
7. No duration is set. Size is set by element interactivity: if a second trap needs a second subsystem, it is another lesson or a lab.
