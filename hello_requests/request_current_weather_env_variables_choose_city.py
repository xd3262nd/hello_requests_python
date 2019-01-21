import requests
import os


key = os.environ.get('WEATHER_KEY')  # Returns None if not found

city = input('Enter city: ')
country = input(f'What country is {city} in? Enter two-letter country code: ')
location = f'{city},{country}'

query = {'q': location, 'units': 'imperial', 'appid': key}

url = 'http://api.openweathermap.org/data/2.5/weather'
data = requests.get(url, params=query).json()
weather_description = data['weather'][0]['description']

temp = data['main']['temp']

print(f'The weather is {weather_description}, the temperature is {temp:.2f}F.')





