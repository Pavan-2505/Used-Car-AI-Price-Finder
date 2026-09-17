import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

df1 = pd.read_csv('train.csv')
df2 = pd.read_csv('Car Sell Dataset.csv')

pd.set_option('display.max_columns', None)

print("Dataset 1:", df1.shape)
df1.info()
print(df1.head())

print("\nDataset 2:", df2.shape)
df2.info()
print(df2.head())

missing_df1 = df1.isnull().sum()
print("\nMissing values in Dataset 1:")
print(missing_df1)
print((missing_df1 / len(df1)) * 100)

missing_df2 = df2.isnull().sum()
print("\nMissing values in Dataset 2:")
print(missing_df2)
print((missing_df2 / len(df2)) * 100)

print("\nDuplicate rows:")
print("Dataset 1:", df1.duplicated().sum())
print("Dataset 2:", df2.duplicated().sum())

print("\nDataset 1 ranges:")
print("Year:", df1['Year'].min(), "-", df1['Year'].max())
print("Kilometers:", df1['Kilometers_Driven'].min(), "-", df1['Kilometers_Driven'].max())
print("Seats:", df1['Seats'].min(), "-", df1['Seats'].max())
print("Price:", df1['Price'].min(), "-", df1['Price'].max())

print("\nDataset 2 ranges:")
print("Year:", df2['Year'].min(), "-", df2['Year'].max())
print("Kilometers:", df2['Kilometers'].min(), "-", df2['Kilometers'].max())
print("Price:", df2['Price'].min(), "-", df2['Price'].max())

print("\nHighest kilometers driven:")
print(df1[['Name', 'Year', 'Kilometers_Driven', 'Price']].sort_values('Kilometers_Driven', ascending=False).head(10))

print("\nExtreme kilometer values:")
print("Above 200000:", (df1['Kilometers_Driven'] > 200000).sum())
print("Above 300000:", (df1['Kilometers_Driven'] > 300000).sum())
print("Above 500000:", (df1['Kilometers_Driven'] > 500000).sum())
print("Above 1000000:", (df1['Kilometers_Driven'] > 1000000).sum())
print(df1['Kilometers_Driven'].describe())

print("\nDataset 1:")
print("Fuel:", df1['Fuel_Type'].unique())
print("Transmission:", df1['Transmission'].unique())
print("Owner:", df1['Owner_Type'].unique())
print("Locations:", df1['Location'].unique())

print("\nDataset 2:")
print("Fuel:", df2['Fuel Type'].unique())
print("Transmission:", df2['Transmission'].unique())
print("Owner:", df2['Owner'].unique())
print("Accidental:", df2['Accidental'].unique())
print("States:", df2['State'].unique())

print("\nMileage:")
print(df1['Mileage'].dropna().head(10).to_list())
print(df1['Mileage'].dropna().str.extract(r'(kmpl|km/kg)', expand=False).value_counts())
print(df1[df1['Mileage'].str.contains('km/kg', na=False)][['Name', 'Year', 'Fuel_Type', 'Mileage', 'Price']])

print("\nEngine:")
print(df1['Engine'].dropna().head(10).to_list())
print(df1['Engine'].dropna().str.extract(r'([A-Za-z]+)', expand=False).value_counts())

engine_numeric = pd.to_numeric(df1['Engine'].str.replace('CC', '', regex=False),errors='coerce')

print(engine_numeric.describe())

print(df1.assign(Engine_Numeric=engine_numeric)[['Name', 'Year', 'Engine', 'Engine_Numeric']].sort_values('Engine_Numeric', ascending=False).head(10))

df1['Engine_Clean'] = pd.to_numeric(df1['Engine'].str.replace(' CC', '', regex=False),errors='coerce')

print(df1[['Engine', 'Engine_Clean']].head(10))
print(df1['Engine_Clean'].dtype)
print(df1['Engine_Clean'].isnull().sum())

print("\nPower:")
print(df1['Power'].dropna().str.extract(r'([A-Za-z]+)', expand=False).value_counts())

power_numeric = pd.to_numeric(df1['Power'].str.replace('bhp', '', regex=False),errors='coerce')

print(power_numeric.describe())

print(df1.assign(Power_Numeric=power_numeric)[['Name', 'Year', 'Power', 'Power_Numeric']].sort_values('Power_Numeric', ascending=False).head(10))

df1['Power_Clean'] = pd.to_numeric(df1['Power'].str.replace('bhp', '', regex=False),errors='coerce')

print(df1[['Power', 'Power_Clean']].head(10))
print(df1['Power_Clean'].dtype)
print(df1['Power_Clean'].isnull().sum())

print("\nNew Price:")
print(df1['New_Price'].dropna().str.extract(r'([A-Za-z]+)', expand=False).value_counts())

print(df1[df1['New_Price'].str.contains('Cr', na=False)][['Name', 'Year', 'New_Price', 'Price']])

lakh = pd.to_numeric(df1.loc[df1['New_Price'].str.contains('Lakh', na=False),'New_Price'].str.replace(' Lakh', '', regex=False),errors='coerce')

crore = pd.to_numeric(df1.loc[df1['New_Price'].str.contains('Cr', na=False),'New_Price'].str.replace(' Cr', '', regex=False),errors='coerce')

print("\nLakh:")
print(lakh.describe())

print("\nCrore:")
print(crore.describe())

print("\nNew Price and Price:")
print(df1[['Name', 'Year', 'New_Price', 'Price']].dropna(subset=['New_Price']).head(20))

new_price_clean = df1['New_Price'].copy()
new_price_clean = new_price_clean.str.replace(' Lakh', '', regex=False)
new_price_clean = new_price_clean.str.replace(' Cr', '', regex=False)
new_price_clean = pd.to_numeric(new_price_clean, errors='coerce')

new_price_clean[df1['New_Price'].str.contains('Cr', na=False)] *= 100

df1['New_Price_Clean'] = new_price_clean

print("\nCleaned New Price:")
print(df1[['New_Price', 'New_Price_Clean']].dropna(subset=['New_Price']).head(20))

print(df1['New_Price_Clean'].dtype)
print(df1['New_Price_Clean'].isnull().sum())

print("\nCrore conversion:")
print(df1[df1['New_Price'].str.contains('Cr', na=False)][['Name', 'New_Price', 'New_Price_Clean']])

new_price_year = df1.groupby('Year')['New_Price'].agg(Total_Cars='size',Available='count')

new_price_year['Missing'] = (new_price_year['Total_Cars'] - new_price_year['Available'])

new_price_year['Available_Percent'] = (new_price_year['Available'] /new_price_year['Total_Cars'] * 100)

print("\nNew Price availability by year:")
print(new_price_year)

print("\nMileage units:")
print(df1['Mileage'].dropna().str.extract(r'([a-zA-Z/]+)$')[0].value_counts())

print(df1[df1['Mileage'].str.contains('km/kg', na=False)][['Name', 'Year', 'Fuel_Type', 'Mileage', 'Price']])

mileage_clean = pd.to_numeric(df1['Mileage'].str.extract(r'([\d.]+)')[0],errors='coerce')

mileage_clean[df1['Mileage'].str.contains('km/kg', na=False)] = pd.NA

df1['Mileage_Clean'] = mileage_clean

print("\nCleaned Mileage:")
print(df1[['Mileage', 'Mileage_Clean']].head(20))
print(df1['Mileage_Clean'].dtype)
print(df1['Mileage_Clean'].isna().sum())

