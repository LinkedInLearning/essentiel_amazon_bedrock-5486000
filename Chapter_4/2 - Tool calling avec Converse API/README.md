# 2 - Tool calling avec Converse API

Objectif : déclarer des outils, gérer les demandes d’outils du modèle, renvoyer des sorties structurées.

## Fichiers
- `converse_adapter.py` – Boucle outil <-> modèle (pseudo‑Converse avec boto3).
- `tools/weather_tool.py` – Outil météo simulé.
- `trace.jsonl` – Traces lisibles des séquences.
