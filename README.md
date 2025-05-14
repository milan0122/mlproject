# mlproject : Student Perfromance Indicator
"An end-to-end machine learning project to predict and analyze student academic outcomes based on math"
## 📌 Table of Contents
- [📊 Project Overview](#-project-overview)
- [🧪 Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [📈 Exploratory Data Analysis](#-exploratory-data-analysis)
- [🎯 Model Performance](#-model-performance)
- [🚀 Deployment](#-deployment)
- [📦 Installation](#-installation)
- [🔮 Future Work](#-future-work)
- [🙋 Author](#-author)
- [📄 License](#-license)
## 📊 Project Overview
- Research: Understanding about the data, exploratory data analysis about the data, feature engineering, preprocessing and model training
- Development: Created the component and pipeline for data ingestion, transformation and model training with creating simple interface using flask. 
- Deployment : Application is deployed on AWS 
## 🧪 Features
- Data ingestion and validation
- EDA with visual insights
- Data preprocessing and feature engineering
- Model training with evaluation
- Model serialization using drill
- Logging and exception handling

## Tech Stack
List the tools and technologies used:
- Python, Pandas, NumPy, Scikit-learn
- Matplotlib/Seaborn for visualization
- Flask for simple interface
- Git for CI/CD
- Elastic Beanstalk for deployment
## EDA and Insights 
![Alt Text - Student Performance by gender and lunch](https://github.com/milan0122/mlproject/blob/a7395cf1b7d6cfc4534ac426171d5eb2c470a1d5/screnshots/gender_lunch.png)
![Alt Text - Student Performance by gender ](https://github.com/milan0122/mlproject/blob/a7395cf1b7d6cfc4534ac426171d5eb2c470a1d5/screnshots/gender_bivariate.png)

# Model Performance
Quick summary of model performance 
|Model|Mean Squared Error| R2_score|
|---|---|---|
|Linear Regression |29.09| 0.88|
|RandomForestRegressor|35.4687|0.8542|
|Gradient Boosting Regressor|21.40|0.8722|
|catboostRegressor|36.1037|0.8516|

# Project Clone and setup
- Clone the repository: 
``` 
git clone https://github.com/milan0122/mlproject.git 
```
- Install dependencies 
    ```
     pip install -r requirements.txt
    ```
- Check the simple app interface 
    ```
    cd mlproject/
    python app.py
    ```
 