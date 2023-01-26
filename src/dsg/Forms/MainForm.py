from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView

from src.dsg.uicode.Main_Form import Ui_MainWindow
from src.db.schdl_db import SchdlDB
from src.db.data_list_db import DataListDB


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.data = None
        self.db = None
        self.setupUi(self)
        self.init_schdl_tb()
        self.setup_edit_schdl_screen()
        # self.showFullScreen()

        self.show_schdl_act.triggered.connect(self.show_schdl)
        self.add_schdl_act.triggered.connect(self.show_edit)
        self.write_srvc_act.triggered.connect(self.write_on_service)
        self.schdl_srvc_act.triggered.connect(self.show_schdl_service)
        self.profile_act.triggered.connect(self.show_profile)
        self.exit_act.triggered.connect(self.close)

        self.begin_work.clicked.connect(self.show_schdl)
        self.schdl_upd_tb.clicked.connect(self.update_lesson_schdl_tb)

        # self.lesson_cb

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

    @staticmethod
    def update_schdl_btn_handler():
        db = SchdlDB()
        print(db.get_from_db())

    def update_lesson_schdl_tb(self):

        self.db = SchdlDB()
        tmp_data = self.db.get_from_db()
        self.data = self.db.decode(tmp_data)
        print(self.data)
        col = 0

        for row, row_data in enumerate(self.data):
            for colum, item_tb in enumerate(row_data):
                item = QTableWidgetItem(str(row_data[item_tb]))
                if colum > 0:
                    self.schdl_lesson_tb.setItem(row, col, item)
                    col += 1
                elif col < len(row_data):
                    col = 0

    def init_schdl_tb(self):
        self.schdl_lesson_tb.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.schdl_lesson_tb.setColumnCount(7)
        self.schdl_lesson_tb.setRowCount(10)

    def setup_edit_schdl_screen(self):
        db = DataListDB()
        types_lesson = db.get_from_db_type_lesson()
        lessons = db.get_from_db_lesson()
        teachers = db.get_from_db_teachers()
        auds = db.get_from_db_aud()

        for lesson in lessons:
            self.lesson_cb.addItem(lesson)

        for type_lesson in types_lesson:
            self.type_lesson_cb.addItem(type_lesson)

        for teacher in teachers:
            self.teacher_cb.addItem(teacher)

        for aud in auds:
            self.aud_cb.addItem(aud)

