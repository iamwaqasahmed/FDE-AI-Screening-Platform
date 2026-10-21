# The Hartland data

A generated extract from Hartland Regional Health Authority, the fictional regional body that runs public health programs for a Ministry of Health. Nothing here is a real patient's record, and nothing here is a protocol for care.

This is the small extract for [Week 00 — Self Paced](../README.md). The six-week extract is a different world: [Week 01 — Week 06 data](<../../Week 01 - Week 06/data/README.md>). A count from one folder does not belong in the other.

Open this page when [Module 01](<../Module 01 - Problem Discovery/README.md>) tells you to count. Who the case is for is [target_audience.md](../../target_audience.md). The longer glossary is [Health language](../../health_language.md). What the system does with these files is [The system](../the-system.md). Health experience is not required.

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
| [truth](truth) | Grading only, when present | A clean hidden copy of the same world. The IT team did not send this |
| [eval](eval) | Grading only, when present | Questions with known answers. The IT team did not send this |

Work from [handover](handover) and [corpus](corpus). If [truth](truth) or [eval](eval) is on your machine, leave it closed during Module 01. Opening it skips the discovery.

[`handover/README.txt`](handover/README.txt) and [`handover/data_dictionary.xlsx`](handover/data_dictionary.xlsx) came with the extract. They are the IT team's cover note and field glossary, and they are part of the drop. The operating rules in [corpus](corpus) are the service's own description of the same work. Module 01 asks you to compare the note with the rows and with [corpus](corpus). That comparison is the forward deployed engineer practice in [FDE.md](../../FDE.md): read a messy drop, and check a claim before you build on it.

## The extract

Dates appear as `2024-10-01`, as `30/08/2024`, or as a spreadsheet serial such as `35339`. Read the column before you sort it.

### [`handover/diabetes_registry.csv`](handover/diabetes_registry.csv)

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

### [`handover/grader_workbook.xlsx`](handover/grader_workbook.xlsx)

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

`R0`, `R1`, `R2`, `R3`, and `U` are explained in ordinary language in [Health language](../../health_language.md) and formally in [`corpus/grade_codes.md`](corpus/grade_codes.md). The sheet also contains words that are not in that short list.

### [`handover/pacs_manifest.csv`](handover/pacs_manifest.csv)

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

### [`handover/shared_folder_listing.csv`](handover/shared_folder_listing.csv)

Pictures from clinics that do not use the hospital index. They sit in a folder named `EYE SCREEN 2024 final final`. One row is one file. Some of those names also appear in the [grader workbook](handover/grader_workbook.xlsx). Some do not.

| Column | Meaning |
|---|---|
| `FILE_NAME` | The file name as stored. Some names look like a surname, an initial, a date, and an eye (`L` or `R`). Some look like a camera name, such as `IMG_0001.JPG` |
| `FOLDER` | The folder the listing says the file is in |
| `MODIFIED_DATE` | The date the listing records for that file. The same mixed date formats as the registry |
| `FILE_PATH` | The path the listing records. The picture itself is not in this folder |

### [`handover/letter_dispatch.csv`](handover/letter_dispatch.csv)

The service's log of letters it recorded as sent. One row is one letter. It is not one person, and it is not one grade.

`TEMPLATE_ID` says which wording was used. Both wordings are in [corpus](corpus), and both ids match `document_id` in [`corpus/manifest.csv`](corpus/manifest.csv).

- `letter-result` is the **result letter**. It tells the person the code the grader wrote, such as `R0` or `R2`. The wording is [`corpus/letter_template_result.md`](corpus/letter_template_result.md).
- `letter-recall` is the **recall letter**. It says the screen is not finished and asks the person to come back for another photo. The wording is [`corpus/letter_template_recall.md`](corpus/letter_template_recall.md).

A row here does not line up one-to-one with the [grader workbook](handover/grader_workbook.xlsx).

- A person can have a finished result in [`grader_workbook.xlsx`](handover/grader_workbook.xlsx) and have no row here. A grade does not prove a letter was logged.
- A row here can fail to line up with a completed grade. A recall letter is for a screen that is not finished, so there is no result code to match. Some rows also do not join to a person on the [registry](handover/diabetes_registry.csv) or the [workbook](handover/grader_workbook.xlsx).

`LOCAL_PID` is the id to use when joining this file to the [registry](handover/diabetes_registry.csv) and the [workbook](handover/grader_workbook.xlsx).

| Column | Meaning |
|---|---|
| `LOCAL_PID` | The screening service's person id, the same kind of id as on the [registry](handover/diabetes_registry.csv) and the [workbook](handover/grader_workbook.xlsx), such as `LP011993` |
| `PATIENT_NAME` | The name as this file writes it: surname, then forename, as in `Casey, Brian` |
| `DOB` | Date of birth, in more than one format: `1961-10-01`, day/month/year such as `30/08/2024`, or a spreadsheet serial such as `21459`. A day of 1–12 is written as `YYYY-MM-DD` |
| `CLINIC` | The clinic named on that letter row, such as `Harbour Eye Clinic` |
| `SENT_DATE` | The date the service recorded the letter as sent, in those same mixed formats |
| `TEMPLATE_ID` | `letter-result` or `letter-recall`. These are the `document_id` values in [`corpus/manifest.csv`](corpus/manifest.csv) |

### [`handover/ophthalmology_referrals.csv`](handover/ophthalmology_referrals.csv)

People sent toward the eye specialist. There is one list. It has no separate column for "urgent."

| Column | Meaning |
|---|---|
| `LOCAL_PID` | The local person id on the referral row |
| `PATIENT_NAME` | Name as the row holds it, surname then forename |
| `CLINIC` | The clinic named on the referral row |
| `REFERRED_DATE` | When they were sent toward the eye specialist. The same mixed date formats as the registry |
| `BOOKED_DATE` | The appointment date on the row. Often empty |
| `SEEN_DATE` | The visit date on the row. Often empty |

### [`handover/vendor_scores.csv`](handover/vendor_scores.csv)

What a vendor's model returned on a set of primary-care photos. One row is one picture.

| Column | Meaning |
|---|---|
| `FILE_NAME` | The picture file name. The same kind of name as the shared-folder listing |
| `GRADER_LABEL` | The human code for that picture |
| `MODEL_LABEL` | The code the model returned. Empty means the model returned nothing for that picture |
| `MODEL_SCORE` | A number the model attached to its label, from 0 to 1. Empty when `MODEL_LABEL` is empty |

### [`handover/README.txt`](handover/README.txt) and [`handover/data_dictionary.xlsx`](handover/data_dictionary.xlsx)

These two files arrived inside the handover. They are the cover note and the field glossary the authority's IT team attached. They tell you how to read the extract. They are not the service's rules.

This is the messy world the case is built on. Dates are written in more than one way, the same place is spelled in more than one way, and a sentence in the note can disagree with a row or with [corpus](corpus). A forward deployed engineer reads that drop and checks it. The practice is [FDE.md](../../FDE.md): read an extract that can disagree with its own cover note, and keep only what the rows and the written rules support.

Read each sentence in these two files as a claim. Compare it with the rows, and with the written rules in [corpus](corpus). Keep the sentence when the rows and the corpus agree with it. Where they disagree, follow the corpus. The [issued procedure](corpus/sop_screening_issued.md), the [grade-code list](corpus/grade_codes.md), and the [data-protection rule](corpus/dpo_operating_rule.md) are the rules the later modules follow.

[`README.txt`](handover/README.txt) is a short cover note. It has no columns. It names the snapshot date, 1 October 2026, and then tells you how to join the files and which labels to use.

[`data_dictionary.xlsx`](handover/data_dictionary.xlsx) is one sheet. One row is one field the dictionary claims to explain. The sheet does not list every column in the extract.

| Column | Meaning |
|---|---|
| `field` | A column name the dictionary talks about, such as `REGISTRY_NO` or `RESULT` |
| `description` | The sentence the dictionary gives for that name. Check the sentence. The column table above does not mean the sentence is right |

## The written rules

[`corpus/manifest.csv`](corpus/manifest.csv) is the index of the written rules. One row is one document. The markdown files are prose. They have no columns.

| Column | Meaning |
|---|---|
| `document_id` | The short id for the document |
| `title` | The title in the index |
| `status` | `in_force` or `draft` |
| `filename` | The markdown file in this folder |

| File | What it is |
|---|---|
| [`sop_screening_issued.md`](corpus/sop_screening_issued.md) | The screening procedure that is in force, effective 1 March 2019. An eligible person is a registry row with no deceased or moved flag. Coverage is the share of those people with a recorded result in the last 24 months. A recorded result includes a readable grade and an ungradable grade. A photo with no code is not a completed screen. One referral box covers both mild and sight-threatening disease, and this procedure sets no day target for a specialist visit |
| [`sop_urgent_pathway_draft.md`](corpus/sop_urgent_pathway_draft.md) | A proposed faster path. The status line says it is not issued: draft for clinical review only. It would send sight-threatening disease to ophthalmology within 14 days, and keep mild referable disease off that queue. It becomes current policy only after the clinical lead and the data protection officer both sign, and the issued procedure is updated |
| [`grade_codes.md`](corpus/grade_codes.md) | The official code list that is in force. `R0` is no disease seen. `R1` is mild and not referable. `R2` is referable and not sight-threatening. `R3` is sight-threatening. `U` means the photo could not be read. Only `R2` and `R3` tick the referral box. Words such as "prolif" or "urgent" are not codes. A blank result means the screen is unfinished |
| [`letter_template_result.md`](corpus/letter_template_result.md) | The in-force wording for `letter-result`. Use it after a grader records a code. The letter copies that code. It does not add a diagnosis, a stage of disease, or a specialist outcome. If the referral box was ticked, it says the eye clinic will write about an appointment |
| [`letter_template_recall.md`](corpus/letter_template_recall.md) | The in-force wording for `letter-recall`. Use it when there is no completed result, or the photo could not be read and the person needs another capture. It asks them to contact the clinic and bring the letter. It does not say whether disease is present |
| [`dpo_operating_rule.md`](corpus/dpo_operating_rule.md) | The data protection officer's rule that is in force. Images and extracts stay on the authority network, and every access is logged. Patient images are not used to train a model unless a separate approval is signed. A letter may repeat a code a grader has recorded, and it must not add a diagnosis. A model may sort a queue or flag a photo to retake. A grader still signs every result that refers, recalls, or reassures a patient. The officer will review a bounded eye-screening service, not one release that also covers breast and cervical screening |
| [`clinic_note_pilot_sites.md`](corpus/clinic_note_pilot_sites.md) | The in-force note for the first slice. The sites are Hill Counties Health Centre, Oakridge Primary Care, and North City Eye Clinic. River Outreach, breast screening, and cervical screening are outside this slice. The grader queue is ordered as: no result code, then `U`, then `R2`, then `R3`. The 14-day draft is not current policy. The connection for this slice is a file in and a file out. Each night it takes a registry file, the same kind of extract as [`handover/diabetes_registry.csv`](handover/diabetes_registry.csv). It writes a result file back. There is no API. There is no feed into the electronic health record, the hospital system that holds the patient's chart. Screening keeps its own lists until that connection exists |

## Closed folders

Leave [truth](truth) and [eval](eval) closed during Module 01. Opening them skips the discovery. The IT team did not send these folders. The extract they would send is [handover](handover). These two folders are the grading copy: a clean version of the same people and events, and the questions with known answers. The tables below are the column map for that grading copy.

Dates in [truth](truth) are written as `2025-07-09`.

### [`truth/person.csv`](truth/person.csv)

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

### [`truth/crosswalk.csv`](truth/crosswalk.csv)

One row is one person. This is the link between the clean id and the identifiers in the handover.

| Column | Meaning |
|---|---|
| `person_uid` | The clean id |
| `registry_number`, `local_pid`, `hospital_mrn` | The three handover identifiers for that person |
| `forename`, `surname`, `dob` | Name and date of birth |
| `district`, `home_site` | Area and home clinic, in one spelling |

### [`truth/visit.csv`](truth/visit.csv)

One row is one photography visit.

| Column | Meaning |
|---|---|
| `visit_id` | The identifier of the visit |
| `person_uid` | The person |
| `site_name` | The clinic where the photo was taken |
| `camera_class` | `hospital`, `primary`, or `outreach` |
| `photo_date` | When the photo was taken |

### [`truth/image.csv`](truth/image.csv)

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

### [`truth/grade.csv`](truth/grade.csv)

One row is one person with a recorded grade.

| Column | Meaning |
|---|---|
| `person_uid` | The person |
| `grade` | The code |
| `referable` | Whether a specialist should see them |
| `urgent` | Whether the result is the sight-threatening group |
| `graded_at` | When the grade was recorded |
| `grader_initials` | The initials of the person who read the photo |

### [`truth/letter.csv`](truth/letter.csv)

One row is one letter on the clean copy.

| Column | Meaning |
|---|---|
| `person_uid` | The person |
| `template_id` | Which template. Matches `document_id` in the [corpus index](corpus/manifest.csv) |
| `sent_at` | When the letter was sent |
| `photo_date` | The photo the letter follows |

### [`truth/referral.csv`](truth/referral.csv)

One row is one person sent toward the eye specialist.

| Column | Meaning |
|---|---|
| `person_uid` | The person |
| `referred_at` | When they were sent |
| `booked_at` | When the appointment was booked |
| `seen_at` | When they were seen |
| `specialist_agrees_urgent` | Whether the clean copy treats the referral as urgent |

### [`truth/vendor_score.csv`](truth/vendor_score.csv)

One row is one picture in the vendor pilot.

| Column | Meaning |
|---|---|
| `image_id`, `person_uid` | The picture and the person |
| `file_name` | The shared-folder file name |
| `grader_label` | The human code |
| `model_label` | The code the model returned. Empty means the model returned nothing |
| `model_score` | The number the model attached to its label. Empty when `model_label` is empty |

### [`truth/hospital_eval.csv`](truth/hospital_eval.csv)

One row is one scored picture in a separate hospital set. These rows are not people on the registry.

| Column | Meaning |
|---|---|
| `image_id` | The identifier of the scored picture. These ids look like `HE0001` |
| `person_uid` | A join column. The cells are empty |
| `grader_label` | The human code |
| `referable` | Whether that human code is one a specialist should see |
| `model_label` | The code the model returned |
| `model_positive` | Whether the model called the picture referable |

### [`eval/cases.jsonl`](eval/cases.jsonl)

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

Retinal photographs. The [hospital index](handover/pacs_manifest.csv), the [shared-folder listing](handover/shared_folder_listing.csv), and the [workbook](handover/grader_workbook.xlsx) are in the drop, and each of them names picture files such as `I0000001.jpg`. Those picture files are not in the drop. You can count, join, and draft from the tables and the rules. You cannot look at an eye.

The exercise that uses these files is [Count the files](<../Module 01 - Problem Discovery/05-count-the-files.md>).
