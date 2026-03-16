import streamlit as st
import pandas as pd
import joblib

# Set the title of the web page
st.title("Predictive Maintenance Dashboard")
st.write("Enter the machine's sensor readings below to predict a potential failure.")

# Create input fields for the user
machine_type = st.selectbox("Product Type", options=[0, 1, 2], help="0=Low, 1=Medium, 2=High quality")
air_temp = st.number_input("Air temperature [K]", value=298.1)
process_temp = st.number_input("Process temperature [K]", value=308.6)
rot_speed = st.number_input("Rotational speed [rpm]", value=1551)
torque = st.number_input("Torque [Nm]", value=42.8)
tool_wear = st.number_input("Tool wear [min]", value=0)

# 1. Load the trained AI model
model = joblib.load('predictive_maintenance_model.joblib')

# 2. Create a big button for the user to click
if st.button("Predict Machine Health"):
    
    # 3. Gather all the numbers the user typed into a mini-spreadsheet row
    input_data = pd.DataFrame([[
        machine_type, air_temp, process_temp, rot_speed, torque, tool_wear
    ]], columns=['Type', 'Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]'])
    
    # 4. Have the AI make a prediction based on those numbers
    prediction = model.predict(input_data)
    
    # 5. Display the final result on the screen!
    if prediction[0] == 0:
        st.success("✅ The machine is predicted to be HEALTHY.")
    else:
        st.error("🚨 WARNING: The machine is predicted to FAIL soon. Maintenance required!")