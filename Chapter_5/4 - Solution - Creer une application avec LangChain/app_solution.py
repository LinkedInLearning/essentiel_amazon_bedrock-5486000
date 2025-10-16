
import os, time, requests, json
import streamlit as st
import boto3
from typing import Optional, Dict, Any
from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError

# ----- Chargement des variables d'environnement -----
load_dotenv()
USE_MOCK = os.environ.get("USE_MOCK", "1") == "0"

# ----- Outils -----
def tool_calculator(expr: str) -> str:
    try:
        return str(eval(expr, {"__builtins__": {}}, {}))
    except Exception as e:
        raise RuntimeError(f"Erreur calculatrice: {e}")

def tool_http_get(url: str) -> str:
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.text[:200]
    except Exception as e:
        raise RuntimeError(f"Erreur HTTP GET: {e}")

TOOLS = {"calculator": tool_calculator, "http_get": tool_http_get}

# ----- Mock de décision LLM -----
def mock_route(message: str) -> Dict[str, Any]:
    if "http" in message.lower():
        return {"type": "tool", "tool": "http_get", "args": {"url": "https://example.com"}}
    if any(op in message for op in ["+", "*", "/", "-"]):
        return {"type": "tool", "tool": "calculator", "args": {"expr": "(2+2)*3"}}
    return {"type": "text", "content": "(MOCK) Réponse directe"}

class Decision(BaseModel):
    type: str = Field(...)
    tool: Optional[str] = None
    args: Dict[str, Any] = Field(default_factory=dict)
    content: Optional[str] = None

# ----- Appel deepseek via Bedrock -----
def call_deepseek(prompt: str) -> str:
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
    
    body = {
        "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
        "max_tokens": 300,
        "temperature": 0.7,
        "top_p": 1,
        "stop": ["\n\nHuman:"]
    }

    response = bedrock.invoke_model(
        modelId="us.deepseek.r1-v1:0",  # adapte selon ton accès
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body)
    )

    result = json.loads(response['body'].read())
    print(result)
    return [output['text'] for output in result.get("choices", [])]

# ----- Chaîne de traitement -----
def run_chain(user_message: str, max_retries: int = 1) -> str:
    if USE_MOCK:
        raw = mock_route(user_message)
        try:
            decision = Decision(**raw)
        except ValidationError as e:
            return f"Sortie invalide: {e}"

        if decision.type == "text":
            return decision.content or ""

        if decision.type == "tool" and decision.tool:
            tool_fn = TOOLS.get(decision.tool)
            if not tool_fn:
                return f"Outil inconnu: {decision.tool}"
            last_err = None
            for _ in range(max_retries + 1):
                try:
                    res = tool_fn(**decision.args)
                    return f"{decision.tool} OK — Résultat: {res}"
                except Exception as e:
                    last_err = e
                    time.sleep(0.2)
            return f"Échec après retries — {last_err}"

        return "Type non géré"
    else:
        return call_deepseek(user_message)

# ----- Interface Streamlit -----
st.set_page_config(page_title="Assistant deepseek + Outils", layout="centered")
st.title(" Assistant Intelligent avec deepseek & Outils")

user_input = st.text_input(" Entrez votre message")

if user_input:
    with st.spinner(" Traitement en cours..."):
        result = run_chain(user_input)
    st.success(" Réponse :")
    remaining_words = len(result)-1
    for output in result:
        st.write(output)
        remaining_words-=1
        if remaining_words > 0:
            st.write("\n next possible answer: \n")
