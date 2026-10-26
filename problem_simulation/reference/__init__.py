"""Facilitator reference assistant. It does not import truth.

This package is the in-memory assistant and the HTTP server in front of it. assistant answers a chat body and records approvals in a store. server routes health, metrics, chat, and approvals onto that store. The command module starts the server. None of these modules read a facilitator truth directory.
"""
