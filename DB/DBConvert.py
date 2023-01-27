from DB.CityConfigBean import CityConfigBean
from DB.DataProviderEnum import DataProviderEnum
from DB.EncryptionTypeEnum import EncryptionTypeEnum


def raw2Bean(rawData, encryptMap, providerMap):
    city = rawData[0]
    encryptionId = str(rawData[1])
    providerId = str(rawData[2])
    cityBean = CityConfigBean(city, EncryptionTypeEnum(encryptMap[encryptionId]), DataProviderEnum(providerMap[providerId]))
    return cityBean
