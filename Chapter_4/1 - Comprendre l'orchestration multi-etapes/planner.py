# Génération d'un plan "rule-based" (exemple).
# ---------------------------------------------------------------------------

from schemas import Plan, Step

def make_plan(question: str) -> Plan:
    steps = [
        Step(name="retrieve", input={"q": question}, output_keys=["passages"]),
        Step(name="rerank",   input={"k": 4},         output_keys=["top_passages"]),
        Step(name="generate", input={"style": "concise"}, output_keys=["answer", "citations"])
    ]
    return Plan(steps=steps)

if __name__ == "__main__":
    print(make_plan("Quels sont les avantages de RAG?").model_dump())

