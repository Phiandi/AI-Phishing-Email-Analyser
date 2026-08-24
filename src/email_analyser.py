import joblib
from preprocessing import clean_email

print("=" * 60)
print("        AI PHISHING EMAIL ANALYSER")
print("=" * 60)

# Load saved model and TF-IDF vectorizer
model = joblib.load("models/text_phishing_detector.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# User enters email
email = input("\nPaste an email:\n\n")

# Preprocess email
cleaned_tokens = clean_email(email)
cleaned_email = " ".join(cleaned_tokens)

# Convert email into TF-IDF features
email_vector = vectorizer.transform([cleaned_email])

# Predict label and confidence
prediction = model.predict(email_vector)[0]
probabilities = model.predict_proba(email_vector)[0]
confidence = max(probabilities) * 100

# Risk level
if prediction == 1:
    if confidence >= 80:
        risk = "HIGH"
    elif confidence >= 60:
        risk = "MEDIUM"
    else:
        risk = "LOW"
else:
    risk = "LOW"

# Report
print("\n" + "=" * 60)
print("              AI SECURITY REPORT")
print("=" * 60)

print(f"Prediction        : {'PHISHING EMAIL' if prediction == 1 else 'LEGITIMATE EMAIL'}")
print(f"Confidence Score  : {confidence:.2f}%")
print(f"Risk Level        : {risk}")

print("\nSuspicious Keywords Found")
print("-" * 30)

keywords = ["urgent", "verify", "password", "account", "click", "bank", "login"]

found = [word for word in cleaned_tokens if word in keywords]

if found:
    print(", ".join(sorted(set(found))))
else:
    print("None detected.")

print("\nRecommendation")
print("-" * 30)

if prediction == 1:
    print("⚠️ Do NOT click links or provide passwords.")
    print("⚠️ Verify the sender before responding.")
else:
    print("✅ This email appears legitimate.")
    print("✅ Still verify unexpected requests before acting.")

print("=" * 60)