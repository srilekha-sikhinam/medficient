# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:58:29 2022

@author: Mitch.Burke
"""

import pandas as pd

# First, we'll import our unioned dataset (runtime ~45 seconds)
df = pd.read_csv('data\processed\Hospital_Inpatient_Discharges_17_18.csv')

# Take all columns outside of the original index (first column)
df = df.iloc[:, 1:]


# Let's run some observational metrics on this dataset

print('Overall Shape:')
print(df.shape, '\n')

print('Records per year:')
print(df['year'].value_counts(), '\n')

# Show the column names
print('Columns: ')
print(df.columns, '\n')

# View the data types to see if they all make sense
print('Data Types: ')
print(df.dtypes, '\n')

# Count the number of nans in each column
nans = df.isnull().sum()


###############################################################################
# Given that there are a number of columns that have a significant number of 
# records that are null values, we omit these from the dataset. 
cols_to_omit = ['Payment Typology 2'
              , 'Payment Typology 3'
              , 'Birth Weight'
              , 'Abortion Edit Indicator']

df = df.loc[:, ~df.columns.isin(cols_to_omit)]

# After looking at the proposed labels in detail, we will also filter our 
# dataset to only include numeric values. The '120 +' value makes up only a
# very small amount of records. 
df = df[df['Length of Stay'] != '120 +']

# Finally, let's take one last look at the data. We'll clean 
df_head = df.head()
uniq_vals = df.apply(lambda col: col.unique())

print('Data Types: ')
print(df.dtypes, '\n')


##############################################################################
# Using this information, we can format each field individually. We'll gon one
# by one and format those that need changing.

# Proper case
prpr_cols = ['CCSR Diagnosis Description', 'CCSR Procedure Description',
             'APR DRG Description', 'APR MDC Description']

for col in prpr_cols:
    df[col] = df[col].str.title()
    
# Apply actual gender tags to gender column
gend_dict = {'M': 'Male', 'F': 'Female', 'U': 'Unknown'}

df['Gender'] = df['Gender'].map(gend_dict)

# Standardize emergency department indicator
edi_dict = {'N': 0, 'Y': 1, 'True': 1, 'False': 0, True: 1, False: 0}

df['Emergency Department Indicator'] = df['Emergency Department Indicator'].map(edi_dict)

# Finally, we convert certain data types in need of conversion
df['Length of Stay'] = df['Length of Stay'].astype(int)

# As a last step, we'll reorder the columns so that our target variables are 
# all the way to the right
cols_fin = ['year', 'Hospital Service Area', 'Hospital County',
            'Operating Certificate Number', 'Permanent Facility Id',
            'Facility Name', 'Age Group', 'Zip Code - 3 digits', 
            'Gender', 'Race', 'Ethnicity', 'Type of Admission',
            'Patient Disposition', 'Discharge Year', 'CCSR Diagnosis Code',
            'CCSR Diagnosis Description', 'CCSR Procedure Code',
            'CCSR Procedure Description', 'APR DRG Code', 'APR DRG Description',
            'APR MDC Code', 'APR MDC Description', 'APR Severity of Illness Code',
            'APR Severity of Illness Description', 'APR Risk of Mortality',
            'APR Medical Surgical Description', 'Payment Typology 1',
            'Emergency Department Indicator', 'Total Costs', 'Total Charges',
            'Length of Stay']

df = df.loc[:, cols_fin]

unique_vals_fin = df.apply(lambda col: col.unique())

###############################################################################
# Now we can extract the finalized and cleaned dataset
df.to_csv('data\processed\Hospital_Inpatient_Discharges_17_18_cleaned.csv')



