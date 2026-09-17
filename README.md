# Used Car Price Intelligence & Prediction System

## Project Overview

This project is about analyzing used car data and understanding the factors that affect used car prices.

The main aim is to clean the data, analyze it, find useful patterns and later build a model to predict car prices.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy

## Datasets

Two datasets are used in this project.

### train.csv

- Rows: 5,847
- Columns: 14
- This is the main dataset used for analysis.

It contains information such as:

- Car Name
- Location
- Year
- Kilometers Driven
- Fuel Type
- Transmission
- Owner Type
- Mileage
- Engine
- Power
- Seats
- New Price
- Price

### Car Sell Dataset.csv

- Rows: 140,904
- Columns: 12
- This dataset contains additional used car information.

The main analysis is currently being done using `train.csv`.

## Project Files

- `train.csv` - Main dataset
- `Car Sell Dataset.csv` - Additional dataset
- `UsedCar1.py` - Python program
- `UsedCar_Cleaned.csv` - Cleaned dataset
- `README.md` - Project information

## Data Analysis

The dataset was checked for:

- Missing values
- Duplicate rows
- Data types
- Numerical ranges
- Categorical values
- Inconsistent units
- Extreme values

Some missing values were found in Mileage, Engine, Power, Seats and New Price.

No duplicate rows were found.

The Mileage, Engine, Power and New Price columns were cleaned and converted into numerical values for analysis.

## Feature Extraction

Some new features were created from the existing data:

- `Car_Age`
- `Brand`
- `Model`
- `Km_Per_Year`

These features are used to make the data easier to analyze.

## Exploratory Data Analysis

Different comparisons and graphs were created to understand car prices.

The analysis includes:

- Price distribution
- Price vs Car Age
- Price vs Kilometers Driven
- Price by Brand
- Price by Fuel Type
- Price by Transmission

The transmission analysis compares the prices of Manual and Automatic cars.

## Current Progress

So far, I have completed:

- Dataset loading
- Basic data inspection
- Missing value analysis
- Duplicate checking
- Numerical and categorical analysis
- Unit checking
- Feature extraction
- Initial data cleaning
- Exploratory data analysis
- Fuel type price comparison
- Transmission price comparison

The project is currently in the data analysis and cleaning stage.