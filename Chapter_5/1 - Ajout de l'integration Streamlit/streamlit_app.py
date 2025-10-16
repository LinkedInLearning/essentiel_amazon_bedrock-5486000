import os, json, time
from dotenv import load_dotenv
import streamlit as st
import boto3

load_dotenv()
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", "anthropic.claude-3-5-sonnet-20240620-v1:0")
USE_MOCK = os.environ.get("USE_MOCK", "1") == "1"

bedrock_runtime = None
if not USE_MOCK:
    bedrock_runtime = boto3.client("bedrock-runtime", region_name=AWS_REGION)

def mock_converse(message: str) -> str:
    # Renvoie une réponse simulée, utile pour démo rapide.
    time.sleep(0.2)
    return f"(MOCK) Reçu: {message}. Réponse de démonstration."

def bedrock_converse(message: str) -> str:
    if bedrock_runtime is None:
        raise RuntimeError("bedrock-runtime non initialisé")
    payload = {
        "messages": [{"role": "user", "content": message}],
        "modelId": MODEL_ID,
        "inferenceConfig": {"maxTokens": 256, "temperature": 0.2}
    }
    resp = bedrock_runtime.invoke_model(modelId=MODEL_ID, body=json.dumps(payload))
    body = json.loads(resp.get("body", "{}"))
    return body.get("outputText") or body.get("content") or str(body)

def mock_embed(text: str):
    return [len(text) % 7, sum(ord(c) for c in text) % 13, 1.0]

def bedrock_embed(text: str):
    if bedrock_runtime is None:
        raise RuntimeError("bedrock-runtime non initialisé pour embeddings")
    payload = {"inputText": text, "modelId": "amazon.titan-embed-text-v2"}
    resp = bedrock_runtime.invoke_model(modelId=payload["modelId"], body=json.dumps(payload))
    body = json.loads(resp.get("body", "{}"))
    return body.get("embedding", [0.0, 0.0, 0.0])

st.set_page_config(page_title="Bedrock + Streamlit (démo)", page_icon="", layout="centered")
st.title(" Démo Bedrock + Streamlit — 5 min")
st.caption("Mode MOCK" if USE_MOCK else f"Connecté Bedrock · Région {AWS_REGION}")

with st.form("chat_form"):
    user_input = st.text_input("Ton message", "Bonjour, peux-tu résumer RAG ?")
    do_embed = st.checkbox("Générer des embeddings (optionnel)", value=False)
    ok = st.form_submit_button("Envoyer")

if ok and user_input.strip():
    with st.spinner("Génération en cours..."):
        if USE_MOCK:
            answer = mock_converse(user_input)
            emb = mock_embed(user_input) if do_embed else None
        else:
            answer = bedrock_converse(user_input)
            emb = bedrock_embed(user_input) if do_embed else None
    st.subheader("Réponse")
    st.write(answer)
    if emb is not None:
        st.subheader("Embeddings (aperçu)")
        st.write(emb[:3])
