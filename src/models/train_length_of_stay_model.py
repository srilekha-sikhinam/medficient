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
from data_cleaners import *
from model_building_helpers import *

model_folder = 'models'
bins = [1, 5, 15, 30, 45, 60, 90, 120]
labels = ['1 to 5', '6 to 15', '16 to 30', '31 to 45', '46 to 60', '60 to 90', '90 to 120']
data_file_path = 'data'

def train_all_pop_model(best_params):
    print('Training all patient model')
    df = load_data('all', data_file_path)
    df['Length of Stay Bin'] = pd.cut(x = df['Length of Stay'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\all_pop_rf_model.pkl')


def train_heart_patient_model(best_params):
    print('Training heart patient model')
    df = load_data(194.0, data_file_path)
    df['Length of Stay Bin'] = pd.cut(x = df['Length of Stay'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\heart_patient_rf_model.pkl')


def train_knee_rep_patient_model(best_params):
    print('Training knee rep model')
    df = load_data(302.0, data_file_path)
    df['Length of Stay Bin'] = pd.cut(x = df['Length of Stay'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\knee_rep_patient_rf_model.pkl')


def train_kidney_patient_model(best_params):
    print('Training kidney patient model')
    df = load_data(463.0, data_file_path)
    df['Length of Stay Bin'] = pd.cut(x = df['Length of Stay'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\kidney_patient_rf_model.pkl')


def train_schizophrenia_patient_model(best_params):
    print('Training schizophrenia patient model')
    df = load_data(750.0, data_file_path)
    df['Length of Stay Bin'] = pd.cut(x = df['Length of Stay'], bins = bins, labels = labels, include_lowest = True)
    X, y, X_train, X_test, y_train, y_test = get_train_test_data(df)
    model = train_model(best_params, X_train, y_train, model_folder + '\\schizophrenia_patient_rf_model.pkl')


def train_copd_patient_model(best_params):
    print('Training COPD patient model')
    df = load_data(140.0, data_file_path)
    df['Length of Stay Bin'] = pd.cut(x = df['Length of Stay'], bins = bins, labels = labels, include_lowest = True)
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
    #train_all_pop_model(best_params['all'])
    #train_heart_patient_model(best_params[194.0])
    #train_copd_patient_model(best_params[140.0])
    #train_schizophrenia_patient_model(best_params[750.0])
    #train_kidney_patient_model(best_params[463.0])
    train_knee_rep_patient_model(best_params[302.0])
