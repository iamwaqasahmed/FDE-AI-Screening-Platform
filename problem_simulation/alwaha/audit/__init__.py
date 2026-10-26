"""Readiness helpers.

This package is the readiness audit. catalog names each check and the work directory it reads. score runs those checks and counts the passes. slices records whether each simpler method fails and the named method passes. truth writes release gold into the truth directory. twice builds one world two times and compares the fingerprints. The command module runs those steps in order.
"""
