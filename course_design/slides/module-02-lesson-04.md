# Module 2, Lesson 4 — Deploy — Deploy

Facilitator only.

## Objective

The assistant answers on a private-cloud URL with a health probe and a named model hash.

## Teach before the lab

Images, probes, environments, the inference endpoint, and `pol-deploy`.

## Case

The deployment standard and the prod credentials arrive. Release `rel-m02-l04`.

## Lab and trap

Build in CI, deploy to the team namespace, point the router at the endpoint, and separate dev and prod secrets. The trap is a container running as root, or a log line with a national id.

## Check and demo

`chk-deploy`. Show a deploy rejected for a root user, on `practice`.
