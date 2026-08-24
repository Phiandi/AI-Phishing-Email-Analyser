# AI Phishing Email Analyser Lab – Learning Notes

These notes document everything I learned while building my AI Phishing Email Analyser project from the beginning of the lab until the final evaluation stage.

---

# Day 1 – Introduction to Phishing & Project Setup

## What is phishing?

Phishing is a cyberattack where an attacker sends fraudulent emails or messages to trick people into revealing sensitive information such as passwords, banking details, or personal information.

## Difference between phishing and spam

**Spam** is unwanted bulk email that is usually sent for advertising or promotional purposes.

**Phishing** is a malicious email that is specifically designed to steal sensitive information, install malware, or trick a user into clicking harmful links.

## Five common phishing indicators

1. Urgent or threatening language.
2. Suspicious hyperlinks or shortened URLs.
3. Requests for passwords or personal information.
4. Poor spelling or grammar.
5. Unknown or suspicious sender email addresses or domains.

## What is a dataset?

A dataset is a collection of organised information that is used to train and test a machine learning model. In this project, the dataset contains emails labelled as either legitimate or phishing.

## What is supervised machine learning?

Supervised machine learning learns from labelled examples. In this project:

* **0** = Legitimate email.
* **1** = Phishing email.

The model learns patterns from these labelled emails so it can predict whether a new email is phishing or legitimate.

## Day 1 Reflection

Today I set up the AI Phishing Email Analyser project. I created a Python virtual environment, installed the required libraries, loaded the phishing email dataset into Python using Pandas, and explored the dataset to understand its structure, features, and labels. I also learned the basics of phishing attacks and why machine learning can be used to detect them.

---

# Day 2 – Machine Learning Basics

## What are Features (X)?

Features are pieces of information about an email that help the AI make a decision. Examples include:

* Number of words.
* Number of links.
* Number of spelling errors.
* Number of urgent keywords.
* Number of email addresses.

These values become the inputs that the machine learning model learns from.

## What are Labels (y)?

The label is the correct answer for each email.

* **0** = Legitimate email.
* **1** = Phishing email.

The model compares the features with these labels while learning.

## Why split the dataset?

The AI learns patterns from the **training dataset** and is evaluated on the **testing dataset**. Testing the model on unseen emails helps measure how well it performs in real-world situations.

## What is Logistic Regression?

Logistic Regression is a supervised machine learning algorithm used for **binary classification**. It predicts whether an email belongs to one of two categories: legitimate or phishing.

## What I learned today

* Loaded the phishing dataset.
* Separated features (X) and labels (y).
* Split the dataset into training and testing sets.
* Trained my first Logistic Regression model.
* Made predictions using the trained model.
* Calculated prediction confidence using `predict_proba()`.
* Saved the trained model using Joblib.

## Why save the model?

Saving a trained model allows it to be reused later without training it again. This makes the application faster because it only needs to load the saved model instead of retraining it every time.

## Day 2 Reflection

Today I trained my first machine learning model using Logistic Regression. I learned how the model learns from training data and how it is evaluated using testing data. I also learned that a prediction and a confidence score are different. A model can predict phishing while still having moderate confidence depending on the patterns it learned from the dataset.

---

# Day 3 – Training a Machine Learning Model

## Reflection

Today I focused on training and testing my first phishing detection model. I learned how the complete machine learning workflow fits together before introducing Natural Language Processing.

## What I accomplished

* Prepared the dataset for machine learning.
* Trained a Logistic Regression classifier.
* Tested the model using unseen data.
* Saved the trained model as `phishing_detector.pkl`.
* Built a simple predictor that could classify an email as phishing or legitimate.

## Confidence score

I learned that the model produces both:

* A **prediction** (phishing or legitimate).
* A **confidence score**, which shows how certain the model is about its prediction.

This helped me understand that predictions are probabilities, not guaranteed answers.

## Key Takeaway

Today I successfully built and saved my first phishing detection model, making it possible to reuse it later inside a real application.

---

# Day 4 – Natural Language Processing (NLP)

Today I learned how to prepare raw email text before it can be used for machine learning.

## What is Natural Language Processing (NLP)?

Natural Language Processing (NLP) is a branch of Artificial Intelligence that helps computers understand, process, and analyse human language such as emails, messages, and documents.

## NLP Pipeline

### Convert text to lowercase

This treats words like **"Your"** and **"your"** as the same word.

### What is tokenization?

Tokenization means breaking a sentence into individual words.

Example:

**Before**

> Your account has been suspended immediately.

**After**

`["your", "account", "has", "been", "suspended", "immediately"]`

### Remove punctuation

Punctuation symbols such as `. , : ! ?` are removed because they usually do not help the model detect phishing.

### What is text preprocessing?

Text preprocessing is the process of cleaning raw text before it is used by a machine learning model.

## Day 4 Reflection

Today I built my first NLP pipeline. I learned how to clean email text by converting it to lowercase, breaking it into words, and removing punctuation. I also created my first reusable preprocessing script that prepares email text for machine learning.

---

# Day 5 – Text Cleaning & TF-IDF

Today I learned how to clean email text and convert words into numerical features that machine learning models can understand.

## What are stopwords?

Stopwords are very common English words that usually do not help the AI decide whether an email is phishing.

Examples include:

* the
* is
* and
* to
* has
* been

Removing them helps the model focus on more meaningful words.

## What is lemmatization?

Lemmatization converts different forms of a word into its base dictionary form.

Examples:

* verified → verify
* verifying → verify
* accounts → account
* clicking → click

## Why does lemmatization help AI?

Instead of learning several versions of the same word, the AI learns one main concept.

For example:

* verify
* verified
* verifying

All become **verify**, making the model more consistent.

## Building a reusable preprocessing function

I created a `clean_email()` function that automatically performs:

* Lowercase conversion.
* Tokenization.
* Punctuation removal.
* Stopword removal.
* Lemmatization.

This function can clean one email or an entire dataset.

## Applying preprocessing to a dataset

I learned how to use Pandas `.apply()` to clean every email in a dataset using a single function.

## What is TF-IDF?

**TF-IDF (Term Frequency–Inverse Document Frequency)** converts words into numbers so that a machine learning model can learn patterns from text.

Important words such as:

* verify
* urgent
* password
* account

receive higher importance than very common words.

## What I learned today

* Cleaned raw email text.
* Removed unnecessary words.
* Applied preprocessing to multiple emails.
* Converted cleaned text into TF-IDF numerical features.
* Prepared email text for machine learning.

## Day 5 Reflection

Today I learned how NLP prepares text for machine learning. I built a reusable preprocessing pipeline and converted cleaned email text into TF-IDF feature vectors. This was my first experience transforming human language into numerical data that a machine learning model can understand.

---

# Day 6 – Building the AI Phishing Email Detection Pipeline

Today I connected Natural Language Processing with Machine Learning to build a complete phishing email analyser that works with real email text.

## What I accomplished

* Created `email_analyser.py`.
* Allowed users to paste an email into the application.
* Connected the analyser to the `clean_email()` preprocessing function.
* Automatically cleaned user input using the NLP pipeline.
* Converted cleaned email text into TF-IDF features.

## Training a second machine learning model

Today I trained a **second Logistic Regression model** using real email text instead of manually created numerical features.

### Steps completed

* Loaded `sample_emails.csv`.
* Cleaned every email using `clean_email()`.
* Converted cleaned emails into TF-IDF vectors.
* Trained a Logistic Regression classifier.
* Saved the trained model as `models/text_phishing_detector.pkl`.
* Saved the TF-IDF vectorizer as `models/tfidf_vectorizer.pkl`.

## Why are there two models?

### Model 1 – `phishing_detector.pkl`

Uses engineered numerical email features such as:

* Number of links.
* Number of urgent keywords.
* Number of spelling errors.
* Number of words.

### Model 2 – `text_phishing_detector.pkl`

Uses the actual content of email text after TF-IDF preprocessing. This is the model used by the final AI phishing analyser.

## Using the saved model

I learned how to:

* Load a trained model with `joblib.load()`.
* Load the saved TF-IDF vectorizer.
* Use `transform()` instead of `fit_transform()` for new emails.
* Predict phishing or legitimate emails using the saved model.
* Calculate prediction confidence with `predict_proba()`.

## Day 6 Reflection

Today I connected my NLP pipeline with a machine learning model. Instead of entering numbers manually, the application now accepts real email text, cleans it, converts it into TF-IDF features, and sends it to a trained AI model for prediction.

---

# Day 7 – Building the AI Security Report

Today I transformed the phishing detector into a cybersecurity style email analysis tool.

## Building the AI Security Report

I upgraded the analyser to display:

* Prediction (Phishing or Legitimate).
* Confidence Score.
* Risk Level.
* Suspicious keywords detected.
* Security recommendations.

## AI Email Analysis Pipeline

1. User pastes an email.
2. Email is preprocessed using NLP.
3. Cleaned text is converted into TF-IDF features.
4. The saved Logistic Regression model analyses the email.
5. The application generates a complete AI security report.

## Files created and updated

### New Python files

* `src/email_analyser.py`
* `src/train_text_model.py`

### New model files

* `models/text_phishing_detector.pkl`
* `models/tfidf_vectorizer.pkl`

## Security recommendations generated by the analyser

If an email is predicted as phishing, the analyser recommends:

* Do not click suspicious links.
* Do not provide passwords or banking information.
* Verify the sender before responding.

If the email is legitimate, it still recommends verifying unexpected requests before taking action.

## Day 7 Reflection

Today I completed the end-to-end AI phishing email analyser. The application now accepts real email text, preprocesses it automatically, predicts whether the email is phishing or legitimate, calculates a confidence score, assigns a risk level, detects suspicious keywords, and provides security recommendations.

---

# Day 8 – Model Evaluation & GitHub Project Completion

Today I completed the final stage of the project by evaluating the machine learning model and preparing the project for GitHub.

## Why evaluate a machine learning model?

Model evaluation helps measure how well the AI performs on unseen emails instead of relying only on predictions.

## Model evaluation metrics

### Accuracy

Accuracy measures the overall percentage of correct predictions made by the model.

### Precision

Precision measures how often emails predicted as phishing were actually phishing.

### Recall

Recall measures how many phishing emails the model successfully detected.

### F1-Score

The F1-Score combines Precision and Recall into a single balanced score.

### Classification Report

The classification report provides a detailed summary of the model's performance for each class, including precision, recall, F1-score, and support.

## What is a confusion matrix?

A confusion matrix is a table that compares the model's predictions with the actual labels.

### Four possible outcomes

* **True Positive (TP):** Correctly identified a phishing email.
* **True Negative (TN):** Correctly identified a legitimate email.
* **False Positive (FP):** Incorrectly flagged a legitimate email as phishing.
* **False Negative (FN):** Failed to detect a phishing email.

The confusion matrix helps identify where the model makes mistakes.

## Model Performance Chart

I created a bar chart showing the model's:

* Accuracy.
* Precision.
* Recall.
* F1-Score.

This makes it easier to visualise model performance.

## GitHub Project Preparation

Today I organised the project into a professional portfolio repository.

### Assets folder

Created an `assets/` folder to store project images and screenshots.

### Screenshots prepared

* Email analyser input.
* Cleaned email output.
* AI phishing prediction report.
* Model evaluation report.
* Confusion matrix.
* Model performance chart.

### README

I created a professional `README.md` that includes:

* Project overview.
* Features.
* Technologies used.
* Project structure.
* Installation guide.
* Usage instructions.
* Machine learning pipeline.
* Results.
* Future improvements.

## Skills I Demonstrated Throughout This Project

### Cybersecurity

* Phishing detection.
* Email threat analysis.
* Security recommendations.
* Suspicious keyword detection.

### Machine Learning

* Supervised learning.
* Binary classification.
* Logistic Regression.
* Model training and testing.
* Model evaluation.

### Natural Language Processing

* Tokenization.
* Stopword removal.
* Lemmatization.
* Text preprocessing.
* TF-IDF feature engineering.

### Python Programming

* Pandas.
* NumPy.
* Scikit-learn.
* NLTK.
* Matplotlib.
* Joblib.
* VS Code development workflow.

## Day 8 Reflection

Today I completed and polished the AI Phishing Email Analyser project. I evaluated the machine learning model using Accuracy, Precision, Recall, F1-Score, a Classification Report, and a Confusion Matrix. I also generated performance charts and organised the project into a professional GitHub repository with documentation, screenshots, and project assets. This project brought together Python, Natural Language Processing, Machine Learning, and Cybersecurity into one complete end-to-end phishing email detection application.

---

# Final Project Summary

Over eight days, I built an AI powered phishing email analyser from scratch. I started by learning phishing fundamentals and machine learning basics, then trained a Logistic Regression model, built an NLP preprocessing pipeline, converted email text into TF-IDF features, trained a second text-based classifier, created an AI security report with confidence scoring and recommendations, evaluated the model, and prepared the project for GitHub. This project strengthened my practical skills in Python, Machine Learning, Natural Language Processing, and Cybersecurity while giving me a portfolio project that demonstrates an end to end AI solution.
