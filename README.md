# Used Car Price Intelligence & Prediction System

## Project Overview

This project is about analyzing used car data and understanding the factors that affect used car prices.

The main aim is to clean the data, analyze it, find useful patterns and later build a machine learning model to predict car prices.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy

## Datasets

Two datasets are used in this project.

### 1. train.csv

- Rows: 5,847
- Columns: 14

This is the main dataset used for analysis.

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

### 2. Car Sell Dataset.csv

- Rows: 140,904
- Columns: 12

This dataset contains additional information about used cars.

The main analysis is currently being done using `train.csv`. The second dataset has also been checked to understand its data and structure.

## Project Files

- `train.csv` - Main dataset
- `Car Sell Dataset.csv` - Additional dataset
- `UsedCar1.py` - Python code for the project
- `README.md` - Project details
- `graphs/` - Folder where the graphs are saved

## Data Analysis

The datasets were checked for:

- Missing values
- Duplicate rows
- Data types
- Numerical ranges
- Categorical values
- Inconsistent units
- Extreme values

Missing values were found in columns such as Mileage, Engine, Power, Seats and New Price.

Duplicate rows were checked in both datasets.

The Mileage, Engine, Power and New Price columns were examined and converted into numerical values for analysis.

Mileage values recorded in `km/kg` were kept out of the cleaned mileage feature because they use a different unit.

New Price values recorded in lakhs and crores were also converted into a common numerical scale.

## Feature Extraction

Some new features were created from the existing data:

- `Car_Age` - Calculates the age of a car using 2019 as the reference year.
- `Brand` - Extracted from the car name.
- `Model` - Extracted from the car name.
- `Km_Per_Year` - Estimates how many kilometres a car has been driven per year.

These features help in understanding the relationship between car details and their prices.

## Exploratory Data Analysis (EDA)

Different graphs were created using Matplotlib and Seaborn to understand the data better.

The graphs include:

- Distribution of used car prices
- Price vs Car Age
- Price vs Kilometers Driven
- Median Price by Brand
- Median Price by Fuel Type
- Median Price by Transmission
- Median Price by Owner Type
- Median Price by Location
- Price vs Mileage
- Price vs Power
- Price vs Engine Size
- Median Price by Year

## Statistical Analysis

Some statistical methods were used to understand the data.

The analysis includes:

- Summary statistics for important numerical columns
- Correlation between price and other numerical features
- Outlier detection using the IQR method
- Comparison of prices between Manual and Automatic cars
- Mann–Whitney U test to check whether the price distributions of Manual and Automatic cars are significantly different

A p-value below 0.05 is considered statistically significant for the transmission comparison.

## Outlier Analysis

Outliers were checked in the following columns:

- Price
- Kilometers Driven
- Engine
- Power
- Mileage

The IQR method was used to calculate the lower and upper limits and count the values outside these limits.

Boxplots were also created to understand the outliers visually. These values are only identified for further investigation and are not automatically removed.

## Graph Output

The graphs are saved as PNG images inside the `graphs` folder.

The current code generates 16 graphs, including EDA graphs and outlier boxplots.

The graphs are also displayed while running the program.

The current version does not save a cleaned CSV dataset or separate text reports.

## Current Progress

So far, I have completed:

- Dataset loading
- Basic data inspection
- Missing value analysis
- Duplicate checking
- Numerical and categorical analysis
- Unit checking
- Initial data cleaning
- Feature extraction
- Exploratory Data Analysis
- Summary statistics
- Correlation analysis
- Outlier analysis
- Fuel type price comparison
- Transmission price comparison
- Mann–Whitney U test
- Saving graphs in a separate folder

The project is currently in the data analysis and cleaning stage. Machine learning model training and price prediction have not been started yet.

## Future Work

The next steps for this project are:

- Finalizing the data cleaning process
- Handling the remaining missing values
- Preparing the data for machine learning
- Selecting useful features
- Training machine learning models
- Comparing model performance
- Evaluating prediction accuracy
- Building the used car price prediction system

## Project Goal

The final goal is to build a system that can predict used car prices based on details such as manufacturing year, kilometres driven, fuel type, transmission, mileage, engine capacity and power.