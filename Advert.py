import streamlit as st
import pandas as pd
import pickle

st.write("""
# Advertising Sales Prediction App

This app predicts the **Sales** of Advertising
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0.7, 44.5, 296.4)
    Radio = st.sidebar.slider('Radio', 0.3, 39.3, 49.6)
    Newspaper = st.sidebar.slider('Newspaper', 0.3, 45.1, 114.0)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("Advert.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
