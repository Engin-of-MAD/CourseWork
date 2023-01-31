# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(779, 709)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.show_schdle = QAction(MainWindow)
        self.show_schdle.setObjectName(u"show_schdle")
        self.show_schdl_act = QAction(MainWindow)
        self.show_schdl_act.setObjectName(u"show_schdl_act")
        self.edit_schdl_act = QAction(MainWindow)
        self.edit_schdl_act.setObjectName(u"edit_schdl_act")
        self.select_act = QAction(MainWindow)
        self.select_act.setObjectName(u"select_act")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.write_srvc_act = QAction(MainWindow)
        self.write_srvc_act.setObjectName(u"write_srvc_act")
        self.schdl_srvc_act = QAction(MainWindow)
        self.schdl_srvc_act.setObjectName(u"schdl_srvc_act")
        self.list_srvc = QAction(MainWindow)
        self.list_srvc.setObjectName(u"list_srvc")
        self.profile_act = QAction(MainWindow)
        self.profile_act.setObjectName(u"profile_act")
        self.exit_act = QAction(MainWindow)
        self.exit_act.setObjectName(u"exit_act")
        self.add_schdl_act = QAction(MainWindow)
        self.add_schdl_act.setObjectName(u"add_schdl_act")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setPointSize(7)
        self.stackedWidget.setFont(font)
        self.GreetingScreen = QWidget()
        self.GreetingScreen.setObjectName(u"GreetingScreen")
        self.gridLayout_10 = QGridLayout(self.GreetingScreen)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.greeting_lbl = QLabel(self.GreetingScreen)
        self.greeting_lbl.setObjectName(u"greeting_lbl")
        font1 = QFont()
        font1.setPointSize(36)
        self.greeting_lbl.setFont(font1)
        self.greeting_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.greeting_lbl, 1, 0, 1, 3)

        self.begin_work = QPushButton(self.GreetingScreen)
        self.begin_work.setObjectName(u"begin_work")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.begin_work.sizePolicy().hasHeightForWidth())
        self.begin_work.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(11)
        self.begin_work.setFont(font2)

        self.gridLayout_10.addWidget(self.begin_work, 3, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 3, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_10.addItem(self.verticalSpacer_8, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.GreetingScreen)
        self.ShowSchedule = QWidget()
        self.ShowSchedule.setObjectName(u"ShowSchedule")
        self.gridLayout_5 = QGridLayout(self.ShowSchedule)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.schdl_upd_tb = QPushButton(self.ShowSchedule)
        self.schdl_upd_tb.setObjectName(u"schdl_upd_tb")
        self.schdl_upd_tb.setFont(font2)

        self.gridLayout_5.addWidget(self.schdl_upd_tb, 5, 1, 1, 1)

        self.label_2 = QLabel(self.ShowSchedule)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(24)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 5, 2, 1, 1)

        self.schdl_lesson_tb = QTableWidget(self.ShowSchedule)
        if (self.schdl_lesson_tb.columnCount() < 7):
            self.schdl_lesson_tb.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.schdl_lesson_tb.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.schdl_lesson_tb.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.schdl_lesson_tb.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.schdl_lesson_tb.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.schdl_lesson_tb.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.schdl_lesson_tb.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.schdl_lesson_tb.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.schdl_lesson_tb.setObjectName(u"schdl_lesson_tb")
        self.schdl_lesson_tb.setFont(font2)

        self.gridLayout_5.addWidget(self.schdl_lesson_tb, 3, 0, 1, 3)

        self.verticalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_11, 0, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_12, 2, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(10, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.verticalSpacer_13, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.ShowSchedule)
        self.EditSrvc = QWidget()
        self.EditSrvc.setObjectName(u"EditSrvc")
        self.gridLayout_3 = QGridLayout(self.EditSrvc)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_11, 7, 4, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 2, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 10, 3, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(100)
        self.gridLayout_4.setVerticalSpacing(30)
        self.day_cb = QComboBox(self.EditSrvc)
        self.day_cb.setObjectName(u"day_cb")
        font4 = QFont()
        font4.setPointSize(13)
        self.day_cb.setFont(font4)

        self.gridLayout_4.addWidget(self.day_cb, 5, 2, 1, 1)

        self.lesson_cb = QComboBox(self.EditSrvc)
        self.lesson_cb.setObjectName(u"lesson_cb")
        self.lesson_cb.setFont(font4)

        self.gridLayout_4.addWidget(self.lesson_cb, 2, 2, 1, 1)

        self.teacher = QLabel(self.EditSrvc)
        self.teacher.setObjectName(u"teacher")
        self.teacher.setFont(font4)

        self.gridLayout_4.addWidget(self.teacher, 3, 0, 1, 1)

        self.audition = QLabel(self.EditSrvc)
        self.audition.setObjectName(u"audition")
        self.audition.setFont(font4)

        self.gridLayout_4.addWidget(self.audition, 4, 0, 1, 1)

        self.lessob_lbl = QLabel(self.EditSrvc)
        self.lessob_lbl.setObjectName(u"lessob_lbl")
        self.lessob_lbl.setFont(font4)

        self.gridLayout_4.addWidget(self.lessob_lbl, 2, 0, 1, 1)

        self.type_lesson_cb = QComboBox(self.EditSrvc)
        self.type_lesson_cb.setObjectName(u"type_lesson_cb")
        self.type_lesson_cb.setFont(font4)

        self.gridLayout_4.addWidget(self.type_lesson_cb, 1, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.teacher_cb = QComboBox(self.EditSrvc)
        self.teacher_cb.setObjectName(u"teacher_cb")
        self.teacher_cb.setFont(font4)

        self.gridLayout_4.addWidget(self.teacher_cb, 3, 2, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.EditSrvc)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setFont(font4)

        self.gridLayout_4.addWidget(self.dateTimeEdit, 0, 2, 1, 1)

        self.type_lesson_lbl = QLabel(self.EditSrvc)
        self.type_lesson_lbl.setObjectName(u"type_lesson_lbl")
        sizePolicy.setHeightForWidth(self.type_lesson_lbl.sizePolicy().hasHeightForWidth())
        self.type_lesson_lbl.setSizePolicy(sizePolicy)
        self.type_lesson_lbl.setFont(font4)

        self.gridLayout_4.addWidget(self.type_lesson_lbl, 1, 0, 1, 1)

        self.aud_cb = QComboBox(self.EditSrvc)
        self.aud_cb.setObjectName(u"aud_cb")
        self.aud_cb.setFont(font4)

        self.gridLayout_4.addWidget(self.aud_cb, 4, 2, 1, 1)

        self.date_lbl = QLabel(self.EditSrvc)
        self.date_lbl.setObjectName(u"date_lbl")
        self.date_lbl.setFont(font4)

        self.gridLayout_4.addWidget(self.date_lbl, 0, 0, 1, 1)

        self.label_6 = QLabel(self.EditSrvc)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.gridLayout_4.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_5 = QLabel(self.EditSrvc)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)

        self.student_cb = QComboBox(self.EditSrvc)
        self.student_cb.setObjectName(u"student_cb")
        self.student_cb.setFont(font4)

        self.gridLayout_4.addWidget(self.student_cb, 6, 2, 1, 1)

        self.send_btn = QPushButton(self.EditSrvc)
        self.send_btn.setObjectName(u"send_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy2)
        self.send_btn.setFont(font2)

        self.gridLayout_4.addWidget(self.send_btn, 7, 1, 1, 1)

        self.error_add_lbl = QLabel(self.EditSrvc)
        self.error_add_lbl.setObjectName(u"error_add_lbl")
        font5 = QFont()
        font5.setPointSize(10)
        self.error_add_lbl.setFont(font5)
        self.error_add_lbl.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.error_add_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.error_add_lbl, 7, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 7, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 7, 0, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_21, 0, 3, 1, 1)

        self.label_4 = QLabel(self.EditSrvc)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 1, 3, 1, 1)

        self.stackedWidget.addWidget(self.EditSrvc)
        self.EditSchdl = QWidget()
        self.EditSchdl.setObjectName(u"EditSchdl")
        self.gridLayout_7 = QGridLayout(self.EditSchdl)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_18, 3, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_19, 3, 2, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_14, 4, 1, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_16, 2, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_7.addItem(self.verticalSpacer_15, 0, 1, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_22, 6, 1, 1, 1)

        self.label_3 = QLabel(self.EditSchdl)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_3, 1, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(100)
        self.gridLayout_6.setVerticalSpacing(30)
        self.old_aud_lbl = QLabel(self.EditSchdl)
        self.old_aud_lbl.setObjectName(u"old_aud_lbl")
        self.old_aud_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.old_aud_lbl, 7, 2, 1, 1)

        self.day_lbl_edit = QLabel(self.EditSchdl)
        self.day_lbl_edit.setObjectName(u"day_lbl_edit")
        self.day_lbl_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.day_lbl_edit, 8, 0, 1, 1)

        self.stud_lb_editl = QLabel(self.EditSchdl)
        self.stud_lb_editl.setObjectName(u"stud_lb_editl")
        self.stud_lb_editl.setFont(font4)

        self.gridLayout_6.addWidget(self.stud_lb_editl, 9, 0, 1, 1)

        self.stud_cb_edit = QComboBox(self.EditSchdl)
        self.stud_cb_edit.setObjectName(u"stud_cb_edit")
        self.stud_cb_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.stud_cb_edit, 9, 1, 1, 1)

        self.day_cb_edit = QComboBox(self.EditSchdl)
        self.day_cb_edit.setObjectName(u"day_cb_edit")
        self.day_cb_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.day_cb_edit, 8, 1, 1, 1)

        self.lesson_cb_edit = QComboBox(self.EditSchdl)
        self.lesson_cb_edit.setObjectName(u"lesson_cb_edit")
        self.lesson_cb_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.lesson_cb_edit, 5, 1, 1, 1)

        self.old_day_lbl = QLabel(self.EditSchdl)
        self.old_day_lbl.setObjectName(u"old_day_lbl")
        self.old_day_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.old_day_lbl, 8, 2, 1, 1)

        self.type_lesson_lbl_edit = QLabel(self.EditSchdl)
        self.type_lesson_lbl_edit.setObjectName(u"type_lesson_lbl_edit")
        sizePolicy.setHeightForWidth(self.type_lesson_lbl_edit.sizePolicy().hasHeightForWidth())
        self.type_lesson_lbl_edit.setSizePolicy(sizePolicy)
        self.type_lesson_lbl_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.type_lesson_lbl_edit, 4, 0, 1, 1)

        self.teacher_cb_edit = QComboBox(self.EditSchdl)
        self.teacher_cb_edit.setObjectName(u"teacher_cb_edit")
        self.teacher_cb_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.teacher_cb_edit, 6, 1, 1, 1)

        self.teacher_edit_lbl = QLabel(self.EditSchdl)
        self.teacher_edit_lbl.setObjectName(u"teacher_edit_lbl")
        self.teacher_edit_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.teacher_edit_lbl, 6, 0, 1, 1)

        self.date_lbl_edit = QLabel(self.EditSchdl)
        self.date_lbl_edit.setObjectName(u"date_lbl_edit")
        self.date_lbl_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.date_lbl_edit, 3, 0, 1, 1)

        self.dateTime_edit = QDateTimeEdit(self.EditSchdl)
        self.dateTime_edit.setObjectName(u"dateTime_edit")
        self.dateTime_edit.setFont(font4)
        self.dateTime_edit.setProperty("showGroupSeparator", False)
        self.dateTime_edit.setCalendarPopup(False)
        self.dateTime_edit.setCurrentSectionIndex(0)

        self.gridLayout_6.addWidget(self.dateTime_edit, 3, 1, 1, 1)

        self.aud_lbl_edit = QLabel(self.EditSchdl)
        self.aud_lbl_edit.setObjectName(u"aud_lbl_edit")
        self.aud_lbl_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.aud_lbl_edit, 7, 0, 1, 1)

        self.type_lesson_cb_edit = QComboBox(self.EditSchdl)
        self.type_lesson_cb_edit.setObjectName(u"type_lesson_cb_edit")
        self.type_lesson_cb_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.type_lesson_cb_edit, 4, 1, 1, 1)

        self.aud_cb_edit = QComboBox(self.EditSchdl)
        self.aud_cb_edit.setObjectName(u"aud_cb_edit")
        self.aud_cb_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.aud_cb_edit, 7, 1, 1, 1)

        self.lessob_lbl_edit = QLabel(self.EditSchdl)
        self.lessob_lbl_edit.setObjectName(u"lessob_lbl_edit")
        self.lessob_lbl_edit.setFont(font4)

        self.gridLayout_6.addWidget(self.lessob_lbl_edit, 5, 0, 1, 1)

        self.old_type_lesson_lbl = QLabel(self.EditSchdl)
        self.old_type_lesson_lbl.setObjectName(u"old_type_lesson_lbl")
        self.old_type_lesson_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.old_type_lesson_lbl, 4, 2, 1, 1)

        self.new_values_lbl = QLabel(self.EditSchdl)
        self.new_values_lbl.setObjectName(u"new_values_lbl")
        self.new_values_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.new_values_lbl, 1, 1, 1, 1)

        self.old_teacher_lbl = QLabel(self.EditSchdl)
        self.old_teacher_lbl.setObjectName(u"old_teacher_lbl")
        self.old_teacher_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.old_teacher_lbl, 6, 2, 1, 1)

        self.num_row_lbl = QLabel(self.EditSchdl)
        self.num_row_lbl.setObjectName(u"num_row_lbl")
        self.num_row_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.num_row_lbl, 2, 0, 1, 1)

        self.old_values_lbl = QLabel(self.EditSchdl)
        self.old_values_lbl.setObjectName(u"old_values_lbl")
        self.old_values_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.old_values_lbl, 1, 2, 1, 1)

        self.old_date_time = QLabel(self.EditSchdl)
        self.old_date_time.setObjectName(u"old_date_time")
        self.old_date_time.setFont(font4)

        self.gridLayout_6.addWidget(self.old_date_time, 3, 2, 1, 1)

        self.old_stud_lbl = QLabel(self.EditSchdl)
        self.old_stud_lbl.setObjectName(u"old_stud_lbl")
        self.old_stud_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.old_stud_lbl, 9, 2, 1, 1)

        self.old_lessons_lbl = QLabel(self.EditSchdl)
        self.old_lessons_lbl.setObjectName(u"old_lessons_lbl")
        self.old_lessons_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.old_lessons_lbl, 5, 2, 1, 1)

        self.row_state_lbl = QLabel(self.EditSchdl)
        self.row_state_lbl.setObjectName(u"row_state_lbl")
        self.row_state_lbl.setFont(font4)

        self.gridLayout_6.addWidget(self.row_state_lbl, 2, 2, 1, 1)

        self.values = QLabel(self.EditSchdl)
        self.values.setObjectName(u"values")
        self.values.setFont(font4)

        self.gridLayout_6.addWidget(self.values, 1, 0, 1, 1)

        self.num_row_sb = QSpinBox(self.EditSchdl)
        self.num_row_sb.setObjectName(u"num_row_sb")
        self.num_row_sb.setFont(font4)
        self.num_row_sb.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.num_row_sb, 2, 1, 1, 1)

        self.update_edit_schdl_btn = QPushButton(self.EditSchdl)
        self.update_edit_schdl_btn.setObjectName(u"update_edit_schdl_btn")
        self.update_edit_schdl_btn.setFont(font2)

        self.gridLayout_6.addWidget(self.update_edit_schdl_btn, 10, 1, 1, 1)

        self.error_edit_lbl = QLabel(self.EditSchdl)
        self.error_edit_lbl.setObjectName(u"error_edit_lbl")
        self.error_edit_lbl.setFont(font5)
        self.error_edit_lbl.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout_6.addWidget(self.error_edit_lbl, 10, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.EditSchdl)
        self.WriteOnService = QWidget()
        self.WriteOnService.setObjectName(u"WriteOnService")
        self.gridLayout_8 = QGridLayout(self.WriteOnService)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.feedback_lbl = QLabel(self.WriteOnService)
        self.feedback_lbl.setObjectName(u"feedback_lbl")
        self.feedback_lbl.setFont(font4)
        self.feedback_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.feedback_lbl, 6, 0, 1, 1)

        self.type_of_service_lbl = QLabel(self.WriteOnService)
        self.type_of_service_lbl.setObjectName(u"type_of_service_lbl")
        self.type_of_service_lbl.setFont(font4)
        self.type_of_service_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.type_of_service_lbl, 2, 0, 1, 1)

        self.executor_lbl = QLabel(self.WriteOnService)
        self.executor_lbl.setObjectName(u"executor_lbl")
        self.executor_lbl.setFont(font4)
        self.executor_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.executor_lbl, 4, 0, 1, 1)

        self.type_of_service_cb = QComboBox(self.WriteOnService)
        self.type_of_service_cb.setObjectName(u"type_of_service_cb")

        self.gridLayout_9.addWidget(self.type_of_service_cb, 2, 1, 1, 1)

        self.name_service_cb = QComboBox(self.WriteOnService)
        self.name_service_cb.setObjectName(u"name_service_cb")

        self.gridLayout_9.addWidget(self.name_service_cb, 0, 1, 1, 1)

        self.executor_cb = QComboBox(self.WriteOnService)
        self.executor_cb.setObjectName(u"executor_cb")

        self.gridLayout_9.addWidget(self.executor_cb, 4, 1, 1, 1)

        self.feed_back_txt_edit = QTextEdit(self.WriteOnService)
        self.feed_back_txt_edit.setObjectName(u"feed_back_txt_edit")

        self.gridLayout_9.addWidget(self.feed_back_txt_edit, 6, 1, 1, 1)

        self.name_of_service = QLabel(self.WriteOnService)
        self.name_of_service.setObjectName(u"name_of_service")
        self.name_of_service.setFont(font4)
        self.name_of_service.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_9.addWidget(self.name_of_service, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_5, 5, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 6, 2, 1, 1)

        self.send_btn_srvc = QPushButton(self.WriteOnService)
        self.send_btn_srvc.setObjectName(u"send_btn_srvc")
        self.send_btn_srvc.setFont(font2)

        self.gridLayout_8.addWidget(self.send_btn_srvc, 7, 2, 1, 1)

        self.stackedWidget.addWidget(self.WriteOnService)
        self.Schedule_Of_Service = QWidget()
        self.Schedule_Of_Service.setObjectName(u"Schedule_Of_Service")
        self.gridLayout_11 = QGridLayout(self.Schedule_Of_Service)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tableWidget_2 = QTableWidget(self.Schedule_Of_Service)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_11.addWidget(self.tableWidget_2, 3, 0, 1, 3)

        self.verticalSpacer_19 = QSpacerItem(36, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_19, 4, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_17, 2, 0, 1, 1)

        self.update_service_tb_btn = QPushButton(self.Schedule_Of_Service)
        self.update_service_tb_btn.setObjectName(u"update_service_tb_btn")
        self.update_service_tb_btn.setFont(font5)

        self.gridLayout_11.addWidget(self.update_service_tb_btn, 5, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_14, 5, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_13, 5, 0, 1, 1)

        self.label = QLabel(self.Schedule_Of_Service)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label, 1, 0, 1, 3)

        self.verticalSpacer_18 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_18, 0, 0, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.verticalSpacer_20, 6, 1, 1, 1)

        self.stackedWidget.addWidget(self.Schedule_Of_Service)
        self.Profile = QWidget()
        self.Profile.setObjectName(u"Profile")
        self.gridLayout_2 = QGridLayout(self.Profile)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spec_lbl = QLabel(self.Profile)
        self.spec_lbl.setObjectName(u"spec_lbl")
        self.spec_lbl.setFont(font4)
        self.spec_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.spec_lbl, 5, 1, 1, 1)

        self.spec_field_lbl = QLabel(self.Profile)
        self.spec_field_lbl.setObjectName(u"spec_field_lbl")
        self.spec_field_lbl.setFont(font4)

        self.gridLayout_2.addWidget(self.spec_field_lbl, 5, 3, 1, 1)

        self.post_lbl = QLabel(self.Profile)
        self.post_lbl.setObjectName(u"post_lbl")
        self.post_lbl.setFont(font4)
        self.post_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.post_lbl, 4, 1, 1, 1)

        self.fio_lbl = QLabel(self.Profile)
        self.fio_lbl.setObjectName(u"fio_lbl")
        self.fio_lbl.setFont(font4)
        self.fio_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.fio_lbl, 3, 1, 1, 1)

        self.profile_lbl = QLabel(self.Profile)
        self.profile_lbl.setObjectName(u"profile_lbl")
        self.profile_lbl.setFont(font3)
        self.profile_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.profile_lbl, 2, 1, 1, 3)

        self.fio_field_lbl = QLabel(self.Profile)
        self.fio_field_lbl.setObjectName(u"fio_field_lbl")
        self.fio_field_lbl.setFont(font4)

        self.gridLayout_2.addWidget(self.fio_field_lbl, 3, 3, 1, 1)

        self.post_field_lbl = QLabel(self.Profile)
        self.post_field_lbl.setObjectName(u"post_field_lbl")
        self.post_field_lbl.setFont(font4)

        self.gridLayout_2.addWidget(self.post_field_lbl, 4, 3, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 3, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_15, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 4, 4, 1, 1)

        self.stackedWidget.addWidget(self.Profile)

        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 779, 21))
        self.schedule = QMenu(self.menubar)
        self.schedule.setObjectName(u"schedule")
        self.programm = QMenu(self.menubar)
        self.programm.setObjectName(u"programm")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.programm.menuAction())
        self.menubar.addAction(self.schedule.menuAction())
        self.schedule.addSeparator()
        self.schedule.addAction(self.show_schdl_act)
        self.schedule.addAction(self.edit_schdl_act)
        self.schedule.addAction(self.add_schdl_act)
        self.programm.addAction(self.profile_act)
        self.programm.addAction(self.action)
        self.programm.addAction(self.exit_act)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.show_schdle.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c...", None))
        self.show_schdl_act.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c...", None))
        self.edit_schdl_act.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c...", None))
        self.select_act.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440\u043a\u0430", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.write_srvc_act.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c \u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0443", None))
        self.schdl_srvc_act.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433", None))
        self.list_srvc.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u0443\u0433", None))
        self.profile_act.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.exit_act.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.add_schdl_act.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c...", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.greeting_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c", None))
        self.begin_work.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.schdl_upd_tb.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u043d\u044f\u0442\u0438\u0439", None))
        ___qtablewidgetitem = self.schdl_lesson_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043d\u044f\u0442\u0438\u0435", None));
        ___qtablewidgetitem1 = self.schdl_lesson_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0438\u0442\u0435\u043b\u044c", None));
        ___qtablewidgetitem2 = self.schdl_lesson_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c", None));
        ___qtablewidgetitem3 = self.schdl_lesson_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u043d\u0438\u043a", None));
        ___qtablewidgetitem4 = self.schdl_lesson_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0417\u0430\u043d\u0442\u0438\u0439", None));
        ___qtablewidgetitem5 = self.schdl_lesson_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f", None));
        ___qtablewidgetitem6 = self.schdl_lesson_tb.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0438 \u0414\u0430\u0442\u0430", None));
        self.teacher.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.audition.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f", None))
        self.lessob_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043d\u044f\u0442\u0438\u0435", None))
        self.type_lesson_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0417\u0430\u043d\u044f\u0442\u0438\u0439", None))
        self.date_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0412\u0440\u0435\u043c\u044f:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u043d\u0438\u043a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.error_add_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.old_aud_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.day_lbl_edit.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c", None))
        self.stud_lb_editl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u043d\u0438\u043a", None))
        self.old_day_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.type_lesson_lbl_edit.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0417\u0430\u043d\u044f\u0442\u0438\u0439", None))
        self.teacher_edit_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.date_lbl_edit.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0438 \u0412\u0440\u0435\u043c\u044f", None))
        self.aud_lbl_edit.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f", None))
        self.lessob_lbl_edit.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043d\u044f\u0442\u0438\u0435", None))
        self.old_type_lesson_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.new_values_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0435 \u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None))
        self.old_teacher_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.num_row_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0421\u0442\u0440\u043e\u043a\u0438", None))
        self.old_values_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None))
        self.old_date_time.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.old_stud_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.old_lessons_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.row_state_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.values.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f:", None))
        self.update_edit_schdl_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.error_edit_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
        self.feedback_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0437\u044b\u0432", None))
        self.type_of_service_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.executor_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c", None))
        self.name_of_service.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430", None))
        self.send_btn_srvc.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u0430", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0433", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u044f\u0442\u043d\u0438\u0446\u0430", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u043d\u044c\u0435", None));
        self.update_service_tb_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0423\u0441\u043b\u0443\u0433", None))
        self.spec_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.spec_field_lbl.setText(QCoreApplication.translate("MainWindow", u"<????????????????>", None))
        self.post_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.fio_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e:", None))
        self.profile_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.fio_field_lbl.setText(QCoreApplication.translate("MainWindow", u"<????????????????>", None))
        self.post_field_lbl.setText(QCoreApplication.translate("MainWindow", u"<????????????????>", None))
        self.schedule.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.programm.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
    # retranslateUi

