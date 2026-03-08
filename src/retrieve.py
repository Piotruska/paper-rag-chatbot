import chromadb
import ollama

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

print("Top matching chunks:\n")

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"--- Result {i} ---")
    print(doc)
    print("\n")