import pandas as pd
import numpy as np
import datetime
import random

# Load cleaned data
df = pd.read_csv('data/cleaned_data.csv')

# -----------------------------
# 1. Create synthetic patient IDs
# -----------------------------
num_patients = 1000  # you can adjust

df['patient_id'] = np.random.randint(1, num_patients+1, size=len(df))

# -----------------------------
# 2. Create synthetic dates
# -----------------------------
def random_date():
    start = datetime.datetime(2023, 1, 1)
    end = datetime.datetime(2024, 1, 1)
    return start + datetime.timedelta(days=random.randint(0, 365))

df['date'] = [random_date() for _ in range(len(df))]

# -----------------------------
# 3. Sort by patient and date
# -----------------------------
df = df.sort_values(by=['patient_id', 'date'])

print("Time-series dataset created!")
print(df.head())

# Save new dataset
df.to_csv('data/time_series_data.csv', index=False)

print("✅ Saved as time_series_data.csv")
