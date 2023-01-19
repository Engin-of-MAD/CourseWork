from PySide2.QtWidgets import QMainWindow, QApplication
from dsg.LoginScreen import LoginScreen


class MainWindow(QMainWindow, LoginScreen):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
