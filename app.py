from re import X
import streamlit as st
import pandas as pd

st.title("🏏 Cricket Match Predictor")

st.markdown("Enter the match state below:")
home_team = st.selectbox("Home Team", ['RCB', 'MI', 'CSK', 'GT', 'KKR', 'SRH', 'RR', 'LSG', 'PBKS', 'DC'])
away_team = st.selectbox("Away Team", ['RCB', 'MI', 'CSK', 'GT', 'KKR', 'SRH', 'RR', 'LSG', 'PBKS', 'DC'])
city = st.selectbox("City", ['Bengaluru', 'Sharjah', 'Chennai', 'Dubai', 'Kimberley',
       'Hyderabad', 'Kolkata', 'Mumbai', 'Jaipur', 'Navi Mumbai', 'Delhi',
       'Ahmedabad', 'Durban', 'Visakhapatnam', 'Rajkot', 'Pune',
       'Chandigarh', 'Raipur', 'Kochi', 'Centurion', 'Port Elizabeth',
       'Indore', 'Dharamsala', 'Abu Dhabi', 'Johannesburg', 'Cape Town',
       'Cuttack', 'Kanpur', 'Lucknow', 'East London', 'Ranchi', 'Nagpur',
       'Bloemfontein', 'Guwahati'])

current_innings = st.selectbox("Batting Team", [home_team, away_team])
current_score = st.number_input("Current Score", min_value=0, value=38)

running_over = st.number_input("Current Over (e.g. 4.5)", min_value=0.0, max_value=20.0, value=4.5)
wickets = st.slider("Wickets Fallen", min_value=0, max_value=10, value=2)

if st.button("Submit"):
    match_data = {
        'home_team': [home_team],
        'away_team': [away_team],
        'city': [city],
        'current_innings': [current_innings],
        'current_score': [current_score],
        'strikeRate': [0.0 if running_over==0 else (current_score/(running_over*6))*100],
        'runningOver': [running_over],
        'wickets': [wickets]
    }
    df = pd.DataFrame(match_data)

    st.subheader("📋 Match State:")
    st.write(df)

    # 👇 You can add prediction logic here once your model is ready
    st.success("Ready to send this data to your model!")
    import joblib
    model = joblib.load('score_projectory.pkl')
    projected_score = model.predict(df)
    st.write(f"Projected Score : {projected_score[0]:.0f}")

