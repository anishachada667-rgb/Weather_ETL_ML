# Weather ETL & ML Pipeline

## Overview
Weather ETL & ML Pipeline automates the collection, transformation, and analysis of hourly weather data.
The pipeline pulls data from public APIs, cleans and transforms it, stores it in CSV format, 
and performs simple machine learning to predict temperature trends.

**Key Features:**
- Automated ETL pipeline using Python & Pandas
- Feature engineering for ML model inputs
- Simple ML model for temperature trend prediction
- Data visualization with Matplotlib/Seaborn
- CSV output for further analysis or reporting

## Architecture
Weather API
│
▼
Python ETL Script → Clean/Transform Data
│
▼
CSV / DataFrame → ML Feature Engineering
│
▼
Simple ML Model → Temperature Trend Prediction

## Setup Instructions

1. Clone the repository
   ```bash
   git clone https://github.com/anishachada667-rgb/Weather_ETL_ML.git
   cd Weather_ETL_ML