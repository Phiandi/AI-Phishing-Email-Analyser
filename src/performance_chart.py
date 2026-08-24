import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)
from sklearn.model_selection import train_test_split

from preprocessing import clean_email

# Load dataset
df = pd.read_csv("dataset/sample_emails.csv")

# Clean emails
df["cleaned_email"] = df["email"].apply(
    lambda text: " ".join(clean_email(text))
)

X = df["cleaned_email"]
y = df["label"]

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.4,
    random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation metrics
metrics = {
    "Accuracy": accuracy_score(y_test, y_pred),
    "Precision": precision_score(y_test, y_pred, zero_division=0),
    "Recall": recall_score(y_test, y_pred, zero_division=0),
    "F1-Score": f1_score(y_test, y_pred, zero_division=0)
}

# Create chart
plt.figure(figsize=(6,4))
plt.bar(metrics.keys(), metrics.values())

plt.ylim(0,1)
plt.title("AI Phishing Model Performance")
plt.ylabel("Score")

# Add values on top of bars
for i, value in enumerate(metrics.values()):
    plt.text(i, value + 0.02, f"{value:.2f}", ha="center")

plt.tight_layout()

# Save chart
plt.savefig("results/model_performance.png", dpi=300)

print("="*55)
print("MODEL PERFORMANCE CHART CREATED")
print("="*55)
print("Saved as: results/model_performance.png")

plt.show()