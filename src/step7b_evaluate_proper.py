import pandas as pd
import joblib

# -----------------------------
# 1. Load trained model & scaler
# -----------------------------
model = joblib.load('models/isolation_forest.pkl')
scaler = joblib.load('models/scaler.pkl')

# -----------------------------
# 2. Load WBIT test dataset
# -----------------------------
df = pd.read_csv('data/wbit_proper_test.csv')

# -----------------------------
# 3. Use SAME features as training (delta-only)
# -----------------------------
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

# -----------------------------
# 4. Scale features
# -----------------------------
X_scaled = scaler.transform(X)

# -----------------------------
# 5. Predict anomalies
# -----------------------------
df['anomaly_label'] = model.predict(X_scaled)

# -----------------------------
# 6. Evaluate Performance
# -----------------------------

# True Positives (Correctly detected WBIT)
true_positive = df[(df['is_wbit'] == 1) & (df['anomaly_label'] == -1)].shape[0]
total_wbit = df[df['is_wbit'] == 1].shape[0]

detection_rate = (true_positive / total_wbit) * 100

# False Positives (Normal samples wrongly flagged)
false_positive = df[(df['is_wbit'] == 0) & (df['anomaly_label'] == -1)].shape[0]
total_normal = df[df['is_wbit'] == 0].shape[0]

false_positive_rate = (false_positive / total_normal) * 100

# -----------------------------
# 7. Print Results
# -----------------------------
print("\n========== MODEL EVALUATION ==========")
print("Total WBIT cases:", total_wbit)
print("Detected WBIT:", true_positive)
print("Detection Rate (Sensitivity): {:.2f}%".format(detection_rate))

print("\nTotal Normal cases:", total_normal)
print("False Positives:", false_positive)
print("False Positive Rate: {:.2f}%".format(false_positive_rate))
print("======================================\n")
