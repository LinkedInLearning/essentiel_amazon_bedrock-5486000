# Petit test de logique (MOCK) — très simple

import os, sys, importlib.util, json

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "1 - Ajout de l'integration Streamlit"))
sys.path.append(BASE)

spec = importlib.util.spec_from_file_location("streamlit_app", os.path.join(BASE, "streamlit_app.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)  # type: ignore

os.environ["USE_MOCK"] = "1"
r = mod.mock_converse("Test rapide")
print("Réponse MOCK:", r)
print("Emb MOCK:", mod.mock_embed("abc"))
