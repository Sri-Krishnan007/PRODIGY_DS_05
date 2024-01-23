# Import necessary libraries
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
# Update the file path to the correct location on your machine
file_path = 'C:/Users/srikr/Desktop/COLLEGE/Extra/AccidentsBig.csv'
df_acc = pd.read_csv(file_path)

# Display basic information about the dataset
print(df_acc.info())

# Explore the first few rows of the dataset
print(df_acc.head())

# Check for missing values
print(df_acc.isnull().sum())

# Convert the 'Time' column to datetime objects
df_acc['Time'] = pd.to_datetime(df_acc['Time'])

# Extract information about the day of the week, month, and hour of the accident
df_acc['Day_of_Week'] = df_acc['Time'].dt.dayofweek
df_acc['Month'] = df_acc['Time'].dt.month
df_acc['Hour'] = df_acc['Time'].dt.hour

# Visualize accidents by day of the week
sns.countplot(x='Day_of_Week', data=df_acc)
plt.title('Accidents by Day of the Week')
plt.show()

# Visualize accidents by month
sns.countplot(x='Month', data=df_acc)
plt.title('Accidents by Month')
plt.show()

# Visualize accidents by hour of the day
sns.countplot(x='Hour', data=df_acc)
plt.title('Accidents by Hour of the Day')
plt.show()

# Visualize accidents by road conditions
sns.countplot(x='Weather_Conditions', data=df_acc, order=df_acc['Weather_Conditions'].value_counts().index)
plt.title('Accidents by Weather Conditions')
plt.xticks(rotation=90)
plt.show()

# Visualize accidents by severity
sns.countplot(x='Accident_Severity', data=df_acc)
plt.title('Accident Severity')
plt.show()

# Visualize accident hotspots on a map (if latitude and longitude columns are available)
plt.scatter(df_acc['longitude'], df_acc['latitude'], alpha=0.1)
plt.title('Accident Hotspots')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
