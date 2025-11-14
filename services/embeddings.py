import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding
