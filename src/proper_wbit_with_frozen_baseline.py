import pandas as pd
import numpy as np

# Load original realistic data
df = pd.read_csv('data/realistic_patient_data.csv')

# Load frozen baseline
baseline = pd.read_csv('data/frozen_baseline.csv')

df_wbit = df.copy()

# 5% swap
swap_fraction = 0.05
num_swaps = int(len(df_wbit) * swap_fraction)

swap_indices = np.random.choice(df_wbit.index, size=num_swaps, replace=False)

# Swap CBC values ONLY (baseline stays same)
for idx in swap_indices:
    random_row = df.sample(1)
    for col in ['Hb','RBC','WBC','Platelets','MCV','MCH','RDW']:
        df_wbit.loc[idx, col] = random_row.iloc[0][col]

df_wbit['is_wbit'] = 0
df_wbit.loc[swap_indices, 'is_wbit'] = 1

# Merge frozen baseline
df_wbit = df_wbit.merge(baseline, on='patient_id')

# Recalculate delta using frozen baseline
parameters = ['Hb','RBC','WBC','Platelets','MCV','MCH','RDW']

for param in parameters:
    df_wbit[param + '_delta'] = (
        (df_wbit[param] - df_wbit[param + '_baseline'])
        / df_wbit[param + '_baseline']
    ) * 100

df_wbit.to_csv('data/wbit_frozen_test.csv', index=False)

print("✅ WBIT simulated with frozen baseline!")
print("Total WBIT cases:", num_swaps)
