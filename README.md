## 🌍 Carbon Footprint Prediction using Machine Learning
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b?logo=streamlit)
[![Requirements](https://img.shields.io/badge/Requirements-TXT-important?logo=pip)](https://github.com/suryamothukuri/Carbon-footprint-prediction/blob/main/requirements.txt)

A full-stack data science project that analyzes individual lifestyle choices to estimate monthly carbon emissions. This project combines exploratory data analysis, machine learning modeling, and an interactive dashboard to help users understand and reduce their carbon footprint.

---

#### 📌 Project Overview

> **Goal**: Predict a person’s monthly carbon emissions (in kg CO₂) based on lifestyle factors like transport, diet, energy usage, and waste management  
> **Type**: End-to-end ML Project | Dashboard | Environmental Awareness  
> **Audience**: Students, researchers, environmentally-conscious users, and data science enthusiasts

---

#### 🎯 Objectives

- Perform detailed **EDA** to uncover patterns in carbon-emitting behaviors
- Engineer meaningful features using real-world CO₂ equivalence mappings
- Build and compare multiple **regression models**
- Create a **Streamlit dashboard** to visualize insights and estimate emissions interactively

---

#### 🧪 Methodology

#### 🔹 Data Preparation
- Cleaned raw survey data, handled missing values
- Created new columns: `diet_emissions`, `vehicle_emissions`, `flight_emissions`, `waste_emissions`

#### 🔹 Exploratory Data Analysis (EDA)
- Visualized distributions, correlations, and categorical interactions
- Used boxplots, heatmaps, mosaic plots, and spider charts

#### 🔹 Modeling
- Built multiple regression models: Ridge, Random Forest, SVR, XGBoost, CatBoost
- Used `GridSearchCV` for hyperparameter tuning
- Selected **CatBoost** as the best model based on R² and RMSE

#### 🔹 Deployment
- Developed an interactive Streamlit app for users to estimate their emissions
- Model serialized using `joblib` / `.cbm` and used inside the app

---

#### 🚀 Deployment Instructions

1. **Clone the repository**

    ```bash
    git clone https://github.com/suryamothukuri/Carbon-footprint-prediction.git
    cd Carbon-footprint-prediction
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**

    ```bash
    streamlit run app/app.py
    ```

---

#### 🙌 Acknowledgements

This project is inspired by research into climate change, behavioral data science, and the global push for sustainable living.  
CO₂ equivalence factors used in this project are based on reliable environmental datasets and academic sources.

---

> *"Measure what you can, manage what you can’t. Prediction is the first step toward change."*  
> — Surya Mothukuri
