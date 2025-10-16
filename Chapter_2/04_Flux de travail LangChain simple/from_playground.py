from langchain_aws import BedrockEmbeddings

embeddings_model = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0", 
                                     region_name="us-east-1")

embeddings = embeddings_model.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ]
)
print("-- exemple avec un document ---")
print(embeddings)

print("-- exemple avec du text directement en entre ---")
embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")

print(embedded_query[:5])
print(len(embedded_query))