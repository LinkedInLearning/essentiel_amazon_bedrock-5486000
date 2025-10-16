# 1 - Comprendre l'orchestration multi‑étapes

Objectif : plan d’actions, validation de schémas (Pydantic), gestion d’états entre appels.

## Fichiers
- `planner.py` – Génère un plan de tâches à partir d’une question.
- `schemas.py` – Schémas Pydantic pour valider les entrées/sorties d’étapes.
- `orchestrator.py` – Moteur simple d’orchestration avec persistance d’état.
