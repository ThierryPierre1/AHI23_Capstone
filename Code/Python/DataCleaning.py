import pandas as pd
import numpy as np

# Read in the data
file_path = "/Users/thierrypierre/Documents/GitHub/AHI23_Capstone/Data/Rodent_Inspection-4.csv"
RodentData = pd.read_csv(file_path)

# Check the data
print(RodentData.head())

# Check the data types
print(RodentData.dtypes)

# Drop missing values
RodentData.dropna(inplace=True)
RodentData.drop(['JOB_TICKET_OR_WORK_ORDER_ID', 'JOB_ID', 'JOB_PROGRESS', 'APPROVED_DATE'], axis=1, inplace=True)

# Drop values that are before 2020
RodentData = RodentData[RodentData['INSPECTION_DATE'].str.contains('2020', '2021')]

# Convert 'LATITUDE' and 'LONGITUDE' to numeric values
RodentData['LATITUDE'] = pd.to_numeric(RodentData['LATITUDE'], errors='coerce')
RodentData['LONGITUDE'] = pd.to_numeric(RodentData['LONGITUDE'], errors='coerce')

# Check the data types
print(RodentData.dtypes)

# how many missing values   
print(RodentData.isnull().sum())

# how many rows and columns
print(RodentData.shape) 

print(RodentData.head())

# Save the cleaned data
RodentData.to_csv("/Users/thierrypierre/Documents/GitHub/AHI23Capstone/Data/Rodent_Inspection-4_cleaned.csv", index=False)


### Idea ###
# create a variable/column that converts the results of each inpsection into a numerical value; 
# For Example: a column for Initial inspections, 
# where a "Passed" result would be = 1, 
# "Rat activity" would be = 2, 
# and "Failed for other R" would be = 3.
# this would be helpful when creating another layer for ARCgis and the SAS frequency tables

# create a variable/column that converts the results of each inpsection into a numerical value;
# Intial Inspection
# Passed = 1
# Rat Activity = 2
# Failed for other R = 3

# Load the cleaned data
CleanRodentData = pd.read_csv("/Users/thierrypierre/Documents/GitHub/AHI23_Capstone/Data/Rodent_Inspection-4_cleaned.csv")

# Check the data types
print(CleanRodentData.dtypes)

# Create a new column for Initial Inspections
CleanRodentData['INITIAL_INSPECTION'] = np.where(CleanRodentData['RESULT'] == 'Passed', 1, np.where(CleanRodentData['RESULT'] == 'Rat Activity', 2, np.where(CleanRodentData['RESULT'] == 'Failed for other R', 3, 0)))

# Check the data types
print(CleanRodentData.dtypes)

# Create a new column for Compliance Inspections
CleanRodentData['COMPLIANCE_INSPECTION'] = np.where(CleanRodentData['RESULT'] == 'Passed', 1, np.where(CleanRodentData['RESULT'] == 'Rat Activity', 2, np.where(CleanRodentData['RESULT'] == 'Failed for other R', 3, 0)))

# Check the data types
print(CleanRodentData.dtypes)

# Save the cleaned data with the new columns to a new csv file
CleanRodentData.to_csv("/Users/thierrypierre/Documents/GitHub/AHI23_Capstone/Data/Rodent_Inspection-4_cleaned.csv", index=False)

# Clean the NYC population data for SAS analysis
# Read in the data
NYC_Population = pd.read_csv("/Users/thierrypierre/Documents/GitHub/AHI23_Capstone/Data/Demographic_Statistics_By_Zip_Code.csv")

# Check the data
print(NYC_Population.head())

# Check the data types
print(NYC_Population.dtypes)

# Drop missing values
NYC_Population.dropna(inplace=True)

# Check for missing values
print(NYC_Population.isnull().sum())

# Save the cleaned data
NYC_Population.to_csv("/Users/thierrypierre/Documents/GitHub/AHI23_Capstone/Data/Demographic_Statistics_By_Zip_Code_cleaned.csv", index=False)