import pandas as pd
from preprocessing import clean_email

# Load sample dataset
df = pd.read_csv("dataset/sample_emails.csv")

# Clean every email
df["cleaned_email"] = df["email"].apply(clean_email)

print("=" * 55)
print("CLEANED EMAIL DATASET")
print("=" * 55)

print(df[["email", "cleaned_email", "label"]])