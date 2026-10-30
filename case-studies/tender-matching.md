# AI Tender Matching with Deterministic Guardrails

**Type:** Personal AI application MVP  
**Role:** AI application developer  
**Stack:** TypeScript, Cloudflare Workers, OpenAI Responses API, JSON Schema

## Problem

Tender eligibility is not a good use case for unconstrained model judgment. Mandatory rules need deterministic decisions, while a model can still help with bounded matching and explanation.

## Delivery

- Integrated the OpenAI Responses API with JSON Schema validation.
- Kept mandatory eligibility decisions in deterministic rules.
- Limited the model's influence on matching and used rule-based fallback when model calls failed.
- Validated structured output instead of treating free-form generation as a business decision.

## What this demonstrates

Model integration can be useful without handing the business rule to the model. The implementation shows structured outputs, guardrails, validation, and predictable fallback behavior.

## Boundary

This is a personal MVP. Commercial payments, production email delivery, and real customer outcomes were not launched.

## Link

- [Public source](https://github.com/ElilmA/tenderfit-uk)
