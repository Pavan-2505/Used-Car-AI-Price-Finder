import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

#Load Datasets
df1 = pd.read_csv('train.csv')
df2=pd.read_csv('Car Sell Dataset.csv')

pd.set_option('display.max_columns', None)

#Dataset 1
print("---------FIRST DATASET---------")
print("The Dataset contains", df1.shape[0], "rows and", df1.shape[1], "columns")
df1.info()
print(df1.head())

#Dataset 2
print("\n---------SECOND DATASET---------")
print(f"The Dataset contains {df2.shape[0]} rows and {df2.shape[1]} columns")
df2.info()
print(df2.head())

print("\n---------MISSING VALUES:DATASET 1---------")
missing_df1=df1.isnull().sum()
print(missing_df1)
missing_percentage_df1=(missing_df1/len(df1))*100
print(missing_percentage_df1)

print("\n---------MISSING VALUES: DATASET 2---------")
missing_df2=df2.isnull().sum()
print(missing_df2)
missing_percentage_df2=(missing_df2/len(df2))*100
print(missing_percentage_df2)

print("\n========== INITIAL OBSERVATIONS ==========")

print("Dataset 1 has missing values in Mileage, Engine, Power, Seats and New_Price.")
print("New_Price has the highest amount of missing data in Dataset 1.")
print("Dataset 2 currently has no missing values.")

print("\n========== DUPLICATES: DATASET 1 ==========")
print("Number of duplicate rows in Dataset 1:",df1.duplicated().sum())

print("\n========== DUPLICATES: DATASET 2 ==========")
print("Number of duplicate rows in Dataset 2:",df2.duplicated().sum())

print("\n========== POSSIBLE INVALID VALUES: DATASET 1=========")
print(f"Year Range: {df1['Year'].min()} to {df1['Year'].max()}")
print(f"Kilometers driven range: {df1['Kilometers_Driven'].min()} to {df1['Kilometers_Driven'].max()}")
print(f"Seats Range: {df1['Seats'].min()} to {df1['Seats'].max()}")
print(f"Price Range: {df1['Price'].min()} to {df1['Price'].max()}")

print("\n========== POSSIBLE INVALID VALUES: DATASET 2========")
print(f"Year Range: {df2['Year'].min()} to {df2['Year'].max()}")
print(f"Kilometers driven range: {df2['Kilometers'].min()} to {df2['Kilometers'].max()}")
print(f"Price Range: {df2['Price'].min()} to {df2['Price'].max()}")

print(df1[df1['Kilometers_Driven']==df1['Kilometers_Driven'].max()])
print(df1[['Name', 'Year', 'Kilometers_Driven', 'Price']]
      .sort_values('Kilometers_Driven', ascending=False)
      .head(10))

print("\n========== EXTREME KILOMETER VALUES: DATASET 1 ==========")
print("Above 200,000 km:",(df1['Kilometers_Driven'] > 200000).sum())
print("Above 300,000 km:",(df1['Kilometers_Driven'] > 300000).sum())
print("Above 500,000 km:",(df1['Kilometers_Driven'] > 500000).sum())
print("Above 1,000,000 km:",(df1['Kilometers_Driven'] > 1000000).sum())

print("\n KILOMOETER SUMMARY")
print(df1['Kilometers_Driven'].describe())

print("\n========== UNIQUE VALUES: DATASET 1 ==========")

print("\nFuel Type:")
print(df1['Fuel_Type'].unique())

print("\nTransmission:")
print(df1['Transmission'].unique())

print("\nOwner Type:")
print(df1['Owner_Type'].unique())

print("\n========== UNIQUE VALUES: DATASET 2=========")
print(f"Fuel Type: {df2['Fuel Type'].unique()}")
print(f"Transmission: {df2['Transmission'].unique()}")
print(f"Owner: {df2['Owner'].unique()}")
print(f"Accidental: {df2['Accidental'].unique()}")

print("\n========== LOCATION VALUES: DATASET 1 ==========")
print(f"Number of unique locations: {df1['Location'].nunique()}")
print(df1['Location'].unique())

print("\n========== STATE VALUES: DATASET 2 ==========")
print(f"Number of unique states: {df2['State'].nunique()}")
print(df2['State'].unique())

print("\n========== TEXT AND UNIT INSPECTION: DATASET 1 ==========")
print("\nMileage examples:")
print(df1['Mileage'].dropna().head(10).to_list())
print("\nEngine examples:")
print(df1['Engine'].dropna().head(10).to_list())
print("\nPower examples:")
print(df1['Power'].dropna().head(10).to_list())
print("\nNew Price examples:")
print(df1['New_Price'].dropna().head(10).to_list())

print("\n========== MILEAGE UNIT COUNTS ==========")
print(df1['Mileage'].dropna().str.extract(r'(kmpl|km/kg)', expand=False).value_counts())

print("\n========== KM/KG MILEAGE VALUES ==========")
print(df1[df1['Mileage'].str.contains('km/kg', na=False)]['Mileage'].unique())

print("\n========== MILEAGE UNIQUE UNITS ==========")

print(df1['Mileage'].dropna().str.extract(r'([A-Za-z/]+)', expand=False).value_counts())

print("\n========== KM/KG CARS ==========")
print(df1[df1['Mileage'].str.contains('km/kg', na=False)][['Name', 'Fuel_Type', 'Mileage']])

print("\n========== FULL DETAILS OF KM/KG RECORDS ==========")
print(df1[df1['Mileage'].str.contains('km/kg', na=False)].to_string())

print("\n========== Power Unit Check ==========")
print(df1['Power'].dropna().str.extract(r'([A-Za-z]+)',expand=False).value_counts())

print("\n========== Power Value Range =========")
power_numeric=pd.to_numeric(df1['Power'].str.replace('bhp','',regex=False), errors='coerce')
print(f"Maximum Power: {power_numeric.max()}")
print(f"Minimum Power: {power_numeric.min()}")

print("\n========== POWER SUMMARY ==========")
print(power_numeric.describe())

print("\n========== HIGHEST POWER CARS ==========")
print(df1.assign(Power_Numeric=power_numeric)[['Name', 'Year', 'Power', 'Power_Numeric']].sort_values('Power_Numeric', ascending=False).head(10))

df1['Power_Clean']=pd.to_numeric(df1['Power'].str.replace('bhp','',regex=False),errors='coerce')

print("\n========== CLEANED POWER ==========")
print(df1[['Power', 'Power_Clean']].head(10))
print("\nData type:")
print(df1['Power_Clean'].dtype)
print("\nMissing values:")
print(df1['Power_Clean'].isnull().sum())

print("\n========== Engine Unit Check ==========")
print(df1['Engine'].dropna().str.extract(r'([A-Za-z]+)',expand=False).value_counts())

print("\n========== Engine Value Range =========")
engine_numeric=pd.to_numeric(df1['Engine'].str.replace('CC','',regex=False), errors='coerce')
print(f"Maximum Engine: {engine_numeric.max()}")
print(f"Minimum Engine: {engine_numeric.min()}")

print("\n========== ENGINE SUMMARY ==========")
print(engine_numeric.describe())

print("\n========== HIGHEST ENGINE CARS ==========")
print(df1.assign(Engine_Numeric=engine_numeric)[['Name', 'Year', 'Engine', 'Engine_Numeric']].sort_values('Engine_Numeric', ascending=False).head(10))

df1['Engine_Clean'] = pd.to_numeric(df1['Engine'].str.replace(' CC', '', regex=False),errors='coerce')

print("\n========== CLEANED ENGINE ==========")
print(df1[['Engine', 'Engine_Clean']].head(10))
print("\nData type:")
print(df1['Engine_Clean'].dtype)
print("\nMissing values:")
print(df1['Engine_Clean'].isnull().sum())