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