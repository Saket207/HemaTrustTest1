import pandas as pd
import numpy as np

df = pd.read_csv('data/wbit_frozen_test.csv')

# Thresholds tuned for ±5% normal variation
MCV_THRESHOLD = 12
MCH_THRESHOLD = 12
RDW_THRESHOLD = 15
TOTAL_DELTA_THRESHOLD = 80

delta_cols = [
    'Hb_delta','RBC_delta','WBC_delta',
    'Platelets_delta','MCV_delta','MCH_delta','RDW_delta'
]

df['total_delta_magnitude'] = df[delta_cols].abs().sum(axis=1)

stable_violations = (
    (df['MCV_delta'].abs() > MCV_THRESHOLD).astype(int) +
    (df['MCH_delta'].abs() > MCH_THRESHOLD).astype(int) +
    (df['RDW_delta'].abs() > RDW_THRESHOLD).astype(int)
)

conditions = (
    (stable_violations >= 2) |
    (df['total_delta_magnitude'] > TOTAL_DELTA_THRESHOLD)
)

df['rule_anomaly'] = np.where(conditions, -1, 1)

# Evaluation
true_positive = df[(df['is_wbit'] == 1) & (df['rule_anomaly'] == -1)].shape[0]
total_wbit = df[df['is_wbit'] == 1].shape[0]

false_positive = df[(df['is_wbit'] == 0) & (df['rule_anomaly'] == -1)].shape[0]
total_normal = df[df['is_wbit'] == 0].shape[0]

detection_rate = (true_positive / total_wbit) * 100
false_positive_rate = (false_positive / total_normal) * 100

print("\n========== FINAL RULE-BASED MODEL ==========")
print("Detection Rate: {:.2f}%".format(detection_rate))
print("False Positive Rate: {:.2f}%".format(false_positive_rate))
print("============================================\n")
