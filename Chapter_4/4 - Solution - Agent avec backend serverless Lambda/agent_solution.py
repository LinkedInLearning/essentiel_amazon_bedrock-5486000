# Implémentation simple d'agent outillé avec validation et réponse finale.
# ---------------------------------------------------------------------------

import boto3, os, json
from pydantic import BaseModel, Field, ValidationError

REGION = os.environ.get("AWS_REGION", "us-east-1")
LAMBDA_ARN = os.environ.get("WEATHER_LAMBDA_ARN", "arn:aws:lambda:REGION:ACCOUNT:function:weather-fn")
lam = boto3.client("lambda", region_name=REGION)

class WeatherOut(BaseModel):
    city: str = Field(...)
    temperatureC: float = Field(...)
    conditions: str = Field(...)

def call_weather(city: str) -> WeatherOut:
    resp = lam.invoke(
        FunctionName=LAMBDA_ARN,
        InvocationType="RequestResponse",
        Payload=json.dumps({"city": city}).encode("utf-8")
    )
    payload = json.loads(resp["Payload"].read())
    if isinstance(payload, dict) and "body" in payload:
        payload = json.loads(payload["body"])
    return WeatherOut(**payload)

def infer_city(text: str) -> str:
    # Heuristique simple : détecte une ville connue; à remplacer par NER/LLM.
    for c in ["Paris", "Lyon", "Marseille"]:
        if c.lower() in text.lower():
            return c
    return "Paris"

def answer(question: str) -> str:
    if "météo" in question.lower() or "meteo" in question.lower():
        city = infer_city(question)
        try:
            data = call_weather(city)
        except ValidationError as e:
            return f"Erreur de validation des données météo: {e}"
        return f"Météo de {data.city} : {data.temperatureC}°C, {data.conditions}."
    return "Posez une question météo (ex: 'Météo à Lyon aujourd'hui ?')."

if __name__ == "__main__":
    print(answer("Donne la météo à Lyon."))
