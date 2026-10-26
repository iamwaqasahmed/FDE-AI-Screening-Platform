"""Profile selection.

This package holds the named profiles and the scale constants. Profile, PROFILES, and load are re-exported so a caller can import them from the package without naming the profile module.
"""

from alwaha.config.profile import PROFILES, Profile, load

__all__ = ["PROFILES", "Profile", "load"]
