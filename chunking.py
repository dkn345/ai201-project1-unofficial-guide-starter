import os
import random
DOCS_PATH = "documents"

def load_documents():
    """Load all .txt documents from the documents folder."""
    documents = []

    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            documents.append({
                "source": filename,
                "text": text,
            })

    print(f"Loaded {len(documents)} document(s)")
    return documents


def clean_text(text):
    """Basic cleaning."""
    lines = []

    for line in text.splitlines():
        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)


def chunk_document(text, source):
    """
    Split a document into chunks.

    Chunk size: 250
    Overlap: 25
    """
    chunk_size = 250
    overlap = 25
    min_length = 50

    chunks = []

    prefix = source.replace(".txt", "")
    counter = 0

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk_text = text[start:end].strip()

        if len(chunk_text) >= min_length:
            chunks.append({
                "text": chunk_text,
                "source": source,
                "chunk_id": f"{prefix}_{counter}",
            })

            counter += 1

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    documents = load_documents()

    all_chunks = []

    for doc in documents:
        cleaned_text = clean_text(doc["text"])

        chunks = chunk_document(
            cleaned_text,
            doc["source"]
        )

        all_chunks.extend(chunks)

    print(f"\nTotal chunks: {len(all_chunks)}")

    print("\Random 5 chunks:\n")
    
    all_chunks = random.sample(all_chunks,5)
    for chunk in all_chunks[:5]:
        print("=" * 60)
        print("SOURCE:", chunk["source"])
        print("CHUNK ID:", chunk["chunk_id"])
        print(chunk["text"])
        print()

