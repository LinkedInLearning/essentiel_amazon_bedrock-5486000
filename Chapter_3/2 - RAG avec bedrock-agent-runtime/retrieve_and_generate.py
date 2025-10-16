# Exemple d'appel RetrieveAndGenerate (placeholders à remplacer).
# Doc: service 'bedrock-agent-runtime' avec l'opération retrieve_and_generate
# ---------------------------------------------------------------------------

import boto3, os, json

REGION = os.environ.get("AWS_REGION", "us-east-1")
runtime = boto3.client("bedrock-agent-runtime", region_name=REGION)

def answer_with_rag(kb_id: str, query: str) -> dict:
    """
    Appelle RetrieveAndGenerate pour récupérer des passages + générer une réponse.
    """
    resp = runtime.retrieve_and_generate(
        input={
            "text": query
        },
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": kb_id,
                "modelArn": "arn:aws:bedrock:us-east-1:888577055734:inference-profile/us.deepseek.r1-v1:0",
                "retrievalConfiguration": {
                    "vectorSearchConfiguration": {
                        "numberOfResults": 4
                    }
                    # Optionnel: "rerankingConfiguration": {...}
                },
                "generationConfiguration": {
                    "promptTemplate": {
                        "textPromptTemplate": open("prompt_petite_strategie.md", "r", encoding="utf-8").read()
                    }
                }
            }
        }
    )
    return resp

if __name__ == "__main__":
    KB_ID = "EF9OINURXA"
    q = "Explique la différence entre retrieval et re‑ranking."
    out = answer_with_rag(KB_ID, q)
    print(json.dumps(out, indent=2, ensure_ascii=False))
