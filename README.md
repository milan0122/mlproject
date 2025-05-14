# mlproject : Student Perfromance Indicator
"An end-to-end machine learning project to predict and analyze student academic outcomes based on math"
### Breif Description about the project
- Research: Understanding about the data, exploratory data analysis about the data, feature engineering, preprocessing and model training
- Development: Created the component and pipeline for data ingestion, transformation and model training with creating simple interface using flask. 
- Deployment : Application is deployed on AWS 

## EDA and Insights 
![Alt Text - description of the image]()

# Model Performance
Quick summary of model performance 
|Model|Mean Squared Error| R2_score|
|---|---|---|
|Linear Regression |29.09| 0.88|
|RandomForestRegressor|35.4687|0.8542|
|Gradient Boosting Regressor|21.40|0.8722|
|catboostRegressor|36.1037|0.8516|

## Tech Stack 
List the tools and technologies used:
- Python, Pandas, NumPy, Scikit-learn
- Matplotlib/Seaborn for visualization
- Flask for simple interface
- Git for CI/CD
- Elastic Beanstalk for deployment
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
 