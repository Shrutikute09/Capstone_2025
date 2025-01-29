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
1. **Air Quality Dataset**  
   - Source: [EPA AirData](https://aqs.epa.gov/aqsweb/airdata/download_files.html#Raw)  
   - Features: Pollutant concentrations, geographic and temporal data, monitoring methods.  
   - Size: Millions of records spanning multiple years.  

2. **Weather Dataset**  
   - Source: [GHCN-Daily](https://www.ncei.noaa.gov/cdo-web/datatools/selectlocation)  
   - Features: Temperature, precipitation, wind speed, and more.  
   - Size: Over 1.4 billion data points from 100,000+ stations worldwide.  

3. **Traffic Dataset**  
   - Source: Aggregated from city-specific databases (e.g., NYC DOT, SFCTA).  
   - Features: Traffic volume, timestamps, road segments, congestion levels.  
   - Format: CSV/JSON files, varying by city.  

## Methodology

### 1. Data Collection and Preprocessing
- Handling missing data and normalizing formats.
- Aligning temporal and geographic attributes across datasets.
- Decoding quality flags and transforming features.

### 2. Exploratory Data Analysis (EDA)
- Tools: Matplotlib, Seaborn, Tableau.  
- Analyzing trends in pollutants, weather, and traffic patterns.  
- Identifying correlations and anomalies.

### 3. Modeling and Algorithms
- Techniques: Regression (Linear, Random Forest), Clustering (K-means), Time-series Forecasting (ARIMA, LSTM).  
- Evaluation Metrics: R², MAE, RMSE.

### 4. Deployment
- Developing an interactive dashboard using **Streamlit** or **Flask**, integrated with Tableau for visualizations.  

## Deliverables

1. **Interactive Dashboard**  
   A tool to visualize air quality trends, predict pollutant levels, and map geographic distributions.  
2. **Comprehensive Report**  
   Detailed insights into factors affecting air quality, with recommendations for stakeholders.

## Tools and Technologies

- **Programming Languages**: Python, SQL  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, PyTorch  
- **Platforms**: Tableau, Google Colab, Jupyter Notebook  
- **Deployment**: Streamlit/Flask  

## How to Run the Project

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/air-quality-analysis.git
   ```
2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Download the datasets and place them in the `data/` directory.  
4. Run the preprocessing script:  
   ```bash
   python preprocess.py
   ```
5. Launch the dashboard:  
   ```bash
   streamlit run dashboard.py
   ```

## Contributors

- **Atreyo Das**: Advanced data preprocessing and time-series analysis.  
- **Ömer Seyfeddin Koç**: Predictive modeling and machine learning.  
- **Shruti Suhas Kute**: Data visualization and dashboard development.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Data provided by [EPA AirData](https://aqs.epa.gov/), [GHCN-Daily](https://www.ncei.noaa.gov/), and city-specific traffic databases.  
- Supervised by Dr. Fatema Nafa, Northeastern University.
