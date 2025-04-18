# Analyzing Air Quality: Insights into the Impact of Weather and Traffic in Big Cities

## Overview

This project explores the relationship between air quality, weather conditions, and traffic patterns in urban areas. By combining multiple datasets and leveraging machine learning techniques, the project aims to deliver actionable insights for policymakers, urban planners, and the general public to address air pollution challenges.

## Problem Statement

Air pollution is a pressing issue in urban and industrial settings, posing risks to public health and the environment. This project seeks to:

- Identify key contributors to poor air quality, including weather and traffic.
- Predict air quality indices using machine learning models.
- Provide data-driven recommendations for effective mitigation strategies.

## Datasets

The analysis integrates data from the following publicly available datasets:
  
### 1. Air Quality Dataset
- **Source:** EPA AirData
- **Features:** Pollutant concentrations (PM2.5, PM10, NO2), geographic and temporal data, monitoring methods.
- **Size:** Millions of records spanning multiple years.

### 2. Weather Dataset
- **Source:** Open-Meteo
- **Features:** Temperature, precipitation, wind speed, humidity, and more.
- **Size:** Over 1.4 billion data points from 100,000+ stations worldwide.

### 3. Traffic Dataset
- **Source:**  DATA.NY.GOV
- **Features:** Traffic count, Vehicle class, Direction, Facility.
- **Format:** CSV file.

**Processed File:** `updated_air_quality_dataset.csv`

## Methodology

### 1. Data Collection and Preprocessing
- Handling missing data and normalizing formats.
- Aligning temporal and geographic attributes across datasets.
- Decoding quality flags and transforming features.
- Data merging performed in `Air_Quality_Dataset_Merging.ipynb` & `Adding_Weather_Traffic_Data.ipynb`.

### 2. Exploratory Data Analysis (EDA)
- **Tools:** Matplotlib, Seaborn.
- Analyzing trends in pollutants, weather, and traffic patterns.
- Identifying correlations and anomalies.
- Analysis script: `EDA.ipynb`

### 3. Modeling and Algorithms
- **Techniques:**
  - Regression Models: XGBoost, Random Forest Regressor (Grid Search optimization)
  - Time-series Forecasting: ARIMA, LSTM
- **Evaluation Metrics:** R², MAE, RMSE
- Models:
  - `Air Quality Prediction - Random Forest Regressor used Grid Search.ipynb`
  - `Random Forest - Updated Feature Engineering.ipynb`
  - `XGBoost_PM2.5.ipynb`
  - `XGBoost_PM10.ipynb`
  - `XGBoost_NO2.ipynb`
  - `LSTM - Time Series.ipynb`
  - `AirQuality_ARIMA.ipynb`

### 4. Data Visualization
- **Tools:** Tableau
- Showcasing trends in pollutant levels over the years
- Displaying correlation between air pollution metrics and other features
- Presenting model performances through graphs
- **Link:** [Dashboard](https://public.tableau.com/app/profile/atreyo.das/viz/Capstone_Air_Quality_17440009911560/Dashboard1) 

  
## Tools and Technologies

- **Programming Languages**: Python 
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, XGBoost, Scikit-learn, Tensorflow, Statsmodel 
- **Platforms**: Tableau, Google Colab, Jupyter Notebook  

## Contributors

- **Atreyo Das**
- **Omer Koc**  
- **Shruti Suhas Kute**

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Data provided by [EPA AirData](https://aqs.epa.gov/), [Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api), and [DATA.NY.GOV](https://catalog.data.gov/dataset/mta-bridges-and-tunnels-hourly-crossings-beginning-2019).  
- Supervised by Dr. Fatema Nafa, Northeastern University.
