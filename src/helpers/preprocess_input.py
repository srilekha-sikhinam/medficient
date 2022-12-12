import pandas as pd

def clean_input(input_feature_arr, options):
    patient_info_df = pd.DataFrame(columns=input_feature_arr.keys())
    patient_info_df = patient_info_df.append(input_feature_arr, ignore_index=True)
    patient_info_df['Permanent Facility Id'] = patient_info_df['Permanent Facility Id'].astype('float64')
    patient_info_df['CCSR Diagnosis Code'] = patient_info_df['CCSR Diagnosis Code'].astype('int64')
    patient_info_df['CCSR Procedure Code'] = patient_info_df['CCSR Procedure Code'].astype('int64')
    patient_info_df['Age Group'] = encode_age(input_feature_arr['Age Group'])
    patient_info_df['APR Risk of Mortality'] = encode_risk_of_mortality(input_feature_arr['APR Risk of Mortality'])
    patient_info_df['APR Severity of Illness Code'] = encode_risk_of_mortality(input_feature_arr['APR Severity of Illness Code'])
    patient_info_df['Emergency Department Indicator'] = get_er_dept_indicator(input_feature_arr['Emergency Department Indicator'])
    categorical_columns = list(patient_info_df.select_dtypes(include='object'))
    for col in categorical_columns:
        col_to_append = get_encoded_columns(col, input_feature_arr[col], options[col])
        patient_info_df = pd.concat([patient_info_df, col_to_append], axis=1)
    patient_info_df = patient_info_df.loc[:, ~patient_info_df.columns.isin(categorical_columns)]
    return patient_info_df

def encode_age(age_cat):
    if age_cat == '0 to 17':
        return 1
    elif age_cat == '18 to 29':
        return 2
    elif age_cat == '30 to 49':
        return 3
    elif age_cat == '50 to 69':
        return 4
    elif age_cat == '70 or Older':
        return 5

def encode_risk_of_mortality(risk):
    if risk == 'Minor':
        return 1
    if risk == 'Moderate':
        return 2
    if risk == 'Major':
        return 3
    if risk == 'Extreme':
        return 4

def get_er_dept_indicator(er_indicator):
    if er_indicator == 'Yes':
        return 1
    else:
        return 0

def get_encoded_columns(col, new_inputs, options):
    #Remove new_inputs from options
    options.remove(new_inputs)
    df_dummies = pd.get_dummies(list([new_inputs]) + options, prefix=col).head(1)
    return df_dummies
