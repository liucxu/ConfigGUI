from DB.CityConfigBean import CityConfigBean
from DB.CityDataSqlDriver import CityDataSqlDriver
from DB.DataProviderEnum import DataProviderEnum
from DB.EncryptionTypeEnum import EncryptionTypeEnum


class CityDataProvider:
    def __init__(self):
        self.dataCity = []
        self.driver = CityDataSqlDriver()
        self.initDataFromDB()

    def initDataFromDB(self):
        self.dataCity.extend(self.driver.queryServiceCity())

    def refreshData(self, out):
        for city in self.dataCity:
            out.append(city)

    def deleteServiceCity(self, cityId):
        self.driver.deleteServiceCityById(cityId)
        self.initDataFromDB()

    def queryEncryptType(self):
        return self.driver.queryEncryptDic()

    def queryDataProvider(self):
        return self.driver.queryProvider()

    def createCityConfigInfo(self, city):
        self.driver.createCityConfigInfo(city)
        self.initDataFromDB()

    def queryCityByCityName(self, cityName):
        return self.driver.queryCityInfoByCityName(cityName)

    def updateCityServiceInfo(self, city):
        self.driver.updateCityServiceInfo(city)
        self.initDataFromDB()
    # def deleteCityConfig(self, cityInfo:CityConfigBean):
