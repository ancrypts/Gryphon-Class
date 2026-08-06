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
    page_title="WeatherFy",
    page_icon="🌦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.stApp{
background:#0D1117;
color:white;
}

/* Hide Streamlit spacing */
.block-container{
padding-top:2rem;
padding-bottom:2rem;
max-width:900px;
}

/* Title */

.title{
font-size:48px;
font-weight:700;
text-align:center;
color:white;
letter-spacing:-1px;
margin-bottom:8px;
}

.subtitle{
text-align:center;
color:#8B949E;
font-size:16px;
margin-bottom:35px;
}

/* Input */

.stTextInput input{
background:#161B22;
border:1px solid #30363D;
border-radius:14px;
color:white;
padding:14px;
font-size:16px;
}

.stTextInput input:focus{
border:1px solid #4F8CFF;
box-shadow:none;
}

/* Button */

.stButton>button{
width:100%;
height:52px;
border-radius:14px;
background:#4F8CFF;
border:none;
color:white;
font-weight:600;
font-size:16px;
transition:0.3s;
}

.stButton>button:hover{
background:#3B78F0;
}

/* Weather Card */

.weather-card{

background:#161B22;

border:1px solid #30363D;

border-radius:24px;

padding:35px;

text-align:center;

margin-top:25px;

}

/* City */

.city{

font-size:34px;

font-weight:700;

color:white;

margin-top:10px;

}

/* Temp */

.temp{

font-size:72px;

font-weight:700;

margin-top:10px;

color:white;

}

/* Desc */

.desc{

font-size:18px;

color:#8B949E;

margin-top:5px;

}

/* Metrics */

.metric{

background:#161B22;

border:1px solid #30363D;

border-radius:18px;

padding:22px;

text-align:center;

margin-top:20px;

}

.metric-title{

font-size:14px;

color:#8B949E;

}

.metric-value{

font-size:30px;

font-weight:700;

color:white;

margin-top:8px;

}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------

st.markdown("""
<div class="title">
WeatherFy
</div>

<div class="subtitle">
Modern Weather Dashboard
</div>
""", unsafe_allow_html=True)

city = st.text_input(
    "City",
    placeholder="Enter a city name..."
)

# ----------------------------
# Fetch Weather
# ----------------------------

if st.button("Get Weather"):

    if city.strip() == "":
        st.warning("Please enter a city name.")
        st.stop()

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    with st.spinner("Fetching latest weather..."):

        try:

            response = requests.get(url, timeout=10)

            if response.status_code == 200:

                data = response.json()

                temperature = round(data["main"]["temp"])
                feels_like = round(data["main"]["feels_like"])
                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]
                wind_speed = data["wind"]["speed"]
                visibility = data.get("visibility", 0) / 1000

                weather = data["weather"][0]["main"]
                description = data["weather"][0]["description"].title()

                city_name = data["name"]
                country = data["sys"]["country"]

                icon = data["weather"][0]["icon"]
                icon_url = f"https://openweathermap.org/img/wn/{icon}@4x.png"

                # Main Card

                st.markdown(f"""
                <div class="weather-card">

                    <img src="{icon_url}" width="120">

                    <div class="city">
                    {city_name}, {country}
                    </div>

                    <div class="temp">
                    {temperature}°
                    </div>

                    <div class="desc">
                    {description}
                    </div>

                </div>
                """, unsafe_allow_html=True)

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.markdown(f"""
                    <div class="metric">
                        <div class="metric-title">
                        Feels Like
                        </div>

                        <div class="metric-value">
                        {feels_like}°C
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""
                    <div class="metric">
                        <div class="metric-title">
                        Humidity
                        </div>

                        <div class="metric-value">
                        {humidity}%
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    st.markdown(f"""
                    <div class="metric">
                        <div class="metric-title">
                        Wind Speed
                        </div>

                        <div class="metric-value">
                        {wind_speed} m/s
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                col4, col5, col6 = st.columns(3)

                with col4:
                    st.markdown(f"""
                    <div class="metric">
                        <div class="metric-title">
                        Pressure
                        </div>

                        <div class="metric-value">
                        {pressure} hPa
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with col5:
                    st.markdown(f"""
                    <div class="metric">
                        <div class="metric-title">
                        Visibility
                        </div>

                        <div class="metric-value">
                        {visibility:.1f} km
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                with col6:
                    st.markdown(f"""
                    <div class="metric">
                        <div class="metric-title">
                        Condition
                        </div>

                        <div class="metric-value">
                        {weather}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

            elif response.status_code == 404:
                st.error("City not found.")

            elif response.status_code == 401:
                st.error("Invalid OpenWeather API key.")

            else:
                st.error("Unable to fetch weather data.")

        except Exception as e:
            st.error(f"Error: {e}")
