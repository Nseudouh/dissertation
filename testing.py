import streamlit as st
import pandas as pd
from transformers import pipeline


st.title("Mobile Telecommunication Sentiment Analysis")
st.markdown("This application is all about sentiment analysis of network providers. Analysising the reviews of custoners through the use of streamlit.")
st.sidebar.title("Sentiment Analysis of  Network Providers")
st.sidebar.markdown('Displaying the analysis of passengers reviews and the deploying the models that was implemented')

input_text = st.text_input("Get Predictions", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
if input_text:
    sentiment_pipe = pipeline("sentiment-analysis")
    res = sentiment_pipe(input_text)
    #print(res)
    st.write("Your predict is ", "POSITIVE")

data= pd.read_csv("Reviews Sentiment.csv")

if st.checkbox("Show new_data"):
    st.write(data.head(50))