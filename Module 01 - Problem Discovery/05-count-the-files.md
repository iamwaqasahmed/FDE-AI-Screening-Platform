# Count the files

Open the files now. The extract is [data/handover](../data/handover). The written rules are [data/corpus](../data/corpus). If the file names are unfamiliar, read [data/README.md](../data/README.md) first. It explains each file in ordinary language and does not contain the counts.

`data/handover/README.txt` is the authority's cover note. It is part of the drop, and it is not this lesson. The data dictionary is also part of the drop. Compare both with the issued procedure before you trust either one.

You can use a spreadsheet or Python. You do not need a statistics background. A **median** is the middle value after you sort the numbers. If there is an even count, average the two middle values.

The image manifests name files. The picture bytes are not in the drop. A capture, for you, is a path, a date, and a row.

## Which file is which

| File | Plain meaning |
|---|---|
| `diabetes_registry.csv` | People known to have diabetes |
| `grader_workbook.xlsx` | The graders' queue. It has several tabs |
| `pacs_manifest.csv` | Hospital image index |
| `shared_folder_listing.csv` | Files from clinics that do not use the hospital index |
| `letter_dispatch.csv` | Letters the service recorded as sent |
| `ophthalmology_referrals.csv` | People sent toward the eye specialist |
| `vendor_scores.csv` | What last year's model returned on a set of photos |
| `data/corpus` | The written rules, letter templates, and clinic note |

Useful columns, in ordinary language:

- `LOCAL_PID` is a local person id. It appears on more than one file.
- `REGISTRY_NO` is the id the cover note tells you to join on.
- `HOSPITAL_MRN` on the PACS file is a hospital number, a third kind of id.
- `FLAG` and `RECORD_STATUS` are both about whether a registry row counts. The cover note, the dictionary, and the issued procedure do not describe them in the same way.
- `DISTRICT` is where the person lives for this program. The same place is sometimes spelled in more than one way.
- `RESULT` and `NOTES` in the workbook are the grader's code and free text. The grade-code list in the corpus is the translator. The `OLD` tab is part of the mess.

## What to count

Use the snapshot date on the cover note and the 24-month rule in the issued procedure. Write each query down. The debrief has the figures. Your counts should match them.

- Who is eligible, after you choose which written definition to follow.
- Coverage for the whole authority, and coverage for each district.
- How many people have a photo and no result code.
- The mix of result codes, after you map free text such as `prolif`, `urgent`, and `ungradable`.
- Median days from photo to letter, for completed results only. Some letter rows match nobody. Some completed results have no letter.
- Median days from an urgent result to a specialist visit. The referral file has no column called urgent. The issued procedure explains why the list looks like that.
- What `vendor_scores.csv` actually contains, set beside the 93% sentence.
- Which corpus documents are in force, and which document is still a draft. Read the status line at the top of each note.
- How many shared-folder names appear on no workbook row.

Try joining on `REGISTRY_NO`, on `LOCAL_PID`, and on the hospital number. Record which join works for which file.

Next: [Write the brief](06-write-the-brief.md).
