import sys
from dataclasses import dataclass
import os
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self) -> None:
        self.data_transform_config =DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function responsible to data transformation
        '''
        try:
            numerical_cols = ['writing_score','reading_score']
            categorical_cols = ['gender','race_ethnicity','parental_level_of_eucation','lunch','test_preparation_course']


            num_pipeline=Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())

                ]
            )
            logging.info('numerical columns scaling and imputing complete')

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ohe',OneHotEncoder())
                ]
            )
            logging.info('categorical columns encoding and imputing complete')
            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,numerical_cols),
                    ('cat_pipeline',cat_pipeline,categorical_cols)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e ,sys)
        

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Read train and test data for transformation')

            preprocessing_obj = self.get_data_transformer_object()

            target_col = 'math_score'
            input_feat_train_df = train_df.drop(columns=[target_col],axis=1)
            target_feat_train_df = train_df[target_col]

            input_feat_test_df = test_df.drop(columns=[target_col],axis=1)
            target_feat_test_df = test_df[target_col]
            logging.info('applying preprocessing to training and test datafrae')
            print(input_feat_train_df.shape)
            input_train = preprocessing_obj.fit_transform(input_feat_train_df)
            input_test = preprocessing_obj.transform(input_feat_test_df)

            train_arr = np.c_[input_train,np.array(target_feat_train_df)] # this concatenate arrays by columns ( side by side)
            test_arr = np.c_[input_test,np.array(target_feat_test_df)] 

            logging.info(f'Saving preprocessing object')
            save_object(
                file_path = self.data_transform_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transform_config.preprocessor_obj_file_path
            )


        except Exception as e:
            raise CustomException(e,sys)
