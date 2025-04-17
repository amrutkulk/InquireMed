# scripts/preprocess_fda.py

import os
import json
import requests

def fetch_fda_drug_data(limit=25):
    print("🔄 Fetching drug data from openFDA API...")
    url = f"https://api.fda.gov/drug/label.json?limit={limit}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code} {response.text}")

    data = response.json()
    results = data.get("results", [])

    cleaned = []
    for i, drug in enumerate(results):
        cleaned.append({
            "id": drug.get("id"),
            "brand_name": drug.get("openfda", {}).get("brand_name", ["N/A"])[0],
            "substance_name": drug.get("openfda", {}).get("substance_name", ["N/A"])[0],
            "purpose": drug.get("purpose", ["N/A"])[0],
            "indications_and_usage": drug.get("indications_and_usage", ["N/A"])[0],
            "warnings": drug.get("warnings", ["N/A"])[0]
        })

    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/fda_drugs_sample.json", "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2)

    print("✅ Saved cleaned FDA drug sample to data/raw/fda_drugs_sample.json")

if __name__ == "__main__":
    fetch_fda_drug_data()
