# scripts/preprocess_pubmed.py

import os
import json
import tempfile
from datasets import load_dataset

# Redirect all HF paths and temp dir
os.environ["HF_DATASETS_CACHE"] = "D:/Projects/Inquiremed Data/HF_CACHE"
os.environ["HF_HOME"] = "D:/Projects/Inquiremed Data/HF_HOME"
tempfile.tempdir = "D:/Projects/Inquiremed Data/HF_TEMP"

def preprocess_pubmed_sample():
    print("🔄 Loading ccdv/pubmed-summarization dataset...")

    dataset = load_dataset("ccdv/pubmed-summarization", split="train[:100]")

    cleaned_data = []
    for i, record in enumerate(dataset):
        cleaned_data.append({
            "id": i,
            "title": record["article"][:200],  # Truncate for brevity
            "abstract": record["abstract"]
        })

    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/pubmed_sample.json", "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=2)

    print("✅ Saved cleaned sample to data/raw/pubmed_sample.json")

if __name__ == "__main__":
    preprocess_pubmed_sample()
