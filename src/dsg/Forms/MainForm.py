from PySide2.QtWidgets import QMainWindow, QStackedLayout, QSizePolicy
from src.dsg.uicode.Main_Form import Ui_MainWindow
from src.dsg.Forms.Schedule_show import ShowSchedule


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.widget1 = ShowSchedule()
        self.widget1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setLayout(QStackedLayout(self))
        self.layout().addWidget(self.widget1)

        self.setupUi(self)
        self.show_act.triggered.connect(self.show_schdl)

    def show_schdl(self):
        self.stack_layout.setCurrentIndex(0)


