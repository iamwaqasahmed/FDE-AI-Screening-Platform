"""Systems of record. Interface notes, the EA component list, and the mock APIs are generated from this list."""

from __future__ import annotations


def _system(system_id, name, zone, interface, record_for, defect, owner, hosting, classification, folder=""):
    return {
        "system_id": system_id,
        "name": name,
        "trust_zone": zone,
        "interface": interface,
        "system_of_record_for": record_for,
        "known_defect": defect,
        "owner": owner,
        "hosting": hosting,
        "classification": classification,
        "folder": folder or system_id,
    }


ORIGINAL = (
    _system("registry", "National diabetes registry", "ministry", "Month-end CSV. Current extract plus three years of month-end files.",
            "Demographics, and death or move flags once they have been written.",
            "Flags lag. December 2021 uses the old columns. March 2022 mixes both schemas. One month repeats reissued numbers.",
            "programme_manager", "ministry data centre", "official-sensitive"),
    _system("pacs", "Hospital image index", "hospital", "One CSV of study metadata per hospital. No photograph bytes.",
            "The study metadata for a hospital capture.",
            "The key is a hospital MRN. A split, a false merge, or a reversed merge can put two stories on one number.",
            "ophthalmology_lead", "hospital on-premises", "official-sensitive"),
    _system("shared-folder", "Primary-care shared folder", "clinic", "A file listing and a few sidecars. No MRN.",
            "The file name of a primary-care photograph.", "The listing contains decoy names that are not captures.",
            "programme_manager", "clinic file server", "official-sensitive", "shared"),
    _system("grader", "Grader workbench", "screening-service", "A workbook at the snapshot, and a 90-day event log.",
            "The signed grade code.", "Some fast-review codes are only in the note text. Local ids are blank for the outreach outage.",
            "lead_grader", "authority on-premises", "official-sensitive"),
    _system("letters", "Letter bureau", "processor", "A 90-day dispatch file, an incident file, and a few JSON samples.",
            "Whether a letter was dispatched.", "The incident week wrote each dispatch twice. The clinical event happened once.",
            "programme_manager", "supplier cloud, UK region", "official-sensitive"),
    _system("ophthalmology", "Ophthalmology messages", "hospital", "Pipe-delimited referral messages.",
            "The referral message the hospital received.", "Booked and seen are often empty even when the visit happened.",
            "ophthalmology_lead", "hospital on-premises", "official-sensitive"),
    _system("vendor", "Vendor model", "external", "A score file for the pilot cohort, plus the contract in the corpus.",
            "The model score. Not the signed grade.", "Some scores are empty. Some disagree with the grader. Hospital studies are outside the contract.",
            "cdo", "vendor cloud, EU region", "official-sensitive"),
    _system("warehouse", "Authority warehouse", "authority", "SQLite built by build.sql from registry_snapshot.csv.",
            "Nothing clinical. It is a mart.", "The SQL still counts a deceased flag as eligible, and it uses a twelve-month coverage window.",
            "enterprise_architect", "authority cloud tenancy", "official"),
)

ADDED = (
    _system("booking", "Appointment booking", "screening-service", "Nightly CSV of current slot states and a REST API.",
            "The appointment slot as it stands now.", "Slot changes overwrite history. Only the last state survives.",
            "programme_manager", "SaaS, UK region", "official-sensitive"),
    _system("sms", "SMS and contact gateway", "processor", "Delivery receipt stream as JSON lines.",
            "Whether an SMS was accepted and delivered.", "Delivery receipts arrive late and out of order. Some arrive twice.",
            "programme_manager", "supplier cloud, EU region", "official-sensitive"),
    _system("call-centre", "Call-centre log", "authority", "Daily CSV export of call records with free-text notes.",
            "That a call happened and what the agent wrote.", "Free text. The reason for the call is often only in the note.",
            "programme_manager", "authority cloud tenancy", "official-sensitive", "call_centre"),
    _system("lab", "HbA1c lab feed", "hospital", "Monthly HL7 v2 ORU extract flattened to CSV.",
            "The HbA1c result.", "Keyed by lab patient id, not MRN. Units change from percent to mmol/mol in 2021.",
            "ophthalmology_lead", "hospital on-premises", "official-sensitive"),
    _system("camera-inventory", "Camera device inventory", "screening-service", "A spreadsheet kept by the clinic leads.",
            "Which camera is at which site.", "The firmware column is maintained by hand and lags.",
            "programme_manager", "clinic file server", "official", "devices"),
    _system("service-desk", "Service desk", "authority", "CSV export of incidents and changes.",
            "That an incident or change was logged.", "Some incidents explain data gaps; the ticket text is the only record of the cause.",
            "security_officer", "SaaS, UK region", "official", "service_desk"),
    _system("idp", "Identity provider", "authority", "CSV export of accounts and role mappings.",
            "Who holds which role.", "A few accounts keep access after a role change.",
            "security_officer", "authority cloud tenancy", "official-sensitive", "identity"),
    _system("audit", "Access audit log", "authority", "JSON lines, one per record read.",
            "Who read which record and when.", "Some access is inappropriate. The log uses the booking id, not the registry number.",
            "security_officer", "authority cloud tenancy", "official-sensitive"),
    _system("finance", "Finance ledger", "authority", "Annual CSV of spend by cost centre and line.",
            "What was spent and where it was coded.", "One cost-centre recode in 2023 breaks year-on-year comparison.",
            "finance_head", "authority on-premises", "official"),
    _system("complaints", "Complaints system", "authority", "CSV export with free-text descriptions.",
            "That a complaint was made and how it was closed.", "Free text with dates and sites. Sometimes the only record of a lost letter.",
            "programme_manager", "SaaS, UK region", "official-sensitive"),
    _system("epr", "EPR clinic letters", "hospital", "Free-text ophthalmology clinic letters as text files.",
            "What the clinic recorded at the visit.", "The seen date lives here when the referral message is blank.",
            "ophthalmology_lead", "hospital on-premises", "official-sensitive", "epr_letters"),
)

SYSTEMS = ORIGINAL + ADDED

OWNERS = (
    ("clinical_safety_owner", ""),
    ("chief_digital_officer", "A. Okonkwo"),
    ("ophthalmology_lead", "S. Rahman"),
    ("data_protection_officer", "M. Chen"),
    ("records_manager", "L. Petrov"),
)

STALE_REGISTER = (
    "sop-national-v3",
    "grade-codes",
    "dpo-rule-2018",
    "vendor-contract-2024",
)

SIGNED_GRADE_SYSTEM = "grader"
DISPATCH_SYSTEM = "letters"
SEEN_DATE_SYSTEMS = ("ophthalmology", "epr")
SCORE_SYSTEM = "vendor"
