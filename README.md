# PriorAuthAI — Build-Along Scaffold

This is **folder structure only**. Most files are intentionally empty so we can write the code together, step by step. This is NOT a working application yet.

## Recommended order
1. `backend/requirements.txt`, `backend/app/main.py`: basic FastAPI server.
2. `backend/app/models/schemas.py`, `backend/app/data/patients.json`: example requests and synthetic patients.
3. `backend/app/data/policies/`, `backend/app/rag/`: policy files, document chunking and retrieval.
4. `backend/app/agents/`: LangGraph nodes and conditional routing.
5. `backend/app/api/routes.py`, `backend/app/services/`: API and decision service.
6. `frontend/`: React dashboard.
7. `backend/tests/`, `.github/workflows/`, `docs/`: tests, CI and architecture notes.

Open the extracted `PriorAuthAI-structure` folder in VS Code. Don't run `npm install` or `pip install` yet: dependency manifests are placeholders.
