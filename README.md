# 🌤️ Weather App in Python

A simple beginner-friendly weather application built with **Python**.
The app takes a city name from the user and displays the current weather information without requiring a personal API key.

## ✨ Features

* 🌍 Search weather by city name
* 🌡️ Display current temperature
* 💧 Display humidity
* 🌤️ Display current weather condition
* 🤗 Display "feels like" temperature
* 🔑 No personal API key required

## Technologies Used

* **Python**
* **Requests** – Used to retrieve weather data
* **wttr.in** – Provides the weather information

## Requirements

Make sure Python is installed on your computer.

Install the required Python package:

```bash
pip install requests
```

If you're using VS Code, you can also run:

```bash
python -m pip install requests
```

## 🚀 How to Run

1. Clone or download this repository.

2. Open the project folder in VS Code or your preferred code editor.

3. Install the required package:

```bash
pip install requests
```

4. Run the Python file:

```bash
python weather.py
```

5. Enter the name of a city when prompted.

### Example

```text
Enter city name: Ahmedabad

Weather in Ahmedabad
Temperature: 30 °C
Feels Like: 32 °C
Humidity: 65 %
Condition: Partly cloudy
```

## Project Structure

```text
Weather-App/
│
├── weather.py
└── README.md
```

## Learning Outcomes

This project helped me practice:

* Python programming fundamentals
* Taking user input
* Using external Python libraries
* Sending HTTP requests
* Working with JSON data
* Extracting information from nested data

## Note

This project uses **wttr.in** for weather data and does not require the user to create or manage an API key.
