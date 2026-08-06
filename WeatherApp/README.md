# 🔥 MakaBhosraAAG - Weather App

A simple and responsive weather application built with **Python**, **Streamlit**, and the **OpenWeatherMap API**.

Users can enter any city name and instantly view its current weather information including:

- 🌡️ Temperature
- 💧 Humidity
- 🌬️ Wind Speed
- ☁️ Weather Condition

---

## 📷 Preview

<img width="900" alt="Weather App Preview" src="https://placehold.co/900x450?text=Add+Your+Screenshot+Here">

> Replace the image above with a screenshot of your application.

---

## 🚀 Features

- Search weather by city name
- Displays:
  - Temperature (°C)
  - Humidity (%)
  - Wind Speed (m/s)
  - Weather Condition
- Clean Streamlit UI
- Uses OpenWeatherMap API
- Environment variable support using `.env`

---

## 🛠️ Tech Stack

- Python 3
- Streamlit
- Requests
- Python-dotenv
- OpenWeatherMap API

---

## 📂 Project Structure

```
Weather-App/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-app.git
```

```bash
cd weather-app
```

---

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

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Get an OpenWeatherMap API Key

Visit:

https://openweathermap.org/api

Create an account and generate your free API key.

---

### 5. Create a `.env` file

```env
API_KEY=YOUR_OPENWEATHERMAP_API_KEY
```

Example:

```env
API_KEY=1234567890abcdef1234567890abcdef
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📌 How It Works

1. Enter a city name.
2. Click **Fetch Weather Data**.
3. The app sends a request to the OpenWeatherMap API.
4. The weather information is displayed using Streamlit metrics.

---

## 📦 Dependencies

Major libraries used:

- streamlit
- requests
- python-dotenv

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## ❗ Error Handling

The application handles:

- Invalid city names
- Failed API requests
- Missing API key

---

## 🔮 Future Improvements

- 🌍 Detect current location
- 📅 5-Day Weather Forecast
- 🌙 Dark/Light Mode
- 🌦️ Weather Icons
- 📈 Air Quality Index
- 🌅 Sunrise & Sunset Time
- ❤️ Favorite Cities
- 🗺️ Interactive Weather Maps

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Animesh**

- Cyber Security Student
- Video Editor
- Graphic Designer
- Social Media Manager

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
