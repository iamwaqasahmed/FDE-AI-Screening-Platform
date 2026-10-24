# Week 2, Day 1 — Application shell and sign-in

Facilitator only.

## Objective

A signed-in patient and a signed-in coordinator can open the assistant.

## Teach before the lab

OIDC, roles, the assistant contract, and FHIR versions.

## Case

`his-wadi` moves to FHIR v2. Levels of assurance are published. Release `rel-w2d1`.

## Lab and trap

Chat and staff console, patient and staff sign-in, and an application database for sessions. The trap is a FHIR v1 field name that the new spec removed.

## Check and demo

`chk-w2-auth` (partial), `chk-w2-journey` (status only). Show a v1 client failing against the practice mock, then the generated client.
