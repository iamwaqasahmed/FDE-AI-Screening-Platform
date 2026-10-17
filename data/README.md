# The Hartland data

A generated extract from Hartland Regional Health Authority, the fictional regional body that runs public health programs for a Ministry of Health. Nothing here is a real patient's record, and nothing here is a protocol for care.

New to health services? Read this page, then continue in [Module 01](<../Module 01 - Problem Discovery/README.md>). The longer glossary is [Health language](<../Module 01 - Problem Discovery/01-health-language.md>).

## On this page

- [The path a person takes](#the-path-a-person-takes)
- [Which folder to open](#which-folder-to-open)
- [The extract](#the-extract)
- [The written rules](#the-written-rules)
- [What is not here](#what-is-not-here)

## The path a person takes

**Screening** checks people who may feel well, to find disease early.

**Diabetes** can, over years, damage the back of the eye. **Diabetic eye screening** photographs that part of the eye (a retinal photo, also called a fundus photo). A trained **grader** reads the photograph and writes a code. A letter tells the person the result. If the grader says a specialist should see them, that request is a **referral**. The eye specialist service is **ophthalmology**.

The files follow that path:

1. The person is on the diabetes **registry**, the authority's list of people known to have diabetes.
2. Someone takes a photo. The hospital stores an index row. A local clinic may only have a file in a shared folder.
3. The grader records a result in a workbook. Until that happens, the photo has no result.
4. A letter may be sent.
5. Some people appear on the referral list for the eye specialist.

You are not expected to judge a photograph. The picture files are not in this folder. A row that names a picture is the record you have.

## Which folder to open

| Folder | Who it is for | What it holds |
|---|---|---|
| [handover](handover) | You, on site | The messy extract the authority's IT team would send |
| [corpus](corpus) | You | The written rules, letter templates, and clinic note |
| `truth` | Grading only, when present | A clean hidden copy of the same world |
| `eval` | Grading only, when present | Questions with known answers |

Work from `handover` and `corpus`. If `truth` or `eval` is on your machine, leave it closed during Module 01. Opening it skips the discovery.

`handover/README.txt` and `handover/data_dictionary.xlsx` came with the extract. They are part of the drop. The operating rules in `corpus` are the other description of the same service. Module 01 asks you to compare them.

## The extract

Dates appear as `2024-10-01`, as `30/08/2024`, or as a spreadsheet serial such as `35339`. Read the column before you sort it.

### `handover/diabetes_registry.csv`

One row is one person on the diabetes list.

| Column | Meaning |
|---|---|
| `REGISTRY_NO` | An identifier printed on the register |
| `LOCAL_PID` | A local person id used by the screening service |
| `FORENAME`, `SURNAME`, `DOB`, `SEX` | Name, date of birth, sex |
| `DISTRICT` | The area they are counted in. Spelling is not consistent |
| `HOME_CLINIC` | The clinic they are attached to |
| `DIABETES_TYPE` | Type 1 or Type 2. Both are diabetes. The eye pathway uses the same list |
| `DIAGNOSIS_DATE` | When diabetes was recorded |
| `RECORD_STATUS` | A label the export puts on the row |
| `FLAG` | A second label. Empty, `DECEASED`, and `MOVED` appear here |
| `TRAVEL_BURDEN` | How hard it is for the person to reach a clinic. Higher means harder |

### `handover/grader_workbook.xlsx`

The graders' queue. Open every tab, including `OLD`. One row is one photographed person, not one eye.

| Column | Meaning |
|---|---|
| `LOCAL_PID` | The same local person id as the registry, when it was copied onto the sheet |
| `PATIENT_NAME`, `DOB` | Name and date of birth as the sheet holds them |
| `CLINIC` | Where the photo was taken |
| `PHOTO_DATE` | When the photo was taken |
| `GRADE_DATE` | When a grader recorded a result. Blank if nobody has finished |
| `FILE_NAME` | The picture file the row points at |
| `RESULT` | The grader's code, or empty |
| `REFERRAL` | `yes` if the person was sent toward the eye specialist, otherwise empty |
| `NOTES` | Free text. Urgent cases are sometimes written only here |
| `GRADER` | The initials of the person who read the photo |

`R0`, `R1`, `R2`, `R3`, and `U` are explained in ordinary language in [Health language](<../Module 01 - Problem Discovery/01-health-language.md>) and formally in `corpus/grade_codes.md`. The sheet also contains words that are not in that short list.

### `handover/pacs_manifest.csv`

The hospital image index. **PACS** is the system hospitals use to file medical images. One row is one hospital picture. These rows use `HOSPITAL_MRN`, a hospital number, not the registry id.

### `handover/shared_folder_listing.csv`

Pictures from clinics that do not use the hospital index. They sit in a folder named `EYE SCREEN 2024 final final`. One row is one file name. Some of those names also appear in the grader workbook. Some do not.

### `handover/letter_dispatch.csv`

Letters the service recorded as sent. A **result letter** tells a person their grader's code. A **recall letter** asks them to come back because the screen is not finished. The wording templates are in the corpus. Not every completed grade has a letter row, and not every letter row matches a grade.

### `handover/ophthalmology_referrals.csv`

People sent toward the eye specialist. There is one list. It has no separate column for "urgent." `REFERRED_DATE` is when they were sent. `BOOKED_DATE` and `SEEN_DATE` are the appointment and the visit. Those last two are often empty.

### `handover/vendor_scores.csv`

What a vendor's model returned on a set of primary-care photos. `GRADER_LABEL` is the human code. `MODEL_LABEL` and `MODEL_SCORE` are the model. An empty model label means the model returned nothing for that picture.

### `handover/README.txt` and `handover/data_dictionary.xlsx`

The cover note and a field glossary shipped with the extract. Read them as claims about the files, then check the claims against the rows and against `corpus`.

## The written rules

`corpus/manifest.csv` lists each document, its title, and whether it is `in_force` or `draft`.

| File | What it is |
|---|---|
| `sop_screening_issued.md` | The screening procedure that is in force. It defines who counts as screened |
| `sop_urgent_pathway_draft.md` | A proposed faster path for sight-threatening disease. Read its status line |
| `grade_codes.md` | The official code list |
| `letter_template_result.md` | The letter used after a grader records a code |
| `letter_template_recall.md` | The letter used when the person still needs a photo or a result |
| `dpo_operating_rule.md` | What the data protection officer will allow: where data may live, what a letter may say, and what a model must not do |
| `clinic_note_pilot_sites.md` | Which clinics are in the first slice, and how the grader queue should be ordered |

## What is not here

Retinal photographs. The manifests and the workbook name files, and those files are not in the drop. You can count, join, and draft from the tables and the rules. You cannot look at an eye.

The exercise that uses these files is [Count the files](<../Module 01 - Problem Discovery/05-count-the-files.md>).
