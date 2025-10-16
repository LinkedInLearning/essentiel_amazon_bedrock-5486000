import boto3

MODEL_ID = "us.deepseek.r1-v1:0"

def ask(prompt, temperature=0.5):
    br = boto3.client("bedrock-runtime", region_name="us-east-1")
    r = br.converse(
        modelId=MODEL_ID,
        messages=[{"role": "user",
                   "content": [{"text": prompt}]}],
        inferenceConfig={"maxTokens": 128, "temperature": temperature},
    )
    return r["output"]["message"]["content"][0]

if __name__ == "__main__":
    prompts = [
        "Explique l'IA générative en 2 phrases.",
        "Explique l'IA générative à un lycéen, en 2 phrases, avec un exemple.",
        "Explique l'IA générative à un décideur, en 2 phrases, avec un KPI."
    ]
    for p in prompts:
        for t in [0.0, 0.7, 1.0]:
            print("\n--- Prompt:", p, "| temperature:", t)
            print("\n --- Next ---")
            print(ask(p, temperature=t))
