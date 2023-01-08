from PyQt6 import QtCore
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QHBoxLayout

from Config.UIConfig import BUTTONNAME_CREATE, BUTTONNAME_MODIFY, BUTTONNAME_CONFIRM, NOTIFY_TITLE_DIALOG, \
    NOTIFY_MSG_DELETE_DIALOG
from DB.CityDataProvider import CityDataProvider
from UI.CityConfigItemUI import CityConfigItemWidget
from UI.CommonDialog import CommonDialog
from UI.CreateCityConfigDialog import CreateCityConfigDialog


class CityConfigUI(QWidget):
    def __init__(self):
        super().__init__()
        self.buttonsLayout = None
        self.list = QListWidget(self)
        self.list.setStyleSheet("QListWidget::item { border-bottom: 1px solid gray; }")
        self.vbox = QVBoxLayout()
        self.confirmButton = QPushButton(BUTTONNAME_CONFIRM)
        self.showMaximized()
        self.initUI()
        self.selectedIndex = -1
        self.flagChanged = False
        self.widget = None

    @DeprecationWarning
    def initUIDeperate(self):
        self.list.addItems(['sparrow', 'robin', 'crow', 'raven',
                            'woopecker', 'hummingbird', 'sparrow', 'robin', 'crow', 'raven',
                            'woopecker', 'hummingbird', 'sparrow', 'robin', 'crow', 'raven',
                            'woopecker', 'hummingbird', 'sparrow', 'robin', 'crow', 'raven',
                            'woopecker', 'hummingbird', 'sparrow', 'robin', 'crow', 'raven',
                            'woopecker', 'hummingbird', 'sparrow', 'robin', 'crow', 'raven',
                            'woopecker', 'hummingbird', 'sparrow', 'robin', 'crow', 'raven',
                            'woopecker', 'hummingbird', 'sparrow', 'robin', 'crow', 'raven',
                            'woopecker', 'hummingbird'])
        self.vbox.addWidget(self.list)
        self.initButtons()
        self.vbox.addLayout(self.buttonsLayout)
        self.setLayout(self.vbox)

    def initButtons(self):
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addStretch(1)
        self.buttonsLayout.addWidget(self.confirmButton)
        self.confirmButton.clicked.connect(self.onConfirmClicked)

    def onDialogCreateClicked(self):
        createDialog = CreateCityConfigDialog(self)
        createDialog.exec()

    def onDialogUpdateClicked(self):
        createDialog = CreateCityConfigDialog(self)
        createDialog.exec()

    def onConfirmClicked(self):
        createDialog = CreateCityConfigDialog(self)
        createDialog.exec()

    def onDialogDelClicked(self):
        toConfirmDeleteDialog = CommonDialog(NOTIFY_TITLE_DIALOG, NOTIFY_MSG_DELETE_DIALOG, confirmFun=self.deleteItem)
        self.widget = self.sender()
        toConfirmDeleteDialog.exec()
        # gp = widget.mapToGlobal(QtCore.QPoint())
        # lp = self.list.viewport().mapFromGlobal(gp)
        # row = self.list.row(self.list.itemAt(lp))
        # toDeleteItem = self.list.takeItem(row)
        # print(str(toDeleteItem))

    def deleteItem(self):
        self.flagChanged = True
        print('待删除的City信息,name: %s' % self.widget.city.city)

    def initUI(self):
        datas = []
        CityDataProvider().refreshData(datas)
        for index in range(0, len(datas)):
            city = datas[index]
            item = CityConfigItemWidget(city, index)
            #
            # item delete and edit
            #
            item.delClicked.connect(self.onDialogDelClicked)
            item.editClicked.connect(self.onDialogUpdateClicked)
            myQListWidgetItem = QListWidgetItem(self.list)
            myQListWidgetItem.setSizeHint(item.sizeHint())
            self.list.addItem(myQListWidgetItem)
            self.list.setItemWidget(myQListWidgetItem, item)
        # self.setCentralWidget(self.list)
        self.vbox.addWidget(self.list)
        self.initButtons()
        self.vbox.addLayout(self.buttonsLayout)
        self.setLayout(self.vbox)
