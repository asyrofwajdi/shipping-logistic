import pickle
import streamlit as st

# Reading Model
shipping_model = pickle.load(open('shipping_model.sav','rb'))

# web title
st.title('Shipping Logistic Prediction')

Warehouse_block = st.text_input('Warehouse block')
Mode_of_Shipment = st.text_input('Mode of Shipment')
Customer_care_calls = st.text_input('Customer care call')
Customer_rating = st.text_input('Customer Rating')
Cost_of_the_Product = st.text_input('Cost of product')
Prior_purchases = st.text_input('Prior purchase')
Product_importance = st.text_input('Product important')
Gender = st.text_input('Gender')
Discount_offered = st.text_input('Discount Offered')
Weight_in_gms = st.text_input('Weight in grams')

# Code for prediction
delivery = ''
# Result
if st.button('Delivery Prediction'):
    preds = grid_search_dt.predict([[Warehouse_block, Mode_of_Shipment, Customer_care_calls, Customer_rating, Cost_of_the_Product, Prior_purchases, Product_importance, Gender, Discount_offered, Weight_in_gms]])
    
    if(preds[0] == 1):
        delivery = 'Not reach on time'
    else : 
        delivery = 'Reach on time'
    st.success(delivery)

