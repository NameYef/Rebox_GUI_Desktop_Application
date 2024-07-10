# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'name_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_NameDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(490, 336)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.profile_name = QLineEdit(Dialog)
        self.profile_name.setObjectName(u"profile_name")
        self.profile_name.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.profile_name)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel = QPushButton(self.widget)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout.addWidget(self.cancel)

        self.ok = QPushButton(self.widget)
        self.ok.setObjectName(u"ok")
        self.ok.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout.addWidget(self.ok)


        self.verticalLayout_2.addWidget(self.widget)
        self.cancel.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Enter profile name", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

