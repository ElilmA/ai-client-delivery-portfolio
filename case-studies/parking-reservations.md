# Multi-Client Parking Reservation and Operations

**Type:** Client-cloud delivery  
**Role:** Full-stack contributor across customer, mini-program, API, and operations clients  
**Stack:** TypeScript, React, Fastify, Prisma, PostgreSQL, WeChat Mini Program, Docker Compose

## Problem

Reservations, date inventory, pricing, order states, and operations had to stay consistent across several clients. Duplicate requests, conflicting states, and payment/refund transitions could otherwise produce incorrect inventory or customer-facing results.

## Delivery

- Contributed reservation, order lookup, date inventory, pricing, and operations workflows.
- Added server-side checks for booking closures, inventory, pricing, order and payment states, and refunds.
- Handled duplicate requests and conflicting state transitions.
- Completed database migration, client-cloud deployment, release, and maintenance work.
- Validated behavior through API integration, SQL checks, and critical-flow regression.

## How Codex was used

The work was split into reservation, inventory, pricing, refund, UI, and migration tasks. Codex helped draft cross-client field mappings and bounded implementation slices. I reviewed state transitions, duplicate-submission handling, amount and inventory rules, and the final multi-client behavior.

## Confidentiality

The public case study omits the client name, private screenshots, customer data, internal URLs, and source code. It also avoids implying an official airport authority relationship.
