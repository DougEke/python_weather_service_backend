import requests

class DataModel:
    def __init__(self):
        self.__message = "===> DataModel..."

    # Display weather data back in a formatted way, retrieved via weatherapi
    def getWeatherDataFromWeatherApi(self, url):
        return requests.get(url)
    
    # Display weather data back in a formatted way, retrieved via the openweatherapi
    def getWeatherDataFromOpenWeatherApi(self, url):
        print(self.__message)
        return requests.get(url)

    