import chromadb
from chromadb.utils import embedding_functions
from config import CHROMA_COLLECTION, CHROMA_PATH, EMBEDDING_MODEL, N_RESULTS
from chunking import load_documents, clean_text, chunk_document
_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=EMBEDDING_MODEL
)
_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_or_create_collection(
    name=CHROMA_COLLECTION,
    embedding_function=_ef,
    metadata={"hnsw:space": "cosine"},
)


def get_collection():
    
    return _collection


def embed_and_store(chunks):
   
    _collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"]} for c in chunks],
        ids=[c["chunk_id"] for c in chunks],
    )
    print(f"Stored {_collection.count()} total chunks in the vector database.")


def retrieve(query, n_results=N_RESULTS):
   
    if _collection.count() == 0:
        return []

    # Your implementation here.
    results = _collection.query(
        query_texts=[query],
        n_results=N_RESULTS,
        include=["documents", "metadatas", "distances"]
    )
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    chunks = []

    for i in range(len(documents)):
        chunks.append({
            "text": documents[i],
            "source": metadatas[i]["source"],
            "distance": distances[i]
        })

    
    for chunk in chunks:
        print(f"[{chunk['source']}] (dist: {chunk['distance']:.3f}) {chunk['text'][:80]}...")
    return chunks

if __name__ == "__main__":
    documents = load_documents()

    all_chunks = []

    for doc in documents:
        cleaned_text = clean_text(doc["text"])
        chunks = chunk_document(cleaned_text, doc["source"])
        all_chunks.extend(chunks)

    embed_and_store(all_chunks)

    print("Running retrieval test...")

    retrieve("Grades for 3354? median GPA mean GPA")