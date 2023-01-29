from Config.JsonConfig import CITY_NAME_JSON, AES_KEY_TYPE_JSON, DATA_PROVIDER
from DB.DataProviderEnum import DataProviderEnum
from DB.EncryptionTypeEnum import EncryptionTypeEnum


class CityConfigBean:
    def __init__(self, cityId, city, encryption: EncryptionTypeEnum, provider: DataProviderEnum):
        self.cityId = cityId
        self.city = city
        self.encryption = encryption
        self.provider = provider

    def toDic(self):
        # dictCity = {CITY_NAME_JSON: self.city, AES_KEY_TYPE_JSON: self.encryption.value,
        #             DATA_PROVIDER: self.provider.value}】
        dictCity = {}
        dictCity[CITY_NAME_JSON] = self.city
        dictCity[AES_KEY_TYPE_JSON] = self.encryption.value
        dictCity[DATA_PROVIDER] = self.provider.value
        return dictCity
