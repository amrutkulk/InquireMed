import os
import pickle
from pathlib import Path
import chromadb

# Use new PersistentClient for Chroma v0.4+
client = chromadb.PersistentClient(path="db/chroma")

# File paths for embeddings
embedding_files = {
    "fda": "embeddings/fda_embeddings.pkl",
    "pubmed": "embeddings/pubmed_embeddings.pkl"
}

for collection_name, file_path in embedding_files.items():
    print(f"📦 Indexing {collection_name} embeddings from {file_path}")
    
    with open(file_path, "rb") as f:
        data = pickle.load(f)

    # Drop existing collection to avoid conflicts
    if collection_name in [c.name for c in client.list_collections()]:
        client.delete_collection(name=collection_name)

    collection = client.create_collection(name=collection_name)

    for doc in data:
        # ✅ Ensure embedding is a plain list, not a NumPy array
        collection.add(
            ids=[doc["id"]],
            embeddings=[doc["embedding"].tolist()],
            documents=[doc["text"]],
            metadatas=[{"source": collection_name}]
        )

print("✅ ChromaDB index built and stored in db/chroma/")
