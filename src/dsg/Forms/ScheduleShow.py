from PySide2.QtWidgets import QWidget, QHeaderView
from src.dsg.uicode.ShowSchedule import Ui_ShowSchedule



class ShowSchedule(QWidget, Ui_ShowSchedule):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.schld_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
