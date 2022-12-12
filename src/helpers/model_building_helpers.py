#Import all needed models
import pandas as pd
import numpy as np
import _pickle as cpickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV
from sklearn.dummy import DummyClassifier
from sklearn.metrics import log_loss, f1_score, classification_report, make_scorer, precision_score, recall_score, accuracy_score, confusion_matrix, plot_confusion_matrix


#Encodes variables and returns the train/test sets with the correct columns and encodings
def get_train_test_data(df):
    X = df.loc[:, ~df.columns.isin(['Length of Stay', 'Total Costs', 'Total Charges', 'Length of Stay Bin'])]
    y = df[['Length of Stay Bin']]

    categorical_columns = list(df.select_dtypes(include='object'))

    X = pd.get_dummies(X)

    X = X.loc[:, ~X.columns.isin(categorical_columns)]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

    return X, y, X_train, X_test, y_train, y_test

def get_cost_train_test_data(df):
    df = df.dropna()
    X = df.loc[:, ~df.columns.isin(['Total Costs', 'Total Charges', 'Total Costs Bin','Length of Stay'])]
    y = df[['Total Costs Bin']]

    categorical_columns = list(df.select_dtypes(include='object'))

    X = pd.get_dummies(X)

    X = X.loc[:, ~X.columns.isin(categorical_columns)]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

    return X, y, X_train, X_test, y_train, y_test


#Run randomizedsearch to get the best parameters for RandomForestClassifier
def get_best_rf_params(X_train, y_train, param_grid, iterations):
    cross_val = StratifiedKFold(n_splits=3)
    clf = RandomizedSearchCV(RandomForestClassifier(random_state=42), n_iter=iterations, param_distributions=param_grid, cv = cross_val, scoring='f1_macro', verbose=True, n_jobs=-1)

    clf.fit(X_train, np.ravel(y_train))
    # Fit on data
    best_params = clf.best_params_
    best_score = clf.best_score_
    return best_params, best_score

def get_best_gbc_params(X_train, y_train, param_grid, iterations):
    cross_val = StratifiedKFold(n_splits=3)
    clf = RandomizedSearchCV(HistGradientBoostingClassifier(), n_iter=iterations, param_distributions=param_grid, cv = cross_val, scoring='f1_macro', verbose=True, n_jobs=-1)

    clf.fit(X_train, np.ravel(y_train))
    # Fit on data
    best_params = clf.best_params_
    best_score = clf.best_score_
    return best_params, best_score

#Run randomizedsearch to get the best parameters for LogisticRegression
def get_best_lr_params(X_train, y_train, param_grid, iterations):
    cross_val = StratifiedKFold(n_splits=3)
    clf = RandomizedSearchCV(LogisticRegression(random_state=42, multi_class='ovr', n_jobs=-1), n_iter =iterations, param_distributions=param_grid, cv = cross_val, scoring='f1_macro', verbose=True, n_jobs=-1)

    clf.fit(X_train, np.ravel(y_train))
    # Fit on data
    best_params = clf.best_params_
    best_score = clf.best_score_
    return best_params, best_score


def train_model(best_params, X_train, y_train, model_file_name=None):
    print("Training model")
    model = RandomForestClassifier(n_estimators = best_params['n_estimators'], min_samples_split = best_params['min_samples_split'], min_samples_leaf = best_params['min_samples_leaf'], max_depth = best_params['max_depth'], class_weight = best_params['class_weight'], bootstrap= best_params['bootstrap'])
    model.fit(X_train, np.ravel(y_train))
    if model_file_name != None:
        with open(model_file_name, 'wb') as file:  
            cpickle.dump(model, file)
    return model

def train_cost_model(best_params, X_train, y_train, model_file_name=None):
    print("Training model")
    model = HistGradientBoostingClassifier(max_depth = best_params['max_depth'], learning_rate = best_params['learning_rate'], min_samples_leaf = best_params['min_samples_leaf'], loss = best_params['loss'])
    model.fit(X_train, np.ravel(y_train))
    if model_file_name != None:
        with open(model_file_name, 'wb') as file:  
            cpickle.dump(model, file)
    return model


def calculate_scores(model, X_test, y_test):
    print("Getting model scores")
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1_score_macro = f1_score(y_test, y_pred, average='macro')
    f1_score_weighted = f1_score(y_test, y_pred, average='weighted')
    return [acc, f1_score_macro, f1_score_weighted]


def get_model_scores(best_params, X_train, X_test, y_train, y_test):
    trained_model = train_model(best_params, X_train, y_train)
    model_scores = calculate_scores(trained_model, X_test, y_test)
    return model_scores

def get_cost_model_scores(best_params, X_train, X_test, y_train, y_test):
    trained_model = train_cost_model(best_params, X_train, y_train)
    model_scores = calculate_scores(trained_model, X_test, y_test)
    return model_scores


def train_dummy_model(dummy_type, X_train, y_train):
    dummy_clf = DummyClassifier(strategy=dummy_type)
    dummy_clf.fit(X_train, y_train)
    return dummy_clf

def calculate_dummy_scores(model, X_test, y_test):
    dummy_clf_freq_preds = model.predict(X_test)
    acc = accuracy_score(y_test, dummy_clf_freq_preds)
    f1_score_macro = f1_score(y_test, dummy_clf_freq_preds, average='macro')
    f1_score_weighted = f1_score(y_test, dummy_clf_freq_preds, average='weighted')
    return [acc, f1_score_macro, f1_score_weighted]

def get_dummy_scores(dummy_type, X_train, X_test, y_train, y_test):
    trained_dummy_model = train_dummy_model(dummy_type, X_train, y_train)
    dummy_scores = calculate_dummy_scores(trained_dummy_model, X_test, y_test)
    return dummy_scores