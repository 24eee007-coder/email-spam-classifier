# 📧 Email Spam Classifier

A machine learning-based classifier that detects whether an email is **spam** or **ham** (legitimate) using NLP features and supervised learning.

🔗 **Live Demo:** https://email-spam-classifier-nfpj4kbwkwag3xxznbtrwq.streamlit.app

## Features
- Classifies emails as spam or ham in real time
- Bag-of-words features extracted from email text
- Compares Naive Bayes, Logistic Regression and SVM
- Simple web interface built with Streamlit

## Tech Stack
- **Language:** Python
- **Libraries:** scikit-learn, pandas, NumPy, Matplotlib, Seaborn, Streamlit

## Dataset
Enron Email Spam Dataset (5,172 emails, 3,000 word-count features) from Kaggle.

## Results

| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Naive Bayes | 94.2% | 86.8% | 94.3% | 90.4% |
| **Logistic Regression** | **98.3%** | **95.8%** | **98.3%** | **97.0%** |
| SVM | 97.5% | 95.7% | 95.7% | 95.7% |

Logistic Regressio
