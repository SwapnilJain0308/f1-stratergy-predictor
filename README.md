# F1 Pit Strategy Predictor 🏎️

A machine learning model that predicts whether an F1 driver 
should pit, which tyre compound to use next, and the optimal 
pit window — using real race telemetry data.

## Tech Stack
- Python
- FastF1 — real F1 telemetry data
- Pandas — data cleaning and exploration
- Matplotlib — data visualization
- Scikit-learn + XGBoost — ML model (coming soon)
- Streamlit — web app (coming soon)

## Week 1 — What I've done so far
- Loaded Monaco 2023 GP data — 1515 laps, 20 drivers, 31 features
- Visualized lap times for 5 random drivers (Verstappen , Gasly , Alonoso ,Perez , Leclerc)
- Analyzed tyre degradation for Verstappen
- Plotted tyre strategy for all 5  drivers

## Key Observations
- Normal lap time at Monaco = 75-80 seconds
- Lap 55 onwards — all drivers switched to Intermediates (rain)
- Medium tyre showed very low degradation at Monaco
- PER used 4 different compounds — most complex strategy


