from PySide2.QtWidgets import QMainWindow, QApplication
from src.dsg.uicode.LoginScreen import LoginScreen
from src.dsg.Forms.MainScreen import MainForm


class MainScreen(QMainWindow, LoginScreen):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.win = None
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.switch_on_main_screen)

    def switch_on_main_screen(self):
        self.win = MainForm()
        self.win.show()
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    win = MainScreen()
    win.show()
    sys.exit(app.exec_())
