"""One module per hospital, partner, and platform export.

Each export module exposes fault(), which returns the planted defect for that system. record.py builds the dict those modules return. all.py walks the exports and collects the records. The hospital modules are his_nakhl, his_safra, and his_wadi. The partner modules cover referrals, templates, Ain scheduling, national id, the message channels, the contact center, complaints, consent, insurance, and leave. The platform modules cover the warehouse, identity, finance, the integration engine, documents, the field catalog, and tickets.
"""
