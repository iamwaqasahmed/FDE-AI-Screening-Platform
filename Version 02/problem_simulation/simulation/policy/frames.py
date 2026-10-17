"""Sentence frames. Trap documents keep their distinctive words in every frame."""

from __future__ import annotations

from simulation.world.clock import OAKRIDGE_MEMO
from simulation.world.sites import HARBOUR, NCEC, OAKRIDGE, short

_OAK = short(OAKRIDGE)
_MEMO_MONTH = OAKRIDGE_MEMO.strftime("%B")

ELIGIBILITY_V1 = (
    "An eligible person is counted by the screening procedure. A recorded result counts as a completed screen. "
    "Eligible people and a recorded result are the coverage figure in this screening procedure. "
    "A recorded result includes the grader code. The screening procedure is the eligibility rule for a recorded result.",
    "Who is eligible follows this screening procedure. A recorded result counts. "
    "The screening procedure counts an eligible person when a recorded result exists. "
    "Eligible, recorded, result, screening, procedure, and counts are the coverage words in this version.",
    "The screening procedure says an eligible person with a recorded result counts. "
    "A recorded result is what the screening procedure counts. Eligibility is that recorded result.",
)

REGISTER_V2 = (
    "From March 2019 the coverage window is two years. A person stays on the diabetes register while FLAG is empty. "
    "Death and a move both take the person off that register. A signed grade code finishes the encounter. "
    "A photograph with an empty code is unfinished. No national clock governs specialist review.",
    "The coverage window is two years. FLAG empty keeps the person on the register. "
    "A signed grade code finishes the encounter. Specialist review has no national clock.",
    "Two years is the coverage window. An empty FLAG keeps the person. A signed grade code finishes the encounter.",
)

REGISTER_V3 = (
    "A person stays on the diabetes register while FLAG is empty. Death and a move both take the person off that register. "
    "A finished encounter carries a signed grade code. A photograph with an empty code is unfinished. "
    "No national clock governs specialist review.",
    "FLAG empty keeps the person on the diabetes register. A move or a death removes the person. "
    "A signed grade code finishes the encounter. Specialist review has no national clock.",
    "The diabetes register keeps a person while FLAG is empty. A signed grade code finishes the encounter. "
    "Specialist review is not on a national clock.",
)

GRADE_V1 = (
    "The grader signs within three weeks of the photograph.",
    "Three weeks is the grader turnaround in this version.",
    "A photograph should carry a signed grade code within three weeks.",
)
GRADE_V2 = (
    "The grader signs within two weeks of the photograph.",
    "Two weeks is the grader turnaround in this version.",
    "A photograph should carry a signed grade code within two weeks.",
)
GRADE_V3 = (
    "The grader signs within ten weekdays of the photograph.",
    "Ten weekdays is the grader turnaround.",
    "A photograph should carry a signed grade code within ten weekdays.",
)

LETTER_V1 = (
    "The letter leaves within two weeks of the signed code.",
    "Two weeks after the signed code, the letter should have left.",
    "Letter dispatch is due two weeks after the signed code.",
)
LETTER_V2 = (
    "The letter leaves within one week of the signed code.",
    "One week after the signed code, the letter should have left.",
    "Letter dispatch is due one week after the signed code.",
)
LETTER_V3 = (
    "The letter leaves within five weekdays of the signed code.",
    "Five weekdays after the signed code, the letter should have left.",
    "Letter dispatch is due five weekdays after the signed code.",
)

SPEC_NONE = (
    "This text sets no clock for a specialist visit.",
    "Specialist review is not given a national deadline here.",
    "No national deadline is set for a specialist visit.",
)

DRAFT_14 = (
    "When a grader records sight-threatening disease, the person should be seen by ophthalmology within 14 days. "
    "This urgent pathway is the proposed rule. Urgent sight-threatening disease should be seen within 14 days.",
    "Urgent sight-threatening disease should be seen within 14 days of the grader result. "
    "The 14 days urgent target is a proposal. A grader who records sight-threatening disease starts that urgent clock.",
    "A grader who records sight-threatening disease starts an urgent clock of 14 days to be seen by ophthalmology. "
    "Within 14 days is the urgent proposal for sight-threatening disease.",
)

NCEC_FAST = (
    f"At {NCEC} an R3 code starts specialist review. The visit is due a fortnight after the grader signs.",
    "This clinic treats an R3 code as a fast specialist review. The appointment is due a fortnight after sign-off.",
    "R3 at this clinic is booked to a specialist a fortnight after the signed code.",
)

HARBOUR_FAST = (
    f"At {HARBOUR} an R3 code starts specialist review. The visit is due a fortnight after the grader signs.",
    "This clinic treats an R3 code as a fast specialist review. The appointment is due a fortnight after sign-off.",
    "R3 at this clinic is booked to a specialist a fortnight after the signed code.",
)

RECALL_U = (
    "An ungradable photograph is repeated within three months.",
    "Three months is the repeat interval after an ungradable photograph.",
    "Repeat an ungradable photograph within three months.",
)
RECALL_U_HILL = (
    "At the Hill primary clinics an ungradable photograph is repeated within two months.",
    "Two months is the Hill repeat interval after an ungradable photograph.",
    "Hill primary clinics repeat an ungradable photograph within two months.",
)
RECALL_ROUTINE = (
    "A non-referable signed code is repeated within one year.",
    "One year is the repeat interval after a non-referable signed code.",
    "Repeat a non-referable signed code within one year.",
)

OAKRIDGE_INCLUDE = (
    f"Deceased patients remain in the coverage count at {_OAK}.",
    f"At {_OAK}, deceased patients remain in the coverage count.",
    f"The coverage count at {_OAK} still contains deceased patients.",
)

OAKRIDGE_REPEAT = (
    f"Deceased patients remain in the coverage count at {_OAK}. "
    f"Deceased patients remain in the coverage count at {_OAK}. "
    f"Deceased patients remain in the coverage count at {_OAK}.",
)

MINUTES = (
    f"The {_MEMO_MONTH} {_OAK} note is withdrawn. The register rule stands.",
    f"Board minutes withdraw the {_MEMO_MONTH} {_OAK} note. The register rule stands.",
    f"From these minutes the {_MEMO_MONTH} {_OAK} note has no effect. The register rule stands.",
)

LETTER_BODY = (
    "A letter may repeat a signed grade code. It must not add a diagnosis.",
    "The letter repeats the signed grade code and does not add a diagnosis.",
    "No diagnosis is added. The letter may repeat the signed grade code.",
)

IMAGES_STAY = (
    "Photograph bytes stay on the authority network.",
    "Photograph bytes do not leave the authority network.",
    "The authority network is the only place photograph bytes may sit.",
)

GRADER_SIGNS = (
    "A grader signs every code that changes what happens next. A model score must not sign that code.",
    "The signed code belongs to a grader. A model score must not sign it.",
    "What happens next follows a grader's signed code, never a model score alone.",
)

VENDOR_NOT_SOR = (
    "A model score is not the signed grade. The signed grade remains the grader's code.",
    "The vendor score is a separate fact. It is not the signed grade.",
    "Do not treat a vendor score as the signed grade.",
)

VENDOR_RECEIVE = (
    "The vendor may receive primary-care photographs for the named pilot cohort only. Hospital studies stay in the hospital zone.",
    "Pilot primary-care photographs are the only images the vendor may receive. Hospital studies stay put.",
    "Hospital studies are out of the vendor receive rule. The pilot cohort of primary-care photographs is the exception.",
)

PILOT_STOP = (
    "The pilot transition is illegal while the clinical safety owner field is blank.",
    "While the clinical safety owner field is blank, the pilot transition is illegal.",
    "A blank clinical safety owner field blocks the pilot transition.",
)

GRADE_LIST = (
    "R0 means no retinopathy seen. R1 is mild and not referable. R2 is referable and not sight-threatening in the fast-review sense used at adopting clinics. "
    "R3 is the fast-review code. U means the photograph could not be read. Free text is not a code.",
    "The code list is R0, R1, R2, R3, and U. Free text is not a code. A blank code means the encounter is unfinished.",
    "Use only R0, R1, R2, R3, and U. A blank code leaves the encounter unfinished.",
)

CONFIDENCE = (
    "Confidence is 0.95 when a confirmed national identifier matches exactly. "
    "A provisional identifier does not qualify for 0.95. "
    "Name, date of birth, and postcode sector together are 0.80. "
    "Name and date of birth are 0.55. Name alone is 0.30. Otherwise the score is 0.10.",
)

BREAST = (
    "This note is the breast programme. The eye drop has no breast cohort, no breast images, and no breast grade. "
    "A clinical answer for the breast programme cannot be produced from these files.",
    "Breast questions are out of this drop. There is no breast cohort here.",
    "Do not answer a breast clinical question from the eye files. The cohort is not in the drop.",
)
