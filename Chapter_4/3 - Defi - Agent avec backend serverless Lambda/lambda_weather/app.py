# Lambda météo minimaliste (handler pour API Gateway/Lambda Function URL).
# TODO: remplacer la source météo par un vrai appel API.
# ---------------------------------------------------------------------------

import json

def handler(event, context):
    # event peut contenir {"city": "Paris"} si invoqué direct,
    # ou le body JSON si via HTTP.
    if "body" in event and isinstance(event["body"], str):
        try:
            payload = json.loads(event["body"])
        except Exception:
            payload = {}
    else:
        payload = event if isinstance(event, dict) else {}
    city = payload.get("city", "Paris")
    result = {"city": city, "temperatureC": 21.0, "conditions": "Sunny intervals"}
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(result)
    }

if __name__ == '__main__':
   test =  handler(event={}, context=[])
   print(test)