import streamlit as st
import requests
from dotenv import load_dotenv
import os
load_dotenv()

st.set_page_config(page_title="Weather App", page_icon="☁️", layout="wide")
st.title("Weather App") 
st.subheader("This is a simple weather app that allows you to check the current weather conditions for any city in the world. " \
"Please enter the name of the city below to get started.")
city = st.text_input("Enter city name", "")

if st.button("Get Weather"):
    API_KEY = os.getenv("API_KEY")
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(API_URL)
    if response.status_code == 200:
        st.success("Weather data retrieved successfully!")
        data = response.json()
        st.subheader(f"{city}, {data['sys'].get('country', 'N/A')}")
        cols = st.columns(4)
        
        # prepare displayable weather data as (label, value) pairs
        weather_data = [
            ("Temperature", f"🌡️{data['main']['temp']} °C"),
            ("Description", data['weather'][0]['description']),
            ("Humidity", f"💧{data['main']['humidity']} %"),
            ("Wind Speed", f"💨{data['wind'].get('speed', 'N/A')} m/s"),
            ("Pressure", f"🔽{data['main']['pressure']} hPa"),    
            ("Visibility", f"👁️{data.get('visibility', 'N/A')} meters"),
            ("Cloudiness", f"☁️{data['clouds'].get('all', 'N/A')} %"),
            ("Country", f"📍{data['sys'].get('country', 'N/A')}"),
        ]
        for i, (label, val) in enumerate(weather_data):
            with cols[i % len(cols)]:
                st.metric(label=label, value=val)
    else:
        st.error("City not found. Please enter a valid city name.")
