import tkinter as tk
from tkinter import messagebox
import requests

# (Replace 'YOUR_API_KEY' with your actual API key)
API_KEY = 'YOUR_API_KEY'

def get_weather(city):
    try:
  
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

        response = requests.get(url)
        data = response.json()
  
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        result_label.config(text=f'Temperature: {temperature}°C\nDescription: {description}')
    except Exception as e:
        messagebox.showerror('Error', f'Error fetching weather data: {str(e)}')

def get_weather_button_clicked():
    city = city_entry.get()
    if city:
        get_weather(city)
    else:
        messagebox.showwarning('Warning', 'Please enter a city name.')

app = tk.Tk()
app.title('Weather Checking System')

city_label = tk.Label(app, text='Enter City:')
city_label.pack(pady=10)

city_entry = tk.Entry(app)
city_entry.pack(pady=10)

get_weather_button = tk.Button(app, text='Get Weather', command=get_weather_button_clicked)
get_weather_button.pack(pady=10)

result_label = tk.Label(app, text='')
result_label.pack(pady=10)

app.mainloop()
