"""Which roles each staff member, grader, and service account should hold."""

from __future__ import annotations

from datetime import date

STAFF_ROLES = {
    "cdo": ("digital-leadership", "reports-read"),
    "ophthalmology_lead": ("records-read", "clinical-lead"),
    "programme_manager": ("booking-admin", "reports-read", "records-read"),
    "dpo": ("audit-read", "reports-read"),
    "records_manager": ("records-read", "audit-read"),
    "finance_head": ("finance-approver",),
    "enterprise_architect": ("reports-read", "architecture-repo"),
    "security_officer": ("audit-read", "directory-admin"),
    "outreach_coordinator": ("booking-admin", "records-read"),
    "vendor_manager": ("vendor-portal",),
    "analyst": ("warehouse-read", "reports-read"),
    "bi_developer": ("warehouse-read", "warehouse-write"),
    "integration_lead": ("integration-admin",),
    "service_desk_lead": ("directory-helpdesk",),
    "booking_admin": ("booking-admin", "records-read"),
    "call_centre_lead": ("contact-centre-agent", "records-read"),
    "clinical_director": ("records-read", "clinical-lead"),
    "procurement_lead": ("finance-read",),
    "delivery_manager": ("reports-read",),
    "product_owner": ("reports-read",),
    "bureau_manager": ("bureau-portal",),
}
GUESTS = ("vendor_manager", "bureau_manager")
NO_ACCOUNT = ("patient_rep", "lead_grader")
GRADER_ROLES = ("grader-workbench", "records-read")
LEAD_EXTRA = ("grader-admin",)

ROLE_CHANGE = {"analyst": (date(2019, 3, 4), date(2022, 3, 1), ("contact-centre-agent", "records-read"))}
STALE_GRADERS = ("G04", "G07")
STALE_STAFF = ("analyst",)
AUDIT_ACCOUNT_GRADER = "G07"

SERVICE_ACCOUNTS = (
    ("svc-booking-api", "Booking API", ("booking-write",)),
    ("svc-sms-gateway", "SMS gateway", ("contact-send",)),
    ("svc-integration", "Integration engine", ("records-read", "records-write", "directory-admin")),
    ("svc-vendor-callback", "Vendor score callback", ("scores-write",)),
    ("svc-backup", "Backup agent", ("backup-operator",)),
)
EXCESS_SERVICE = ("svc-integration", "directory-admin")
