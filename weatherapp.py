from flask import Flask, render_template, request, url_for, redirect
from datetime import datetime
from findweather import getWeather, getWeatherCity
import requests
from forms import CityForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '90ee623631701c2469c7b9a37106cf6b01fd31ed'

"""
city_name = "Irvine"
weather_key = 'ddeb6cd1bba9b44090562a986ac163d2'
location_key = "b603597dfdc2ef734491d0fa8f499107"
location_response = requests.get("http://api.ipstack.com/{}?access_key={}".format("128.195.98.51", location_key))
location_data = location_response.json()
city_name = location_data["city"]
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}units={}&appid={}'.format(city_name,'imperial', weather_key))
data = response.json()"""



@app.route('/test')
def test():
	data = getWeatherCity("Houston")
	return str(data)

@app.route('/', methods=["GET", "POST"])
def index():
	data = getWeather()
	form = CityForm()
	if form.validate_on_submit():
		data = getWeatherCity(form.city_name.data)
		return render_template('index.html', data=data, form=form)
	return render_template('index.html', data=data, form=form)


if __name__ == "__main__":
	app.run(debug=True)

