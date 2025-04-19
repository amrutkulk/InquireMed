import json
import pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

input_path = Path("data/raw/fda_events_clean.json")
output_path = Path("embeddings/fda_embeddings.pkl")  # updated path

# Optional: load from .env or default
model_name = "all-MiniLM-L6-v2"

def embed_fda_data():
    print(f"🔍 Loading embedding model: {model_name}")
    model = SentenceTransformer(model_name)

    with open(input_path, "r") as f:
        data = json.load(f)

    texts = [item["combined_text"] for item in data]
    ids = [item["id"] for item in data]

    print("🧠 Generating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True, batch_size=32)

    result = [{"id": ids[i], "embedding": embeddings[i], "text": texts[i]} for i in range(len(ids))]

    # ✅ Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        pickle.dump(result, f)

    print(f"✅ Saved FDA embeddings to {output_path}")

if __name__ == "__main__":
    embed_fda_data()
