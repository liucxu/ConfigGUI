from PyQt6 import QtGui
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QComboBox
from PyQt6.QtCore import Qt

from Config.UIConfig import LABEL_CITY_NAME, LABEL_ENCRYPT_TYPE, LABEL_PROVIDER


class CustomEditDialog(QDialog):
    def __init__(self, title='', confirmFun=None, encryptMap=None, provider=None, updateFun=None, updateCity=None):
        super().__init__()
        self.encryptType = -1
        self.providerId = -1
        self.confirm = confirmFun
        self.setWindowTitle(title)
        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        self.contentLayout = QVBoxLayout()
        self.cityNameLabel = QLabel(LABEL_CITY_NAME)
        self.QLineEditCityName = QLineEdit()
        self.cityH = QHBoxLayout()
        self.cityH.addWidget(self.cityNameLabel)
        self.cityH.addWidget(self.QLineEditCityName)
        self.encryptH = QHBoxLayout()
        self.labelEncrypt = QLabel(LABEL_ENCRYPT_TYPE)
        self.encryptTypeComboBox = QComboBox()
        self.encryptMaps = encryptMap
        self.modelEncryptType = QtGui.QStandardItemModel()
        self.initEncryptComboBox()
        self.encryptH.addWidget(self.labelEncrypt)
        self.encryptH.addWidget(self.encryptTypeComboBox)
        self.encryptH.addStretch(1)
        self.dataProviderH = QHBoxLayout()
        self.dataProviderLabel = QLabel(LABEL_PROVIDER)
        self.dataProviderComboBox = QComboBox()
        self.dataProviderMaps = provider
        self.modelDataProvider = QtGui.QStandardItemModel()
        self.initDataProviderComboBox()
        self.dataProviderH.addWidget(self.dataProviderLabel)
        self.dataProviderH.addWidget(self.dataProviderComboBox)
        self.dataProviderH.addStretch(1)
        self.contentLayout.addLayout(self.cityH)
        self.contentLayout.addLayout(self.encryptH)
        self.contentLayout.addLayout(self.dataProviderH)
        self.layout.addLayout(self.contentLayout)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        self.updateCity = updateCity
        self.updateFun = updateFun
        self.initDataForUpdate()


    def initEncryptComboBox(self):
        for encryptType, encryptName in self.encryptMaps.items():
            it = QtGui.QStandardItem(encryptName)
            it.setData(encryptType)
            self.modelEncryptType.appendRow(it)
        self.encryptTypeComboBox.currentIndexChanged[int].connect(self.OnEncryptIndexChanged)
        self.encryptTypeComboBox.setModel(self.modelEncryptType)

    def initDataProviderComboBox(self):
        for providerId, providerName in self.dataProviderMaps.items():
            it = QtGui.QStandardItem(providerName)
            it.setData(providerId)
            self.modelDataProvider.appendRow(it)
        self.dataProviderComboBox.currentIndexChanged[int].connect(self.OndataProviderIndexSelected)
        self.dataProviderComboBox.setModel(self.modelDataProvider)

    def OnEncryptIndexChanged(self, encryptType):
        self.encryptType = encryptType

    def OndataProviderIndexSelected(self, providerId):
        self.providerId = providerId

    def validate(self):
        if len(self.QLineEditCityName.text().strip()) == 0 or self.encryptType == -1 or self.providerId == -1:
            return False
        return True

    def initDataForUpdate(self):
        if not (self.updateCity is None):
            self.QLineEditCityName.setText(self.updateCity.city)
            allEncryptValues = list(self.encryptMaps.values())
            allProviderValues = list(self.dataProviderMaps.values())
            for index in range(len(allEncryptValues)):
                if allEncryptValues[index] == self.updateCity.encryption.value:
                    self.encryptTypeComboBox.setCurrentIndex(index)
            for index in range(len(allProviderValues)):
                if allProviderValues[index] == self.updateCity.provider.value:
                    self.dataProviderComboBox.setCurrentIndex(index)

    def accept(self) -> None:
        if not (self.confirm is None):
            if self.validate():
                self.confirm((self.QLineEditCityName.text().strip(), self.encryptType, self.providerId), self)
        if not (self.updateFun is None):
            if self.validate():
                self.updateFun((self.QLineEditCityName.text().strip(), self.encryptType, self.providerId), self)
        # self.close()
