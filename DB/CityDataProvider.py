from DB.CityConfigBean import CityConfigBean
from DB.DataProviderEnum import DataProviderEnum
from DB.EncryptionTypeEnum import EncryptionTypeEnum


class CityDataProvider:
    def __init__(self):
        self.dataCity = []
        self.initDataFromDB()

    def initDataFromDB(self):
        city1 = CityConfigBean('WUXI', EncryptionTypeEnum.ECB, DataProviderEnum.DATA_PROVIDER_WUXI)
        city2 = CityConfigBean('WUXI2', EncryptionTypeEnum.CBC, DataProviderEnum.DATA_PROVIDER_TTS)
        city3 = CityConfigBean('WUXI3', EncryptionTypeEnum.ECB, DataProviderEnum.DATA_PROVIDER_BAIDU)
        city4 = CityConfigBean('WUXI4', EncryptionTypeEnum.CBC, DataProviderEnum.DATA_PROVIDER_WUXI)
        city5 = CityConfigBean('WUXI5', EncryptionTypeEnum.ECB, DataProviderEnum.DATA_PROVIDER_TTS)
        city6 = CityConfigBean('WUXI6', EncryptionTypeEnum.CBC, DataProviderEnum.DATA_PROVIDER_BAIDU)
        city7 = CityConfigBean('WUXI7', EncryptionTypeEnum.ECB, DataProviderEnum.DATA_PROVIDER_WUXI)
        city8 = CityConfigBean('WUXI8', EncryptionTypeEnum.CBC, DataProviderEnum.DATA_PROVIDER_TTS)
        self.dataCity.append(city1)
        self.dataCity.append(city2)
        self.dataCity.append(city3)
        self.dataCity.append(city4)
        self.dataCity.append(city5)
        self.dataCity.append(city6)
        self.dataCity.append(city7)
        self.dataCity.append(city8)

    def refreshData(self, out):
        for city in self.dataCity:
            out.append(city)
