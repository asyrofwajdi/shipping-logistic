
import pickle
import streamlit as st
import os

# Ensure the required library is installed
try:
    from sklearn.ensemble import RandomForestClassifier
except ModuleNotFoundError:
    st.error("The scikit-learn library is not installed. Please install it by running 'pip install scikit-learn'.")

# Check if the model file exists
model_path = 'shipping_model.sav'

if not os.path.exists(model_path):
    st.error(f"Model file not found at {model_path}")
else:
    # Reading Model
    with open(model_path, 'rb') as file:
        shipping_model = pickle.load(file)

    # web title
    st.title('Shipping Logistic Prediction')

    # Input fields
    Warehouse_block = st.text_input('Warehouse block')
    Mode_of_Shipment = st.text_input('Mode of Shipment')
    Customer_care_calls = st.number_input('Customer care calls', min_value=0, step=1)
    Customer_rating = st.number_input('Customer Rating', min_value=1, max_value=5, step=1)
    Cost_of_the_Product = st.number_input('Cost of product', min_value=0)
    Prior_purchases = st.number_input('Prior purchases', min_value=0, step=1)
    Product_importance = st.text_input('Product importance')
    Gender = st.text_input('Gender')
    Discount_offered = st.number_input('Discount Offered', min_value=0)
    Weight_in_gms = st.number_input('Weight in grams', min_value=0)

    # Code for prediction
    delivery = ''
    # Result
    if st.button('Delivery Prediction'):
        preds = shipping_model.predict([[Warehouse_block, Mode_of_Shipment, Customer_care_calls, Customer_rating, Cost_of_the_Product, Prior_purchases, Product_importance, Gender, Discount_offered, Weight_in_gms]])
        
        if(preds[0] == 1):
            delivery = 'Not reach on time'
        else:
            delivery = 'Reach on time'
        st.success(delivery)

