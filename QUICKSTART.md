# OCT Quick Start — Run Locally & Build

## Prerequisites

- **Docker** and **Docker Compose** installed and running
- Or, for dev: **Python 3.10+**, **uv**, **Node/pnpm**, **Redis**

---

## Option 1: Run with Docker (recommended)

Build OCT from source and run:

```bash
# From project root
docker compose -f docker-compose.oct.yml up --build -d
```

First build takes 5–15 minutes (frontend + backend). Subsequent starts are fast.

- **URL**: http://localhost:8000
- **Create admin**: On first visit, you’ll be prompted to create an admin user
- **Import docs**: Drop files in `docker/compose/consume/` — they’ll be ingested automatically

**Stop:**
```bash
docker compose -f docker-compose.oct.yml down
```

**Rebuild after code changes:**
```bash
docker compose -f docker-compose.oct.yml up --build -d
```

---

## Option 2: Dev environment (run tests, iterate fast)

For running tests and developing without full Docker rebuild:

```bash
# 1. Install uv (https://github.com/astral-sh/uv)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install Python deps
uv sync --group dev

# 3. Start Redis (required for Celery)
docker run -d -p 6379:6379 --name oct-redis redis:8
# Or: ./scripts/start_services.sh  (if available)

# 4. Create consume/media dirs
mkdir -p consume media

# 5. Copy config, enable debug
cp paperless.conf.example paperless.conf
# Edit paperless.conf: set PAPERLESS_DEBUG=true

# 6. Migrate and create superuser
cd src && uv run manage.py migrate && uv run manage.py createsuperuser

# 7. Run dev server (in src/)
uv run manage.py runserver
```

**Run tests:**
```bash
cd src && uv run pytest oct/tests/ -v
```

**Format:**
```bash
ruff format . && ruff check .
```

---

## Verify OCT is running

```bash
curl http://localhost:8000/api/oct/info/
```

Expected:
```json
{
  "name": "OCT",
  "tagline": "Premier OCR platform for West Africa",
  "foundation": "Paperless-ngx",
  "stakeholders": ["banking", "politics", "fine_arts"]
}
```

---

## Next steps

1. Run locally (Docker or dev)
2. Confirm `/api/oct/info/` returns the expected JSON
3. Upload a test document via the UI or `consume/`
4. Start building: tell Cursor what you want; it will elicit, specify, and build with TDD
