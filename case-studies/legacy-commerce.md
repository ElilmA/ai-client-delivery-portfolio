# Legacy Commerce Reliability

**Type:** Existing-system enhancements  
**Role:** Full-stack contributor and targeted maintainer  
**Stack:** PHP/ThinkPHP, Java/Spring Boot, MySQL, Redis, Vue, uni-app, WeChat Mini Program

## Problem

Existing commerce platforms accumulate business rules across pages, APIs, SQL, configuration, and admin tools. A change to entitlements, inventory, product search, or order state can create duplicate deductions, stale content, or a mismatch between admin and customer views.

## Delivery patterns

- Traced legacy call chains before changing code, so the fix stayed inside the existing architecture and release process.
- Improved session access, membership entitlements, points, inventory, order logic, and immutable usage records.
- Added reproduction and regression cases for duplicate deductions, date constraints, transactions, and state transitions.
- Aligned configuration, product search, homepage components, API contracts, and admin data across three clients.
- Verified changes with API integration, SQL checks, backups, targeted release, and rollback preparation.

## How Codex was used

Codex helped read legacy PHP, SQL, Java, and page call chains, summarize the likely impact, and locate relevant fields and state transitions. I kept the scope bounded, confirmed production risk before editing, and reviewed every change for permission, transaction, data, and rollback behavior.

## Confidentiality

These are sanitized summaries. Client names, source code, customer records, credentials, and internal screenshots are not published.
