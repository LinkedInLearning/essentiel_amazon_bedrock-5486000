# Squelette d'agent : invoque une Lambda météo et compose une réponse.
# Complétez les TODO pour brancher bedrock (outil calling) si besoin.
# ---------------------------------------------------------------------------

import boto3, os, json

REGION = os.environ.get("AWS_REGION", "us-east-1")
LAMBDA_ARN = os.environ.get("WEATHER_LAMBDA_ARN", "arn:aws:lambda:us-east-1:888577055734:function:test")
lam = boto3.client("lambda", region_name=REGION)

def call_weather(city: str) -> dict:
    resp = lam.invoke(
        FunctionName=LAMBDA_ARN,
        InvocationType="RequestResponse",
        Payload=json.dumps({"city": city}).encode("utf-8")
    )
    payload = json.loads(resp["Payload"].read())
    # Si Lambda retourne via proxy (statusCode/body)
    if isinstance(payload, dict) and "body" in payload:
        return json.loads(payload["body"])
    return payload

def agent_answer(question: str) -> str:
    # Heuristique : si 'météo' dans la question -> appeler l'outil Lambda
    if "météo" in question.lower() or "meteo" in question.lower():
        data = call_weather("Paris")
        return f"A {data['city']}, il fait {data['temperatureC']}°C avec '{data['conditions']}'."
    return "Je peux appeler l'outil météo si vous me demandez la météo d'une ville."

if __name__ == "__main__":
    print(agent_answer("Quelle est la météo ?"))
