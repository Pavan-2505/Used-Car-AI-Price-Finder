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

## Data Quality Audit

### Missing Values

#### Dataset 1 — `train.csv`

- `Mileage`: 2 missing values
- `Engine`: 36 missing values
- `Power`: 36 missing values
- `Seats`: 38 missing values
- `New_Price`: 5,032 missing values (86.06%)
- `Price`: No missing values

#### Dataset 2 — `Car Sell Dataset.csv`

- No missing values were found in any column.

### Duplicate Rows

- Dataset 1: 0 duplicate rows
- Dataset 2: 0 duplicate rows

### Numerical Range and Extreme Value Analysis

#### Dataset 1 — `train.csv`

- `Year` ranges from 1998 to 2019.
- `Seats` ranges from 2 to 10.
- `Price` ranges from 0.44 to 160.
- `Kilometers_Driven` ranges from 171 to 6,500,000 km.
- 28 records have more than 200,000 km driven.
- 7 records have more than 300,000 km driven.
- 4 records have more than 500,000 km driven.
- 1 record has more than 1,000,000 km driven.
- The median `Kilometers_Driven` is 52,576 km, while the maximum is 6,500,000 km.
- The 6,500,000 km observation is considered a potential anomaly and requires further investigation before deciding how it should be handled.

#### Dataset 2 — `Car Sell Dataset.csv`

- `Year` ranges from 2000 to 2023.
- `Kilometers` ranges from 10,000 to 179,998 km.
- `Price` ranges from 50,055 to 2,744,280.
- No obviously impossible numerical values were identified during the initial range check.

### Categorical Value Consistency

#### Dataset 1 — `train.csv`

- `Fuel_Type` contains 3 categories: Diesel, Petrol, and Electric.
- `Transmission` contains 2 categories: Manual and Automatic.
- `Owner_Type` contains 4 categories: First, Second, Third, and Fourth & Above.
- No obvious capitalization or spelling inconsistencies were observed in these categorical values.

#### Dataset 2 — `Car Sell Dataset.csv`

- `Fuel Type` contains 5 categories: CNG, Petrol, Diesel, Electric, and Hybrid.
- `Transmission` contains 2 categories: Manual and Automatic.
- `Owner` contains 3 categories: 1st, 2nd, and 3rd+.
- `Accidental` contains 2 categories: No and Yes.
- No obvious capitalization or spelling inconsistencies were observed in these categorical values.

#### Geographical Values

- Dataset 1 contains 11 unique locations: Pune, Chennai, Coimbatore, Jaipur, Mumbai, Kochi, Kolkata, Delhi, Bangalore, Hyderabad, and Ahmedabad.
- Dataset 2 contains 27 unique state/region categories.
- No obvious spelling or capitalization inconsistencies were observed in the geographical values during the initial inspection.
- Dataset 2 includes broader categories such as `North East` and `Other UTs`, which will be retained for further investigation rather than being assumed to be invalid.

### Text and Unit Consistency

#### Dataset 1 — `train.csv`

- `Mileage`, `Engine`, `Power`, and `New_Price` are stored as text values containing numerical information and units.

##### Mileage

- `Mileage` contains 5,842 values reported in `kmpl` and 3 values reported in `km/kg`.
- There are 2 missing values in `Mileage`.
- The three `km/kg` records correspond to Petrol/Diesel vehicles, making their unit potentially inconsistent with their fuel type.
- These three records require further investigation before deciding how they should be handled.

##### Engine

- `Engine` has 5,811 non-missing values, and all of them use the `CC` unit.
- `Engine` ranges from 72 CC to 5,998 CC, with a median of 1,497 CC.
- The highest Engine values correspond to large-engine luxury and performance vehicles.
- No clearly invalid Engine values were identified during the initial investigation.
- A cleaned numerical version, `Engine_Clean`, has been created while preserving the original `Engine` column.

##### Power

- `Power` has 5,811 non-missing values, and all of them use the `bhp` unit.
- `Power` ranges from 34.2 bhp to 560 bhp, with a median of 98.6 bhp.
- The highest Power values correspond to high-performance and luxury vehicles.
- No clearly invalid Power values were identified during the initial investigation.
- A cleaned numerical version, `Power_Clean`, has been created while preserving the original `Power` column.

##### New_Price

- `New_Price` contains 798 values reported in `Lakh` and 17 values reported in `Cr`.
- The `Cr` values were identified as Crore and converted to `Lakh` for consistent numerical representation.
- `New_Price` contains 5,032 missing values, representing approximately 86.06% of the dataset.
- A cleaned numerical version, `New_Price_Clean`, has been created with all available values standardized to `Lakh`.
- Missing `New_Price` values have been preserved as missing and will be considered separately during further analysis.

### New_Price Missingness Analysis

- `New_Price` contains 5,032 missing values out of 5,847 records, representing approximately 86.06% of the dataset.
- Missingness is not evenly distributed across vehicle years.
- Older vehicle years generally have very low `New_Price` availability, while newer vehicle years have a higher proportion of recorded values.
- `New_Price` availability increases from approximately 4.85% in 2010 to 57.43% in 2019.
- The missingness pattern will be considered before deciding whether `New_Price` should be retained, imputed, or excluded during later modeling stages.

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