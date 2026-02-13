import pandas as pd

# Load time-series data
df = pd.read_csv('data/realistic_patient_data.csv')

# Convert date column properly
df['date'] = pd.to_datetime(df['date'])

# -----------------------------
# 1. Create Baseline (First 3 reports per patient)
# -----------------------------
baseline = (
    df.sort_values(by=['patient_id', 'date'])
      .groupby('patient_id')
      .head(3)
      .groupby('patient_id')
      .mean(numeric_only=True)
)

# Rename baseline columns
baseline = baseline.add_suffix('_baseline')

# Merge baseline back to main dataframe
df = df.merge(baseline, on='patient_id')

# -----------------------------
# 2. Calculate Delta %
# -----------------------------
parameters = ['Hb', 'RBC', 'WBC', 'Platelets', 'MCV', 'MCH', 'RDW']

for param in parameters:
    df[param + '_delta'] = (
        (df[param] - df[param + '_baseline']) 
        / df[param + '_baseline']
    ) * 100

print("Baseline and Delta calculated successfully!")
print(df.head())

# Save final dataset
df.to_csv('data/delta_data.csv', index=False)

print("✅ Saved as delta_data.csv")
