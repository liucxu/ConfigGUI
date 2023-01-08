from enum import Enum

from Config import UIConfig


class EncryptionTypeEnum(Enum):
    ECB = UIConfig.ECB
    CBC = UIConfig.CBC
