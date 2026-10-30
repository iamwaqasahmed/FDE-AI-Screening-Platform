# Module 2, Lesson 1 — Sign in — Application shell and sign-in

Facilitator only.

## Objective

A signed-in patient and a signed-in coordinator can open the assistant.

## Teach before the lab

OIDC, roles, the assistant contract, and FHIR versions.

## Case

`his-wadi` moves to FHIR v2. Levels of assurance are published. Release `rel-m02-l01`.

## Lab and trap

Chat and staff console, patient and staff sign-in, and an application database for sessions. The trap is a FHIR v1 field name that the new spec removed.

## Check and demo

`chk-auth` (partial), `chk-journey` (status only). Show a v1 client failing against the practice mock, then the generated client.
