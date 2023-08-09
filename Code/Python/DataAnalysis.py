# For Data
import pandas as pd
import numpy as np
# For Plotting
import matplotlib.pyplot as plt
import seaborn as sns
# For Geospatial Analysis
import webbrowser
from geopy.geocoders import Nominatim
import geopandas as gpd
import folium
# for machine learning
from sklearn import preprocessing, cluster
import scipy


# Read in the data
data = pd.read_csv("Data/Rodent_Inspection-4_cleaned.csv")

# Check the data
print(data.head())

# Filter for 2022
data1 = data[data['INSPECTION_DATE'].str.contains('2021', '2022')]

# Create a map of the rodent inspections
# Create a map of NYC
map = folium.Map(location=[40.7128, -74.0060], tiles='cartodbpositron', zoom_start=12)

# Add points to the map
# Iterate over each row in the DataFrame
for index, row in data1.iterrows():
    # Extract latitude and longitude values
    latitude = float(row['LATITUDE'])
    longitude = float(row['LONGITUDE'])

    # Create a CircleMarker for each location
    folium.CircleMarker([latitude, longitude],
                        radius=15,
                        popup=row['INSPECTION_TYPE'],
                        fill_color="#3db7e4",
                       ).add_to(map)


# Display the map
map.save('Data/rodent_map.html')
map.show_in_browser


### Create a new dataset for inspection type and result based on zip code ###
# Read in the data
data = pd.read_csv("Data/Rodent_Inspection-4_cleaned.csv")

# create a new dataset for inspection type and result based on zip code and year
RealRodentData = data[['ZIP_CODE', 'INSPECTION_TYPE', 'RESULT', 'INSPECTION_DATE']]
print(RealRodentData.head())

# Display the data
RealRodentData.to_csv("Data/RealRodentData.csv", index=False)

