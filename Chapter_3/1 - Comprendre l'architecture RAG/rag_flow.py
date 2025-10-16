# pipeline RAG minimaliste (mock).
# Ce fichier n'appelle pas de service externe : il illustre les étapes.
# Chaque étape est commentée pour expliquer son rôle dans une application RAG.
# ---------------------------------------------------------------------------

from typing import List, Dict

# --- Etape 1 : Index "factice" ------------------------------------------------
# On simule un index/KB sous forme de liste de documents.
# Dans une vraie app, ceci serait un vector store (ex: Amazon S3 Vectors, OpenSearch, pgvector, etc.).
INDEX = [
    {"id": "doc-1", "text": "AWS Bedrock propose des modèles de fondation et des agents."},
    {"id": "doc-2", "text": "RAG combine retrieval et generation pour des réponses ancrées."},
    {"id": "doc-3", "text": "Les embeddings permettent de retrouver des passages pertinents."},
]

def embed(text: str) -> List[float]:
    # Fonction d'embedding factice : retourne un petit vecteur arbitraire.
    # Dans la vraie vie : appeler un modèle d'embeddings (Titan, Cohere, etc.).
    # NB: La fonction ord() en Python est une fonction intégrée qui prend un seul 
    # caractère Unicode comme argument de chaîne et renvoie sa valeur de point de code Unicode entière
    return [len(text) % 7, sum(ord(c) for c in text) % 11, 1.0]

def cosine_sim(a: List[float], b: List[float]) -> float:
    # Similarité cosinus (implémentation minimaliste): La similitude cosinus est une mesure qui 
    # quantifie la similarité entre deux vecteurs non nuls, en utilisant le cosinus de l'angle entre eux
    import math
    dot = sum(x*y for x, y in zip(a, b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(y*y for y in b))
    return dot / (na*nb + 1e-9)

def retrieve(query: str, k: int = 2) -> List[Dict]:
    # Récupère les k documents les plus proches de la requête (mock).
    qv = embed(query)
    scored = []
    for d in INDEX:
        scored.append((cosine_sim(qv, embed(d["text"])), d))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:k]]

def rerank(query: str, passages: List[Dict]) -> List[Dict]:
    # Reclassement simple (ici, identique à retrieve pour l'exemple)
    # En prod : on utiliserait un modèle de re-ranking spécialisé.
    return passages

def generate(query: str, contexts: List[Dict]) -> Dict:
    # Génération factice : concatène des extraits "pertinents" avec une réponse courte.
    # En prod : on appellerait un LLM (via Bedrock Runtime par ex.).
    citations = [c["id"] for c in contexts]
    body = "Voici une réponse basée sur les documents : " + "; ".join(c["text"] for c in contexts)
    return {"answer": body, "citations": citations}

def rag_answer(query: str) -> Dict:
    # Chaîne complète : retrieval -> rerank -> generate (+ citations).
    passages = retrieve(query, k=2)
    reranked = rerank(query, passages)
    out = generate(query, reranked)
    return out

if __name__ == "__main__":
    q = "Comment fonctionne RAG sur AWS?"
    result = rag_answer(q)
    print("Q:", q)
    print("Réponse:", result["answer"])
    print("Citations:", result["citations"])
