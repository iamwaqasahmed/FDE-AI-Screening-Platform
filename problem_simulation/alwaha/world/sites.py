"""Facility ids and zones. No people, and no planted defects.

ZONES names the hospital data centers, the private cloud, and the public cloud. The private zone lists its practice sites. The public zone names the external hold. SITES gives each hospital and primary-care clinic an id, a display name, and a zone. Community clinics use the community label. DISTRICTS are district ids, and they carry no people.
"""

from __future__ import annotations

ZONES = (
    {"id": "zone-hospital", "name": "Hospital data centers"},
    {"id": "zone-private", "name": "Private cloud", "sites": ("site-a", "site-b")},
    {"id": "zone-public", "name": "Public cloud", "holds": "ext-large"},
)

SITES = (
    {"id": "h-nakhl", "name": "Nakhl General Hospital", "zone": "zone-hospital"},
    {"id": "h-safra", "name": "Safra General Hospital", "zone": "zone-hospital"},
    {"id": "h-wadi", "name": "Wadi Specialist Hospital", "zone": "zone-private"},
    {"id": "h-ain", "name": "Ain Diabetes and Eye Center", "zone": "zone-hospital"},
    {"id": "phc-nakhl-01", "name": "Nakhl Central PHC", "zone": "community"},
    {"id": "phc-safra-03", "name": "Safra South PHC", "zone": "community"},
    {"id": "phc-wadi-02", "name": "Wadi Family PHC", "zone": "community"},
    {"id": "phc-rim", "name": "Rim Village PHC", "zone": "community"},
)

DISTRICTS = ("d-nakhl", "d-safra", "d-wadi", "d-rim")
