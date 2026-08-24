from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

# Load resources once
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# Reusable preprocessing function
def clean_email(text):
    # Convert to lowercase
    text = text.lower()

    # Tokenize
    tokens = word_tokenize(text)

    # Remove punctuation
    tokens = [word for word in tokens if word not in string.punctuation]

    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens


# Sample email
email = """
Subject: Urgent Account Verification

Dear Customer,

Your account has been suspended. Click here immediately to verify your password.
"""

processed_email = clean_email(email)

print("=" * 45)
print("REUSABLE PREPROCESSING FUNCTION")
print("=" * 45)
print(processed_email)