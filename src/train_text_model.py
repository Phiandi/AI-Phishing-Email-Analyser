import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from preprocessing import clean_email

# Load dataset
df = pd.read_csv("dataset/sample_emails.csv")

# Clean every email
df["cleaned_email"] = df["email"].apply(
    lambda text: " ".join(clean_email(text))
)

# Create TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["cleaned_email"])

# Labels
y = df["label"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, "models/text_phishing_detector.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print("=" * 55)
print("TEXT PHISHING MODEL TRAINED SUCCESSFULLY")
print("=" * 55)
print("Emails used for training:", len(df))
print("Vocabulary size:", len(vectorizer.get_feature_names_out()))
print("\nFiles saved:")
print("- models/text_phishing_detector.pkl")
print("- models/tfidf_vectorizer.pkl")