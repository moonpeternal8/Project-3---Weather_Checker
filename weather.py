import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()

current = data["current_condition"][0]

while True:
    print(f"\nWeather in {city}")
    print("Temperature:", current["temp_C"], "°C")
    print("Feels Like:", current["FeelsLikeC"], "°C")
    print("Humidity:", current["humidity"], "%")
    print("Condition:", current["weatherDesc"][0]["value"])