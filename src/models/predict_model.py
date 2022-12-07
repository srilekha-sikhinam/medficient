import sys
sys.path.insert(0, '..\src\helpers')
sys.path.insert(0, '..\src\models')

import pandas as pd
import numpy as np
import _pickle as cpickle
from preprocess_input import *

def get_prediction(input_feature_arr, options):
    patient_df = clean_input(input_feature_arr, options)
    model = cpickle.load(open('models\knee_rep_patient_rf_model.pkl', 'rb'))
    prediction = model.predict(patient_df)
    return prediction
