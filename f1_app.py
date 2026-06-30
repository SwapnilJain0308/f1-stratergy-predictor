import streamlit as st
import joblib
import pandas as pd

st.title("F1 Pit Strategy Predictor 🏎️")

model = joblib.load('f1_pit_model.pkl')
driver_options = {
    'ALB': 0, 'ALO': 1, 'BOT': 2, 'DEV': 3, 'GAS': 4,
    'HAM': 5, 'HUL': 6, 'LEC': 7, 'MAG': 8, 'NOR': 9,
    'OCO': 10, 'PER': 11, 'PIA': 12, 'RUS': 13, 'SAI': 14,
    'SAR': 15, 'STR': 16, 'TSU': 17, 'VER': 18, 'ZHO': 19
}

race_options = {
    'Monaco': 0, 'Bahrain': 1, 'Silverstone': 2, 
    'Monza': 3, 'Abu Dhabi': 4
}

st.write("Enter the current race situation:")

lap_number = st.number_input("Lap Number", min_value=1, max_value=80, value=20)
tyre_life = st.number_input("Tyre Age (laps)", min_value=0, max_value=60, value=15)
position = st.number_input("Position", min_value=1, max_value=20, value=5)

compound = st.selectbox("Current Compound", ["SOFT", "MEDIUM", "HARD", "INTERMEDIATE", "WET"])
compound_map = {"SOFT": 0, "MEDIUM": 1, "HARD": 2, "INTERMEDIATE": 3, "WET": 4}

driver_name = st.selectbox("Driver", list(driver_options.keys()))
driver = driver_options[driver_name]

race_name = st.selectbox("Race", list(race_options.keys()))
race = race_options[race_name]

if st.button("Predict"):
    input_data = pd.DataFrame({
        'Driver': [driver],
        'LapNumber': [lap_number],
        'TyreLife': [tyre_life],
        'Compound': [compound_map[compound]],
        'Position': [position],
        'Race': [race]
    })
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("PIT NOW — High chance driver should pit in next 3 laps")
    else:
        st.info("STAY OUT — Driver likely to continue")