import pandas as pd

# Load dataset
df = pd.read_csv("dataset/phishing_email.csv")

print("=" * 50)
print("AI PHISHING EMAIL ANALYSER LAB - DATASET OVERVIEW")
print("=" * 50)

# Show first five rows
print("\nFirst Five Emails")
print(df.head())

# Dataset size
print("\nRows and Columns")
print(df.shape)

# Column names
print("\nDataset Columns")
print(df.columns)

# Dataset information
print("\nDataset Information")
print(df.info())

# Statistical summary
print("\nStatistics")
print(df.describe())

# Count labels
print("\nLabel Counts")
print(df["label"].value_counts())