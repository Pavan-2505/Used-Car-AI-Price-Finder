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

