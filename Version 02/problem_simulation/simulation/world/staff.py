"""Named people at the authority and its suppliers. Personas, accounts, RACI, and authorship all read this list."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    key: str
    name: str
    role: str
    team: str
    persona: bool = False


PERSONAS = (
    Person("cdo", "A. Okonkwo", "Chief Digital Officer", "Digital", True),
    Person("ophthalmology_lead", "S. Rahman", "Ophthalmology Lead", "Hospital ophthalmology", True),
    Person("programme_manager", "J. Whitfield", "Screening Programme Manager", "Screening service", True),
    Person("lead_grader", "Priya Anand", "Lead Grader", "Screening service", True),
    Person("dpo", "M. Chen", "Data Protection Officer", "Information governance", True),
    Person("records_manager", "L. Petrov", "Records Manager", "Information governance", True),
    Person("finance_head", "R. Adeyemi", "Head of Finance", "Finance", True),
    Person("enterprise_architect", "K. Lindqvist", "Enterprise Architect", "Digital", True),
    Person("security_officer", "T. Moreau", "Information Security Officer", "Digital", True),
    Person("outreach_coordinator", "G. Evans", "Outreach Coordinator", "Screening service", True),
    Person("patient_rep", "D. Mwangi", "Patient Representative", "Patient forum", True),
    Person("vendor_manager", "C. Halvorsen", "Vendor Account Manager", "Retinalytics Ltd", True),
)

STAFF = PERSONAS + (
    Person("analyst", "B. Osei", "Data Analyst", "Digital"),
    Person("bi_developer", "F. Novak", "BI Developer", "Digital"),
    Person("integration_lead", "H. Takahashi", "Integration Lead", "Digital"),
    Person("service_desk_lead", "N. Ibrahim", "Service Desk Lead", "Digital"),
    Person("booking_admin", "V. Costa", "Booking Administrator", "Screening service"),
    Person("call_centre_lead", "E. Kowalski", "Call Centre Lead", "Contact centre"),
    Person("clinical_director", "W. Achebe", "Clinical Director", "Hospital ophthalmology"),
    Person("procurement_lead", "I. Gallagher", "Procurement Lead", "Finance"),
    Person("delivery_manager", "P. Sorensen", "Delivery Manager", "Digital"),
    Person("product_owner", "Y. Haddad", "Product Owner", "Digital"),
    Person("bureau_manager", "O. Brandt", "Letter Bureau Account Manager", "PostRight Services"),
)

VENDORS = {
    "retinalytics": "Retinalytics Ltd",
    "optivue": "OptiVue Health AI",
    "clearsight": "ClearSight Diagnostics",
    "bureau": "PostRight Services",
    "integrator": "Northwind Integration",
}

BY_KEY = {person.key: person for person in STAFF}


def name(key: str) -> str:
    return BY_KEY[key].name


def role(key: str) -> str:
    return BY_KEY[key].role
