from PyQt6.QtWidgets import QTabWidget, QWidget, QVBoxLayout

from Config.UIConfig import TABNAME_CITY_CONFIG
from UI.CityConfigUI import CityConfigUI


class Tab(QWidget):
    def __init__(self, p):
        super().__init__()
        self.parent = p
        self.layout = QVBoxLayout()
        self.widget = QTabWidget(self.parent)
        self.tabCityConfig = CityConfigUI()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.init()

    def init(self):
        self.widget.addTab(self.tabCityConfig, TABNAME_CITY_CONFIG)
        self.widget.addTab(self.tab2, "Tab 2")
        self.widget.addTab(self.tab3, "Tab 3")
        self.tabcityconfig()
        self.layout.addWidget(self.widget)
        self.parent.setLayout(self.layout)
        # self.tab2UI()
        # self.tab3UI()

    def tabcityconfig(self):
        # layout = QFormLayout()
        # layout.addRow("姓名", QLineEdit())
        # layout.addRow("地址", QLineEdit())
        self.widget.setTabText(0, TABNAME_CITY_CONFIG)
        # self.tabCityConfig.setLayout(layout)
