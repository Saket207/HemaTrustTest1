import pandas as pd

df = pd.read_csv('data/BDCBC7196_Hematology_Dataset.csv')


print("First 5 rows:")
print(df.head())

print("Columns:")
print(df.columns)

print("Shape:", df.shape)
