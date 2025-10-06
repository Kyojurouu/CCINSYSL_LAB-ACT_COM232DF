import pandas as pd
import spacy

print("Loading dataset and SpaCy model...")
df = pd.read_csv("anomalies_detected_evidence.csv")
nlp = spacy.load("en_core_web_sm")
print(f"Dataset loaded with {len(df)} rows.")

entities = []
print("Extracting entities...")
for idx, text in df["message"].dropna().items():
    for ent in nlp(text).ents:
        entities.append([idx, text, ent.text, ent.label_])
print(f"Extraction complete. Found {len(entities)} entities.")

output_file = "extracted_entities.csv"
pd.DataFrame(entities, columns=["message_id", "message", "entity", "label"]).to_csv(output_file, index=False)
print(f"Entities saved to {output_file}")
