import joblib
import pandas as pd

print("=" * 45)
print(" AI PHISHING EMAIL ANALYSER REPORT ")
print("=" * 45)

# Load saved model
model = joblib.load("models/phishing_detector.pkl")

# Example email features
sample_email = pd.DataFrame([
    {
        "num_words": 120,
        "num_unique_words": 60,
        "num_stopwords": 25,
        "num_links": 10,
        "num_unique_domains": 3,
        "num_email_addresses": 1,
        "num_spelling_errors": 15,
        "num_urgent_keywords": 20,
    }
])
  
# Predict phishing or legitimate
prediction = model.predict(sample_email)[0]

# Predict confidence
probability = model.predict_proba(sample_email)[0]
confidence = max(probability) * 100

# Risk level
if prediction == 1:
    if confidence >= 90:
        risk = "HIGH"
    elif confidence >= 70:
        risk = "MEDIUM"
    else:
        risk = "LOW-MEDIUM"
else:
    if confidence >= 90:
        risk = "LOW"
    elif confidence >= 70:
        risk = "LOW-MEDIUM"
    else:
        risk = "UNCERTAIN"

# Print report
print(f"\nPrediction       : {'LEGITIMATE EMAIL' if prediction == 0 else 'PHISHING EMAIL'}")
print(f"Confidence Score : {confidence:.2f}%")
print(f"Risk Level       : {risk}")

print("\nEmail Features Analysed")
print("-" * 25)
print(f"Words            : {sample_email['num_words'][0]}")
print(f"Links            : {sample_email['num_links'][0]}")
print(f"Urgent Keywords  : {sample_email['num_urgent_keywords'][0]}")
print(f"Spelling Errors  : {sample_email['num_spelling_errors'][0]}")

print("\nRecommendation:")

if prediction == 1:
    print("⚠️ Do NOT click links or provide passwords.")
else:
    print("✅ Safe to read, but always verify the sender before clicking links.")