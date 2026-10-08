import pandas as pd

df = pd.read_csv("data/emails.csv")

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nNull values:", df.isnull().sum().sum())
print("\nSpam vs Ham count:")
print(df["Prediction"].value_counts())