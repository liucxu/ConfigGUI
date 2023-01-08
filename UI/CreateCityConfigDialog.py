from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel

from Config.UIConfig import TITLE_CREATE_CITY_CONFIG


class CreateCityConfigDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle(TITLE_CREATE_CITY_CONFIG)
        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
