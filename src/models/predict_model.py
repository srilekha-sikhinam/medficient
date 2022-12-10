import sys
sys.path.insert(0, '..\src\helpers')
sys.path.insert(0, '..\src\models')

import pandas as pd
import numpy as np
import _pickle as cpickle
from preprocess_input import *

def get_prediction(input_feature_arr, options):
    patient_df = clean_input(input_feature_arr, options)
    los_model = cpickle.load(open('models\knee_rep_patient_rf_model.pkl', 'rb'))
    cost_model = cpickle.load(open('models\knee_rep_patient_cost_model.pkl', 'rb'))
    los_prediction = los_model.predict(patient_df)
    cost_prediction = cost_model.predict(patient_df)
    return [los_prediction, cost_prediction]
