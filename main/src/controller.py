from flask import Flask, jsonify
from data_service import DataService
from datetime import datetime

city = "Kirkby on Bain"
weatherapi_url = 'http://api.weatherapi.com/v1/current.json?key=99df3e2a012f4887b8681628232405&q=' + city + '&aqi=no'
openweather_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=f17a2fb25fcbb581fbdc91627d0afb28'

api = Flask(__name__)

"""
Get the default weather data
"""
@api.route('/weather')
def getWeatherData():
    response =  DataService().getWeatherData(openweather_url)
    # return DataService().getWeatherData(weatherapi_url)

    # Not really needed, just to see what we get back and to check things are working right
    displayWeatherDataFromOpenWeatherApi(city, response)

    return response.json()

# """
# Get the selected weather data
# """
@api.route('/weather/<string:location>')
def getSelectedWeatherData(location: str):
    response = DataService().getWeatherData(getUrlForSelectedLocation(location))

    # Not really needed, just to see what we get back and to check things are working right    
    displayWeatherDataFromOpenWeatherApi(location, response)

    return response.json()
    

"""
Display the weather data returned back from the call to the OpenWeatherApi
"""
def displayWeatherDataFromOpenWeatherApi(city, data):
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f'\n*********************************************************')
    print(f"Weather data for: {city}")
    print(f"As at           : {dt}")
    print(data.json())
    print(f'*********************************************************\n')

def getUrlForSelectedLocation(location):
    # weatherapi_url 
    return 'http://api.weatherapi.com/v1/current.json?key=99df3e2a012f4887b8681628232405&q=' + location + '&aqi=no'

    # # openweather_url 
    # return 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=f17a2fb25fcbb581fbdc91627d0afb28'

"""
Testing of the calls...
"""
getWeatherData()

city = input(f"City to get weather for: ")
getSelectedWeatherData(city)



if __name__ == "__main__":
    api.run(debug = True)