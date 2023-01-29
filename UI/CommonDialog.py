from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class CommonDialog(QDialog):
    def __init__(self, title='', notify='', confirmFun=None,):
        super().__init__()
        self.confirm = confirmFun
        self.setWindowTitle(title)
        QBtn = QDialogButtonBox.StandardButton.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel(notify)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept(self) -> None:
        if not (self.confirm is None):
            self.confirm()
        self.close()
