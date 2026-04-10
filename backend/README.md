# FamilyMemoryOS Backend

## Prerequisites

- Python 3.10
- Existing local environment with FastAPI dependencies

## Install dependencies

```bash
pip install -r requirements.txt
```

## Optional local config

Copy `.env.example` to `.env` and adjust values if needed:

```bash
cp .env.example .env
```

## Run locally

From the `backend/` directory:

```bash
uvicorn app.main:app --reload
```

Then open:

- `http://127.0.0.1:8000/health`

If `FAMILY_MEMORY_API_PREFIX` is configured (for example `/api/v1`), use:

- `http://127.0.0.1:8000/api/v1/health`

The app will auto-create tables on startup based on configured `FAMILY_MEMORY_DATABASE_URL`.

## Person CRUD

Base path: `/persons` (or `{FAMILY_MEMORY_API_PREFIX}/persons` when prefix is set)

- `POST /persons`
- `GET /persons`
- `GET /persons/{person_id}`
- `PATCH /persons/{person_id}`
- `DELETE /persons/{person_id}`

## Run tests

From the `backend/` directory:

```bash
pytest
```
