#This file trains all the models based on the best parameters we found earlier and saves
# the models as pickle files
import sys
import platform
plat = platform.system()
if plat == 'Windows':
    sys.path.insert(0, 'src\helpers')
    sys.path.insert(0, 'src\models')
elif plat =='Linux' or plat=='Darwin':
    sys.path.insert(0, 'src/helpers')
    sys.path.insert(0, 'src/models')
from data_processing import *
from data_cleaners import *
from model_building_helpers import *
import pandas as pd

model_folder = 'models'
data_file_path = 'data'

def train_all_pop_model(best_params):
    df = load_data('all', data_file_path)
    bins = [1, 5000, 10000, 15000, 20000, 30000, 50000, 1250000]
    labels = ['1 - 5000', '5001 - 10000', '10001 - 15000', '15001 - 20000'
          , '20001 - 30000', '30001 - 50000', '50001 - 1250000']
    df['Total Costs Bin'] = pd.cut(x = df['Total Costs'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_cost_train_test_data(df)
    if plat == 'Windows':
        filename = '\\all_pop_cost_model.pkl'
    elif plat =='Linux' or plat=='Darwin':
        filename = '//all_pop_cost_model.pkl'
    model = train_cost_model(best_params, X_train, y_train, model_folder + filename)


def train_heart_patient_model(best_params):
    df = load_data(194.0, data_file_path)
    bins = [1, 5000, 10000, 15000, 20000, 30000, 50000, 1250000]
    labels = ['1 - 5000', '5001 - 10000', '10001 - 15000', '15001 - 20000'
          , '20001 - 30000', '30001 - 50000', '50001 - 1250000']
    df['Total Costs Bin'] = pd.cut(x = df['Total Costs'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_cost_train_test_data(df)
    if plat == 'Windows':
        filename = '\\heart_patient_cost_model.pkl'
    elif plat =='Linux' or plat=='Darwin':
        filename = '//heart_patient_cost_model.pkl'
    model = train_cost_model(best_params, X_train, y_train, model_folder + filename)

def train_knee_rep_patient_model(best_params):
    df = load_data(302.0, data_file_path)
    bins = [1, 5000, 10000, 15000, 20000, 30000, 50000, 1250000]
    labels = ['1 - 5000', '5001 - 10000', '10001 - 15000', '15001 - 20000'
          , '20001 - 30000', '30001 - 50000', '50001 - 1250000']
    df['Total Costs Bin'] = pd.cut(x = df['Total Costs'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_cost_train_test_data(df)
        if plat == 'Windows':
        filename = '\\knee_rep_patient_cost_model.pkl'
    elif plat =='Linux' or plat=='Darwin':
        filename = '//knee_rep_patient_cost_model.pkl'
    model = train_cost_model(best_params, X_train, y_train, model_folder + filename)

def train_kidney_patient_model(best_params):
    df = load_data(463.0, data_file_path)
    bins = [1, 5000, 10000, 15000, 20000, 30000, 50000, 1250000]
    labels = ['1 - 5000', '5001 - 10000', '10001 - 15000', '15001 - 20000'
          , '20001 - 30000', '30001 - 50000', '50001 - 1250000']
    df['Total Costs Bin'] = pd.cut(x = df['Total Costs'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_cost_train_test_data(df)
        if plat == 'Windows':
        filename = '\\kidney_patient_cost_model.pkl'
    elif plat =='Linux' or plat=='Darwin':
        filename = '//kidney_patient_cost_model.pkl'
    model = train_cost_model(best_params, X_train, y_train, model_folder + filename)


def train_schizophrenia_patient_model(best_params):
    df = load_data(750.0, data_file_path)
    bins = [1, 5000, 10000, 15000, 20000, 30000, 50000, 1250000]
    labels = ['1 - 5000', '5001 - 10000', '10001 - 15000', '15001 - 20000'
          , '20001 - 30000', '30001 - 50000', '50001 - 1250000']
    df['Total Costs Bin'] = pd.cut(x = df['Total Costs'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_cost_train_test_data(df)
        if plat == 'Windows':
        filename = '\\schizophrenia_patient_cost_model.pkl'
    elif plat =='Linux' or plat=='Darwin':
        filename = '//schizophrenia_patient_cost_model.pkl'
    model = train_cost_model(best_params, X_train, y_train, model_folder + filename)


def train_copd_patient_model(best_params):
    df = load_data(140.0, data_file_path)
    bins = [1, 5000, 10000, 15000, 20000, 30000, 50000, 1250000]
    labels = ['1 - 5000', '5001 - 10000', '10001 - 15000', '15001 - 20000'
          , '20001 - 30000', '30001 - 50000', '50001 - 1250000']
    df['Total Costs Bin'] = pd.cut(x = df['Total Costs'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_cost_train_test_data(df)
        if plat == 'Windows':
        filename = '\\copd_patient_cost_model.pkl'
    elif plat =='Linux' or plat=='Darwin':
        filename = '//copd_patient_cost_model.pkl'
    model = train_cost_model(best_params, X_train, y_train, model_folder + filename)

if __name__ == "__main__":
    best_params = {
        'all': {'min_samples_leaf': 4, 'max_depth': 30, 'loss': 'log_loss', 'learning_rate': 0.1},
        194.0: {'min_samples_leaf': 4, 'max_depth': 100, 'loss': 'log_loss', 'learning_rate': 0.1},
        140.0: {'min_samples_leaf': 4, 'max_depth': 110, 'loss': 'auto', 'learning_rate': 0.5},
        750.0: {'min_samples_leaf': 2, 'max_depth': 100, 'loss': 'log_loss', 'learning_rate': 0.1},
        463.0: {'min_samples_leaf': 2, 'max_depth': 110, 'loss': 'categorical_crossentropy', 'learning_rate': 0.1},
        302.0: {'min_samples_leaf': 4, 'max_depth': 50, 'loss': 'log_loss', 'learning_rate': 0.1}
    }
    #train_all_pop_model(best_params['all'])
    #train_heart_patient_model(best_params[194.0])
    #train_copd_patient_model(best_params[140.0])
    #train_schizophrenia_patient_model(best_params[750.0])
    #train_kidney_patient_model(best_params[463.0])
    train_knee_rep_patient_model(best_params[302.0])
