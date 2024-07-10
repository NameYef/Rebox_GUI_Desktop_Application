# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'img_dialognhPZnW.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 400)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.img_folder_listWidget = QListWidget(Dialog)
        self.img_folder_listWidget.setObjectName(u"img_folder_listWidget")
        self.img_folder_listWidget.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.img_folder_listWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout.addWidget(self.cancel)

        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        self.ok.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout.addWidget(self.ok)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        self.cancel.clicked.connect(Dialog.close)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

    