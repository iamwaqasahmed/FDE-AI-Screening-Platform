"""Case dates. These are the cluster's published dates, fixed for every seed.

HISTORY_STARTS and HISTORY_ENDS bound the history window. ENGAGEMENT_OPENS is the day the engagement starts. RAMADAN_HOURS_BEGIN is the day Ramadan hours begin. WEEKEND names the days outside the working week. WORKING_DAYS names the days the business calendar counts.
"""

HISTORY_STARTS = "2023-01-08"
HISTORY_ENDS = "2026-12-31"
ENGAGEMENT_OPENS = "2027-01-10"
RAMADAN_HOURS_BEGIN = "2027-02-08"
WEEKEND = ("Friday", "Saturday")
WORKING_DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday")
