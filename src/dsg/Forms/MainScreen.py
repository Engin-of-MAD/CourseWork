from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PySide2.QtCore import QDateTime

from src.dsg.uicode.Main_Form import Ui_MainWindow
from src.db.schdl_db import SchdlDB
from src.db.data_list_db import DataListDB


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.data = None
        self.send_data = dict(date_time=None,
                              type_lesson=None,
                              lesson=None,
                              teacher=None,
                              aud=None,
                              student=None,
                              day=None
                              )

        self.update_data = dict(date_time=None,
                                type_lesson=None,
                                lesson=None,
                                teacher=None,
                                aud=None,
                                student=None,
                                day=None
                                )
        self.db_data_list = DataListDB()
        self.db_schdl = SchdlDB()

        ##########################################################################################

        self.setupUi(self)
        self.init_edit_schdl()
        self.init_schdl_tb()
        self.setup_edit_schdl_screen()
        self.stackedWidget.setCurrentIndex(0)
        # self.showFullScreen()

        self.edit_screen_schdl_slots()
        self.add_schdl_screen_slots()
        self.menubar_slots()
        self.error_edit_lbl.hide()
        self.error_add_lbl.hide()
        self.begin_work.clicked.connect(self.show_schdl)
        self.schdl_upd_tb.clicked.connect(self.update_lesson_schdl_tb)

    ##########################################################################################

    def add_schdl_screen_slots(self):
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm")
        self.dateTimeEdit.setMinimumDateTime(QDateTime().currentDateTime())

        self.lesson_cb.activated[str].connect(self.set_send_data_lesson)
        self.type_lesson_cb.activated[str].connect(self.set_send_data_type_lesson)
        self.teacher_cb.activated[str].connect(self.set_send_data_teachers)
        self.aud_cb.activated[str].connect(self.set_send_data_aud)
        self.day_cb.activated[str].connect(self.set_send_data_day)
        self.student_cb.activated[str].connect(self.set_send_data_students)

        self.dateTimeEdit.dateTimeChanged.connect(self.set_send_data_time_data)
        self.send_btn.clicked.connect(self.send_data_schdl_handler)

    def menubar_slots(self):
        self.edit_schdl_act.triggered.connect(self.show_edit_schdl)
        self.write_srvc_act.triggered.connect(self.show_write_on_service)
        self.show_schdl_act.triggered.connect(self.show_schdl)
        self.add_schdl_act.triggered.connect(self.show_edit)
        self.schdl_srvc_act.triggered.connect(self.show_schdl_service)
        self.profile_act.triggered.connect(self.show_profile)
        self.exit_act.triggered.connect(self.close)

    def edit_screen_schdl_slots(self):
        self.num_row_sb.valueChanged.connect(self.update_old_data_schdl)

        self.lesson_cb_edit.activated[str].connect(self.set_update_data_lesson)
        self.type_lesson_cb_edit.activated[str].connect(self.set_update_data_type_lesson)
        self.stud_cb_edit.activated[str].connect(self.set_update_data_students)
        self.teacher_cb_edit.activated[str].connect(self.set_update_data_teachers)
        self.day_cb_edit.activated[str].connect(self.set_update_data_day)
        self.aud_cb_edit.activated[str].connect(self.set_update_data_aud)

        self.dateTime_edit.dateTimeChanged.connect(self.set_update_data_time_data)
        self.dateTime_edit.setDisplayFormat("yyyy-MM-dd hh:mm")
        self.dateTime_edit.setMinimumDateTime(QDateTime().currentDateTime())

        self.update_edit_schdl_btn.clicked.connect(self.change_old_data_schdl)

    ##########################################################################################

    def set_update_data_teachers(self, teacher):
        self.update_data.update(teacher=teacher)

    def set_update_data_students(self, student):
        self.update_data.update(student=student)

    def set_update_data_time_data(self):
        date_time = self.dateTimeEdit.dateTime()
        self.update_data.update(date_time=date_time.toString("yyyy-MM-dd hh:mm:ss"))

    def set_update_data_lesson(self, lesson):
        self.update_data.update(lesson=lesson)

    def set_update_data_type_lesson(self, type_lesson):
        self.update_data.update(type_lesson=type_lesson)

    def set_update_data_day(self, day):
        self.update_data.update(day=day)

    def set_update_data_aud(self, aud):
        self.update_data.update(aud=aud)

    ##########################################################################################

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

    ##########################################################################################

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

    ##########################################################################################

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

    def update_old_data_schdl(self):
        data = self.db_schdl.get_from_db_schdl_row(self.num_row_sb.value())

        if data is None:
            self.row_state_lbl.setText("Нет данных")
            self.old_lessons_lbl.setText("Нет данных")
            self.old_teacher_lbl.setText("Нет данных")
            self.old_day_lbl.setText("Нет данных")
            self.old_stud_lbl.setText("Нет данных")
            self.old_type_lesson_lbl.setText("Нет данных")
            self.old_aud_lbl.setText("Нет данных")
            self.old_date_time.setText("Нет данных")
        else:
            data = self.db_schdl.decode_row(data)

            self.row_state_lbl.setText(str(self.num_row_sb.value()))
            self.old_lessons_lbl.setText(data["lessons"])
            self.old_teacher_lbl.setText(data["tchr_id"])
            self.old_day_lbl.setText(data["day"])
            self.old_stud_lbl.setText(data["stud_id"])
            self.old_type_lesson_lbl.setText(data["type_lessons"])
            self.old_aud_lbl.setText(data["aud_id"])
            self.old_date_time.setText(str(data["time"]))

    ##########################################################################################

    def setup_edit_schdl(self):

        types_lesson = self.db_data_list.get_from_db_type_lesson()
        lessons = self.db_data_list.get_from_db_lesson()
        teachers = self.db_data_list.get_from_db_teachers()
        auds = self.db_data_list.get_from_db_aud()
        days = self.db_data_list.get_from_db_day()
        students = self.db_data_list.get_from_db_students()

        for lesson in lessons:
            self.lesson_cb_edit.addItem(lesson)

        for type_lesson in types_lesson:
            self.type_lesson_cb_edit.addItem(type_lesson)

        for teacher in teachers:
            self.teacher_cb_edit.addItem(teacher)

        for aud in auds:
            self.aud_cb_edit.addItem(aud)

        for day in days:
            self.day_cb_edit.addItem(day)

        for student in students:
            self.stud_cb_edit.addItem(student)

    def init_edit_schdl(self):

        types_lesson = self.db_data_list.get_from_db_type_lesson()
        lessons = self.db_data_list.get_from_db_lesson()
        teachers = self.db_data_list.get_from_db_teachers()
        auds = self.db_data_list.get_from_db_aud()
        days = self.db_data_list.get_from_db_day()
        students = self.db_data_list.get_from_db_students()

        for lesson in lessons:
            self.lesson_cb_edit.addItem(lesson)

        for type_lesson in types_lesson:
            self.type_lesson_cb_edit.addItem(type_lesson)

        for teacher in teachers:
            self.teacher_cb_edit.addItem(teacher)

        for aud in auds:
            self.aud_cb_edit.addItem(aud)

        for day in days:
            self.day_cb_edit.addItem(day)

        for student in students:
            self.stud_cb_edit.addItem(student)

    def init_schdl_tb(self):
        self.schdl_lesson_tb.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.schdl_lesson_tb.setColumnCount(7)
        self.schdl_lesson_tb.setRowCount(50)

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

    ##########################################################################################

    def send_data_schdl_handler(self):
        db = self.db_schdl
        if self.send_data['aud'] is not None and self.send_data['teacher'] is not None and self.send_data[
            'type_lesson'] is not None and self.send_data['lesson'] is not None:
            print("Данные отправлены")
            print(self.send_data["teacher"], self.send_data["student"])
            code_data = db.code_row(self.send_data)
            print(code_data)
            db.send_data(code_data)
            self.error_add_lbl.setText("Данные отправлены")
            self.error_add_lbl.setStyleSheet("color: green")
        else:
            self.error_add_lbl.show()
            self.error_add_lbl.setStyleSheet("color: red")

    def change_old_data_schdl(self):
        if self.update_data['aud'] is not None and self.update_data['teacher'] is not None and self.update_data[
            'type_lesson'] is not None and self.update_data['lesson'] is not None:
            db = self.db_schdl
            data_update = self.update_data
            data_update = db.code_row(data_update)
            db.update_row(data_update, self.num_row_sb.value())
            index = self.num_row_sb.value()
            print(f'index: {self.num_row_sb.value()}')
            self.error_edit_lbl.setText("Данные изменены")
            self.error_edit_lbl.setStyleSheet("color: green")
            self.error_edit_lbl.show()
        else:
            print(self.update_data)
            self.error_edit_lbl.show()
            self.error_edit_lbl.setStyleSheet("color: red")

