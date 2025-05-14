# it consist of common object
import os 
import sys 
import pandas as pd 
import numpy as np 
import dill
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
        
def evaluate_model(X_train,y_train,X_test,y_test, models,params):
    try:
        report = {}
        for i in range(len(list(models))):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            
            # Use a new variable to avoid overwriting 'params'
            param_grid = list(params.values())[i]
            
            if param_grid:
                grid = GridSearchCV(model, param_grid=param_grid, cv=3, n_jobs=-1, refit=True)
                grid.fit(X_train, y_train)
                model.set_params(**grid.best_params_)
            
            # Fit model (either with best params or as-is)
            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
            
            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e,sys)
    