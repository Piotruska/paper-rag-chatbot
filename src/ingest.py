import fitz # PyMuPDF reader tool for PDF files

pdf_path = "../data/papers/sample_paper.pdf"
doc = fitz.open(pdf_path)
text = ""

for page in doc:
    text += page.get_text()

print(text[:1000])

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

print(f"Total text length: {len(text)}")
print(f"Number of chunks: {len(chunks)}")

print("\nFirst chunk preview:\n")
print(chunks[0])

print("\nSecond chunk preview:\n")
print(chunks[1])
