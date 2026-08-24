import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("dataset/sample_emails.csv")

# TF-IDF expects text, not lists
emails = df["email"].str.lower()

# Create vectorizer
vectorizer = TfidfVectorizer(stop_words="english")

# Convert emails into numerical vectors
X = vectorizer.fit_transform(emails)

print("=" * 55)
print("TF-IDF EMAIL FEATURES")
print("=" * 55)

print("Matrix Shape:", X.shape)

feature_names = vectorizer.get_feature_names_out()

print("\nFirst 15 Features:")
print(feature_names[:15])

print("\nFirst Email Vector (first 15 values):")
print(X.toarray()[0][:15])