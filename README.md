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

### Completed

- Set up the Python virtual environment.
- Loaded the `train.csv` dataset using Pandas.
- Loaded the `Car Sell Dataset.csv` dataset using Pandas.
- Inspected the shape, columns, data types, and initial records of both datasets.
- Created an initial understanding of the variables in both datasets.
- Checked missing values in both datasets.
- Checked for duplicate rows in both datasets.
- Performed an initial range check on important numerical variables.
- Identified potential extreme values in `Kilometers_Driven` in Dataset 1.

### Initial Findings

#### Dataset 1 — `train.csv`

- Contains 5,847 rows and 14 columns.
- Missing values were found in `Mileage`, `Engine`, `Power`, `Seats`, and `New_Price`.
- `New_Price` has the highest amount of missing data, with approximately 86.06% of its values missing.
- No exact duplicate rows were found.
- `Kilometers_Driven` contains several unusually high values.
- The maximum `Kilometers_Driven` value is 6,500,000 km, which requires further investigation.
- `Engine`, `Power`, `Mileage`, and `New_Price` contain values stored as text along with units or other characters.

#### Dataset 2 — `Car Sell Dataset.csv`

- Contains 140,904 rows and 12 columns.
- No missing values were found in the initial analysis.
- No exact duplicate rows were found.
- The initial numerical range checks did not identify any obviously impossible values.

### Current Stage

The project is currently in the **data understanding and data-quality audit** stage.

The identified missing values, extreme values, and text-based numerical fields will be investigated before making any data-cleaning decisions.

No data has been removed or modified based on these findings yet.