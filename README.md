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
- **Features:** Pollutant concentrations (PM2.5, NO2, CO, O3), geographic and temporal data, monitoring methods.
- **Size:** Millions of records spanning multiple years.
- **Processed File:** `updated_air_quality_dataset.csv`

### 2. Weather Dataset
- **Source:** Open-Meteo
- **Features:** Temperature, precipitation, wind speed, humidity, and more.
- **Size:** Over 1.4 billion data points from 100,000+ stations worldwide.

### 3. Traffic Dataset
- **Source:** Aggregated from city-specific databases -> [DATA.GOV](https://catalog.data.gov/dataset/mta-bridges-and-tunnels-hourly-crossings-beginning-2019) 
- **Features:** Traffic volume, timestamps, road segments, congestion levels.
- **Format:** CSV/JSON files, varying by city.

## Methodology

### 1. Data Collection and Preprocessing
- Handling missing data and normalizing formats.
- Aligning temporal and geographic attributes across datasets.
- Decoding quality flags and transforming features.
- Data merging performed in `Air_Quality_Dataset_Merging.ipynb`.

### 2. Exploratory Data Analysis (EDA)
- **Tools:** Matplotlib, Seaborn.
- Analyzing trends in pollutants, weather, and traffic patterns.
- Identifying correlations and anomalies.
- Analysis script: `NYC-NO2.py`

### 3. Modeling and Algorithms
- **Techniques:**
  - Regression Models: Linear Regression, Random Forest Regressor (Grid Search optimization)
  - Time-series Forecasting: ARIMA, LSTM, XGBoost
- **Evaluation Metrics:** R², MAE, RMSE
- Models:
  - `Air Quality Prediction - Random Forest Regressor used Grid Search.ipynb`
  - `XGBoost_PM2.5.ipynb` 

## Tools and Technologies

- **Programming Languages**: Python, SQL  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, PyTorch  
- **Platforms**: Tableau, Google Colab, Jupyter Notebook  

## Contributors

- **Atreyo Das**
- **Omer Koc**  
- **Shruti Suhas Kute** 

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Data provided by [EPA AirData](https://aqs.epa.gov/), [Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api), and [DATA.GOV](https://catalog.data.gov/dataset/mta-bridges-and-tunnels-hourly-crossings-beginning-2019).  
- Supervised by Dr. Fatema Nafa, Northeastern University.
