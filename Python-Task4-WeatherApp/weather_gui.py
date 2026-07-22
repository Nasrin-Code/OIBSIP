import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import requests

API_KEY = "API"

window = tk.Tk()
window.title("Weather App")
window.geometry("500x500")
window.configure(bg="#E8F4FF")

title_label = tk.Label(
    window,
    text="Weather App",
    font=("Arial", 18, "bold"),
    bg="#E8F4FF"
)
title_label.pack(pady=5)

input_frame = tk.Frame(window, bg="#E8F4FF")
input_frame.pack(pady=5)

city_label = tk.Label(
    input_frame,
    text="Enter City:",
    font=("Arial", 12),
    bg="#E8F4FF"
)
city_label.pack()

city_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
city_entry.pack(pady=5)

unit = tk.StringVar(value="metric")

radio_frame = tk.Frame(window, bg="#E8F4FF")
radio_frame.pack()

tk.Radiobutton(
    radio_frame,
    text="Celsius",
    variable=unit,
    value="metric",
    bg="#E8F4FF",
    font=("Arial", 11)
).pack(side="left", padx=10)

tk.Radiobutton(
    radio_frame,
    text="Fahrenheit",
    variable=unit,
    value="imperial",
    bg="#E8F4FF",
    font=("Arial", 11)
).pack(side="left", padx=10)

icon_label = tk.Label(window, bg="#E8F4FF")
icon_label.pack(pady=5)

temperature_label = tk.Label(
    window,
    text="Temperature:",
    font=("Arial", 12),
    bg="#E8F4FF"
)
temperature_label.pack()

humidity_label = tk.Label(
    window,
    text="Humidity:",
    font=("Arial", 12),
    bg="#E8F4FF"
)
humidity_label.pack()

weather_label = tk.Label(
    window,
    text="Weather:",
    font=("Arial", 12),
    bg="#E8F4FF"
)
weather_label.pack()

wind_label = tk.Label(
    window,
    text="Wind Speed:",
    font=("Arial", 12),
    bg="#E8F4FF"
)
wind_label.pack()


def get_weather():

    city = city_entry.get().strip()

    if city == "":
        messagebox.showwarning(
            "Input Error",
            "Please enter a city name."
        )
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units={unit.get()}"
    )

    try:

        response = requests.get(url, timeout=10)

        if response.status_code == 401:
            messagebox.showerror(
                "API Error",
                "Invalid API Key."
            )
            return

        if response.status_code == 404:
            messagebox.showerror(
                "City Not Found",
                "Please enter a valid city."
            )
            return

        response.raise_for_status()

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        icon_code = data["weather"][0]["icon"]

        icon_url = (
            f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        )

        icon_response = requests.get(icon_url)
        image = Image.open(BytesIO(icon_response.content))
        icon_image = ImageTk.PhotoImage(image)

        icon_label.config(image=icon_image)
        icon_label.image = icon_image

        if unit.get() == "metric":
            symbol = "°C"
        else:
            symbol = "°F"

        temperature_label.config(
            text=f"Temperature : {temperature} {symbol}"
        )

        humidity_label.config(
            text=f"Humidity : {humidity}%"
        )

        weather_label.config(
            text=f"Weather : {description}"
        )

        wind_label.config(
            text=f"Wind Speed : {wind_speed} m/s"
        )

    except requests.exceptions.Timeout:
        messagebox.showerror(
            "Timeout",
            "The request took too long."
        )

    except requests.exceptions.ConnectionError:
        messagebox.showerror(
            "Network Error",
            "Check your internet connection."
        )

    except requests.exceptions.RequestException as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


get_weather_button = tk.Button(
    input_frame,
    text="Get Weather",
    command=get_weather,
    width=20,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold")
)
get_weather_button.pack(pady=10)

window.mainloop()
