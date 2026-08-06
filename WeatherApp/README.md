# Weather App

A simple and responsive weather application built with **Streamlit** that fetches real-time weather information using the **OpenWeatherMap API**.

## Features

- Search weather by city name
- Current temperature
- Weather description
- Humidity
- Wind speed
- Atmospheric pressure
- Visibility
- Cloudiness
- Country information
- Clean and responsive Streamlit interface

## Tech Stack

- Python 3
- Streamlit
- Requests
- python-dotenv
- OpenWeatherMap API

## Project Structure

```
Weather-App/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. Create a virtual environment (Recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Get an OpenWeather API Key

1. Visit https://openweathermap.org/
2. Create a free account.
3. Generate an API key.

## Configure Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_OPENWEATHER_API_KEY
```

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

Default URL:

```
http://localhost:8501
```

## Screenshots

You can add screenshots here.

```
assets/
    screenshot.png
```

Example:

```markdown
![Weather App](assets/screenshot.png)
```

## Requirements

Example `requirements.txt`

```txt
streamlit
requests
python-dotenv
```

You can also generate it automatically:

```bash
pip freeze > requirements.txt
```

## API Used

OpenWeather Current Weather API

Documentation:

https://openweathermap.org/current

## Future Improvements

- 5-Day Weather Forecast
- Hourly Forecast
- Air Quality Index (AQI)
- UV Index
- Sunrise & Sunset
- Interactive Weather Maps
- Auto Location Detection
- Dark/Light Theme Toggle
- Weather Icons and Animations
- Search History

## License

This project is licensed under the MIT License.

## Author

**Your Name**

GitHub: https://github.com/yourusername
