import streamlit as st
import pandas as pd
import pickle

st.write("""
# Advertising Sales Prediction App

This app predicts the **Sales** of Advertising
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 230.1, 44.5, 17.2)
    Radio = st.sidebar.slider('Radio', 37.8, 39.3, 45.9)
    Newspaper = st.sidebar.slider('Newspaper', 69.2, 45.1, 69.3)
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
