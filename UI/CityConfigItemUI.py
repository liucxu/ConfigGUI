from PyQt6 import QtCore
from PyQt6.QtCore import QLine
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QHBoxLayout, QWidget, QPushButton

from Config.UIConfig import ITEM_CITY, ITEM_ENCRYPTION, ITEM_PROVIDER, BUTTONNAME_MODIFY, BUTTONNAME_DELETE
from DB.CityConfigBean import CityConfigBean


class CityConfigItemWidget(QWidget):
    editClicked = QtCore.pyqtSignal()
    delClicked = QtCore.pyqtSignal()

    def __init__(self, cityInfo: CityConfigBean, index):
        super().__init__()
        self.textQLabelCityPinYin = QLabel()
        self.textCity = QLabel()
        self.city = cityInfo
        self.index = index
        self.layoutVertical = QVBoxLayout()
        self.horizonCityLayout = QHBoxLayout()
        self.setLabelText(self.textQLabelCityPinYin, self.city.city)
        self.setLabelText(self.textCity, ITEM_CITY)
        self.horizonCityLayout.addWidget(self.textCity)
        self.horizonCityLayout.addWidget(self.textQLabelCityPinYin)
        self.encryption = QLabel()
        self.encryptionType = QLabel()
        self.horizonEncryption = QHBoxLayout()
        self.setLabelText(self.encryption, ITEM_ENCRYPTION)
        self.setLabelText(self.encryptionType, self.city.encryption.value)
        self.horizonEncryption.addWidget(self.encryption)
        self.horizonEncryption.addWidget(self.encryptionType)
        self.provider = QLabel()
        self.providerType = QLabel()
        self.horizonDataProvider = QHBoxLayout()
        self.setLabelText(self.provider, ITEM_PROVIDER)
        self.setLabelText(self.providerType, self.city.provider.value)
        self.horizonDataProvider.addWidget(self.provider)
        self.horizonDataProvider.addWidget(self.providerType)
        self.buttonsLayout = QHBoxLayout()
        self.modifyButton = QPushButton(BUTTONNAME_MODIFY)
        self.deleteButton = QPushButton(BUTTONNAME_DELETE)
        self.buttonsLayout.addStretch(1)
        self.buttonsLayout.addWidget(self.modifyButton)
        self.buttonsLayout.addWidget(self.deleteButton)
        self.modifyButton.clicked.connect(self.editClicked)
        self.deleteButton.clicked.connect(self.delClicked)
        self.layoutVertical.addLayout(self.horizonCityLayout)
        self.layoutVertical.addLayout(self.horizonEncryption)
        self.layoutVertical.addLayout(self.horizonDataProvider)
        self.layoutVertical.addLayout(self.buttonsLayout)
        self.setLayout(self.layoutVertical)

    def setLabelText(self, label: QLabel, text, style=None):
        label.setText(text)
        if not (style is None):
            label.setStyleSheet(style)
