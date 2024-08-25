import streamlit as st
import pickle
import json
import numpy as np

# Load the saved model
with open('decision_tree_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit interface
st.title('Payment Option Prediction')

# Reading dict from JSON files
def load_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error(f"File {filename} not found.")
        return {}
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON from {filename}.")
        return {}

# Load mappings
location_region_mapping = load_json('location_dict.json')
payment_option_mapping = load_json('payment_dict.json')

# Check if mappings are loaded correctly
if not location_region_mapping or not payment_option_mapping:
    st.stop()

# Input data from the user
location_region_input = st.selectbox('Location Region', list(location_region_mapping.values()))
amount_input = st.number_input('Amount', min_value=0)
risk_score_input = st.number_input('Risk Score', min_value=0)
transaction_time_input = st.number_input('Transaction Time', min_value=0)
transaction_fee_input = st.number_input('Transaction Fee', min_value=0)

# Convert categorical input to numeric code
location_region_code = {v: k for k, v in location_region_mapping.items()}[location_region_input]

# Prepare the input for prediction
input_data = np.array([[location_region_code, amount_input, risk_score_input, transaction_time_input, transaction_fee_input]])

# Make prediction
prediction = model.predict(input_data)

# Convert prediction from numeric code to original category
predicted_payment_option = payment_option_mapping.get(str(prediction[0]), "Unknown Option")

# Display the prediction
st.write(f"The predicted payment option is: **{predicted_payment_option}**")
