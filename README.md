# ⚙️ Predictive Maintenance Machine Learning Model

## Overview
This project is an end-to-end machine learning pipeline and interactive web dashboard designed to predict mechanical failures before they happen. By analyzing raw sensor data, this tool helps transition maintenance strategies from reactive (fixing broken machines) to proactive (servicing machines before failure), minimizing costly operational downtime.

## 🛠️ Technology Stack
* **Language:** Python
* **Data Processing:** Pandas
* **Machine Learning:** Scikit-learn (Random Forest Classifier)
* **Web Framework:** Streamlit
* **Model Deployment:** Joblib

## 📊 How It Works
1. **Data Ingestion:** Processed a dataset of 10,000 mechanical operations containing telemetry such as air temperature, process temperature, rotational speed, torque, and tool wear.
2. **Model Training:** Engineered and trained a `Random Forest` classification model to identify complex patterns leading to machine failure. The final model achieved an overall predictive accuracy of 98.45%.
3. **Interactive Dashboard:** Deployed the trained model into a local Streamlit web application. Users can input real-time sensor metrics to instantly predict machine health and trigger early-warning alerts under high-stress conditions.

## 🚀 Running the App Locally
To run this dashboard on your own machine:
1. Clone this repository.
2. Ensure you have the required libraries installed (`pip install pandas scikit-learn streamlit joblib`).
3. Run `streamlit run app.py` in your terminal.
