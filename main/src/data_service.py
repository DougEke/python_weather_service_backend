from data_model import DataModel

class DataService:
    def __init__(self):        
        self.__message = "===> DataService..."
        self.__dataModel = DataModel()

    def getWeatherData(self, url):
        print(self.__message)
        return self.__dataModel.getWeatherDataFromOpenWeatherApi(url)
