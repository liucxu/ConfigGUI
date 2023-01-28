from DB.CityConfigBean import CityConfigBean
from DB.DataProviderEnum import DataProviderEnum
from DB.EncryptionTypeEnum import EncryptionTypeEnum


def raw2Bean(rawData, encryptMap, providerMap):
    cityId = rawData[0]
    city = rawData[1]
    encryptionId = str(rawData[2])
    providerId = str(rawData[3])
    cityBean = CityConfigBean(cityId, city, EncryptionTypeEnum(encryptMap[encryptionId]), DataProviderEnum(providerMap[providerId]))
    return cityBean
