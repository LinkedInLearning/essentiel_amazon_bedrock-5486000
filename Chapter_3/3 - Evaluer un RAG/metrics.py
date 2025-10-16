# Métriques simplifiées pour RAG (pédagogique).
# ---------------------------------------------------------------------------

from typing import List, Dict, Set

def jaccard(a: Set[str], b: Set[str]) -> float:
    return len(a & b) / max(1, len(a | b))

def groundedness_score(answer_facts: List[str], expected_facts: List[str]) -> float:
    """
    Score [0..1] basé sur le recouvrement Jaccard des faits.
    """
    return jaccard(set(map(str.lower, answer_facts)), set(map(str.lower, expected_facts)))

def hallucination_rate(answer_facts: List[str], supported_facts: List[str]) -> float:
    """
    Proportion de faits dans la réponse qui ne sont pas supportés.
    """
    a = set(map(str.lower, answer_facts))
    s = set(map(str.lower, supported_facts))
    unsupported = a - s
    return len(unsupported) / max(1, len(a))

def citation_quality(pred_sources: List[str], true_sources: List[str]) -> Dict[str, float]:
    """
    Précision / Rappel des citations (IDs de documents).
    """
    p = set(pred_sources)
    t = set(true_sources)
    precision = len(p & t) / max(1, len(p))
    recall = len(p & t) / max(1, len(t))
    return {"precision": precision, "recall": recall}

def csat(avg_rating: float) -> float:
    """
    Score CSAT [0..5] moyenné (ex: enquête utilisateur).
    """
    return max(0.0, min(5.0, avg_rating))
