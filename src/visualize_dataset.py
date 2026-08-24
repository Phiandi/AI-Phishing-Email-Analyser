import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset/phishing_email.csv")

# Count labels
counts = df["label"].value_counts()

# Rename labels for readability
counts.index = ["Legitimate", "Phishing"]

# Plot chart
plt.figure(figsize=(6,5))
plt.bar(counts.index, counts.values)

plt.title("Distribution of Legitimate vs Phishing Emails")
plt.xlabel("Email Type")
plt.ylabel("Number of Emails")

plt.tight_layout()
plt.show()