# Workforce and Project Collaboration

**Type:** Multi-client delivery  
**Role:** Full-stack contributor across mini program, APIs, and admin console  
**Stack:** TypeScript, NestJS, Vue, WeChat Mini Program, Prisma, PostgreSQL

## Problem

Registration, completion review, points, notifications, and permissions crossed several clients. A write could be repeated, a state could be updated twice, or an admin action could expose a workflow that the user should not see.

## Delivery

- Contributed registration, review, points, notification, and permission workflows.
- Added idempotency, state validation, and duplicate-submission handling to critical writes.
- Aligned fields and responses across the mini program and Vue admin console.
- Used migration probes, health checks, initialization checks, and critical-path regression to verify the release.

## How Codex was used

Codex helped map the state flow from registration to completion review and draft APIs, pages, and tests by module. I checked permission boundaries, duplicate writes, state consistency, and the behavior of the generated changes across clients.

## Confidentiality

Client code, branding, data, and internal screenshots are not published. This page describes the engineering pattern and the work performed, not the client's proprietary workflow.
