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

from custom_widget import ScaledLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 773)
        MainWindow.setMinimumSize(QSize(300, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(222, 221, 218);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.images_2 = QPushButton(self.icon_name_widget)
        self.images_2.setObjectName(u"images_2")
        self.images_2.setCheckable(True)
        self.images_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.images_2)

        self.videos_2 = QPushButton(self.icon_name_widget)
        self.videos_2.setObjectName(u"videos_2")
        self.videos_2.setCheckable(True)
        self.videos_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.videos_2)

        self.verticalSpacer_2 = QSpacerItem(18, 448, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.exit_2 = QPushButton(self.icon_name_widget)
        self.exit_2.setObjectName(u"exit_2")
        self.exit_2.setCheckable(True)
        self.exit_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.exit_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

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

        self.refresh_button = QPushButton(self.widget_3)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout.addWidget(self.refresh_button)

        self.horizontalSpacer = QSpacerItem(448, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.server_status = QLabel(self.widget_3)
        self.server_status.setObjectName(u"server_status")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.server_status.setFont(font)
        self.server_status.setStyleSheet(u"color: rgb(204, 0, 0);")

        self.horizontalLayout.addWidget(self.server_status)

        self.elapsed_timer = QLabel(self.widget_3)
        self.elapsed_timer.setObjectName(u"elapsed_timer")
        self.elapsed_timer.setMinimumSize(QSize(190, 0))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setItalic(False)
        self.elapsed_timer.setFont(font1)
        self.elapsed_timer.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.elapsed_timer)


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
        self.horizontalLayout_6 = QHBoxLayout(self.home_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.textEdit = QTextEdit(self.home_page)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.textEdit)

        self.stackedWidget.addWidget(self.home_page)
        self.images_page = QWidget()
        self.images_page.setObjectName(u"images_page")
        self.verticalLayout_14 = QVBoxLayout(self.images_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.upper_image_page = QWidget(self.images_page)
        self.upper_image_page.setObjectName(u"upper_image_page")
        self.upper_image_page.setMinimumSize(QSize(0, 50))
        self.upper_image_page.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.upper_image_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.browse_img = QPushButton(self.upper_image_page)
        self.browse_img.setObjectName(u"browse_img")
        self.browse_img.setMinimumSize(QSize(0, 30))
        self.browse_img.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout_4.addWidget(self.browse_img)

        self.horizontalSpacer_2 = QSpacerItem(138, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.image_view_status = QLabel(self.upper_image_page)
        self.image_view_status.setObjectName(u"image_view_status")
        self.image_view_status.setMinimumSize(QSize(100, 0))
        self.image_view_status.setMaximumSize(QSize(500, 16777215))
        self.image_view_status.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.image_view_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.image_view_status)

        self.horizontalSpacer_3 = QSpacerItem(108, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.download_image = QPushButton(self.upper_image_page)
        self.download_image.setObjectName(u"download_image")
        self.download_image.setMinimumSize(QSize(0, 30))
        self.download_image.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout_4.addWidget(self.download_image)

        self.delete_img = QPushButton(self.upper_image_page)
        self.delete_img.setObjectName(u"delete_img")
        self.delete_img.setMinimumSize(QSize(0, 30))
        self.delete_img.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout_4.addWidget(self.delete_img)


        self.verticalLayout_12.addWidget(self.upper_image_page)

        self.image_box = ScaledLabel(self.images_page)
        self.image_box.setObjectName(u"image_box")
        self.image_box.setMaximumSize(QSize(1920, 1080))
        self.image_box.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_12.addWidget(self.image_box)

        self.lower_image_page = QWidget(self.images_page)
        self.lower_image_page.setObjectName(u"lower_image_page")
        self.lower_image_page.setMinimumSize(QSize(0, 70))
        self.lower_image_page.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.lower_image_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.prev_img = QPushButton(self.lower_image_page)
        self.prev_img.setObjectName(u"prev_img")
        self.prev_img.setMinimumSize(QSize(0, 30))
        self.prev_img.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout_5.addWidget(self.prev_img)

        self.next_img = QPushButton(self.lower_image_page)
        self.next_img.setObjectName(u"next_img")
        self.next_img.setMinimumSize(QSize(0, 30))
        self.next_img.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout_5.addWidget(self.next_img)


        self.verticalLayout_12.addWidget(self.lower_image_page)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.stackedWidget.addWidget(self.images_page)
        self.videos_page = QWidget()
        self.videos_page.setObjectName(u"videos_page")
        self.label_9 = QLabel(self.videos_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(210, 220, 381, 201))
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.stackedWidget.addWidget(self.videos_page)
        self.configs_page = QWidget()
        self.configs_page.setObjectName(u"configs_page")
        self.verticalLayout_16 = QVBoxLayout(self.configs_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.config_list = QWidget(self.configs_page)
        self.config_list.setObjectName(u"config_list")
        self.config_list.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.config_list)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.config_list)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(20)
        self.label.setFont(font2)
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

        self.formLayout_18 = QFormLayout()
        self.formLayout_18.setObjectName(u"formLayout_18")
        self.video_fps_label = QLabel(self.config_list)
        self.video_fps_label.setObjectName(u"video_fps_label")
        self.video_fps_label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_18.setWidget(0, QFormLayout.LabelRole, self.video_fps_label)

        self.video_fps_lineEdit = QLineEdit(self.config_list)
        self.video_fps_lineEdit.setObjectName(u"video_fps_lineEdit")
        self.video_fps_lineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_18.setWidget(0, QFormLayout.FieldRole, self.video_fps_lineEdit)


        self.verticalLayout_6.addLayout(self.formLayout_18)


        self.verticalLayout_13.addLayout(self.verticalLayout_6)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.config_list)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
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
        self.label_3.setFont(font2)
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
        self.label_5.setFont(font2)
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


        self.horizontalLayout_7.addWidget(self.config_list)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.project_widget = QWidget(self.configs_page)
        self.project_widget.setObjectName(u"project_widget")
        self.project_widget.setMaximumSize(QSize(10000, 600))
        self.verticalLayout_3 = QVBoxLayout(self.project_widget)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.project_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.label_6)

        self.project_listwidget = QListWidget(self.project_widget)
        self.project_listwidget.setObjectName(u"project_listwidget")
        self.project_listwidget.setMaximumSize(QSize(1000, 16777215))
        self.project_listwidget.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_3.addWidget(self.project_listwidget)


        self.verticalLayout_15.addWidget(self.project_widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.configs_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.label_7)

        self.current_config = QTextEdit(self.configs_page)
        self.current_config.setObjectName(u"current_config")
        self.current_config.setMaximumSize(QSize(300, 500))
        self.current_config.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_10.addWidget(self.current_config)


        self.horizontalLayout_3.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.configs_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setPointSize(15)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.label_2)

        self.config_profile = QListWidget(self.configs_page)
        self.config_profile.setObjectName(u"config_profile")
        self.config_profile.setMaximumSize(QSize(200, 16777215))
        self.config_profile.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.config_profile)


        self.horizontalLayout_3.addLayout(self.verticalLayout_11)


        self.verticalLayout_15.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setContentsMargins(10, -1, -1, -1)
        self.video_name_Label = QLabel(self.configs_page)
        self.video_name_Label.setObjectName(u"video_name_Label")
        self.video_name_Label.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.video_name_Label)

        self.video_name_LineEdit = QLineEdit(self.configs_page)
        self.video_name_LineEdit.setObjectName(u"video_name_LineEdit")
        self.video_name_LineEdit.setMaximumSize(QSize(300, 16777215))
        self.video_name_LineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.video_name_LineEdit)


        self.verticalLayout_16.addLayout(self.formLayout_9)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(400, -1, -1, -1)
        self.save_button = QPushButton(self.configs_page)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(0, 30))
        self.save_button.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout_9.addWidget(self.save_button)

        self.save_new_profile = QPushButton(self.configs_page)
        self.save_new_profile.setObjectName(u"save_new_profile")
        self.save_new_profile.setMinimumSize(QSize(0, 30))
        self.save_new_profile.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout_9.addWidget(self.save_new_profile)

        self.update_profile = QPushButton(self.configs_page)
        self.update_profile.setObjectName(u"update_profile")
        self.update_profile.setMinimumSize(QSize(0, 30))
        self.update_profile.setStyleSheet(u"background-color: rgb(94, 92, 100);")

        self.horizontalLayout_9.addWidget(self.update_profile)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.stackedWidget.addWidget(self.configs_page)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

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

        self.images_1 = QPushButton(self.icon_only_widget)
        self.images_1.setObjectName(u"images_1")
        self.images_1.setCheckable(True)
        self.images_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.images_1)

        self.videos_1 = QPushButton(self.icon_only_widget)
        self.videos_1.setObjectName(u"videos_1")
        self.videos_1.setCheckable(True)
        self.videos_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.videos_1)

        self.verticalSpacer = QSpacerItem(18, 448, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.exit_1 = QPushButton(self.icon_only_widget)
        self.exit_1.setObjectName(u"exit_1")
        self.exit_1.setCheckable(True)
        self.exit_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.exit_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

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
        self.images_1.toggled.connect(self.images_2.setChecked)
        self.videos_1.toggled.connect(self.videos_2.setChecked)
        self.images_2.toggled.connect(self.images_1.setChecked)
        self.videos_2.toggled.connect(self.videos_1.setChecked)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.script_2.setText(QCoreApplication.translate("MainWindow", u"Script", None))
        self.config_2.setText(QCoreApplication.translate("MainWindow", u"Configs", None))
        self.images_2.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.videos_2.setText(QCoreApplication.translate("MainWindow", u"Videos", None))
        self.exit_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.server_status.setText(QCoreApplication.translate("MainWindow", u"Server: Disconnected", None))
        self.elapsed_timer.setText(QCoreApplication.translate("MainWindow", u"Elapsed Time: 00:00:00", None))
        self.run_script.setText(QCoreApplication.translate("MainWindow", u"Run Script", None))
        self.stop_script.setText(QCoreApplication.translate("MainWindow", u"Force Stop", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">WELCOME</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:26pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#---------CONFIGURATION---------#<"
                        "/p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># how many photos matched from 1 photo</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">no_photo_match</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># this is for the detection zone in the 2nd image, the 2 values determine how much away from the object is relevant for detection</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">x_offset_for_detection  # ?? unit away from obj top left x</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\">y_offset_for_detection  # ?? unit away from obj top left y</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">width_offset # How wide the detect zone is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">height_offset # How tall the detect zone is</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># determine how close can boxes of same class be</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">min_x_offset_same_cls # ?? unit away from the closest box of same class</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">min_y_offset_same_cls # ?? unit away from the closest box of same class</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># for detection confidence and threshold</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ratio_threshold # the higher, the more lenient the matching is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">min_matches # higher values will allow boxes with lower confidence</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">max_size_acceptable # the maximum"
                        " size that a new box can replace an existing box, i.e. x times larger than original,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># set higher if boxes diminish fast or object is sometimes big and sometimes small</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># for matching computation, may need higher values only for ambiguous objects</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"># THIS PART BOTTLENECKS THE PROGRAM THE MOST, SETTING EITHER VALUE ABO"
                        "VE 300000 WILL CRASH </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nfeature_obj</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nfeature_detect_zone</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">#---------CONFIGURATION---------#</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.browse_img.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.image_view_status.setText(QCoreApplication.translate("MainWindow", u"Choose an image folder", None))
        self.download_image.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.delete_img.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.image_box.setText("")
        self.prev_img.setText(QCoreApplication.translate("MainWindow", u"Previous Image", None))
        self.next_img.setText(QCoreApplication.translate("MainWindow", u"Next Image", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"VIDEOS PAGE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Resolutions", None))
        self.res_x_label.setText(QCoreApplication.translate("MainWindow", u"resolution_x", None))
        self.res_y_label.setText(QCoreApplication.translate("MainWindow", u"resolution_y", None))
        self.video_fps_label.setText(QCoreApplication.translate("MainWindow", u"video_fps", None))
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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Current configs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.video_name_Label.setText(QCoreApplication.translate("MainWindow", u"video_name", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.save_new_profile.setText(QCoreApplication.translate("MainWindow", u"Save as new profile", None))
        self.update_profile.setText(QCoreApplication.translate("MainWindow", u"Update this profile", None))
        self.home_1.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.script_1.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.config_1.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.images_1.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.videos_1.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.exit_1.setText(QCoreApplication.translate("MainWindow", u"E", None))
    # retranslateUi

