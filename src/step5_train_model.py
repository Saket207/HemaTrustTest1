import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# Load delta dataset
df = pd.read_csv('data/delta_data.csv')

# Use ONLY delta features
delta_features = [
    'Hb_delta',
    'RBC_delta',
    'WBC_delta',
    'Platelets_delta',
    'MCV_delta',
    'MCH_delta',
    'RDW_delta'
]

X = df[delta_features]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = IsolationForest(
    n_estimators=300,
    contamination=0.02,
    random_state=42
)

model.fit(X_scaled)

# Save model
joblib.dump(model, 'models/isolation_forest.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

df['anomaly_label'] = model.predict(X_scaled)
df.to_csv('data/final_with_scores.csv', index=False)

print("✅ Model trained on delta-only features")
print("Anomalies detected:", (df['anomaly_label'] == -1).sum())
