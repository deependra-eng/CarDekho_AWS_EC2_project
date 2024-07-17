import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


# Load the trained model
model = pickle.load(open('XG_model.pkl', 'rb'))

# --- APP TITLE & DESCRIPTION ---
st.title('Car Selling Price Predictor')
st.markdown("Get an estimate of your car's selling price based on its features.")

# Input Fields (based on your model's features)
vehicle_age = st.number_input('Vehicle Age (in years)', min_value=0, format="%d")
km_driven = st.number_input('Kilometers Driven', min_value=0, format="%d")
mileage = st.number_input('Mileage (in kmpl)', min_value=0.0, format="%.1f")
engine = st.number_input('Engine Displacement (in cc)', min_value=0, format="%d")
max_power = st.number_input('Maximum Power (in bhp)', min_value=0.0, format="%.1f")
seats = st.number_input('Number of Seats', min_value=2, max_value=10, step=1, format="%d")

# Seller Type Radio Buttons
seller_type = st.radio("Seller Type", ('Dealer', 'Individual', 'Trustmark Dealer'))
seller_type_mapping = {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3}

# Fuel Type Radio Buttons
fuel_type = st.radio("Fuel Type", ('CNG', 'Diesel', 'Electric', 'LPG', 'Petrol'))
fuel_type_mapping = {'CNG': 1, 'Diesel': 2, 'Electric': 3, 'LPG': 4, 'Petrol': 5}

# Transmission Type Radio Buttons
transmission_type = st.radio("Transmission Type", ('Automatic', 'Manual'))
transmission_type_mapping = {'Automatic': 1, 'Manual': 2}

if st.button('Predict Selling Price'):
    # Create the input data DataFrame (matching model's feature order)
    df = pd.DataFrame({
        'vehicle_age': [vehicle_age],
        'km_driven': [km_driven],
        'mileage': [mileage],
        'engine': [engine],
        'max_power': [max_power],
        'seats': [seats],
        'seller_type_Dealer': [1 if seller_type == 'Dealer' else 0],
        'seller_type_Individual': [1 if seller_type == 'Individual' else 0],
        'seller_type_Trustmark Dealer': [1 if seller_type == 'Trustmark Dealer' else 0],
        'fuel_type_CNG': [1 if fuel_type == 'CNG' else 0],
        'fuel_type_Diesel': [1 if fuel_type == 'Diesel' else 0],
        'fuel_type_Electric': [1 if fuel_type == 'Electric' else 0],
        'fuel_type_LPG': [1 if fuel_type == 'LPG' else 0],
        'fuel_type_Petrol': [1 if fuel_type == 'Petrol' else 0],
        'transmission_type_Automatic': [1 if transmission_type == 'Automatic' else 0],
        'transmission_type_Manual': [1 if transmission_type == 'Manual' else 0]
    })

    prediction = model.predict(df)
    st.success(f'The predicted selling price of the car is ₹{prediction[0]:.2f}')
