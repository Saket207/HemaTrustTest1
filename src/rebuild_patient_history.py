import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv('data/cleaned_data.csv')

num_patients = 1000
reports_per_patient = 5

patients = []

for i in range(num_patients):
    # Pick one base row
    base = df.sample(1).iloc[0]
    
    for r in range(reports_per_patient):
        new_row = base.copy()
        
        # Add realistic biological noise (±5%)
        for col in ['Hb','RBC','WBC','Platelets','MCV','MCH','RDW']:
            variation = np.random.normal(0, 0.05)  # 5% variation
            new_row[col] = new_row[col] * (1 + variation)
        
        new_row['patient_id'] = i
        new_row['date'] = pd.Timestamp('2023-01-01') + pd.Timedelta(days=r*30)
        
        patients.append(new_row)

df_new = pd.DataFrame(patients)

df_new.to_csv('data/realistic_patient_data.csv', index=False)

print("✅ Realistic patient history created with ±5% variation!")
print("Total rows:", len(df_new))
