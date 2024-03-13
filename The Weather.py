import requests
from tkinter import *
from tkinter import messagebox

api = "fecaf5706bb720e13c2fb056792984a9"
url = "https://api.openweathermap.org/data/2.5/weather"



def weather():
    city = entry.get()
    if city == 0:
        messagebox.showinfo(message="Please enter the city !")
    request_url = f"{url}?q={city},{'RO'}&appid={api}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['main']
        weather_data = Label(text=f"{weather} C")
        weather_data.grid(column=1, row=2, pady=20)
        temp_min = round(data['main']['temp_min'] - 273.15, 2)
        temp_min_data = Label(text=f"{temp_min} C")
        temp_min_data.grid(column=1, row=3, pady=20)
        temperature = data['main']['temp']
        temp_convert = round(temperature - 273.15, 2)
        temp_convert_data = Label(text=f"{temp_convert} C")
        temp_convert_data.grid(column=1, row=5, pady=20)



    else:
        messagebox.showinfo(title="Error", message="Somthing rong , please try again and write correctly !")

window = Tk()
window.title("Weather")
window.config(padx=50, pady=30)

title = Label(text="Romania Weather !")
title.grid(column=0, row=0, pady=20)

label = Label(text="Weather in : ")
label.grid(column=0, row=1, pady=20)

entry = Entry()
entry.grid(column=1, row=1, pady=20)

weather_l = Label(text="Weather : ")
weather_l.grid(column=0, row=2, pady=20)

temp_min_l = Label(text="Temp Min : ")
temp_min_l.grid(column=0, row=3, pady=20)

temp_convert_l = Label(text="Temp Now : ")
temp_convert_l.grid(column=0, row=5, pady=20)


button = Button(text="click", width=15, command=weather)
button.grid(column=0, row=6, pady=20)

window.mainloop()