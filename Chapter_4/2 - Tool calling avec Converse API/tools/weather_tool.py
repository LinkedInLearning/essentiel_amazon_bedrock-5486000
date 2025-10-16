# Outil météo simulé (remplacez par l'appel réel d'une API ou Lambda).
# ---------------------------------------------------------------------------

def get_weather(city: str) -> dict:
    """
    Retourne une météo simulée.
    """
    return {
        "city": city,
        "temperatureC": 22.5,
        "conditions": "Partly cloudy"
    }
