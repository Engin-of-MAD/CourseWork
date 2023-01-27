import datetime

from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PySide2.QtCore import QDateTime
from datetime import datetime

from src.dsg.uicode.Main_Form import Ui_MainWindow
from src.db.schdl_db import SchdlDB
from src.db.data_list_db import DataListDB


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.send_data = self.send_data = dict(date_time=None,
                                               type_lesson=None,
                                               lesson=None,
                                               teacher=None,
                                               aud=None,
                                               student=None,
                                               day=None
                                               )

        self.data = None
        self.db_data_list = DataListDB()
        self.db_schdl = SchdlDB()
        self.setupUi(self)
        self.init_schdl_tb()
        self.setup_edit_schdl_screen()
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        # self.showFullScreen()
        self.stackedWidget.setCurrentIndex(0)

        self.edit_schdl_act.triggered.connect(self.show_edit_schdl)
        self.write_srvc_act.triggered.connect(self.show_write_on_service)
        self.show_schdl_act.triggered.connect(self.show_schdl)
        self.add_schdl_act.triggered.connect(self.show_edit)
        self.schdl_srvc_act.triggered.connect(self.show_schdl_service)
        self.profile_act.triggered.connect(self.show_profile)
        self.exit_act.triggered.connect(self.close)

        self.begin_work.clicked.connect(self.show_schdl)
        self.schdl_upd_tb.clicked.connect(self.update_lesson_schdl_tb)

        self.lesson_cb.activated[str].connect(self.set_send_data_lesson)
        self.type_lesson_cb.activated[str].connect(self.set_send_data_type_lesson)
        self.teacher_cb.activated[str].connect(self.set_send_data_teachers)
        self.aud_cb.activated[str].connect(self.set_send_data_aud)
        self.day_cb.activated[str].connect(self.set_send_data_day)
        self.student_cb.activated[str].connect(self.set_send_data_students)
        self.dateTimeEdit.dateTimeChanged.connect(self.set_send_data_time_data)
        # self.lesson_cb
        self.send_btn.clicked.connect(self.send_data_schdl_handler)

    def set_send_data_teachers(self, teacher):
        self.send_data.update(teacher=teacher)

    def set_send_data_students(self, student):
        self.send_data.update(student=student)

    def set_send_data_time_data(self):
        date_time = self.dateTimeEdit.dateTime()
        self.send_data.update(date_time=date_time.toString("yyyy-MM-dd hh:mm:ss"))

    def set_send_data_lesson(self, lesson):
        self.send_data.update(lesson=lesson)

    def set_send_data_type_lesson(self, type_lesson):
        self.send_data.update(type_lesson=type_lesson)

    def set_send_data_day(self, day):
        self.send_data.update(day=day)

    def set_send_data_aud(self, aud):
        self.send_data.update(aud=aud)

    def show_schdl(self):
        self.stackedWidget.setCurrentIndex(1)

    def show_edit(self):
        self.stackedWidget.setCurrentIndex(2)

    def show_write_on_service(self):
        self.stackedWidget.setCurrentIndex(4)

    def show_schdl_service(self):
        self.stackedWidget.setCurrentIndex(5)

    def show_profile(self):
        self.stackedWidget.setCurrentIndex(6)

    def show_edit_schdl(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_greeting_screen(self):
        self.stackedWidget.setCurrentIndex(0)

    @staticmethod
    def update_schdl_btn_handler():
        db = SchdlDB()
        print(db.get_from_db())

    def update_lesson_schdl_tb(self):

        self.db_data_list = SchdlDB()
        tmp_data = self.db_data_list.get_from_db()
        self.data = self.db_data_list.decode(tmp_data)
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
        self.schdl_lesson_tb.setRowCount(20)

    def setup_edit_schdl_screen(self):
        types_lesson = self.db_data_list.get_from_db_type_lesson()
        lessons = self.db_data_list.get_from_db_lesson()
        teachers = self.db_data_list.get_from_db_teachers()
        auds = self.db_data_list.get_from_db_aud()
        days = self.db_data_list.get_from_db_day()
        students = self.db_data_list.get_from_db_students()

        for lesson in lessons:
            self.lesson_cb.addItem(lesson)

        for type_lesson in types_lesson:
            self.type_lesson_cb.addItem(type_lesson)

        for teacher in teachers:
            self.teacher_cb.addItem(teacher)

        for aud in auds:
            self.aud_cb.addItem(aud)

        for day in days:
            self.day_cb.addItem(day)

        for student in students:
            self.student_cb.addItem(student)

    def send_data_schdl_handler(self):
        db = SchdlDB()
        if self.send_data['aud'] is not None and self.send_data['teacher'] is not None and self.send_data['type_lesson'] is not None and self.send_data['lesson'] is not None:
            print("Данные отправлены")
            code_data = db.code_row(self.send_data)
            print(code_data)
            self.db_schdl.send_data_in_schdl(code_data)
        else:
            print("Ошибка")
