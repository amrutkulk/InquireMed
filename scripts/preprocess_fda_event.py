import json
from pathlib import Path
from tqdm import tqdm

input_path = Path("data/raw/fda_sample.json")
output_path = Path("data/raw/fda_events_clean.json")

def preprocess_fda_data():
    with open(input_path, "r") as f:
        data = json.load(f)

    processed = []
    for idx, report in tqdm(enumerate(data.get("results", [])), desc="Processing FDA Reports"):
        patient = report.get("patient", {})
        age = patient.get("patientonsetage", "unknown age")
        sex = patient.get("patientsex", "unknown sex")
        sex = {"1": "male", "2": "female"}.get(sex, "unknown sex")

        drugs = [d.get("medicinalproduct", "").upper() for d in patient.get("drug", []) if d.get("medicinalproduct")]
        drug_indications = [d.get("drugindication", "") for d in patient.get("drug", []) if d.get("drugindication")]
        reactions = [r.get("reactionmeddrapt", "") for r in patient.get("reaction", []) if r.get("reactionmeddrapt")]

        combined_text = f"A {age}-year-old {sex} taking {', '.join(drugs)}"
        if drug_indications:
            combined_text += f" for {', '.join(drug_indications)}"
        if reactions:
            combined_text += f" experienced {', '.join(reactions)}."
        else:
            combined_text += " experienced an unspecified reaction."

        processed.append({
            "id": f"fda_{idx}",
            "age": age,
            "sex": sex,
            "drugs": drugs,
            "indications": drug_indications,
            "reactions": reactions,
            "combined_text": combined_text
        })

    with open(output_path, "w") as f:
        json.dump(processed, f, indent=2)

    print(f"✅ Saved cleaned FDA events to {output_path}")

if __name__ == "__main__":
    preprocess_fda_data()
