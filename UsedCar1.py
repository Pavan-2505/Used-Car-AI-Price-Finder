import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

df1 = pd.read_csv('train.csv')

print("The Dataset contains", df1.shape[0], "rows and", df1.shape[1], "columns")

print(df1.info())

pd.set_option('display.max_columns', None)

print(df1.head())