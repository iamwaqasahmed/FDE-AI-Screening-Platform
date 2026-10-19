# Health language

You can do this case without having worked in a hospital. This note is the shared vocabulary for both tracks. It does not describe Hartland's numbers. Those come later, from the files.

## The organisations

A **Ministry of Health** is the government body responsible for health services in a country.

A **regional health authority** runs those services in one region: hospitals, local clinics, and public health programs. Hartland is a fictional authority. It reports to a ministry.

A **clinician** is a health professional who makes care decisions. In this case you will meet nurses, graders, and eye specialists. You are not being asked to become one of them.

## What screening is

**Screening** checks people who may feel well, to find a disease early. It is different from treating someone who has already come in because they are ill.

Hartland runs three screening programs. You only need a plain description of each:

- **Breast screening** looks for signs of breast cancer, usually with an imaging test read by specialists.
- **Cervical screening** looks for changes that can lead to cervical cancer.
- **Diabetic eye screening** looks for eye damage caused by diabetes, using a photograph.

The email you will read asks for one platform over all three. You do not need the clinical detail of the first two. You do need the eye pathway, because that is the one the files describe.

## Diabetes and the eye

**Diabetes** is a long-term condition that affects how the body handles sugar in the blood. Over years it can damage small blood vessels, including the ones in the **retina**, the light-sensitive layer at the back of the eye. That damage can threaten sight.

A **fundus photo** is a picture of the retina. In screening, a nurse or technician takes the picture. A **grader**, a person trained to read these pictures, records a result. The grader is not replaced by a guess.

The result codes you will see later mean, in ordinary language:

| Code | Ordinary meaning |
|---|---|
| R0 | No diabetic eye disease seen on this photo |
| R1 | Mild changes. The person does not need a specialist for this result |
| R2 | A specialist should see them, but it is not the most urgent group |
| R3 | Sight-threatening. This is the urgent group |
| U | The photo cannot be read. The screen did not produce a usable result |

People also type informal words such as "urgent" or "prolif" in notes. The written grade list tells you how those words should be read. A blank result means the photo was taken and nobody has finished the reading. It does not mean the eye was normal.

**Referable** means the grader judges that an eye specialist should see the patient. **Ophthalmology** is that specialty. A **referral** is the request that sends the patient there.

**Sight-threatening** is the urgent end of referable disease. It is the group a draft rule in this case talks about seeing quickly.

## The path a person takes

Hold this sequence in mind. Your later brief describes where it breaks.

1. The person is known to have diabetes.
2. They should have an eye photo on a regular cycle. In this case the written rule uses 24 months.
3. Someone takes the photo, at a hospital eye clinic or at a local clinic.
4. A grader records a code.
5. A letter tells the person the result.
6. If the grader marks a referral, the person waits for a specialist appointment.

**Coverage** is the share of people who should have been screened and who actually have a recorded result. A photo with no code is not a completed screen.

## Places and lists

A **registry** is the authority's list of people known to have diabetes. It is a data file, not a building.

**Primary care** is the local clinic, closer to where people live. A **hospital eye clinic** is where the specialist service sits.

**PACS** is the hospital's index of medical images. Smaller clinics in this case do not use it. They drop files in a shared folder.

An **electronic health record** is the main system that holds a patient's hospital record. Connecting to it is slow. Screening often keeps its own lists until that connection exists.

A **data protection officer** (DPO) decides whether patient information may be stored, shown, or used to train a model. They can stop a project.

## Two model words

**Sensitivity** asks: of the people who truly have the finding, how many did the model catch? A high sensitivity can still flag many people who do not need a specialist. That second question is **specificity**. When a slide quotes only sensitivity, you do not yet know how crowded the clinic would become.

You are not expected to compute these from images. This drop does not include the image files. You are expected to notice which number was claimed, and which file it actually describes.

## What is yours to decide

You decide what the software should do first, what it must refuse, and which number defines success. The grader decides any result that changes a patient's care: a referral, a recall, or a reassurance.

**Finish.** You can describe the eye pathway, the five codes, and why a slide that quotes only sensitivity is incomplete, without opening the extract.

Next, on the self-paced track: [The discovery skill](<Week 00 - Self Paced/Module 01 - Problem Discovery/02-discovery-skill.md>).
