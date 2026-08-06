import streamlit as st
import requests  
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="MakaBhosraAAG", page_icon="🔥")

st.title('🔥 MakaBhosraAAG') 
st.write('Enter the City Name and Click on the button to get Weather data')
city = st.text_input('Enter the City Name')
API_KEY = os.getenv('API_KEY')
API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

if st.button('Fetch Weather Data'):
    response = requests.get(API_URL)
    if(response.status_code == 200):
        st.success('Weather Data fetched Successfully!')       
        data = response.json()

        # Extract the values
        temprature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather = data['weather'][0]['main']
        name = data['name']
        Country = data['sys']['country']

        st.subheader(f'{name},{Country}')

        print(temprature, humidity,weather,wind_speed)
        # Create 4 Colomns
        col1, col2, = st.columns(2)
        col3, col4, = st.columns(2)

        # Display the values in UI
        col1.metric('Temprature',f'{temprature}°C')
        col2.metric('Humidity',f'{humidity}%')
        col3.metric('Speed',f'{wind_speed} m/s')
        col4.metric('Weather',f'{weather}')
    else:
        st.error('Invalid City Name')

