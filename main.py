from PySide2.QtWidgets import QMainWindow, QApplication

from src.dsg.uicode.LoginScreen import Ui_LoginScreen
from src.dsg.Forms.MainScreen import MainForm


class MainScreen(QMainWindow, Ui_LoginScreen):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.win = None
        self.setupUi(self)
        self.enter_btn.clicked.connect(self.switch_on_main_screen)
        self.exit_btn.clicked.connect(self.close)
        self.setup_msg_error()
        self.login = self.login_edit.text()
        self.password = self.pswd_edit.text()

    def setup_msg_error(self):
        self.error_lbl.hide()

    def switch_on_main_screen(self):
        self.login = self.login_edit.text()
        self.password = self.pswd_edit.text()
        print(self.login, self.password)

        if self.login == "adm" and self.password == "admin":
            self.win = MainForm()
            self.error_lbl.hide()
            self.win.show()
            self.close()
        else:
            self.error_lbl.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    win = MainScreen()
    win.show()
    sys.exit(app.exec_())
