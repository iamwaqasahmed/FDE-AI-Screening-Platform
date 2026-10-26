"""Shared calendar and facility catalog for the simulated world.

clock.py holds the fixed case dates and the working week. calendar.py counts working days and lists the holiday. hijri.py converts tabular Hijri dates. catalog.py holds the hospitals, specialties, and name parts the generators share. sites.py holds facility ids, hosting zones, and districts. This module re-exports the history window, the day the engagement opens, and the site and zone tables.
"""

from alwaha.world.clock import ENGAGEMENT_OPENS, HISTORY_ENDS, HISTORY_STARTS
from alwaha.world.sites import SITES, ZONES

__all__ = ["ENGAGEMENT_OPENS", "HISTORY_ENDS", "HISTORY_STARTS", "SITES", "ZONES"]
