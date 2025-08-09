from flask import Flask ,render_template,request
import numpy as np 
import pandas as pd 
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

application = Flask(__name__)
app=application


#Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

#route for a prediction 
@app.route('/predict',methods=['Get','Post'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data =  CustomData(
            gender = request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=request.form.get('reading_score'),
            writing_score=request.form.get('writing_score') )
        pred_df = data.get_data_as_data_frame()
        predict_data = PredictPipeline()
        results= predict_data.predict(pred_df)
        return render_template('home.html',result=results[0])
    
if __name__=='__main__':
    app.run(host="0.0.0.0")
