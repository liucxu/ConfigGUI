import sys
from PyQt6.QtWidgets import QApplication, QWidget

from Config.UIConfig import WIDTH_WINDOW, HEIGHT_WINDOW, XPOINT_WINDOW, YPOINT_WINDOW, TITLE_WINDOW
from UI.Tab import Tab


class MainUI:
    def __init__(self):
        self.tab = None
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.init()

    def init(self):
        self.window.resize(WIDTH_WINDOW, HEIGHT_WINDOW)
        self.window.move(XPOINT_WINDOW, YPOINT_WINDOW)
        self.window.setWindowTitle(TITLE_WINDOW)
        self.tab = Tab(self.window)

    def show(self):
        self.window.show()
        sys.exit(self.app.exec())
