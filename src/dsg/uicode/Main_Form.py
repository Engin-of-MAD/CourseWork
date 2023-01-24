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
        MainWindow.resize(549, 462)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.GreetingScreen = QWidget()
        self.GreetingScreen.setObjectName(u"GreetingScreen")
        self.gridLayout_10 = QGridLayout(self.GreetingScreen)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.greeting_lbl = QLabel(self.GreetingScreen)
        self.greeting_lbl.setObjectName(u"greeting_lbl")
        font = QFont()
        font.setPointSize(36)
        self.greeting_lbl.setFont(font)
        self.greeting_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.greeting_lbl, 1, 0, 1, 3)

        self.begin_work = QPushButton(self.GreetingScreen)
        self.begin_work.setObjectName(u"begin_work")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.begin_work.sizePolicy().hasHeightForWidth())
        self.begin_work.setSizePolicy(sizePolicy1)

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
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.label_2 = QLabel(self.ShowSchedule)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.schdl_upd_tb = QPushButton(self.ShowSchedule)
        self.schdl_upd_tb.setObjectName(u"schdl_upd_tb")

        self.gridLayout_5.addWidget(self.schdl_upd_tb, 2, 1, 1, 1)

        self.schdl_lesson_tb = QTableWidget(self.ShowSchedule)
        if (self.schdl_lesson_tb.columnCount() < 6):
            self.schdl_lesson_tb.setColumnCount(6)
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
        self.schdl_lesson_tb.setObjectName(u"schdl_lesson_tb")

        self.gridLayout_5.addWidget(self.schdl_lesson_tb, 1, 0, 1, 3)

        self.stackedWidget.addWidget(self.ShowSchedule)
        self.EditScreen = QWidget()
        self.EditScreen.setObjectName(u"EditScreen")
        self.gridLayout_3 = QGridLayout(self.EditScreen)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.send_btn = QPushButton(self.EditScreen)
        self.send_btn.setObjectName(u"send_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.send_btn, 8, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_8, 5, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(100)
        self.formLayout.setVerticalSpacing(30)
        self.date_lbl = QLabel(self.EditScreen)
        self.date_lbl.setObjectName(u"date_lbl")
        font2 = QFont()
        font2.setPointSize(13)
        self.date_lbl.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.date_lbl)

        self.dateEdit = QDateEdit(self.EditScreen)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy2.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dateEdit)

        self.time_lb = QLabel(self.EditScreen)
        self.time_lb.setObjectName(u"time_lb")
        self.time_lb.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.time_lb)

        self.timeEdit = QTimeEdit(self.EditScreen)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy2.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy2)
        self.timeEdit.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.timeEdit)

        self.type_lesson_lbl = QLabel(self.EditScreen)
        self.type_lesson_lbl.setObjectName(u"type_lesson_lbl")
        sizePolicy.setHeightForWidth(self.type_lesson_lbl.sizePolicy().hasHeightForWidth())
        self.type_lesson_lbl.setSizePolicy(sizePolicy)
        self.type_lesson_lbl.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.type_lesson_lbl)

        self.lesson_cb = QComboBox(self.EditScreen)
        self.lesson_cb.setObjectName(u"lesson_cb")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lesson_cb)

        self.lessob_lbl = QLabel(self.EditScreen)
        self.lessob_lbl.setObjectName(u"lessob_lbl")
        self.lessob_lbl.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lessob_lbl)

        self.lesson_cb_2 = QComboBox(self.EditScreen)
        self.lesson_cb_2.setObjectName(u"lesson_cb_2")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lesson_cb_2)

        self.teacher = QLabel(self.EditScreen)
        self.teacher.setObjectName(u"teacher")
        self.teacher.setFont(font2)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.teacher)

        self.teacher_cb = QComboBox(self.EditScreen)
        self.teacher_cb.setObjectName(u"teacher_cb")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.teacher_cb)

        self.audition = QLabel(self.EditScreen)
        self.audition.setObjectName(u"audition")
        self.audition.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.audition)

        self.aud_cb = QComboBox(self.EditScreen)
        self.aud_cb.setObjectName(u"aud_cb")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.aud_cb)


        self.gridLayout_3.addLayout(self.formLayout, 5, 3, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_11, 5, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 9, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 7, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 0, 3, 1, 1)

        self.stackedWidget.addWidget(self.EditScreen)
        self.WriteOnService = QWidget()
        self.WriteOnService.setObjectName(u"WriteOnService")
        self.gridLayout_8 = QGridLayout(self.WriteOnService)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_10, 3, 0, 1, 1)

        self.executor_lbl = QLabel(self.WriteOnService)
        self.executor_lbl.setObjectName(u"executor_lbl")
        self.executor_lbl.setFont(font2)
        self.executor_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.executor_lbl, 5, 1, 1, 1)

        self.type_of_service_lbl = QLabel(self.WriteOnService)
        self.type_of_service_lbl.setObjectName(u"type_of_service_lbl")
        self.type_of_service_lbl.setFont(font2)
        self.type_of_service_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.type_of_service_lbl, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 6, 1, 1, 1)

        self.send_btn_srvc = QPushButton(self.WriteOnService)
        self.send_btn_srvc.setObjectName(u"send_btn_srvc")

        self.gridLayout_8.addWidget(self.send_btn_srvc, 9, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 9, 0, 1, 3)

        self.horizontalSpacer_12 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 3, 5, 1, 1)

        self.executor_cb = QComboBox(self.WriteOnService)
        self.executor_cb.setObjectName(u"executor_cb")

        self.gridLayout_8.addWidget(self.executor_cb, 5, 2, 1, 3)

        self.name_service_cb = QComboBox(self.WriteOnService)
        self.name_service_cb.setObjectName(u"name_service_cb")

        self.gridLayout_8.addWidget(self.name_service_cb, 1, 2, 1, 3)

        self.type_of_service_cb = QComboBox(self.WriteOnService)
        self.type_of_service_cb.setObjectName(u"type_of_service_cb")

        self.gridLayout_8.addWidget(self.type_of_service_cb, 3, 2, 1, 3)

        self.feedback_lbl = QLabel(self.WriteOnService)
        self.feedback_lbl.setObjectName(u"feedback_lbl")
        self.feedback_lbl.setFont(font2)
        self.feedback_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.feedback_lbl, 7, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.name_of_service = QLabel(self.WriteOnService)
        self.name_of_service.setObjectName(u"name_of_service")
        self.name_of_service.setFont(font2)
        self.name_of_service.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.name_of_service, 1, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(185, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_9, 9, 4, 1, 2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_10, 8, 3, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_9, 0, 3, 1, 1)

        self.feed_back_txt_edit = QTextEdit(self.WriteOnService)
        self.feed_back_txt_edit.setObjectName(u"feed_back_txt_edit")

        self.gridLayout_8.addWidget(self.feed_back_txt_edit, 7, 2, 1, 3)

        self.stackedWidget.addWidget(self.WriteOnService)
        self.Schedule_Of_Service = QWidget()
        self.Schedule_Of_Service.setObjectName(u"Schedule_Of_Service")
        self.gridLayout_11 = QGridLayout(self.Schedule_Of_Service)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_14, 2, 2, 1, 1)

        self.update_service_tb_btn = QPushButton(self.Schedule_Of_Service)
        self.update_service_tb_btn.setObjectName(u"update_service_tb_btn")

        self.gridLayout_11.addWidget(self.update_service_tb_btn, 2, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_13, 2, 0, 1, 1)

        self.label = QLabel(self.Schedule_Of_Service)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 3)

        self.tableWidget_2 = QTableWidget(self.Schedule_Of_Service)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.gridLayout_11.addWidget(self.tableWidget_2, 1, 0, 1, 3)

        self.stackedWidget.addWidget(self.Schedule_Of_Service)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spec_lbl = QLabel(self.page)
        self.spec_lbl.setObjectName(u"spec_lbl")
        self.spec_lbl.setFont(font2)
        self.spec_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.spec_lbl, 5, 1, 1, 1)

        self.spec_field_lbl = QLabel(self.page)
        self.spec_field_lbl.setObjectName(u"spec_field_lbl")
        self.spec_field_lbl.setFont(font2)

        self.gridLayout_2.addWidget(self.spec_field_lbl, 5, 3, 1, 1)

        self.post_lbl = QLabel(self.page)
        self.post_lbl.setObjectName(u"post_lbl")
        self.post_lbl.setFont(font2)
        self.post_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.post_lbl, 4, 1, 1, 1)

        self.fio_lbl = QLabel(self.page)
        self.fio_lbl.setObjectName(u"fio_lbl")
        self.fio_lbl.setFont(font2)
        self.fio_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.fio_lbl, 3, 1, 1, 1)

        self.profile_lbl = QLabel(self.page)
        self.profile_lbl.setObjectName(u"profile_lbl")
        font3 = QFont()
        font3.setPointSize(26)
        self.profile_lbl.setFont(font3)
        self.profile_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.profile_lbl, 2, 1, 1, 3)

        self.fio_field_lbl = QLabel(self.page)
        self.fio_field_lbl.setObjectName(u"fio_field_lbl")
        self.fio_field_lbl.setFont(font2)

        self.gridLayout_2.addWidget(self.fio_field_lbl, 3, 3, 1, 1)

        self.post_field_lbl = QLabel(self.page)
        self.post_field_lbl.setObjectName(u"post_field_lbl")
        self.post_field_lbl.setFont(font2)

        self.gridLayout_2.addWidget(self.post_field_lbl, 4, 3, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 3, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_15, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 4, 4, 1, 1)

        self.stackedWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 549, 21))
        self.schedule = QMenu(self.menubar)
        self.schedule.setObjectName(u"schedule")
        self.service = QMenu(self.menubar)
        self.service.setObjectName(u"service")
        self.programm = QMenu(self.menubar)
        self.programm.setObjectName(u"programm")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.programm.menuAction())
        self.menubar.addAction(self.schedule.menuAction())
        self.menubar.addAction(self.service.menuAction())
        self.schedule.addSeparator()
        self.schedule.addAction(self.show_schdl_act)
        self.schedule.addAction(self.edit_schdl_act)
        self.service.addAction(self.write_srvc_act)
        self.service.addAction(self.schdl_srvc_act)
        self.programm.addAction(self.profile_act)
        self.programm.addAction(self.exit_act)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.greeting_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c", None))
        self.begin_work.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u043d\u044f\u0442\u0438\u0439", None))
        self.schdl_upd_tb.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.schdl_lesson_tb.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a", None));
        ___qtablewidgetitem1 = self.schdl_lesson_tb.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a", None));
        ___qtablewidgetitem2 = self.schdl_lesson_tb.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u0430", None));
        ___qtablewidgetitem3 = self.schdl_lesson_tb.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0433", None));
        ___qtablewidgetitem4 = self.schdl_lesson_tb.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u044f\u0442\u043d\u0438\u0446\u0430", None));
        ___qtablewidgetitem5 = self.schdl_lesson_tb.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u0431\u0431\u043e\u0442\u0430", None));
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.date_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
        self.time_lb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.type_lesson_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0417\u0430\u043d\u044f\u0442\u0438\u0439", None))
        self.lessob_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043d\u044f\u0442\u0438\u0435", None))
        self.teacher.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.audition.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f", None))
        self.executor_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c", None))
        self.type_of_service_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.send_btn_srvc.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.feedback_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0437\u044b\u0432", None))
        self.name_of_service.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430", None))
        self.update_service_tb_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0423\u0441\u043b\u0443\u0433", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043d\u0435\u0434\u0435\u043b\u044c\u043d\u0438\u043a", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0442\u043e\u0440\u043d\u0438\u043a", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u0430", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0442\u0432\u0435\u0440\u0433", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u044f\u0442\u043d\u0438\u0446\u0430", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u043a\u0440\u0435\u0441\u043d\u044c\u0435", None));
        self.spec_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.spec_field_lbl.setText(QCoreApplication.translate("MainWindow", u"<????????????????>", None))
        self.post_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.fio_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e:", None))
        self.profile_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.fio_field_lbl.setText(QCoreApplication.translate("MainWindow", u"<????????????????>", None))
        self.post_field_lbl.setText(QCoreApplication.translate("MainWindow", u"<????????????????>", None))
        self.schedule.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.service.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441\u044b", None))
        self.programm.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
    # retranslateUi

