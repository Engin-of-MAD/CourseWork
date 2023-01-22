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
        MainWindow.resize(800, 600)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
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
        self.schedule.addAction(self.select_act)
        self.service.addAction(self.write_act)
        self.service.addAction(self.schdl_act)
        self.service.addAction(self.list_srvc)

        self.retranslateUi(MainWindow)

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
        self.schedule.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.service.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0440\u0432\u0438\u0441\u044b", None))
        self.profile.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.exit.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

