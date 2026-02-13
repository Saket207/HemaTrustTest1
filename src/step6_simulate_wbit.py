import pandas as pd
import numpy as np

# Load dataset with scores
df = pd.read_csv('data/final_with_scores.csv')

# -----------------------------
# 1. Create copy
# -----------------------------
df_wbit = df.copy()

# -----------------------------
# 2. Select 5% rows to swap
# -----------------------------
swap_fraction = 0.05
num_swaps = int(len(df_wbit) * swap_fraction)

swap_indices = np.random.choice(df_wbit.index, size=num_swaps, replace=False)

# Randomly assign them new patient IDs
df_wbit.loc[swap_indices, 'patient_id'] = np.random.randint(
    1, df_wbit['patient_id'].max()+1, size=num_swaps
)

# Mark them as WBIT
df_wbit['is_wbit'] = 0
df_wbit.loc[swap_indices, 'is_wbit'] = 1

df_wbit.to_csv('data/wbit_test_data.csv', index=False)

print("✅ WBIT simulated successfully!")
print("Total WBIT cases:", num_swaps)
