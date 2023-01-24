from PySide2.QtWidgets import QMainWindow
from src.dsg.uicode.Main_Form import Ui_MainWindow



class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showFullScreen()
        self.show_schdl_act.triggered.connect(self.show_schdl)
        self.edit_schdl_act.triggered.connect(self.show_edit)
        self.write_srvc_act.triggered.connect(self.write_on_service)
        self.schdl_srvc_act.triggered.connect(self.show_schdl_service)
        self.profile_act.triggered.connect(self.show_profile)
        self.exit_act.triggered.connect(self.close)
        self.begin_work.clicked.connect(self.show_schdl)

    def show_schdl(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_edit(self):
        self.stackedWidget.setCurrentIndex(2)

    def write_on_service(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_schdl_service(self):
        self.stackedWidget.setCurrentIndex(4)

    def show_profile(self):
        self.stackedWidget.setCurrentIndex(5)
