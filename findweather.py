import requests
from wtforms.validators import ValidationError

weather_key = 'ddeb6cd1bba9b44090562a986ac163d2'
location_key = "b603597dfdc2ef734491d0fa8f499107"
unit = "imperial"

def getWeather():
	location_response = requests.get("http://api.ipstack.com/{}?access_key={}".format("128.195.98.51", location_key))
	location_data = location_response.json()
	city_name = location_data["city"]
	return getWeatherCity(city_name)

def getWeatherCity(city_name):
	response = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(city_name, unit, weather_key))
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(city_name, unit, weather_key)
	data = response.json()
	return data

def validate_city(form, field):
	d = getWeatherCity(field.data)
	if d["cod"] == "404":
		 raise ValidationError('City is not valid')