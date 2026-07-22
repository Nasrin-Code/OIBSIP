import requests
API_KEY = "API"
city = input("Enter city name:")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
print(url)

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("Weather Report:")
        print("----------------")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Weather:", weather_description)
        print("Wind Speed:", wind_speed, "m/s")

    else:
        print("Error:", data["message"])

except requests.exceptions.RequestException:
    print("Network Error! Check your Internet Connection.")
