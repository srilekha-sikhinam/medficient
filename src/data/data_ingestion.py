<<<<<<< HEAD
import pandas as pd

############################### DATA INGESTION ################################

# Import the two datasets 
df_18 = pd.read_csv('data/raw/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2018.csv')
df_17 = pd.read_csv('data/raw/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2017.csv')

# Look at the column names for the '18 dataset
print('18 Dataset')
print(list(df_18.columns), '\n')

# Look at the column names for the '18 dataset
print('17 Dataset')
print(list(df_17.columns), '\n')

# Take the symmetric difference of the column labels to see if they're the same
print('Column Differences:')
print(df_18.columns ^ df_17.columns, '\n')

# Based on this, we see that the '17 df has a field called 'Abortion Edit Indicator', 
# while four other column headers differ by one letter. We'll create a commensurate 
# field in the '18 field set, and we'll rename the four in '17 to replicate the '18 df.

# Create 'Abortion Edit Indicator' column in '18 df
df_18['Abortion Edit Indicator'] = ""

# Rename columns in the '17 set to match the '18 set
df_17.rename(columns = {'CCS Diagnosis Code': 'CCSR Diagnosis Code', 
                        'CCS Diagnosis Description': 'CCSR Diagnosis Description',
                        'CCS Procedure Code': 'CCSR Procedure Code',
                        'CCS Procedure Description': 'CCSR Procedure Description'},
                        inplace = True)

# Rerun the symmetric difference to ensure the columns are the same
print('Column Differences Post-Change:')
print(df_18.columns ^ df_17.columns, '\n')

# Looks like we're good to go here! The columns are the same between the two 
# datasets, so now we can union them.

# Union the datasets
df = pd.concat([df_17, df_18])

# Print the shape of this dataset
print('Concatenated dataset shape:')
print(df.shape, '\n')

################################ DATA EXPORT ##################################

# Write to a csv 
df.to_csv('data/processed/Hospital_Inpatient_Discharges_17_18.csv', index = False)

# Print export note
print('Data Extracted')
=======
import pandas as pd

############################### DATA INGESTION ################################

# Import the two datasets 
df_18 = pd.read_csv('Hospital_Inpatient_Discharges__SPARCS_De-Identified___2018.csv')
df_17 = pd.read_csv('Hospital_Inpatient_Discharges__SPARCS_De-Identified___2017.csv')

# Look at the column names for the '18 dataset
print('18 Dataset')
print(list(df_18.columns), '\n')

# Look at the column names for the '18 dataset
print('17 Dataset')
print(list(df_17.columns), '\n')

# Take the symmetric difference of the column labels to see if they're the same
print('Column Differences:')
print(df_18.columns ^ df_17.columns, '\n')

# Based on this, we see that the '17 df has a field called 'Abortion Edit Indicator', 
# while four other column headers differ by one letter. We'll create a commensurate 
# field in the '18 field set, and we'll rename the four in '17 to replicate the '18 df.

# Create 'Abortion Edit Indicator' column in '18 df
df_18['Abortion Edit Indicator'] = ""

# Rename columns in the '17 set to match the '18 set
df_17.rename(columns = {'CCS Diagnosis Code': 'CCSR Diagnosis Code', 
                        'CCS Diagnosis Description': 'CCSR Diagnosis Description',
                        'CCS Procedure Code': 'CCSR Procedure Code',
                        'CCS Procedure Description': 'CCSR Procedure Description'},
                        inplace = True)

# Rerun the symmetric difference to ensure the columns are the same
print('Column Differences Post-Change:')
print(df_18.columns ^ df_17.columns, '\n')

# Looks like we're good to go here! The columns are the same between the two 
# datasets, so now we can union them.

# Union the datasets
df = pd.concat([df_17, df_18])

# Print the shape of this dataset
print('Concatenated dataset shape:')
print(df.shape, '\n')

################################ DATA EXPORT ##################################

# Write to a csv 
df.to_csv('Hospital_Inpatient_Discharges_17_18.csv', index = False)

# Print export note
print('Data Extracted')
>>>>>>> 247ec2656f15a8ac087580c084bc23ef55f7eb62
