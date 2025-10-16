# Identique au script principal, mais ajoutez une grille d'évaluation qualitative
# (clarté, concision, pertinence) et imprimez un score simple.
import boto3

MODEL_ID = "anthropic.claude-3-haiku-20240307"

def score(answer:str)->int:
    # score naïf (placeholder) : +1 par critère trouvé
    s = 0
    for kw in ["clair", "concis", "pertinent"]:
        if kw in answer.lower():
            s += 1
    return s

def ask(prompt, temperature=0.5):
    br = boto3.client("bedrock-runtime", region_name="us-east-1")
    r = br.converse(
        modelId=MODEL_ID,
        messages=[{"role":"user","content":[{"text":prompt}]}],
        inferenceConfig={"maxTokens":128, "temperature":temperature},
    )
    txt = r["output"]["message"]["content"][0]["text"]
    return txt, score(txt)

if __name__ == "__main__":
    prompts = [
        "Explique l'IA générative en 2 phrases.",
        "Explique l'IA générative à un lycéen, en 2 phrases, avec un exemple.",
        "Explique l'IA générative à un décideur, en 2 phrases, avec un KPI."
    ]
    for p in prompts:
        for t in [0.0, 0.7, 1.0]:
            txt, sc = ask(p, temperature=t)
            print(f"\n--- Prompt: {p} | temperature: {t} | score: {sc}")
            print(txt)
