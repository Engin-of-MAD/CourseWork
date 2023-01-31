# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginScreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(380, 340)
        LoginScreen.setMinimumSize(QSize(0, 0))
        LoginScreen.setMaximumSize(QSize(380, 340))
        self.centralwidget = QWidget(LoginScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 2, 1, 1)

        self.pswd_edit = QLineEdit(self.centralwidget)
        self.pswd_edit.setObjectName(u"pswd_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pswd_edit.sizePolicy().hasHeightForWidth())
        self.pswd_edit.setSizePolicy(sizePolicy)
        self.pswd_edit.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(8)
        self.pswd_edit.setFont(font)
        self.pswd_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.pswd_edit, 4, 2, 1, 1)

        self.login_lbl = QLabel(self.centralwidget)
        self.login_lbl.setObjectName(u"login_lbl")
        font1 = QFont()
        font1.setPointSize(11)
        self.login_lbl.setFont(font1)
        self.login_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.login_lbl, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 9, 3, 1, 1)

        self.pswd_lbl = QLabel(self.centralwidget)
        self.pswd_lbl.setObjectName(u"pswd_lbl")
        self.pswd_lbl.setFont(font1)
        self.pswd_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.pswd_lbl, 4, 1, 1, 1)

        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")

        self.gridLayout.addWidget(self.exit_btn, 9, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 9, 1, 1, 1)

        self.enter_btn = QPushButton(self.centralwidget)
        self.enter_btn.setObjectName(u"enter_btn")

        self.gridLayout.addWidget(self.enter_btn, 6, 2, 1, 1)

        self.login_edit = QLineEdit(self.centralwidget)
        self.login_edit.setObjectName(u"login_edit")
        sizePolicy.setHeightForWidth(self.login_edit.sizePolicy().hasHeightForWidth())
        self.login_edit.setSizePolicy(sizePolicy)
        self.login_edit.setMinimumSize(QSize(200, 0))
        self.login_edit.setFont(font)

        self.gridLayout.addWidget(self.login_edit, 3, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 3)

        self.auth_lbl = QLabel(self.centralwidget)
        self.auth_lbl.setObjectName(u"auth_lbl")
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(28)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        self.auth_lbl.setFont(font2)
        self.auth_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.auth_lbl, 1, 1, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.error_lbl = QLabel(self.centralwidget)
        self.error_lbl.setObjectName(u"error_lbl")
        font3 = QFont()
        font3.setPointSize(9)
        self.error_lbl.setFont(font3)
        self.error_lbl.setAutoFillBackground(False)
        self.error_lbl.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.error_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.error_lbl, 5, 1, 1, 1)

        LoginScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoginScreen)
        self.statusbar.setObjectName(u"statusbar")
        LoginScreen.setStatusBar(self.statusbar)

        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"MainWindow", None))
        self.login_lbl.setText(QCoreApplication.translate("LoginScreen", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.pswd_lbl.setText(QCoreApplication.translate("LoginScreen", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.exit_btn.setText(QCoreApplication.translate("LoginScreen", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.enter_btn.setText(QCoreApplication.translate("LoginScreen", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.auth_lbl.setText(QCoreApplication.translate("LoginScreen", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.error_lbl.setText(QCoreApplication.translate("LoginScreen", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
    # retranslateUi

