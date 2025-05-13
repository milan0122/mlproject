import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from dataclasses import dataclass
from sklearn.ensemble import(AdaBoostRegressor,GradientBoostingRegressor,RandomForestRegressor)
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from src.utils import (save_object,evaluate_model)
from sklearn.metrics import r2_score

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info('Split the training and test input data')
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],train_array[:,-1],
                test_array[:,:-1],test_array[:,-1]
            )
            models = {
                'Linear Regression ': LinearRegression(),
                'K_Neighbors Regressor':KNeighborsRegressor(),
                'Random Forest Regressor': RandomForestRegressor(),
                'Adaboosting Regressor':AdaBoostRegressor(),
                'Gradient Boosting Regressor':GradientBoostingRegressor(),

}
            model_report:dict = evaluate_model(X_train,y_train,X_test,y_test,models)

            # get the best score
            best_model_score = max(sorted(model_report.values()))

            # get the best model name from dict 
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score <= 0.8:
                raise CustomException('No best model found')
            logging.info(f'Best model on both training and testing dataset :{best_model_name}')


            
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            logging.info('saved the best model')

            #checking with best model
            predicte = best_model.predict(X_test)
            score = r2_score(y_test,predicte)

            return score
        except Exception as e:
            raise CustomException(e,sys)
        
        
    