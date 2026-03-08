import fitz # PyMuPDF reader tool for PDF files
import ollama
import chromadb

#opening PDF and extracting text
pdf_path = "../data/papers/sample_paper.pdf"
doc = fitz.open(pdf_path)
text = ""

#removes references section from the text to avoid including it in the chunks
references_index = text.find("References")
if references_index != -1:
    text = text[:references_index]

#simple chunking
chunk_size = 800
overlap = 150

chunks = []
start = 0

while start < len(text):
    end = start + chunk_size
    chunk = text[start:end]
    chunks.append(chunk)
    start += chunk_size - overlap

print(f"Created {len(chunks)} chunks")

#create chroma database
client = chromadb.PersistentClient(path="../db")
collection = client.get_or_create_collection("papers")

# create embeddings and store them
for i, chunk in enumerate(chunks):

    # generate embedding for the chunk using Ollama "embeddinggemma" model
    embedding = ollama.embeddings(
        model="embeddinggemma",
        prompt=chunk,
    )["embedding"]

    # add the embedding and chunk to the chroma collection
    collection.add(
        ids=[str(i)],
        embeddings=[embedding],
        documents=[chunk]
    )
print(f"{len(chunks)} Chunks stored as {collection.count()} vectors in database.")

