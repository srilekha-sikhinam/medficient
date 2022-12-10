import pandas as pd
import numpy as np

#Gets the dataset for the correct code and returns it as a dataframe
def get_subpop_file(drg_code):
    print(drg_code)
    if drg_code == 194.0:
        df = pd.read_csv('data/processed/HID_cleaned_HeartFailure.csv')
        return df
    elif drg_code == 140.0:
        df = pd.read_csv('data/processed/HID_cleaned_ChronicObstructivePulmonaryDisease.csv')
        return df
    elif drg_code == 750.0:
        df = pd.read_csv('data/processed/HID_cleaned_Schizophrenia.csv')
        return df
    elif drg_code == 463.0:
        df = pd.read_csv('data/processed/HID_cleaned_Kidney&UrinaryTractInfections.csv')
        return df
    elif drg_code == 302.0:
        df = pd.read_csv('data/processed/HID_cleaned_KneeJointReplacement.csv')
        return df
    else:
        df = pd.read_csv('data/processed/Hospital_Inpatient_Discharges_17_18_cleaned.csv')
        return df

def encode_ordinal_variables(df):
    #Encode age category as ordinal labels with youngest age group being the lowest value
    age_to_encode = {'0 to 17': 1, '18 to 29': 2, '30 to 49': 3, '50 to 69': 4, '70 or Older': 5}
    risk_of_mortality_to_encode = {'Minor': 1, 'Moderate': 2, 'Major': 3, 'Extreme': 4}

    df['Age Group'].replace(age_to_encode, inplace=True)
    df['APR Risk of Mortality'].replace(risk_of_mortality_to_encode, inplace=True)

    return df

def fill_nan_values(df):
    df['CCSR Diagnosis Code'].replace(to_replace="^[A-Z]\w+", value=np.nan, regex=True, inplace=True)
    df['CCSR Procedure Code'].replace(to_replace="^[A-Z]\w+", value=np.nan, regex=True, inplace=True)
    df.fillna(df.mode().iloc[0], inplace=True)
    return df

def convert_column_data_types(df):
    #Convert float columns to integers
    for column in list(df.select_dtypes(include='float64')):
        df[column] = df[column].astype('int64')
    df['CCSR Diagnosis Code'] = df['CCSR Diagnosis Code'].astype('int64')
    df['CCSR Procedure Code'] = df['CCSR Procedure Code'].astype('int64')
    return df

#Return the correct dataframe
def load_data(drg_code):
    filename = get_subpop_file(drg_code)
    print(filename)
    df = get_subpop_file(drg_code)
#     df.drop(columns=['APR DRG Description', 'Patient Disposition'], inplace=True)
    df = encode_ordinal_variables(df)
    df = fill_nan_values(df)
    df = convert_column_data_types(df)
    return df