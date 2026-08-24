# AI Phishing Email Analyser

An AI powered phishing email detection project built with **Python, Natural Language Processing (NLP), and Machine Learning**. The application analyses email content, identifies phishing indicators, and predicts whether an email is **phishing** or **legitimate** while providing a confidence score and security recommendations.

---

## Project Overview

Phishing attacks remain one of the most common cybersecurity threats. This project demonstrates how Natural Language Processing and Machine Learning can be used to automatically analyse email text and detect suspicious messages.

The analyser performs text preprocessing, converts email text into numerical features using TF-IDF, and classifies emails using a Logistic Regression model.

---

## Features

- Email text preprocessing using NLP.
- Tokenization.
- Stopword removal.
- Lemmatization.
- TF-IDF vectorization.
- Logistic Regression phishing classifier.
- Confidence score generation.
- Risk level assessment.
- Suspicious keyword detection.
- Security recommendations.

---

## Technologies Used

- Python 3.14
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Matplotlib
- Joblib
- VS Code

---

## Project Structure

```text
AI-Phishing-Email-Analyser/
├── assets/
│   └── screenshots/
├── dataset/
├── models/
├── results/
├── src/
├── README.md
├── requirements.txt
└── notes.md
```

## Machine Learning Pipeline

1. User enters an email.
2. Email is cleaned using NLP preprocessing.
3. TF-IDF converts text into numerical features.
4. Logistic Regression predicts phishing or legitimate.
5. The analyser generates a security report.

## Skills Demonstrated

- Natural Language Processing (NLP)
- Machine Learning Classification
- TF-IDF Feature Engineering
- Logistic Regression
- Data Preprocessing
- Model Evaluation
- Python Programming
- Cybersecurity Fundamentals
- Threat Detection

## Installation

```bash
git clone <repository-url>
cd AI-Phishing-Email-Analyser

py -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

## Running the Project

Train the text model:

```bash
py src/train_text_model.py
```

Run the phishing analyser:

```bash
py src/email_analyser.py
```

Evaluate the model:

```bash
py src/evaluate_model.py
```

Generate the confusion matrix:

```bash
py src/confusion_matrix_plot.py
```

## Results

The project generates:

- AI phishing predictions.
- Confidence scores.
- Confusion matrix.
- Model performance chart.
- AI security report.

## Future Improvements

- Larger phishing email dataset.
- Random Forest and XGBoost comparison.
- Streamlit web application.
- URL reputation checking.
- Email attachment analysis.
- Explainable AI (SHAP/LIME).

## Author

**Mohau Klas Phiandi**

Bachelor of science in Mathematical Sciences 
Major:Computer Science

Cybersecurity | Networking | Machine Learning | Data Science