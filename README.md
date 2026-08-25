# 🛡️ AI Phishing Email Analyser

<p align="center">
 <img src="assets/banner.png" alt="AI Phishing Email Analyser Banner" width="100%">
</p>

<p align="center">
  An end-to-end phishing email detection system built with Python, Natural Language Processing (NLP), TF-IDF, and Logistic Regression.
</p>

<p align="center">
  Detect phishing emails • Analyse suspicious content • Generate AI-powered security reports
</p>

---

## Project Overview

Phishing emails are among the most common cybersecurity attacks used to steal passwords, banking information, and personal data. This project uses Machine Learning and Natural Language Processing to analyse email content and predict whether an email is **Phishing** or **Legitimate**.

The application cleans raw email text, converts it into numerical TF-IDF features, uses a trained Logistic Regression model for prediction, calculates a confidence score, detects suspicious keywords, and produces a cybersecurity-style security report.

---

## Built With

- Python 3.14
- Scikit-learn
- NLTK
- Pandas
- NumPy
- Matplotlib
- Joblib

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9-orange?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![NLTK](https://img.shields.io/badge/NLTK-NLP-green)](https://www.nltk.org/)
[![Machine Learning](https://img.shields.io/badge/Machine-Learning-red)](https://scikit-learn.org/)
[![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Email%20Security-darkblue)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🧠 AI Workflow](#-ai-workflow)
- [🔤 NLP Pipeline](#-nlp-pipeline)
- [📂 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [🚀 How to Run the Project](#-how-to-run-the-project)
- [📊 Model Performance](#-model-performance)
- [🖼️ Project Screenshots](#️-project-screenshots)
- [📚 Learning Journey](#-learning-journey)
- [🛠️ Future Improvements](#️-future-improvements)
- [👨‍💻 Author](#-author)

---

## ✨ Features

- Detect phishing and legitimate emails using Machine Learning.
- Clean email text using Natural Language Processing (NLP).
- Remove stopwords and punctuation.
- Apply lemmatization for better word normalization.
- Convert email text into TF-IDF numerical features.
- Generate prediction confidence scores.
- Detect suspicious phishing keywords.
- Produce an AI-powered cybersecurity security report.

---

## 🧠 AI Workflow

<p align="center">
  <img src="assets/diagrams/ai_workflow.png" alt="AI Workflow Diagram" width="90%">
</p>

### How the analyser works

1. The user enters or pastes an email.
2. The email is cleaned using Natural Language Processing.
3. TF-IDF converts the cleaned text into numerical features.
4. A Logistic Regression model analyses the email.
5. The application predicts whether the email is **Phishing** or **Legitimate**.
6. The analyser generates a confidence score, risk level, suspicious keywords, and a security recommendation.