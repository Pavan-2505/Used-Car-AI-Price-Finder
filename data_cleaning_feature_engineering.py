engine_numeric = pd.to_numeric(df1['Engine'].str.replace('CC', '', regex=False), errors='coerce')

print(engine_numeric.describe())

print(df1.assign(Engine_Numeric=engine_numeric)[['Name', 'Year', 'Engine', 'Engine_Numeric']].sort_values('Engine_Numeric', ascending=False).head(10))

df1['Engine_Clean'] = pd.to_numeric(df1['Engine'].str.replace(' CC', '', regex=False), errors='coerce')

print(df1[['Engine', 'Engine_Clean']].head(10))
print(df1['Engine_Clean'].dtype)
print(df1['Engine_Clean'].isnull().sum())

print("\nPower:")
print(df1['Power'].dropna().str.extract(r'([A-Za-z]+)', expand=False).value_counts())

power_numeric = pd.to_numeric(df1['Power'].str.replace('bhp', '', regex=False), errors='coerce')

print(power_numeric.describe())

print(df1.assign(Power_Numeric=power_numeric)[['Name', 'Year', 'Power', 'Power_Numeric']].sort_values('Power_Numeric', ascending=False).head(10))

df1['Power_Clean'] = pd.to_numeric(df1['Power'].str.replace('bhp', '', regex=False), errors='coerce')

print(df1[['Power', 'Power_Clean']].head(10))
print(df1['Power_Clean'].dtype)
print(df1['Power_Clean'].isnull().sum())

print("\nNew Price:")
print(df1['New_Price'].dropna().str.extract(r'([A-Za-z]+)', expand=False).value_counts())

print(df1[df1['New_Price'].str.contains('Cr', na=False)][['Name', 'Year', 'New_Price', 'Price']])

lakh = pd.to_numeric(df1.loc[df1['New_Price'].str.contains('Lakh', na=False), 'New_Price'].str.replace(' Lakh', '', regex=False), errors='coerce')

crore = pd.to_numeric(df1.loc[df1['New_Price'].str.contains('Cr', na=False), 'New_Price'].str.replace(' Cr', '', regex=False), errors='coerce')

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

new_price_year = df1.groupby('Year')['New_Price'].agg(Total_Cars='size', Available='count')

new_price_year['Missing'] = new_price_year['Total_Cars'] - new_price_year['Available']

new_price_year['Available_Percent'] = new_price_year['Available'] / new_price_year['Total_Cars'] * 100

print("\nNew Price availability by year:")
print(new_price_year)

print("\nMileage units:")
print(df1['Mileage'].dropna().str.extract(r'([a-zA-Z/]+)$')[0].value_counts())

print(df1[df1['Mileage'].str.contains('km/kg', na=False)][['Name', 'Year', 'Fuel_Type', 'Mileage', 'Price']])

mileage_clean = pd.to_numeric(df1['Mileage'].str.extract(r'([\d.]+)')[0], errors='coerce')

mileage_clean[df1['Mileage'].str.contains('km/kg', na=False)] = np.nan

df1['Mileage_Clean'] = mileage_clean

print("\nCleaned Mileage:")
print(df1[['Mileage', 'Mileage_Clean']].head(20))
print(df1['Mileage_Clean'].dtype)
print(df1['Mileage_Clean'].isna().sum())

df1['Car_Age'] = 2019 - df1['Year']

print("\nCar Age:")
print(df1[['Year', 'Car_Age']].head(10))
print(df1['Car_Age'].describe())

df1['Brand'] = df1['Name'].str.split().str[0]

df1['Model'] = df1['Name'].str.split().str[1]

df1['Km_Per_Year'] = df1['Kilometers_Driven'] / (df1['Car_Age'] + 1)

print("\nFeature extraction:")
print(df1[['Name', 'Brand', 'Model', 'Year', 'Car_Age', 'Kilometers_Driven', 'Km_Per_Year', 'Engine_Clean', 'Power_Clean', 'Mileage_Clean']].head(10))

print("\nBrands:")
print(df1['Brand'].nunique())

print("\nModels:")
print(df1['Model'].nunique())

print("\nKm per year:")
print(df1['Km_Per_Year'].describe())

