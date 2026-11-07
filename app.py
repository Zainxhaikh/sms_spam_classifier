import streamlit as st
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
nltk.download("punkt")
nltk.download("stopwords")

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        # check if the word is alphanumeric
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))    
         
    return " ".join(y)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("SMS Spam Classifier")
input_sms = st.text_area("Enter your message here:")

if st.button("Predict"):
    #preprocess the input
    transform_sms = transform_text(input_sms)

    # vectorize the input
    vector_input = vectorizer.transform([transform_sms])

    # prediction
    result = model.predict(vector_input)[0]

    # Display the result
    if result == 1:
        st.header("Spam")   
    else:
        st.header("Not Spam")
