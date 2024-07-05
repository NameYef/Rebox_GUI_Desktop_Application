# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 709)
        MainWindow.setMinimumSize(QSize(300, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMaximumSize(QSize(70, 16777215))
        self.icon_only_widget.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.verticalLayout_2 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(18, 94, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.home_1 = QPushButton(self.icon_only_widget)
        self.home_1.setObjectName(u"home_1")
        self.home_1.setCheckable(True)
        self.home_1.setChecked(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1)

        self.script_1 = QPushButton(self.icon_only_widget)
        self.script_1.setObjectName(u"script_1")
        self.script_1.setCheckable(True)
        self.script_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.script_1)

        self.config_1 = QPushButton(self.icon_only_widget)
        self.config_1.setObjectName(u"config_1")
        self.config_1.setCheckable(True)
        self.config_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.config_1)

        self.verticalSpacer = QSpacerItem(18, 448, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.exit_1 = QPushButton(self.icon_only_widget)
        self.exit_1.setObjectName(u"exit_1")
        self.exit_1.setCheckable(True)
        self.exit_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.exit_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toggle = QPushButton(self.widget_3)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.toggle.setCheckable(True)

        self.horizontalLayout.addWidget(self.toggle)

        self.horizontalSpacer = QSpacerItem(448, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(300, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.script_page = QWidget()
        self.script_page.setObjectName(u"script_page")
        self.verticalLayout_5 = QVBoxLayout(self.script_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.console_log = QTextEdit(self.script_page)
        self.console_log.setObjectName(u"console_log")
        self.console_log.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.console_log)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.run_script = QPushButton(self.script_page)
        self.run_script.setObjectName(u"run_script")
        self.run_script.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.run_script.setCheckable(False)
        self.run_script.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.run_script)

        self.stop_script = QPushButton(self.script_page)
        self.stop_script.setObjectName(u"stop_script")
        self.stop_script.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.stop_script.setCheckable(True)
        self.stop_script.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.stop_script)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.stackedWidget.addWidget(self.script_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label_2 = QLabel(self.home_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 170, 301, 211))
        font = QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.home_page)
        self.configs_page = QWidget()
        self.configs_page.setObjectName(u"configs_page")
        self.verticalLayout_14 = QVBoxLayout(self.configs_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.config_list = QWidget(self.configs_page)
        self.config_list.setObjectName(u"config_list")
        self.config_list.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.config_list)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.config_list)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.res_x_label = QLabel(self.config_list)
        self.res_x_label.setObjectName(u"res_x_label")
        self.res_x_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.res_x_label)

        self.res_x_lineEdit = QLineEdit(self.config_list)
        self.res_x_lineEdit.setObjectName(u"res_x_lineEdit")
        self.res_x_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.res_x_lineEdit)


        self.verticalLayout_6.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.res_y_label = QLabel(self.config_list)
        self.res_y_label.setObjectName(u"res_y_label")
        self.res_y_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.res_y_label)

        self.res_y_lineEdit = QLineEdit(self.config_list)
        self.res_y_lineEdit.setObjectName(u"res_y_lineEdit")
        self.res_y_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.res_y_lineEdit)


        self.verticalLayout_6.addLayout(self.formLayout_2)


        self.verticalLayout_13.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.config_list)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.label_4)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.no_photo_match_label = QLabel(self.config_list)
        self.no_photo_match_label.setObjectName(u"no_photo_match_label")
        self.no_photo_match_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.no_photo_match_label)

        self.no_photo_match_lineEdit = QLineEdit(self.config_list)
        self.no_photo_match_lineEdit.setObjectName(u"no_photo_match_lineEdit")
        self.no_photo_match_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.no_photo_match_lineEdit)


        self.verticalLayout_8.addLayout(self.formLayout_3)

        self.formLayout_13 = QFormLayout()
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.nfeature_obj_label = QLabel(self.config_list)
        self.nfeature_obj_label.setObjectName(u"nfeature_obj_label")
        self.nfeature_obj_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_13.setWidget(0, QFormLayout.LabelRole, self.nfeature_obj_label)

        self.nfeature_obj_lineEdit = QLineEdit(self.config_list)
        self.nfeature_obj_lineEdit.setObjectName(u"nfeature_obj_lineEdit")
        self.nfeature_obj_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_13.setWidget(0, QFormLayout.FieldRole, self.nfeature_obj_lineEdit)


        self.verticalLayout_8.addLayout(self.formLayout_13)

        self.formLayout_14 = QFormLayout()
        self.formLayout_14.setObjectName(u"formLayout_14")
        self.nfeature_det_label = QLabel(self.config_list)
        self.nfeature_det_label.setObjectName(u"nfeature_det_label")
        self.nfeature_det_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_14.setWidget(0, QFormLayout.LabelRole, self.nfeature_det_label)

        self.nfeature_det_lineEdit = QLineEdit(self.config_list)
        self.nfeature_det_lineEdit.setObjectName(u"nfeature_det_lineEdit")
        self.nfeature_det_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_14.setWidget(0, QFormLayout.FieldRole, self.nfeature_det_lineEdit)


        self.verticalLayout_8.addLayout(self.formLayout_14)


        self.verticalLayout_13.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.config_list)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.label_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.x_off_label = QLabel(self.config_list)
        self.x_off_label.setObjectName(u"x_off_label")
        self.x_off_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.x_off_label)

        self.x_off_lineEdit = QLineEdit(self.config_list)
        self.x_off_lineEdit.setObjectName(u"x_off_lineEdit")
        self.x_off_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.x_off_lineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.x_off_lineEdit)


        self.verticalLayout_7.addLayout(self.formLayout_4)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.y_off_label = QLabel(self.config_list)
        self.y_off_label.setObjectName(u"y_off_label")
        self.y_off_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.y_off_label)

        self.y_off_lineEdit = QLineEdit(self.config_list)
        self.y_off_lineEdit.setObjectName(u"y_off_lineEdit")
        self.y_off_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.y_off_lineEdit)


        self.verticalLayout_7.addLayout(self.formLayout_8)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.width_off_label = QLabel(self.config_list)
        self.width_off_label.setObjectName(u"width_off_label")
        self.width_off_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.width_off_label)

        self.width_off_lineEdit = QLineEdit(self.config_list)
        self.width_off_lineEdit.setObjectName(u"width_off_lineEdit")
        self.width_off_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.width_off_lineEdit)


        self.verticalLayout_7.addLayout(self.formLayout_5)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.height_off_lineEdit = QLineEdit(self.config_list)
        self.height_off_lineEdit.setObjectName(u"height_off_lineEdit")
        self.height_off_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.height_off_lineEdit)

        self.height_off_label = QLabel(self.config_list)
        self.height_off_label.setObjectName(u"height_off_label")
        self.height_off_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.height_off_label)


        self.verticalLayout_7.addLayout(self.formLayout_7)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.min_x_label = QLabel(self.config_list)
        self.min_x_label.setObjectName(u"min_x_label")
        self.min_x_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.min_x_label)

        self.min_x_lineEdit = QLineEdit(self.config_list)
        self.min_x_lineEdit.setObjectName(u"min_x_lineEdit")
        self.min_x_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.min_x_lineEdit)


        self.verticalLayout_7.addLayout(self.formLayout_6)

        self.formLayout_12 = QFormLayout()
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.min_y_label = QLabel(self.config_list)
        self.min_y_label.setObjectName(u"min_y_label")
        self.min_y_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.min_y_label)

        self.min_y_lineEdit = QLineEdit(self.config_list)
        self.min_y_lineEdit.setObjectName(u"min_y_lineEdit")
        self.min_y_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_12.setWidget(0, QFormLayout.FieldRole, self.min_y_lineEdit)


        self.verticalLayout_7.addLayout(self.formLayout_12)


        self.verticalLayout_13.addLayout(self.verticalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.config_list)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.label_5)

        self.formLayout_15 = QFormLayout()
        self.formLayout_15.setObjectName(u"formLayout_15")
        self.ratio_lineEdit = QLineEdit(self.config_list)
        self.ratio_lineEdit.setObjectName(u"ratio_lineEdit")
        self.ratio_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_15.setWidget(0, QFormLayout.FieldRole, self.ratio_lineEdit)

        self.ratio_label = QLabel(self.config_list)
        self.ratio_label.setObjectName(u"ratio_label")
        self.ratio_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_15.setWidget(0, QFormLayout.LabelRole, self.ratio_label)


        self.verticalLayout_9.addLayout(self.formLayout_15)

        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.min_match_lineEdit = QLineEdit(self.config_list)
        self.min_match_lineEdit.setObjectName(u"min_match_lineEdit")
        self.min_match_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.min_match_lineEdit)

        self.min_match_label = QLabel(self.config_list)
        self.min_match_label.setObjectName(u"min_match_label")
        self.min_match_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.min_match_label)


        self.verticalLayout_9.addLayout(self.formLayout_11)

        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.max_size_label = QLabel(self.config_list)
        self.max_size_label.setObjectName(u"max_size_label")
        self.max_size_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.max_size_label)

        self.max_size_lineEdit = QLineEdit(self.config_list)
        self.max_size_lineEdit.setObjectName(u"max_size_lineEdit")
        self.max_size_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.max_size_lineEdit)


        self.verticalLayout_9.addLayout(self.formLayout_10)


        self.verticalLayout_13.addLayout(self.verticalLayout_9)


        self.horizontalLayout_3.addWidget(self.config_list)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.project_widget = QWidget(self.configs_page)
        self.project_widget.setObjectName(u"project_widget")
        self.project_widget.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.project_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.project_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.label_6)

        self.project_listwidget = QListWidget(self.project_widget)
        self.project_listwidget.setObjectName(u"project_listwidget")
        self.project_listwidget.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.project_listwidget)


        self.verticalLayout_12.addWidget(self.project_widget)

        self.project_widget_2 = QWidget(self.configs_page)
        self.project_widget_2.setObjectName(u"project_widget_2")
        self.project_widget_2.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_11 = QVBoxLayout(self.project_widget_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.project_widget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.label_8)

        self.boxed_img_folder = QListWidget(self.project_widget_2)
        self.boxed_img_folder.setObjectName(u"boxed_img_folder")
        self.boxed_img_folder.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.boxed_img_folder)


        self.verticalLayout_12.addWidget(self.project_widget_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_12)


        self.verticalLayout_14.addLayout(self.horizontalLayout_3)

        self.save_button = QPushButton(self.configs_page)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.verticalLayout_14.addWidget(self.save_button)

        self.stackedWidget.addWidget(self.configs_page)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMinimumSize(QSize(200, 0))
        self.icon_name_widget.setMaximumSize(QSize(200, 16777215))
        self.icon_name_widget.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.verticalLayout = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(18, 94, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.home_2 = QPushButton(self.icon_name_widget)
        self.home_2.setObjectName(u"home_2")
        self.home_2.setCheckable(True)
        self.home_2.setChecked(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2)

        self.script_2 = QPushButton(self.icon_name_widget)
        self.script_2.setObjectName(u"script_2")
        self.script_2.setCheckable(True)
        self.script_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.script_2)

        self.config_2 = QPushButton(self.icon_name_widget)
        self.config_2.setObjectName(u"config_2")
        self.config_2.setCheckable(True)
        self.config_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.config_2)

        self.verticalSpacer_2 = QSpacerItem(18, 448, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.exit_2 = QPushButton(self.icon_name_widget)
        self.exit_2.setObjectName(u"exit_2")
        self.exit_2.setCheckable(True)
        self.exit_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.exit_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toggle.toggled.connect(self.icon_only_widget.setHidden)
        self.toggle.toggled.connect(self.icon_name_widget.setVisible)
        self.home_1.toggled.connect(self.home_2.setChecked)
        self.script_1.toggled.connect(self.script_2.setChecked)
        self.config_1.toggled.connect(self.config_2.setChecked)
        self.exit_1.toggled.connect(self.exit_2.setChecked)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.script_2.toggled.connect(self.script_1.setChecked)
        self.config_2.toggled.connect(self.config_1.setChecked)
        self.exit_2.toggled.connect(self.exit_1.setChecked)
        self.exit_2.pressed.connect(MainWindow.close)
        self.exit_1.pressed.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_1.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.script_1.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.config_1.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.exit_1.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.run_script.setText(QCoreApplication.translate("MainWindow", u"Run Script", None))
        self.stop_script.setText(QCoreApplication.translate("MainWindow", u"Force Stop", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"[WIP]", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Resolutions", None))
        self.res_x_label.setText(QCoreApplication.translate("MainWindow", u"resolution_x", None))
        self.res_y_label.setText(QCoreApplication.translate("MainWindow", u"resolution_y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Effectiveness", None))
        self.no_photo_match_label.setText(QCoreApplication.translate("MainWindow", u"no_photo_match", None))
        self.nfeature_obj_label.setText(QCoreApplication.translate("MainWindow", u"nfeature_obj", None))
        self.nfeature_det_label.setText(QCoreApplication.translate("MainWindow", u"nfeature_detect_zone", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Offsets", None))
        self.x_off_label.setText(QCoreApplication.translate("MainWindow", u"x_offset_for_detection", None))
        self.y_off_label.setText(QCoreApplication.translate("MainWindow", u"y_offset_for_detection", None))
        self.width_off_label.setText(QCoreApplication.translate("MainWindow", u"width_offset", None))
        self.height_off_label.setText(QCoreApplication.translate("MainWindow", u"height_offset", None))
        self.min_x_label.setText(QCoreApplication.translate("MainWindow", u"min_x_offset_same_cls", None))
        self.min_y_label.setText(QCoreApplication.translate("MainWindow", u"min_y_offset_same_cls", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Confidence", None))
        self.ratio_label.setText(QCoreApplication.translate("MainWindow", u"ratio_threshold", None))
        self.min_match_label.setText(QCoreApplication.translate("MainWindow", u"min_matches", None))
        self.max_size_label.setText(QCoreApplication.translate("MainWindow", u"max_size_acceptable", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Project Folder", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Where to store boxed images?", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.home_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.script_2.setText(QCoreApplication.translate("MainWindow", u"Script", None))
        self.config_2.setText(QCoreApplication.translate("MainWindow", u"Configs", None))
        self.exit_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

