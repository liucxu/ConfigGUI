from DB.DataProviderEnum import DataProviderEnum
from DB.EncryptionTypeEnum import EncryptionTypeEnum


class CityConfigBean:
    def __init__(self, city, encryption: EncryptionTypeEnum, provider: DataProviderEnum):
        self.city = city
        self.encryption = encryption
        self.provider = provider
