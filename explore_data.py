import pandas as pd

df = pd.read_excel("grounds_data.xlsx")

print("📊 Columns in the dataset:")
print(df.columns)

print("\n🔍 First few rows:")
print(df.head())
