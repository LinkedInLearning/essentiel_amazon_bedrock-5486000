import boto3

MODEL_ID = "global.anthropic.claude-sonnet-4-20250514-v1:0"

SYSTEM = "Tu es un traducteur professionnel. Préserve le sens, le ton et les acronymes (AWS, IAM, VPC)."

def translate(text, target_lang="fr"):
    br = boto3.client("bedrock-runtime", region_name="us-east-1")
    msg = [
        {"role": "user", "content": [{"text": f"{SYSTEM}\n\nTraduire en {target_lang}: {text}"}]}
    ]
    r = br.converse(modelId=MODEL_ID, messages=msg,
                    inferenceConfig={"maxTokens":256,"temperature":0.2})
    return r["output"]["message"]["content"][0]["text"]

if __name__ == "__main__":
    print(translate("Cloud is changing software delivery.", "fr"))
