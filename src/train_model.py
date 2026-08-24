import pandas as pd

# Load the phishing dataset
df = pd.read_csv("dataset/phishing_email.csv")

print("=" * 50)
print("AI PHISHING EMAIL ANALYSER")
print("=" * 50)

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Separate Features (X) and Label (y)
X = df.drop("label", axis=1)
y = df["label"]

print("\nFeatures Preview:")
print(X.head())

print("\nLabels Preview:")
print(y.head())

from sklearn.model_selection import train_test_split

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Set Shape")
print(X_train.shape)

print("\nTesting Set Shape")
print(X_test.shape)

from sklearn.linear_model import LogisticRegression

# Create model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, y_train)

print("\nModel Training Complete!")

# Predict on testing dataset
predictions = model.predict(X_test)

print("\nFirst 10 Predictions:")
print(predictions[:10])

print("\nFirst 10 Actual Labels:")
print(y_test.iloc[:10].values)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

import joblib

# Save trained model
joblib.dump(model, "models/phishing_detector.pkl")

print("\nModel Saved Successfully!")