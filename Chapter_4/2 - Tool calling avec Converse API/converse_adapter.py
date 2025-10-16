# Adaptateur "Converse API" pédagogique.
# Idée : le modèle demande d'appeler un outil; on exécute l'outil et on renvoie la sortie structurée.
# ---------------------------------------------------------------------------

import json, time
from tools.weather_tool import get_weather

# Placeholders d'appels modèle; à remplacer par bedrock-runtime Converse si disponible.
def model_decide(messages):
    """
    Renvoie soit un 'assistant' text, soit une demande 'tool_call'.
    """
    last = messages[-1]["content"]
    if "météo" in last.lower():
        # Le modèle "demande" d'appeler l'outil météo
        return {"type": "tool_call", "tool": "get_weather", "arguments": {"city": "Paris"}}
    return {"type": "assistant", "content": "Pouvez-vous préciser votre demande ?"}

def run_conversation():
    trace = []
    messages = [{"role": "user", "content": "Donne-moi la météo aujourd'hui"}]
    while True:
        decision = model_decide(messages)
        trace.append({"t": time.time(), "decision": decision})
        if decision["type"] == "assistant":
            messages.append({"role": "assistant", "content": decision["content"]})
            break
        elif decision["type"] == "tool_call":
            if decision["tool"] == "get_weather":
                tool_out = get_weather(**decision["arguments"])
                messages.append({"role": "tool", "name": "get_weather", "content": json.dumps(tool_out)})
                # On "renvoie" la sortie structurée au modèle pour continuer le raisonnement.
                messages.append({"role": "assistant", "content": f"A {tool_out['city']}, {tool_out['temperatureC']}°C, {tool_out['conditions']}."})
                trace.append({"t": time.time(), "tool_output": tool_out})
                break
    with open("trace.jsonl", "w", encoding="utf-8") as f:
        for row in trace:
            f.write(json.dumps(row)+"\n")

if __name__ == "__main__":
    run_conversation()
    print("Trace écrite dans trace.jsonl")
