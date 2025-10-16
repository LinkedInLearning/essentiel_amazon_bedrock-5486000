# langchain
from langchain_aws import ChatBedrock
from langchain_core.prompts import PromptTemplate

# common
from pprint import pprint



llm = ChatBedrock(
    model_id="us.deepseek.r1-v1:0", 
    region_name="us-east-1",
    streaming=False,
    model_kwargs={"temperature": 0.001, "max_tokens":100}
    )

prompt = PromptTemplate.from_template("Résume: {texte} en 3 puces.")

chain = prompt | llm

pprint(chain.invoke({"texte":"Explique l'IA générative à un lycéen, en 2 phrases, avec un exemple."}))
