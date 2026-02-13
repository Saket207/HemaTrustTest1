import pandas as pd

# Load dataset
df = pd.read_csv('data/BDCBC7196_Hematology_Dataset.csv')

# Rename columns to consistent format
df = df.rename(columns={
    'PLATELETS': 'Platelets'
})

# Keep only required columns
required_columns = ['Hb', 'RBC', 'WBC', 'Platelets', 'MCV', 'MCH', 'RDW']
df = df[required_columns]

# Drop missing values
df = df.dropna()

print("Cleaned Data Shape:", df.shape)
print(df.head())

# Save cleaned dataset
df.to_csv('data/cleaned_data.csv', index=False)

print("✅ Cleaned data saved successfully!")
