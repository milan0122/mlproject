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
## 📊 Project Overview
- Research: Understanding about the data, exploratory data analysis about the data, feature engineering, preprocessing and model training
- Development: Created the component and pipeline for data ingestion, transformation and model training with creating simple interface using flask. 
- Deployment : Application is deployed on AWS 
## 🧪 Features
- EDA with visual insights : research
- Data preprocessing and feature engineering: research
- model training and evaluation : research
- Data ingestion and validation : development
- Model training with evaluation : development
- Model serialization using drill : artifacts
- Logging and exception handling : logs 

## Tech Stack
List the tools and technologies used:
- Python, Pandas, NumPy, Scikit-learn
- Matplotlib/Seaborn for visualization
- Flask for simple interface
- Git for CI/CD
- Elastic Beanstalk for deployment
## EDA and Insights 
![Alt text - Student Performance by gender and lunch](https://github.com/milan0122/mlproject/blob/a7395cf1b7d6cfc4534ac426171d5eb2c470a1d5/screnshots/gender_lunch.png)
![Alt text - Distribution of each categorical features with their category](https://github.com/milan0122/mlproject/blob/a7395cf1b7d6cfc4534ac426171d5eb2c470a1d5/screnshots/distribution_categorical.png)
![Alt text - Student Performance impact by gender ](https://github.com/milan0122/mlproject/blob/a7395cf1b7d6cfc4534ac426171d5eb2c470a1d5/screnshots/gender_bivariate.png)
![Alt text - Student Performance impact by Race/ethnicity ](https://github.com/milan0122/mlproject/blob/a7395cf1b7d6cfc4534ac426171d5eb2c470a1d5/screnshots/race_ethnicity.png)
![Alt text - Student Performance by test_preparation_course ](https://github.com/milan0122/mlproject/blob/a7395cf1b7d6cfc4534ac426171d5eb2c470a1d5/screnshots/test_prep.png)
![Alt text - Student Performance Calculator UI](https://github.com/milan0122/mlproject/blob/45c49a74f9502260bf16504fc45e5092f4f80a61/screnshots/ui.png)
#### Final Insights
- Student's Performance is related with lunch, race, parental level education
- Females lead in pass percentage and also are top-scorers
- Student's Performance is not much related with test preparation course
- Finishing preparation course is benefitial.
## Model Performance
Quick summary of model performance 
|Model|Mean Squared Error| R2_score|
|---|---|---|
|Linear Regression |29.09| 0.88|
|RandomForestRegressor|35.4687|0.8542|
|Gradient Boosting Regressor|21.40|0.8722|
|catboostRegressor|36.1037|0.8516|

## Project Clone and setup
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
 