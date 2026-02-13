import pandas as pd

# Load realistic patient history (±5% variation)
df = pd.read_csv('data/realistic_patient_data.csv')

df['date'] = pd.to_datetime(df['date'])

# Compute baseline from FIRST 3 reports per patient
baseline = (
    df.sort_values(by=['patient_id','date'])
      .groupby('patient_id')
      .head(3)
      .groupby('patient_id')
      .mean(numeric_only=True)
)

baseline = baseline.add_suffix('_baseline')

# Save baseline separately (frozen reference)
baseline.to_csv('data/frozen_baseline.csv')

print("✅ Baseline frozen successfully!")
