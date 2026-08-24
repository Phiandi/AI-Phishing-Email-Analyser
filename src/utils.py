import joblib

MODEL_PATH = "models/text_phishing_detector.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"


def load_model():
    """Load the trained phishing detection model."""
    return joblib.load(MODEL_PATH)


def load_vectorizer():
    """Load the trained TF-IDF vectorizer."""
    return joblib.load(VECTORIZER_PATH)