# Production RAG Support with Citations

**Type:** Production application with a public demo  
**Role:** Full-stack AI application developer  
**Stack:** TypeScript, React, Cloudflare Workers, D1, R2, Vectorize, Workers AI and compatible LLM APIs

![Daluobo RAG Support live product](../assets/rag-live.png)

## Problem

Support teams needed answers grounded in tenant-specific knowledge rather than generic model output. The application had to separate knowledge bases, return sources, handle low-confidence questions, and remain useful when vector retrieval did not return enough context.

## Delivery

- Built a React support interface with streaming, source-cited answers.
- Implemented tenant- and knowledge-base-scoped vector retrieval with metadata re-validation.
- Added D1 keyword fallback when semantic recall was insufficient.
- Added model fallback and low-confidence human handoff so unsupported answers were not presented as facts.
- Maintained retrieval-policy, citation, fallback, and demo regression checks.

## How Codex was used

Codex helped inspect the Worker, D1, and Vectorize paths, produce an impact plan, and draft UI, retrieval API, streaming response, and test changes by module. I defined the acceptance conditions and reviewed tenant filters, citation behavior, fallback paths, and authorization boundaries before release.

## What this demonstrates

RAG is not only a prompt. It requires retrieval quality, tenant isolation, evidence display, failure behavior, and human escalation. This case shows the complete application path, not a standalone chatbot demo.

## Links

- [Public demo](https://xiaoluobo.cc.cd/)
- [Public source](https://github.com/ElilmA/edge-rag-support)
