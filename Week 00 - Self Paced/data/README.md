# The Hartland data

A generated extract from Hartland Regional Health Authority, the fictional regional body that runs public health programs for a Ministry of Health. Nothing here is a real patient's record, and nothing here is a protocol for care.

This is the small extract for [Week 00 — Self Paced](../README.md). The six-week extract is a different world: [Week 01 — Week 06 data](<../../Week 01 - Week 06/data/README.md>). A count from one folder does not belong in the other.

Open this page when [Module 01](<../Module 01 - Problem Discovery/README.md>) tells you to count. Who the case is for is [target_audience.md](../../target_audience.md). The longer glossary is [Health language](../../health_language.md). Health experience is not required.

## On this page

- [The path a person takes](#the-path-a-person-takes)
- [Which folder to open](#which-folder-to-open)
- [The extract](#the-extract)
- [The written rules](#the-written-rules)
- [Closed folders](#closed-folders)
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

`R0`, `R1`, `R2`, `R3`, and `U` are explained in ordinary language in [Health language](../../health_language.md) and formally in `corpus/grade_codes.md`. The sheet also contains words that are not in that short list.

### `handover/pacs_manifest.csv`

The hospital image index. **PACS** is the system hospitals use to file medical images. One row is one hospital picture. These rows use `HOSPITAL_MRN`, a hospital number.

| Column | Meaning |
|---|---|
| `STUDY_UID` | The identifier of one picture on the hospital index |
| `ACCESSION` | The visit that picture belongs to. More than one picture can share an accession |
| `HOSPITAL_MRN` | The hospital number for the person. The registry uses `REGISTRY_NO`. The screening service uses `LOCAL_PID` |
| `STUDY_DATE` | When the index says the picture was taken. The same mixed date formats as the registry |
| `MODALITY` | The kind of picture. `OP` means an eye photograph |
| `STATION_NAME` | The clinic named on the index |
| `FILE_PATH` | The path the index records for the picture file. The picture itself is not in this folder |

### `handover/shared_folder_listing.csv`

Pictures from clinics that do not use the hospital index. They sit in a folder named `EYE SCREEN 2024 final final`. One row is one file. Some of those names also appear in the grader workbook. Some do not.

| Column | Meaning |
|---|---|
| `FILE_NAME` | The file name as stored. Some names look like a surname, an initial, a date, and an eye (`L` or `R`). Some look like a camera name, such as `IMG_0001.JPG` |
| `FOLDER` | The folder the listing says the file is in |
| `MODIFIED_DATE` | The date the listing records for that file. The same mixed date formats as the registry |
| `FILE_PATH` | The path the listing records. The picture itself is not in this folder |

### `handover/letter_dispatch.csv`

Letters the service recorded as sent. A **result letter** tells a person their grader's code. A **recall letter** asks them to come back because the screen is not finished. The wording templates are in the corpus. Not every completed grade has a letter row, and not every letter row matches a grade.

| Column | Meaning |
|---|---|
| `LOCAL_PID` | The local person id on the letter row |
| `PATIENT_NAME` | Name as the row holds it, surname then forename |
| `DOB` | Date of birth. The same mixed date formats as the registry |
| `CLINIC` | The clinic named on the letter row |
| `SENT_DATE` | When the service recorded the letter as sent. The same mixed date formats as the registry |
| `TEMPLATE_ID` | Which template was used. `letter-result` and `letter-recall` match `document_id` in `corpus/manifest.csv` |

### `handover/ophthalmology_referrals.csv`

People sent toward the eye specialist. There is one list. It has no separate column for "urgent."

| Column | Meaning |
|---|---|
| `LOCAL_PID` | The local person id on the referral row |
| `PATIENT_NAME` | Name as the row holds it, surname then forename |
| `CLINIC` | The clinic named on the referral row |
| `REFERRED_DATE` | When they were sent toward the eye specialist. The same mixed date formats as the registry |
| `BOOKED_DATE` | The appointment date on the row. Often empty |
| `SEEN_DATE` | The visit date on the row. Often empty |

### `handover/vendor_scores.csv`

What a vendor's model returned on a set of primary-care photos. One row is one picture.

| Column | Meaning |
|---|---|
| `FILE_NAME` | The picture file name. The same kind of name as the shared-folder listing |
| `GRADER_LABEL` | The human code for that picture |
| `MODEL_LABEL` | The code the model returned. Empty means the model returned nothing for that picture |
| `MODEL_SCORE` | A number the model attached to its label, from 0 to 1. Empty when `MODEL_LABEL` is empty |

### `handover/README.txt` and `handover/data_dictionary.xlsx`

The cover note and a field glossary shipped with the extract. Read them as claims about the files, then check the claims against the rows and against `corpus`.

`README.txt` is a short cover note. It has no columns.

`data_dictionary.xlsx` is one sheet. One row is one field the dictionary claims to explain.

| Column | Meaning |
|---|---|
| `field` | A column name |
| `description` | The sentence the dictionary gives for that name |

## The written rules

`corpus/manifest.csv` is the index of the written rules. One row is one document. The markdown files are prose. They have no columns.

| Column | Meaning |
|---|---|
| `document_id` | The short id for the document |
| `title` | The title in the index |
| `status` | `in_force` or `draft` |
| `filename` | The markdown file in this folder |

| File | What it is |
|---|---|
| `sop_screening_issued.md` | The screening procedure that is in force. It defines who counts as screened |
| `sop_urgent_pathway_draft.md` | A proposed faster path for sight-threatening disease. Read its status line |
| `grade_codes.md` | The official code list |
| `letter_template_result.md` | The letter used after a grader records a code |
| `letter_template_recall.md` | The letter used when the person still needs a photo or a result |
| `dpo_operating_rule.md` | What the data protection officer will allow: where data may live, what a letter may say, and what a model must not do |
| `clinic_note_pilot_sites.md` | Which clinics are in the first slice, and how the grader queue should be ordered |

## Closed folders

Leave `truth` and `eval` closed during Module 01. Opening them skips the discovery. The tables below are the column map for grading.

Dates in `truth` are written as `2025-07-09`.

### `truth/person.csv`

One row is one person on the clean copy of the registry.

| Column | Meaning |
|---|---|
| `person_uid` | The clean id for one person. It does not appear in the handover |
| `forename`, `surname`, `dob`, `sex` | Name, date of birth, and sex. Sex is `M`, `F`, or `U` |
| `district` | The area they are counted in, in one spelling |
| `home_site` | The clinic they are attached to |
| `diabetes_type` | Type 1 or Type 2 |
| `diagnosis_date` | When diabetes was recorded |
| `travel_burden` | How hard it is for the person to reach a clinic. Higher means harder |
| `flag` | Empty, `DECEASED`, or `MOVED` |
| `registry_number`, `local_pid`, `hospital_mrn` | The three identifiers the handover splits across files |
| `cohort` | `none` if there is no photo, `photo_no_result` if there is a photo and no grade, `completed` if a grade was recorded |
| `grade` | The grade code on the clean copy. Empty when there is no completed grade |
| `screening_site` | Where the photo was taken. Empty when there is no photo |
| `camera_class` | `hospital`, `primary`, or `outreach`. Empty when there is no photo |

### `truth/crosswalk.csv`

One row is one person. This is the link between the clean id and the identifiers in the handover.

| Column | Meaning |
|---|---|
| `person_uid` | The clean id |
| `registry_number`, `local_pid`, `hospital_mrn` | The three handover identifiers for that person |
| `forename`, `surname`, `dob` | Name and date of birth |
| `district`, `home_site` | Area and home clinic, in one spelling |

### `truth/visit.csv`

One row is one photography visit.

| Column | Meaning |
|---|---|
| `visit_id` | The identifier of the visit |
| `person_uid` | The person |
| `site_name` | The clinic where the photo was taken |
| `camera_class` | `hospital`, `primary`, or `outreach` |
| `photo_date` | When the photo was taken |

### `truth/image.csv`

One row is one picture. A visit can have a left eye, a right eye, or only one of them.

| Column | Meaning |
|---|---|
| `image_id` | The identifier of the picture |
| `person_uid`, `visit_id` | The person and the visit |
| `eye` | `L` or `R` |
| `file_name`, `file_path` | The name and path the handover indexes use |
| `quality` | `readable`, `ungradable`, or `unknown` |
| `grade` | The code stored on that picture. Empty when nobody has finished |
| `camera_class` | `hospital`, `primary`, or `outreach` |
| `file_present` | Whether the picture bytes are in the folder |
| `is_pilot` | Whether this picture is in the vendor pilot set |

### `truth/grade.csv`

One row is one person with a recorded grade.

| Column | Meaning |
|---|---|
| `person_uid` | The person |
| `grade` | The code |
| `referable` | Whether a specialist should see them |
| `urgent` | Whether the result is the sight-threatening group |
| `graded_at` | When the grade was recorded |
| `grader_initials` | The initials of the person who read the photo |

### `truth/letter.csv`

One row is one letter on the clean copy.

| Column | Meaning |
|---|---|
| `person_uid` | The person |
| `template_id` | Which template. Matches `document_id` in the corpus index |
| `sent_at` | When the letter was sent |
| `photo_date` | The photo the letter follows |

### `truth/referral.csv`

One row is one person sent toward the eye specialist.

| Column | Meaning |
|---|---|
| `person_uid` | The person |
| `referred_at` | When they were sent |
| `booked_at` | When the appointment was booked |
| `seen_at` | When they were seen |
| `specialist_agrees_urgent` | Whether the clean copy treats the referral as urgent |

### `truth/vendor_score.csv`

One row is one picture in the vendor pilot.

| Column | Meaning |
|---|---|
| `image_id`, `person_uid` | The picture and the person |
| `file_name` | The shared-folder file name |
| `grader_label` | The human code |
| `model_label` | The code the model returned. Empty means the model returned nothing |
| `model_score` | The number the model attached to its label. Empty when `model_label` is empty |

### `truth/hospital_eval.csv`

One row is one scored picture in a separate hospital set. These rows are not people on the registry.

| Column | Meaning |
|---|---|
| `image_id` | The identifier of the scored picture. These ids look like `HE0001` |
| `person_uid` | A join column. The cells are empty |
| `grader_label` | The human code |
| `referable` | Whether that human code is one a specialist should see |
| `model_label` | The code the model returned |
| `model_positive` | Whether the model called the picture referable |

### `eval/cases.jsonl`

One JSON object per line. One line is one graded question. The known counts live in `expected`. This page does not repeat them.

| Field | Meaning |
|---|---|
| `case_id` | An id for the question |
| `case_type` | The kind of question |
| `user` | Who the question is for |
| `question` | The question in ordinary language |
| `tool` | The tool name the checker expects |
| `document_id` | The corpus document the question relies on |
| `truth_ids` | Clean ids of example rows bound to the question |
| `expected` | The known answer. The fields inside depend on the question |

## What is not here

Retinal photographs. The manifests and the workbook name files, and those files are not in the drop. You can count, join, and draft from the tables and the rules. You cannot look at an eye.

The exercise that uses these files is [Count the files](<../Module 01 - Problem Discovery/05-count-the-files.md>).
