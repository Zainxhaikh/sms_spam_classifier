# SMS Spam Classifier

An NLP based Machine Learning web app that detects whether an SMS message is Spam or Not Spam.

Live Demo: https://smsspamclassifiergit-c5tvkbejwe3bxtfyha5kwb.streamlit.app/

## Tech Stack
- Python
- Scikit-learn
- Streamlit
- Pandas, NumPy
- NLTK

## How it Works
- SMS Spam Collection dataset used for training
- Text Preprocessing: Lowercasing, Tokenization, Stopwords Removal, Stemming
- TF-IDF Vectorizer used to convert text into numbers
- Naive Bayes / Logistic Regression model trained to classify Spam vs Ham
- Model saved as `model.pkl` and `vectorizer.pkl`

## Project Files
- `app.py` - Streamlit web app
- `sms_spam_classifier.ipynb` - Model training notebook
- `model.pkl` - Trained model
- `vectorizer.pkl` - TF-IDF Vectorizer

## How to Run Locally
1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`
4. Type any SMS message and check if it is Spam or Not Spam

## Features
- Real-time spam detection
- Clean Streamlit UI
- Live deployed app

## Author
Zain Ul Abidin - Aspiring AI/ML Developer
Live Demo: https://smsspamclassifiergit-c5tvkbejwe3bxtfyha5kwb.streamlit.app/
This is to check spam and not spam messages
