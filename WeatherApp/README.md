# MakaBhosraAAG - Weather App

A simple and responsive weather application built with **Python**, **Streamlit**, and the **OpenWeatherMap API**.

Users can enter any city name and instantly view its current weather information including:

- Temperature
- Humidity
- Wind Speed
- Weather Condition

---

## Preview

> Add a screenshot of your application here.

---

## Features

- Search weather by city name
- Displays:
  - Temperature (°C)
  - Humidity (%)
  - Wind Speed (m/s)
  - Weather Condition
- Clean Streamlit user interface
- Uses the OpenWeatherMap API
- Environment variable support using `.env`

---

## Tech Stack

- Python 3
- Streamlit
- Requests
- Python-dotenv
- OpenWeatherMap API

---

## Project Structure

```text
Weather-App/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get an OpenWeatherMap API Key

Visit:

https://openweathermap.org/api

Create an account and generate your free API key.

### 5. Create a `.env` File

```env
API_KEY=YOUR_OPENWEATHERMAP_API_KEY
```

Example:

```env
API_KEY=1234567890abcdef1234567890abcdef
```

---

## Running the Application

Start the Streamlit server using:

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

---

## How It Works

1. Enter a city name.
2. Click the **Fetch Weather Data** button.
3. The application sends a request to the OpenWeatherMap API.
4. Current weather details are displayed on the screen.

---

## Dependencies

Main libraries used in this project:

- streamlit
- requests
- python-dotenv

Install all dependencies with:

```bash
pip install -r requirements.txt
```

---

## Error Handling

The application handles:

- Invalid city names
- Failed API requests
- Missing API key

---

## Future Improvements

- Current location detection
- Five-day weather forecast
- Dark and light theme support
- Weather icons
- Air Quality Index (AQI)
- Sunrise and sunset information
- Favorite cities
- Interactive weather maps

---

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

---

## Author

**Animesh**

- Cyber Security Student
- Video Editor
- Graphic Designer
- Social Media Manager
