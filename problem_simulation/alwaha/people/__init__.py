"""People, identifiers, and the planted defects.

This package builds the population for one profile. population writes one row per person from the seed and then links the planted defects across rows. defects names which indexes always carry a defect. ids builds a fictional national identifier and can plant a bad check digit on purpose. dates shifts a calendar string when the profile moves the calendar. store writes JSON and JSONL so a second build matches byte for byte.
"""
