import pandas as pd
from sklearn.ensemble import IsolationForest
 
df = pd.read_csv("feature_engineered_evidence.csv")
 
model = IsolationForest(random_state=42)
df["is_anomaly"] = model.fit_predict(df.select_dtypes(include=["number"]))
 
df.to_csv("anomalies_detected_evidence.csv", index=False)