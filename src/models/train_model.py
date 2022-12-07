#This file trains all the models based on the best parameters we found earlier and saves
# the models as pickle files
import sys
sys.path.insert(0, '..\helpers')
sys.path.insert(0, '..\models')
from data_cleaners import *
from model_building_helpers import *

model_folder = '..\..\models'

def train_all_pop_model(best_params):
    df = load_data('all')
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\all_pop_rf_model.pkl')


def train_heart_patient_model(best_params):
    df = load_data(194.0)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\heart_patient_rf_model.pkl')


def train_knee_rep_patient_model(best_params):
    df = load_data(302.0)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\knee_rep_patient_rf_model.pkl')


def train_kidney_patient_model(best_params):
    df = load_data(463.0)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\kidney_patient_rf_model.pkl')


def train_schizophrenia_patient_model(best_params):
    df = load_data(750.0)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\schizophrenia_patient_rf_model.pkl')


def train_copd_patient_model(best_params):
    df = load_data(140.0)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\copd_patient_rf_model.pkl')

if __name__ == "__main__":
    best_params = {
        'all': {'n_estimators': 650, 'min_samples_split': 5, 'min_samples_leaf': 2, 'max_depth': 110, 'class_weight': 'balanced', 'bootstrap': True},
        194.0: {'n_estimators': 750, 'min_samples_split': 5, 'min_samples_leaf': 2, 'max_depth': 90, 'class_weight': 'balanced_subsample', 'bootstrap': True},
        140.0: {'n_estimators': 200, 'min_samples_split': 2, 'min_samples_leaf': 4, 'max_depth': 40, 'class_weight': 'balanced_subsample', 'bootstrap': True},
        750.0: {'n_estimators': 650, 'min_samples_split': 10, 'min_samples_leaf': 2, 'max_depth': 40, 'class_weight': 'balanced', 'bootstrap': True},
        463.0: {'n_estimators': 500, 'min_samples_split': 2, 'min_samples_leaf': 2, 'max_depth': 20, 'class_weight': 'balanced', 'bootstrap': True},
        302.0: {'n_estimators': 300, 'min_samples_split': 5, 'min_samples_leaf': 4, 'max_depth': 100, 'class_weight': 'balanced', 'bootstrap': True}
    }
    train_all_pop_model(best_params['all'])
    train_heart_patient_model(best_params[194.0])
    train_copd_patient_model(best_params[140.0])
    train_schizophrenia_patient_model(best_params[750.0])
    train_kidney_patient_model(best_params[463.0])
    train_knee_rep_patient_model(best_params[302.0])
