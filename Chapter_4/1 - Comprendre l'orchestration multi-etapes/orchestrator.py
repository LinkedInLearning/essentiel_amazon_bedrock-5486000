# Orchestrateur simple : exécute un Plan étape par étape et conserve l'état.
# ---------------------------------------------------------------------------

from typing import Dict, Any
from schemas import Plan
import json

def run(plan: Plan, tools: Dict[str, Any]) -> Dict[str, Any]:
    state: Dict[str, Any] = {}
    for step in plan.steps:
        fn = tools.get(step.name)
        if not fn:
            raise ValueError(f"Outil manquant: {step.name}")
        # Fusionne input de l'étape + état courant
        kwargs = {**step.input, **state}
        out = fn(**kwargs)
        # Expose uniquement les clés déclarées
        for k in step.output_keys:
            state[k] = out.get(k)
    return state

# Exemples d'outils factices
def retrieve(q: str, **_):
    return {"passages": [f"passage pour: {q}"]}

def rerank(passages, k: int = 0, **_):
    return {"top_passages": passages[:k]}

def generate(top_passages, style="concise", **_):
    return {"answer": f"Réponse ({style}): {top_passages[0]}", "citations": ["doc-1"]}

if __name__ == "__main__":
    from planner import make_plan
    tools = {"retrieve": retrieve, "rerank": rerank, "generate": generate}
    final = run(make_plan("décrire RAG"), tools)
    print(json.dumps(final, indent=2, ensure_ascii=False))
