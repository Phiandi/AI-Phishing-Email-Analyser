import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
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
    X, y,
    test_size=0.4,
    random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Plot
fig, ax = plt.subplots(figsize=(5,5))
ax.imshow(cm)

# Labels
classes = ["Legitimate", "Phishing"]
ax.set_xticks([0,1])
ax.set_xticklabels(classes)
ax.set_yticks([0,1])
ax.set_yticklabels(classes)

ax.set_xlabel("Predicted Label")
ax.set_ylabel("Actual Label")
ax.set_title("Confusion Matrix")

# Add numbers inside boxes
for i in range(2):
    for j in range(2):
        ax.text(j, i, str(cm[i, j]),
                ha="center",
                va="center",
                fontsize=14)

plt.tight_layout()

# Save image
plt.savefig("results/confusion_matrix.png", dpi=300)

print("="*55)
print("CONFUSION MATRIX CREATED SUCCESSFULLY")
print("="*55)
print("Saved as: results/confusion_matrix.png")

plt.show()