import streamlit as st
import joblib
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="F1 Pit Strategy Predictor", page_icon="🏎️", layout="wide")

st.title("🏎️ F1 Pit Strategy Predictor")
st.markdown("*Predict whether an F1 driver should pit based on real race telemetry data*")
st.divider()

model = joblib.load('f1_pit_model.pkl')
all_laps = pd.read_csv('all_races_2023_laps.csv')

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

race_name_map = {0: 'Monaco', 1: 'Bahrain', 2: 'Silverstone', 3: 'Monza', 4: 'Abu Dhabi'}

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Race Situation")

    driver_name = st.selectbox("Driver", list(driver_options.keys()))
    driver = driver_options[driver_name]

    race_name = st.selectbox("Race", list(race_options.keys()))
    race = race_options[race_name]

    compound = st.selectbox("Current Compound", ["SOFT", "MEDIUM", "HARD", "INTERMEDIATE", "WET"])
    compound_map = {"SOFT": 0, "MEDIUM": 1, "HARD": 2, "INTERMEDIATE": 3, "WET": 4}

    lap_number = st.number_input("Lap Number", min_value=1, max_value=80, value=20)
    tyre_life = st.number_input("Tyre Age (laps)", min_value=0, max_value=60, value=15)
    position = st.number_input("Current Position", min_value=1, max_value=20, value=5)

    predict_btn = st.button("🔮 Predict Strategy", use_container_width=True)

with col2:
    st.subheader(f"{driver_name} — Tyre Strategy at {race_name} 2023")

    selected_race_name = race_name_map[race]
    race_data = all_laps[(all_laps['Race'] == selected_race_name) & (all_laps['Driver'] == driver_name)]

    if len(race_data) > 0:
        fig = px.scatter(
            race_data,
            x='LapNumber',
            y='TyreLife',
            color='Compound',
            color_discrete_map={
                'SOFT': '#FF3333',
                'MEDIUM': '#FFD700',
                'HARD': '#FFFFFF',
                'INTERMEDIATE': '#39FF14',
                'WET': '#00BFFF'
            },
            title=f'{driver_name} Tyre Strategy — {selected_race_name} 2023',
            labels={'LapNumber': 'Lap Number', 'TyreLife': 'Tyre Age (laps)'}
        )
        fig.update_layout(
            plot_bgcolor='#0e1117',
            paper_bgcolor='#0e1117',
            font_color='white',
            legend_title_text='Compound'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No historical data for this driver/race combination")

st.divider()

if predict_btn:
    input_data = pd.DataFrame({
        'Driver': [driver],
        'LapNumber': [lap_number],
        'TyreLife': [tyre_life],
        'Compound': [compound_map[compound]],
        'Position': [position],
        'Race': [race]
    })

    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]

    st.subheader("Prediction Result")

    m1, m2, m3 = st.columns(3)

    with m1:
        if prediction == 1:
            st.metric("Strategy", "PIT NOW 🔴")
        else:
            st.metric("Strategy", "STAY OUT 🟢")

    with m2:
        confidence = prediction_proba[1] * 100 if prediction == 1 else prediction_proba[0] * 100
        st.metric("Confidence", f"{confidence:.1f}%")

    with m3:
        st.metric("Tyre Age", f"{tyre_life} laps")

    if prediction == 1:
        st.error(f"⚠️ HIGH PIT PROBABILITY — {driver_name} should consider pitting in the next 3 laps")
    else:
        st.success(f"✅ STAY OUT — {driver_name} can continue on current tyres")