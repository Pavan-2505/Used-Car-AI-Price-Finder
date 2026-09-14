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
print("---------SECOND DATASET---------")
print(f"The Dataset contains {df2.shape[0]} rows and {df2.shape[1]} columns")
df2.info()
print(df2.head())

