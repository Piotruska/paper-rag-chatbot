import chromadb
import ollama

from src.retrieve import query_embedding

client = chromadb.PersistentClient(path="../db")
collection = client.get_collection("papers")

query = "What are the main contributions of the paper?"

query_embedding = ollama.embeddings(
    model="embeddinggemma",
    prompt=query,
)["embedding"]

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

retrieved_chunks = results["documents"][0]
context = "\n\n".join(retrieved_chunks)

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{query}
"""

response = ollama.chat(
    model="mistral",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("Answer:\n")
print(response["message"]["content"])