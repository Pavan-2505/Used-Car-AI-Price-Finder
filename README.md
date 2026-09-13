# Used Car Price Intelligence & Prediction System

## Project Overview

This project is being developed to analyze used-car data and progressively build a used-car price intelligence system.

At the current stage, the project has started with the **data loading and initial setup** using Python.

## Current Progress

The current Python script:

- Imports NumPy
- Imports Pandas
- Imports Matplotlib
- Imports Seaborn
- Imports the `warnings` module
- Suppresses warning messages
- Loads the `train.csv` dataset using Pandas
- Displays the loaded dataset for initial inspection

The currently loaded dataset contains **5,847 rows and 14 columns**.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Current Project Files

```text
Project UsedCar/
│
├── .venv/
├── Car Sell Dataset.csv
├── train.csv
└── UsedCar1.py
```

## Current Python Code

The current data-loading stage includes:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

df1 = pd.read_csv('train.csv')
```

## Dataset

The project is currently working with the `train.csv` file.

The dataset has been loaded successfully into a Pandas DataFrame named `df1`.

## Project Status

**Current status:** Initial data loading and setup.

Further analysis and processing will be added as the project develops.
