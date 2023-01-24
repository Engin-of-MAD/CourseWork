from PySide2.QtWidgets import QMainWindow, QStackedLayout, QSizePolicy
from src.dsg.uicode.Main_Form import Ui_MainWindow
from src.dsg.Forms.Schedule_show import ShowSchedule


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show_act.triggered.connect(self.show_schdl)

    def show_schdl(self):
       self.stackedWidget.setCurrentIndex(0)


