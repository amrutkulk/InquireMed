from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Load query embedding model
MODEL_NAME = "all-MiniLM-L6-v2"
embedding_fn = SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)

# Connect to ChromaDB
client = chromadb.PersistentClient(path="db/chroma")

def search_collection(query: str, source: str = "fda", top_k: int = 5):
    # Validate source
    if source not in ["fda", "pubmed"]:
        raise ValueError("Source must be 'fda' or 'pubmed'")

    # Load collection
    collection = client.get_collection(name=source, embedding_function=embedding_fn)

    # Search
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    # Format output
    matches = []
    for doc, meta, score in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
        matches.append({
            "source": meta["source"],
            "score": round(score, 4),
            "text": doc
        })

    return matches

# Test via CLI
if __name__ == "__main__":
    print("🔍 Inquirmed Search CLI")
    source = input("Choose source (fda/pubmed): ").strip().lower()
    query = input("Enter your query: ").strip()

    results = search_collection(query, source)
    print("\nTop results:")
    for idx, match in enumerate(results, 1):
        print(f"\nResult {idx}:")
        print(f"Score: {match['score']}")
        print(f"Text: {match['text']}")
