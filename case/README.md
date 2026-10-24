# Al-Waha Health Cluster

You are with the patient-access service of the Al-Waha Health Cluster, a fictional health cluster in Saudi Arabia. Everyone in the case is invented. Nothing here is a patient's record or a protocol for care.

The program map is [../README.md](../README.md). The words are [access_language.md](access_language.md). The syllabus is [../FDE Program Syllabus.md](<../FDE Program Syllabus.md>).

## The client

Al-Waha runs three hospitals, a diabetes and eye center, and about 24 primary health care centers. Some of those centers are in villages about 200 km from the nearest hospital. The cluster books outpatient care across about 15 specialties.

History in the files runs from 2023 into 2026. Your engagement opens on 10 January 2027. The cluster's weekend is Friday and Saturday. A few weeks after your four weeks, Ramadan begins, and the cluster will change its clinic hours.

## The ask

The Chief Digital and Transformation Officer wants this, in their words:

> An AI virtual front desk that books, reschedules, answers questions, and chases referrals in every hospital, live before Ramadan.

Leaders will also tell you about long specialist waits, abandoned calls, people who miss appointments, primary-care doctors who are angry about returned referrals, and a chatbot from 2023 that was switched off.

Treat those sentences as claims. Your first job is to find which problems are real, how large they are, and which ones an AI system should touch.

## Three places a system can run

| Place | What already lives there | What it means for you |
|---|---|---|
| Hospital data centers | Older hospital systems, and a scheduling system that sends a nightly file | Some facts arrive late, and some never appear as an API |
| The cluster's private cloud, on two sites | The newer hospital system, the referral platform, and a small GPU quota | This is where the cluster will let you deploy, and where patient data may be processed |
| A public-cloud model | One external language model the cluster already contracts | Use it only for content the cluster has classed as public |

The private cloud is the deployment target in Week 2. A design that uses all three places is a hybrid design. The cluster will give you a deployment standard and a data catalog. Read both before you move data.

## What you will build

Over four weeks your team builds an assistant for this service, then makes it accurate, observable, secure, and operable. You choose the architecture. The cluster grades the behavior of the system you deploy: the bookings it makes, the referrals it returns, the documents it cites, and the patient data it keeps inside the private cloud.

| Week | You leave the week with |
|---|---|
| 1 | A working proof of concept, an architecture diagram, and a design note that says which approach you chose and why |
| 2 | An application signed in to the cluster, wired to its systems, tested, and deployed on the private cloud |
| 3 | Customized models, retrieval over the cluster's documents, and an evaluation report |
| 4 | Security, monitoring, a serving design that meets the surge, and an operations and governance plan |

Weeks 3 and 4 also rehearse the discovery and the proposal you will need for a real client afterward. The rehearsal client is Al-Waha. The later project is a different client.

## How the case behaves

- New files and API changes arrive on a schedule. A decision that was reasonable on Monday can be incomplete by Thursday.
- Interviews are a tool. People answer the question you ask, and they do not volunteer the constraint that blocks your design.
- The cluster's rules on clinical safety, data protection, and security are in its document system. Following a leader's wish against a rule in force is a failed design.
- Coding assistants are allowed. Patient data, secrets, and unpublished cluster documents stay out of their prompts. The starter repository enforces that.

## Teams

A team of five shares one world, so another team's counts will not match yours. During the four weeks each person rotates through the lead, the AI and data work, the application and integration work, the product work, and the architecture and client work. Individual labs use a smaller personal world.
