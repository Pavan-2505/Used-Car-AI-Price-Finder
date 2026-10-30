# Main runner for the four-file split of UsedCar1.py
# The analysis statements below are preserved from the original file.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from scipy.stats import mannwhitneyu
from pathlib import Path

warnings.filterwarnings('ignore')

df1 = pd.read_csv('train.csv')
df2 = pd.read_csv('Car Sell Dataset.csv')

graph_folder = Path('graphs')
graph_folder.mkdir(exist_ok=True)

pd.set_option('display.max_columns', None)

# Run the first three sections in this same namespace so the original
# variables and cleaned columns are available to the later sections.
exec(compile(Path('data_inspection.py').read_text(encoding='utf-8'), 'data_inspection.py', 'exec'), globals())
exec(compile(Path('data_cleaning_feature_engineering.py').read_text(encoding='utf-8'), 'data_cleaning_feature_engineering.py', 'exec'), globals())
exec(compile(Path('exploratory_data_analysis.py').read_text(encoding='utf-8'), 'exploratory_data_analysis.py', 'exec'), globals())

print("\nPrice statistics:")
print(df1['Price'].describe())

print("\nCar age statistics:")
print(df1['Car_Age'].describe())

print("\nKilometers statistics:")
print(df1['Kilometers_Driven'].describe())

print("\nMileage statistics:")
print(df1['Mileage_Clean'].describe())

print("\nEngine statistics:")
print(df1['Engine_Clean'].describe())

print("\nPower statistics:")
print(df1['Power_Clean'].describe())

print("\nCorrelation with Price:")
print(df1[['Price', 'Car_Age', 'Kilometers_Driven', 'Mileage_Clean', 'Engine_Clean', 'Power_Clean']].corr()['Price'].sort_values(ascending=False))

print("\nOutlier analysis")

columns = [
    'Price',
    'Kilometers_Driven',
    'Engine_Clean',
    'Power_Clean',
    'Mileage_Clean'
]

for col in columns:
    q1 = df1[col].quantile(0.25)
    q3 = df1[col].quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = df1[(df1[col] < lower) | (df1[col] > upper)]

    print("\n", col)
    print("Lower limit:", lower)
    print("Upper limit:", upper)
    print("Number of outliers:", len(outliers))

plt.figure(figsize=(8, 5))
sns.boxplot(y=df1['Price'])
plt.title('Price Outliers')
plt.ylabel('Price (Lakh)')
plt.savefig(graph_folder / '13_price_outliers.png', dpi=150, bbox_inches='tight')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(y=df1['Kilometers_Driven'])
plt.title('Kilometers Driven Outliers')
plt.ylabel('Kilometers Driven')
plt.savefig(graph_folder / '14_kilometers_outliers.png', dpi=150, bbox_inches='tight')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(y=df1['Engine_Clean'])
plt.title('Engine Outliers')
plt.ylabel('Engine (CC)')
plt.savefig(graph_folder / '15_engine_outliers.png', dpi=150, bbox_inches='tight')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(y=df1['Power_Clean'])
plt.title('Power Outliers')
plt.ylabel('Power (bhp)')
plt.savefig(graph_folder / '16_power_outliers.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nTransmission price comparison")

automatic = df1[df1['Transmission'] == 'Automatic']['Price'].dropna()
manual = df1[df1['Transmission'] == 'Manual']['Price'].dropna()

print("Automatic median:", automatic.median())
print("Manual median:", manual.median())

stat, p_value = mannwhitneyu(automatic, manual, alternative='two-sided')

print("U statistic:", stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("The difference is statistically significant.")
else:
    print("The difference is not statistically significant.")

print("\nAll graphs saved in:", graph_folder.resolve())
print("Total graphs saved: 16")