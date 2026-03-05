#Import requests. Import rich for color coding. Import datetime to convert timestamp into day of the week. 
import requests
from rich import print
from datetime import datetime


#STEP 2 API Integration
#Develop a function to display city weather
def display_current_weather(city):
  """Display current weather""" 
  api_key = 
  api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}"

#Make a request of api_url to verify it works. Should give you [Response 200]
  response = requests.get(api_url)

#Convert into a json (too see all the information). Create a new variable. 
  current_weather_data = response.json()

#Extract specific info like city and temperature. Replace variable names in the print message section. 
  current_weather_city = current_weather_data['city']
  current_weather_temperature = round(current_weather_data['temperature']['current'])
  fahrenheit_temp = round(current_weather_temperature * 9 / 5) + 32

  #print(current_weather_data)

  
  print(f"Today: {current_weather_temperature}ºC / [blue bold] {fahrenheit_temp}ºF [/blue bold]")
##END STEP 2 API Integration

#STEP 3 Weekly Forecast Function
#create a function to display the forecast
def display_forecast_weather(city_name):
  """Display weekly forecast"""
  api_key = 
  api_url = f"https://api.shecodes.io/weather/v1/forecast?query={city_name}&key={api_key}"
  
  response = requests.get(api_url)
  forecast_weather_data = response.json()

  print("\n[bold underline]Forecast:[/bold underline] ")


  for day in forecast_weather_data['daily']:
    timestamp = day['time']
    date = datetime.fromtimestamp(timestamp)
    formatted_day = date.strftime("%A")
    temperature = day['temperature']['day']
    fahrenheit_temp = (temperature * 9 / 5) + 32


    if date.date() != datetime.today().date():
      print(f"\n{formatted_day}:[bold] {round(temperature)}ºC[bold] / [blue bold] {round(fahrenheit_temp)} ºF[/blue bold]")

def welcome():
  print("\n[bold]Welcome to my Weather App![/bold]:bug:")

  
def credit():
  print("\n[yellow]This app was created by Leticia Gmx:bug:[/yellow]")

  

##END STEP 3 Weekly Forecast Function
welcome()
city_name = input("\nEnter a city: ").strip().capitalize()

if city_name:
  display_current_weather(city_name)
  display_forecast_weather(city_name)
  credit()
  

else:
  print("Invalid city name.")
