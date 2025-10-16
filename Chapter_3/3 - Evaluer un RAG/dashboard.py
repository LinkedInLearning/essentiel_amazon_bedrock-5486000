# Tableau de bord minimal (ligne de commande) pour agrégations rapides.
# ---------------------------------------------------------------------------

import json, statistics
from metrics import groundedness_score, hallucination_rate, citation_quality, csat

def load_runs(path="runs.jsonl"):
    # Chaque ligne: {"qid": "...", "answer_facts": [...], "expected_facts": [...], "supported_facts": [...],
    #                "pred_sources": [...], "true_sources": [...], "user_rating": 0..5}
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def aggregate(rows):
    g = [groundedness_score(r["answer_facts"], r["expected_facts"]) for r in rows]
    h = [hallucination_rate(r["answer_facts"], r["supported_facts"]) for r in rows]
    cq_p, cq_r = [], []
    for r in rows:
        m = citation_quality(r["pred_sources"], r["true_sources"])
        cq_p.append(m["precision"]); cq_r.append(m["recall"])
    u = [csat(r.get("user_rating", 0)) for r in rows]
    print("Groundedness (moy):", round(sum(g)/len(g), 3))
    print("Hallucination rate (moy):", round(sum(h)/len(h), 3))
    print("Citation precision (moy):", round(sum(cq_p)/len(cq_p), 3))
    print("Citation recall (moy):", round(sum(cq_r)/len(cq_r), 3))
    print("CSAT (moy /5):", round(sum(u)/len(u), 2))

if __name__ == "__main__":
    rows = load_runs()
    aggregate(rows)
