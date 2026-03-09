import chromadb
import ollama

client = chromadb.PersistentClient(path="../db")
collection = client.get_collection("papers")

print("Paper chatbot ready. Type 'exit' to stop.\n")

while True:

    query = input("Ask a question about the paper: ")

    if query.lower() == "exit":
        print("Goodbye.")
        break

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
    print("\n" + "-" * 50 + "\n")