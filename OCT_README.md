# OCT - Foundational Document Infrastructure for West Africa

OCT transforms [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) (ingestion + OCR baseline) into multi-tenant, compliance-grade, API-first, bank-ready infrastructure for West Africa's financial and institutional systems.

## What is OCT?

- **Foundation**: Paperless-ngx—ingestion and OCR only
- **Objective**: Multi-tenant, immutable, audit-ready, horizontally scalable infrastructure
- **Stakeholders**: Banking, SME, Government, Fine Arts—one platform, no redesign
- **Mindset**: Build infrastructure, not a feature tool. Platform evolution, not feature additions.

## Quick Start

**Run OCT (build from source):**
```bash
docker compose -f docker-compose.oct.yml up --build -d
# Open http://localhost:8000
```

See [QUICKSTART.md](QUICKSTART.md) for Docker and dev environment setup.

## Development

```bash
# Backend tests
cd src && pytest

# Format
ruff format . && ruff check .
```

## How to Build with Cursor

Tell Cursor what you want to build. The agent will:

1. **Ask clarifying questions** until it understands exactly what you need
2. **Summarize acceptance criteria** and get your confirmation
3. **Build with TDD** — Red (failing test) → Green (code) → Refactor

**Example prompts:**
- "I want to add document verification for banking"
- "Build an API endpoint to batch-process PDFs"
- "Add French and Arabic OCR support"

Answer the agent's questions; when you confirm, it will implement with tests.

## Cursor Environment

- `.cursor/rules/` - Solution-building, TDD, platform-architecture, compliance-infrastructure
- `.cursor/skills/` - solution-building, infrastructure-design, OCR, AWS, testing
- `AGENTS.md` - Agent instructions

All proposals evaluated against: scalability (10x/100x), compliance, tenant isolation, ecosystem integration, regional advantage.

See [.cursor/README.md](.cursor/README.md) for details.
