import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)
from sklearn.model_selection import train_test_split

from preprocessing import clean_email

# Load dataset
df = pd.read_csv("dataset/sample_emails.csv")

# Clean emails
df["cleaned_email"] = df["email"].apply(
    lambda text: " ".join(clean_email(text))
)

# Features and labels
X = df["cleaned_email"]
y = df["label"]

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("=" * 60)
print("MODEL EVALUATION REPORT")
print("=" * 60)

print(f"Accuracy  : {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision : {precision_score(y_test, y_pred, zero_division=0):.2f}")
print(f"Recall    : {recall_score(y_test, y_pred, zero_division=0):.2f}")
print(f"F1-Score  : {f1_score(y_test, y_pred, zero_division=0):.2f}")

print("\nClassification Report")
print("-" * 60)
print(classification_report(y_test, y_pred, zero_division=0))