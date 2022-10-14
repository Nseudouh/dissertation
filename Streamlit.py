import streamlit as st
import pandas as pd
from transformers import pipeline
from textblob import TextBlob
import plotly as px
st.title("Mobile Telecommunication Sentiment Analysis")
st.markdown("This application is about sentiment analysis of network providers. Analysising the reviews of custoners through the use of streamlit.")
reasons = {'speed' : ['fast', 'speed', 'per second','slow'], 'price' : ['price', 'affordable', 'automated billing'],
           'coverage' : ['remote', 'international'], 'good' : ['lovely', 'love'],
           'Poor Customer Service': [ 'not good', 'bad customer service','poor services in some areas', 'long wait time to reach customer service', ' i have to wait for  a long time before i can reach the customer service'],
           'Bad Network': ['poor network','high international call charges', 'horrible data bundle', 'not reliable at all']

           }
networks = ['EE','ee','Vodafone','vodafone','giffgaff','Giffgaff','lebara', 'Lebara']
network: str = ''
with st.form(key= 'nlpForm'):
    input_text = st.text_input("Enter Text Here", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False)
    submit_bottom= st.form_submit_button(label= 'Analyse')
if input_text:
    reason: list = []
    key_list = reasons.keys()
    for key in key_list:
        for k in reasons[key]:
            if input_text.__contains__(k):
                if reason.__contains__(key):
                    continue
                else:
                    reason.append(key)
    for n in networks:
        if input_text.__contains__(n):
            network = n
    sentiment_pipe = pipeline("sentiment-analysis")
    res = sentiment_pipe(input_text)
    res[0]['Network'] = network
    res[0]['Reason'] = reason
    st.write(res)

