# F1 Pit Strategy Predictor 🏎️

A machine learning model that predicts whether an F1 driver 
should pit based on real race telemetry data from FastF1.

## 🚀 Live App
Try it here
https://f1-stratergy-predictor-k6banp5xjakwqe9fez88cr.streamlit.app/

## Tech Stack
- Python
- FastF1 — real F1 telemetry data
- Pandas — data cleaning and exploration
- Matplotlib / Plotly — data visualization
- Scikit-learn + XGBoost — ML model
- Streamlit — web app

## Week 1 — Data Exploration
- Loaded Monaco 2023 GP data — 1515 laps, 20 drivers, 31 features
- Visualized lap times for 5 drivers (VER, GAS, PER, ALO, LEC)
- Analyzed tyre degradation for Verstappen
- Plotted tyre strategy for all 5 drivers

## Key Observations
- Normal lap time at Monaco = 75-80 seconds
- Lap 55 onwards — all drivers switched to Intermediates (rain)
- Medium tyre showed very low degradation at Monaco
- PER used 4 different compounds — most complex strategy

## Week 2 — Feature Engineering & Model
- Loaded 5 races: Monaco, Bahrain, Silverstone, Monza, Abu Dhabi 2023
- Combined 5657 laps into one training dataset
- Built WillPit target column — 527 positive cases across 5 races
- Features: TyreLife, LapNumber, Compound, Position, Driver, Race
- Logistic Regression — 90.4% accuracy but 0% pit stop recall
- XGBoost — 87.2% accuracy, 79% pit stop recall, F1: 0.54
- Tuned XGBoost — 89.7% accuracy, 79% recall, F1: 0.59
- TyreLife is the most important feature for pit prediction

## Week 3 — Web App
- Built Streamlit web app with interactive Plotly graphs
- Driver and race dropdown with F1 tyre color coding
- Confidence score from XGBoost model
- Deployed on Streamlit Cloud

## How to Run Locally
1. Clone the repo
2. Install dependencies:
