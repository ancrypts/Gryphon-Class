import streamlit as st
import requests
from dotenv import load_dotenv
import os

# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

API_KEY = os.getenv("API_KEY")

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Weather Forecast",
    page_icon="🌤️",
    layout="centered"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#74ebd5,#ACB6E5);
    font-family: 'Segoe UI', sans-serif;
}

.main-title{
    text-align:center;
    color:white;
    font-size:45px;
    font-weight:bold;
    margin-bottom:0;
}

.subtitle{
    text-align:center;
    color:white;
    margin-bottom:30px;
}

.weather-card{
    background:rgba(255,255,255,0.25);
    backdrop-filter: blur(15px);
    border-radius:20px;
    padding:25px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.2);
    text-align:center;
}

.metric-card{
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 5px 10px rgba(0,0,0,0.15);
}

.metric-title{
    font-size:16px;
    color:gray;
}

.metric-value{
    font-size:26px;
    font-weight:bold;
    color:#007BFF;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.markdown(
    "<h1 class='main-title'>🌤️ Weather Forecast</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p class='subtitle'>Check real-time weather anywhere in the world</p>",
    unsafe_allow_html=True,
)

# ----------------------------
# Input
# ----------------------------
city = st.text_input("📍 Enter City Name")

# ----------------------------
# Button
# ----------------------------
if st.button("Get Weather"):

    if city.strip() == "":
        st.warning("Please enter a city name.")
        st.stop()

    API_URL = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    with st.spinner("Fetching weather..."):

        try:
            response = requests.get(API_URL)

            if response.status_code == 200:

                data = response.json()

                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                wind_speed = data["wind"]["speed"]
                weather = data["weather"][0]["main"]
                description = data["weather"][0]["description"].title()
                city_name = data["name"]
                country = data["sys"]["country"]
                icon = data["weather"][0]["icon"]

                icon_url = f"https://openweathermap.org/img/wn/{icon}@4x.png"

                st.markdown(
                    f"""
                    <div class="weather-card">
                        <h2>{city_name}, {country}</h2>
                        <img src="{icon_url}" width="120">
                        <h1>{temperature} °C</h1>
                        <h4>{description}</h4>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.write("")

                col1, col2 = st.columns(2)
                col3, col4 = st.columns(2)

                with col1:
                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">🌡 Temperature</div>
                            <div class="metric-value">{temperature} °C</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with col2:
                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">💧 Humidity</div>
                            <div class="metric-value">{humidity}%</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with col3:
                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">🌬 Wind Speed</div>
                            <div class="metric-value">{wind_speed} m/s</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                with col4:
                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">☁ Weather</div>
                            <div class="metric-value">{weather}</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            elif response.status_code == 404:
                st.error("❌ City not found.")

            else:
                st.error("Something went wrong. Please try again.")

        except requests.exceptions.RequestException:
            st.error("Unable to connect to the Weather API.")
