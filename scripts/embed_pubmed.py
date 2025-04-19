import json
import pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

input_path = Path("data/raw/pubmed_sample.json")
output_path = Path("embeddings/pubmed_embeddings.pkl")

# Optional: load from .env
model_name = "all-MiniLM-L6-v2"

def embed_pubmed_data():
    print(f"🔍 Loading embedding model: {model_name}")
    model = SentenceTransformer(model_name)

    with open(input_path, "r") as f:
        data = json.load(f)

    texts = []
    ids = []

    print("📚 Processing PubMed entries...")
    for item in tqdm(data):
        title = item.get("title", "")
        abstract = item.get("abstract", "")
        full_text = f"{title}. {abstract}".strip()
        if full_text:
            texts.append(full_text)
            ids.append(f"pubmed_{item.get('id', len(ids))}")

    print("🧠 Generating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True, batch_size=32)

    result = [{"id": ids[i], "embedding": embeddings[i], "text": texts[i]} for i in range(len(ids))]

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        pickle.dump(result, f)

    print(f"✅ Saved PubMed embeddings to {output_path}")

if __name__ == "__main__":
    embed_pubmed_data()
