import pickle
import streamlit as st

# Reading Model
shipping_model = pickle.load(open('shipping_model.sav'))

# web title
st.title('Shipping Logistic Prediction')
