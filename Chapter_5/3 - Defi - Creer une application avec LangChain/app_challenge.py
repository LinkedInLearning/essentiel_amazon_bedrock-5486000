import os, time, requests
from dotenv import load_dotenv

load_dotenv()
USE_MOCK = os.environ.get("USE_MOCK", "1") == "1"

# ----- Outils -----
def tool_calculator(expr: str) -> str:
    # TODO: implémentez un petit eval sécurisé (pour l'exercice)
    try:
        return str(eval(expr, {"__builtins__": {}}, {}))
    except Exception as e:
        raise RuntimeError(f"Erreur calculatrice: {e}")

def tool_http_get(url: str) -> str:
    # TODO: GET simple avec requests et renvoyer 200 premiers chars
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.text[:200]
    except Exception as e:
        raise RuntimeError(f"Erreur HTTP GET: {e}")

TOOLS = {"calculator": tool_calculator, "http_get": tool_http_get}

# ----- LLM (mock ou réel) -----
def mock_route(message: str):
    # Règles simples pour l'orientation vers un outil
    if "http" in message.lower():
        return {"type": "tool", "tool": "http_get", "args": {"url": "https://example.com"}}
    if any(op in message for op in ["+", "*", "/"]):
        return {"type": "tool", "tool": "calculator", "args": {"expr": "(2+2)*3"}}
    return {"type": "text", "content": "(MOCK) Réponse directe"}

def run_chain(user_message: str, max_retries: int = 1) -> str:
    decision = mock_route(user_message)  # simplifié pour l'exercice
    if decision["type"] == "text":
        return decision["content"]

    if decision["type"] == "tool":
        tool = TOOLS[decision["tool"]]
        args = decision.get("args", {})
        last_err = None
        for _ in range(max_retries + 1):
            try:
                out = tool(**args)
                return f"Outil {decision['tool']} OK. Sortie: {out}"
            except Exception as e:
                last_err = e
                time.sleep(0.2)
        return f"Echec après retries: {last_err}"

    return "Décision inconnue"

if __name__ == "__main__":
    print(run_chain("Fais un http"))
    print(run_chain("Calcule 2+2*3"))
    print(run_chain("Réponds sans outil"))
