# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowSchedule.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ShowSchedule(object):
    def setupUi(self, ShowSchedule):
        if not ShowSchedule.objectName():
            ShowSchedule.setObjectName(u"ShowSchedule")
        ShowSchedule.resize(485, 466)
        self.gridLayout = QGridLayout(ShowSchedule)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_update = QPushButton(ShowSchedule)
        self.btn_update.setObjectName(u"btn_update")

        self.gridLayout.addWidget(self.btn_update, 2, 2, 1, 1)

        self.schld_view = QTableView(ShowSchedule)
        self.schld_view.setObjectName(u"schld_view")

        self.gridLayout.addWidget(self.schld_view, 1, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)


        self.retranslateUi(ShowSchedule)

        QMetaObject.connectSlotsByName(ShowSchedule)
    # setupUi

    def retranslateUi(self, ShowSchedule):
        ShowSchedule.setWindowTitle(QCoreApplication.translate("ShowSchedule", u"Form", None))
        self.btn_update.setText(QCoreApplication.translate("ShowSchedule", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

