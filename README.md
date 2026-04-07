# 🚀 RUL Predictor (Remaining Useful Life)

## 🔍 Problem Statement

This project predicts the Remaining Useful Life (RUL) of machines using sensor data. It helps in predictive maintenance by estimating when a machine is likely to fail.

## 🧠 Approach

* Data preprocessing using Pandas
* Feature engineering and cleaning
* Model training using:

  * Random Forest Regressor
  * XGBoost Regressor
* Model evaluation using Mean Absolute Error (MAE)
* Final model saved as `model.pkl` using Joblib

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Matplotlib, Seaborn
* Streamlit

## 🌐 Deployment

The trained model is deployed using Streamlit for interactive prediction.

## ▶️ How to Run Locally

1. Install dependencies:
   pip install -r requirements.txt

2. Run the Streamlit app:
   streamlit run app.py

## 📁 Project Files

* `app.py` → Streamlit web application
* `model.pkl` → trained machine learning model
* `rulmodel.ipynb` → training and experimentation notebook

## 📊 Model Evaluation

* Metric used: Mean Absolute Error (MAE)
  (Add your actual MAE value here if available)

## 📈 Visualizations

* Data distribution plots
* Feature analysis using Seaborn & Matplotlib

## 🚀 Future Improvements

* Implement deep learning models (LSTM)
* Add real-time sensor data integration
* Deploy as REST API using Flask/FastAPI
* Improve model accuracy with feature selection
