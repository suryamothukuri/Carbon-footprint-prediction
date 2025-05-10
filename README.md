# Carbon-footprint-prediction
# 🌍 Carbon Footprint Prediction using Machine Learning

A full-stack data science project that analyzes individual lifestyle choices to estimate monthly carbon emissions. This project combines exploratory data analysis, machine learning modeling, and an interactive dashboard to help users understand and reduce their carbon footprint.

---

## 📌 Project Overview

> **Goal**: Predict a person’s monthly carbon emissions (in kg CO₂) based on lifestyle factors like transport, diet, energy usage, and waste management  
> **Type**: End-to-end ML Project | Dashboard | Environmental Awareness  
> **Audience**: Students, researchers, environmentally-conscious users, and data science enthusiasts

---

## 🎯 Objectives

- Perform detailed **EDA** to uncover patterns in carbon-emitting behaviors
- Engineer meaningful features using real-world CO₂ equivalence mappings
- Build and compare multiple **regression models**
- Create a **Streamlit dashboard** to visualize insights and estimate emissions interactively

---

## 🧪 Methodology

### 🔹 Data Preparation
- Handled missing values and inconsistent data types
- Engineered new features: `diet_emissions`, `vehicle_emissions`, `flight_emissions`, `waste_emissions`

### 🔹 Exploratory Data Analysis (EDA)
- Boxplots, correlation heatmaps, spider (radar) charts, mosaic plots
- Identified key emission drivers across different demographics

### 🔹 Modeling
- Trained 6 models: Ridge, Decision Tree, Random Forest, SVR, XGBoost, and CatBoost
- Performed **hyperparameter tuning** using `GridSearchCV`
- **CatBoost** selected as the best model (highest R², lowest RMSE)

### 🔹 Deployment
- Built an interactive app using **Streamlit** to estimate personal carbon emissions

---

## 📁 Project Structure
