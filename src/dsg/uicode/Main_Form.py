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
        MainWindow.resize(525, 448)
        self.show_schdle = QAction(MainWindow)
        self.show_schdle.setObjectName(u"show_schdle")
        self.show_act = QAction(MainWindow)
        self.show_act.setObjectName(u"show_act")
        self.edit_act = QAction(MainWindow)
        self.edit_act.setObjectName(u"edit_act")
        self.select_act = QAction(MainWindow)
        self.select_act.setObjectName(u"select_act")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.write_act = QAction(MainWindow)
        self.write_act.setObjectName(u"write_act")
        self.schdl_act = QAction(MainWindow)
        self.schdl_act.setObjectName(u"schdl_act")
        self.list_srvc = QAction(MainWindow)
        self.list_srvc.setObjectName(u"list_srvc")
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

        self.gridLayout_10.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.begin_work = QPushButton(self.GreetingScreen)
        self.begin_work.setObjectName(u"begin_work")

        self.gridLayout_10.addWidget(self.begin_work, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.greeting_lbl = QLabel(self.GreetingScreen)
        self.greeting_lbl.setObjectName(u"greeting_lbl")
        font = QFont()
        font.setPointSize(36)
        self.greeting_lbl.setFont(font)
        self.greeting_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.greeting_lbl, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.GreetingScreen)
        self.ShowSchedule = QWidget()
        self.ShowSchedule.setObjectName(u"ShowSchedule")
        self.gridLayout_5 = QGridLayout(self.ShowSchedule)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(-1, 0, 0, -1)
        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.update_btn = QPushButton(self.ShowSchedule)
        self.update_btn.setObjectName(u"update_btn")

        self.gridLayout_4.addWidget(self.update_btn, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.schdl_tb = QTableView(self.ShowSchedule)
        self.schdl_tb.setObjectName(u"schdl_tb")

        self.gridLayout_4.addWidget(self.schdl_tb, 0, 0, 1, 3)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.ShowSchedule)
        self.EditScreen = QWidget()
        self.EditScreen.setObjectName(u"EditScreen")
        self.gridLayout_9 = QGridLayout(self.EditScreen)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 9, -1, -1)
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 6, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.audition = QLabel(self.EditScreen)
        self.audition.setObjectName(u"audition")

        self.gridLayout_9.addWidget(self.audition, 7, 1, 1, 1)

        self.lesson_cb = QComboBox(self.EditScreen)
        self.lesson_cb.setObjectName(u"lesson_cb")

        self.gridLayout_9.addWidget(self.lesson_cb, 4, 3, 1, 5)

        self.type_lesson_lbl = QLabel(self.EditScreen)
        self.type_lesson_lbl.setObjectName(u"type_lesson_lbl")

        self.gridLayout_9.addWidget(self.type_lesson_lbl, 5, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(210, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_6, 8, 0, 1, 4)

        self.time_lb = QLabel(self.EditScreen)
        self.time_lb.setObjectName(u"time_lb")

        self.gridLayout_9.addWidget(self.time_lb, 2, 1, 1, 1)

        self.lessob_lbl = QLabel(self.EditScreen)
        self.lessob_lbl.setObjectName(u"lessob_lbl")

        self.gridLayout_9.addWidget(self.lessob_lbl, 4, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.EditScreen)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_9.addWidget(self.comboBox_6, 7, 3, 1, 5)

        self.dateEdit = QDateEdit(self.EditScreen)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout_9.addWidget(self.dateEdit, 1, 3, 1, 5)

        self.timeEdit = QTimeEdit(self.EditScreen)
        self.timeEdit.setObjectName(u"timeEdit")

        self.gridLayout_9.addWidget(self.timeEdit, 2, 3, 1, 5)

        self.date_lbl = QLabel(self.EditScreen)
        self.date_lbl.setObjectName(u"date_lbl")

        self.gridLayout_9.addWidget(self.date_lbl, 1, 1, 1, 1)

        self.teacher = QLabel(self.EditScreen)
        self.teacher.setObjectName(u"teacher")

        self.gridLayout_9.addWidget(self.teacher, 6, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.EditScreen)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_9.addWidget(self.comboBox_4, 5, 3, 1, 5)

        self.send_btn = QPushButton(self.EditScreen)
        self.send_btn.setObjectName(u"send_btn")

        self.gridLayout_9.addWidget(self.send_btn, 8, 4, 1, 1)

        self.comboBox_5 = QComboBox(self.EditScreen)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_9.addWidget(self.comboBox_5, 6, 3, 1, 5)

        self.horizontalSpacer_11 = QSpacerItem(108, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_11, 8, 7, 1, 1)

        self.stackedWidget.addWidget(self.EditScreen)
        self.WriteOnService = QWidget()
        self.WriteOnService.setObjectName(u"WriteOnService")
        self.gridLayout_8 = QGridLayout(self.WriteOnService)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)

        self.feed_back_txt_edit = QTextEdit(self.WriteOnService)
        self.feed_back_txt_edit.setObjectName(u"feed_back_txt_edit")

        self.gridLayout_8.addWidget(self.feed_back_txt_edit, 6, 2, 1, 3)

        self.executor_lbl = QLabel(self.WriteOnService)
        self.executor_lbl.setObjectName(u"executor_lbl")

        self.gridLayout_8.addWidget(self.executor_lbl, 4, 1, 1, 1)

        self.name_of_service = QLabel(self.WriteOnService)
        self.name_of_service.setObjectName(u"name_of_service")

        self.gridLayout_8.addWidget(self.name_of_service, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.feedback_lbl = QLabel(self.WriteOnService)
        self.feedback_lbl.setObjectName(u"feedback_lbl")

        self.gridLayout_8.addWidget(self.feedback_lbl, 6, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(185, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_9, 7, 4, 1, 2)

        self.send_btn_srvc = QPushButton(self.WriteOnService)
        self.send_btn_srvc.setObjectName(u"send_btn_srvc")

        self.gridLayout_8.addWidget(self.send_btn_srvc, 7, 3, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_12, 2, 5, 1, 1)

        self.name_service_cb = QComboBox(self.WriteOnService)
        self.name_service_cb.setObjectName(u"name_service_cb")

        self.gridLayout_8.addWidget(self.name_service_cb, 0, 2, 1, 3)

        self.executor_cb = QComboBox(self.WriteOnService)
        self.executor_cb.setObjectName(u"executor_cb")

        self.gridLayout_8.addWidget(self.executor_cb, 4, 2, 1, 3)

        self.type_of_service_cb = QComboBox(self.WriteOnService)
        self.type_of_service_cb.setObjectName(u"type_of_service_cb")

        self.gridLayout_8.addWidget(self.type_of_service_cb, 2, 2, 1, 3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 7, 0, 1, 3)

        self.type_of_service_lbl = QLabel(self.WriteOnService)
        self.type_of_service_lbl.setObjectName(u"type_of_service_lbl")

        self.gridLayout_8.addWidget(self.type_of_service_lbl, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 3, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 5, 1, 1, 1)

        self.stackedWidget.addWidget(self.WriteOnService)
        self.Schedule_Of_Service = QWidget()
        self.Schedule_Of_Service.setObjectName(u"Schedule_Of_Service")
        self.gridLayout_11 = QGridLayout(self.Schedule_Of_Service)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_13, 1, 0, 1, 1)

        self.update_service_tb_btn = QPushButton(self.Schedule_Of_Service)
        self.update_service_tb_btn.setObjectName(u"update_service_tb_btn")

        self.gridLayout_11.addWidget(self.update_service_tb_btn, 1, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_14, 1, 2, 1, 1)

        self.service_tb = QTableView(self.Schedule_Of_Service)
        self.service_tb.setObjectName(u"service_tb")

        self.gridLayout_11.addWidget(self.service_tb, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.Schedule_Of_Service)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spec_lbl = QLabel(self.page)
        self.spec_lbl.setObjectName(u"spec_lbl")
        self.spec_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.spec_lbl, 5, 1, 1, 1)

        self.fio_lbl = QLabel(self.page)
        self.fio_lbl.setObjectName(u"fio_lbl")
        self.fio_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.fio_lbl, 3, 1, 1, 1)

        self.post_lbl = QLabel(self.page)
        self.post_lbl.setObjectName(u"post_lbl")
        self.post_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.post_lbl, 4, 1, 1, 1)

        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 5, 3, 1, 1)

        self.profile_lbl = QLabel(self.page)
        self.profile_lbl.setObjectName(u"profile_lbl")
        font1 = QFont()
        font1.setPointSize(26)
        self.profile_lbl.setFont(font1)
        self.profile_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.profile_lbl, 2, 1, 1, 3)

        self.post_field_lbl = QLabel(self.page)
        self.post_field_lbl.setObjectName(u"post_field_lbl")

        self.gridLayout_2.addWidget(self.post_field_lbl, 4, 3, 1, 1)

        self.fio_field_lbl = QLabel(self.page)
        self.fio_field_lbl.setObjectName(u"fio_field_lbl")

        self.gridLayout_2.addWidget(self.fio_field_lbl, 3, 3, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_15, 3, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 3, 2, 1, 1)

        self.stackedWidget.addWidget(self.page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 525, 21))
        self.schedule = QMenu(self.menubar)
        self.schedule.setObjectName(u"schedule")
        self.service = QMenu(self.menubar)
        self.service.setObjectName(u"service")
        self.profile = QMenu(self.menubar)
        self.profile.setObjectName(u"profile")
        self.exit = QMenu(self.menubar)
        self.exit.setObjectName(u"exit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.schedule.menuAction())
        self.menubar.addAction(self.service.menuAction())
        self.menubar.addAction(self.profile.menuAction())
        self.menubar.addAction(self.exit.menuAction())
        self.schedule.addSeparator()
        self.schedule.addAction(self.show_act)
        self.schedule.addAction(self.edit_act)
        self.service.addAction(self.write_act)
        self.service.addAction(self.schdl_act)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.show_schdle.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c...", None))
        self.show_act.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c...", None))
        self.edit_act.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c...", None))
        self.select_act.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440\u043a\u0430", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.write_act.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c \u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0443", None))
        self.schdl_act.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433", None))
        self.list_srvc.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0441\u043b\u0443\u0433", None))
        self.begin_work.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.greeting_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.audition.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f", None))
        self.type_lesson_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0417\u0430\u043d\u044f\u0442\u0438\u0439", None))
        self.time_lb.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f", None))
        self.lessob_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043d\u044f\u0442\u0438\u0435", None))
        self.date_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
        self.teacher.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.send_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.executor_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c", None))
        self.name_of_service.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430", None))
        self.feedback_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0437\u044b\u0432", None))
        self.send_btn_srvc.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.type_of_service_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0423\u0441\u043b\u0443\u0433\u0438", None))
        self.update_service_tb_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.spec_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f:", None))
        self.fio_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e:", None))
        self.post_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<????????????????>", None))
        self.profile_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.post_field_lbl.setText(QCoreApplication.translate("MainWindow", u"<????????????????>", None))
        self.fio_field_lbl.setText(QCoreApplication.translate("MainWindow", u"<????????????????>", None))
        self.schedule.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.service.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441\u044b", None))
        self.profile.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.exit.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

