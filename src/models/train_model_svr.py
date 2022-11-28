#Import statements for entire notebook
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.compose import TransformedTargetRegressor
from sklearn.svm import SVR
import pickle

#Load in the data
df = pd.read_csv('data\processed\Hospital_Inpatient_Discharges_17_18_cleaned.csv')
df.head()

#Reduce sample for training
sample_df = df.copy()

#Fill na with most common values
sample_df = sample_df.fillna(sample_df.mode().iloc[0])

sample_df_heart_failure = sample_df[(sample_df['APR DRG Description'].str.startswith('Heart')) | (sample_df['APR DRG Code'] == 194)]

X = sample_df_heart_failure.loc[:, ~sample_df.columns.isin(['Length of Stay', 'Total Costs', 'Total Charges'])]
y = sample_df_heart_failure[['Length of Stay']]

curr_columns = X.columns

X = pd.get_dummies(X)

X = X.loc[:, ~X.columns.isin(curr_columns)]

X_train_all_features, X_test_all_features, y_train_all_features, y_test_all_features = train_test_split(X, y, test_size = 0.25)


y['Length of Stay'] = y['Length of Stay'].astype('float64')


tt2 = TransformedTargetRegressor(regressor=SVR(kernel='rbf', degree=3, gamma='scale', coef0=0.01, C=1), func=np.log, inverse_func=np.exp)
tt2.fit(X_test_all_features, y_test_all_features)

filename = 'models/finalized_length_of_stay_svr_model'
pickle.dump(tt2, open(filename, 'wb'))