# House Price Prediction

## Overview
This project focuses on predicting house prices using various machine learning models. The dataset is preprocessed and analyzed using exploratory data analysis (EDA) techniques before training multiple models. The best-performing model is selected based on evaluation metrics, and a FastAPI-based web service is deployed on Render.

## Dataset Analysis
- **Checked for null values** and handled them appropriately.
- **Generated a correlation matrix** to analyze relationships between features.
- **Used the `skimpy` library** to obtain a detailed summary of the dataset.

## Model Training & Evaluation
Multiple machine learning models were trained, including:
- **Linear Regression**
- **Support Vector Machine (SVM)**
- **Decision Tree**
- **Random Forest**
- **XGBoost**
- **And more...**

### Model Selection Criteria
- **R² Score**: Measures the goodness of fit.
- **Mean Absolute Error (MAE)**: Evaluates prediction error.

The best-performing model was selected based on these metrics.

## Hyperparameter Tuning
- **GridSearchCV** was used for hyperparameter tuning to optimize model performance.

## FastAPI Deployment
- Developed a **FastAPI** backend to serve predictions.
- Deployed the API on **Render** for accessibility.

## Deployment on Render
The FastAPI application is deployed on **Render**, making it accessible online. You can test the API using the provided endpoint.
**Deployed Link:** https://house-price-prediction-plf7.onrender.com/
