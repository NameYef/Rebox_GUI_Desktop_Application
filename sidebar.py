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
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

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
        self.icon_name_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(94, 92, 100);\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"	text-align:left;\n"
"	height:30px;\n"
"	padding-left:10px;\n"
"	border:none;\n"
"}\n"
"QPushButton::checked {\n"
"	\n"
"	color: rgb(94, 92, 100);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font-weight:bold;\n"
"}\n"
"\n"
"")
        self.verticalLayout_26 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSpacer_4 = QSpacerItem(18, 94, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_2 = QPushButton(self.icon_name_widget)
        self.home_2.setObjectName(u"home_2")
        self.home_2.setMinimumSize(QSize(0, 0))
        self.home_2.setStyleSheet(u"")
        self.home_2.setCheckable(True)
        self.home_2.setChecked(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2)

        self.script_2 = QPushButton(self.icon_name_widget)
        self.script_2.setObjectName(u"script_2")
        self.script_2.setStyleSheet(u"")
        self.script_2.setCheckable(True)
        self.script_2.setChecked(False)
        self.script_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.script_2)

        self.config_2 = QPushButton(self.icon_name_widget)
        self.config_2.setObjectName(u"config_2")
        self.config_2.setStyleSheet(u"")
        self.config_2.setCheckable(True)
        self.config_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.config_2)

        self.images_2 = QPushButton(self.icon_name_widget)
        self.images_2.setObjectName(u"images_2")
        self.images_2.setStyleSheet(u"")
        self.images_2.setCheckable(True)
        self.images_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.images_2)

        self.videos_2 = QPushButton(self.icon_name_widget)
        self.videos_2.setObjectName(u"videos_2")
        self.videos_2.setStyleSheet(u"")
        self.videos_2.setCheckable(True)
        self.videos_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.videos_2)


        self.verticalLayout_25.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(18, 448, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_2)

        self.exit_2 = QPushButton(self.icon_name_widget)
        self.exit_2.setObjectName(u"exit_2")
        self.exit_2.setStyleSheet(u"")
        self.exit_2.setCheckable(True)
        self.exit_2.setAutoExclusive(True)

        self.verticalLayout_25.addWidget(self.exit_2)


        self.verticalLayout_26.addLayout(self.verticalLayout_25)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toggle = QPushButton(self.widget_3)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")
        self.toggle.setCheckable(True)

        self.horizontalLayout.addWidget(self.toggle)

        self.refresh_button = QPushButton(self.widget_3)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

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
        self.verticalLayout_24 = QVBoxLayout(self.script_page)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.image_preview = ScaledLabel(self.script_page)
        self.image_preview.setObjectName(u"image_preview")
        self.image_preview.setMinimumSize(QSize(0, 400))
        self.image_preview.setMargin(0)

        self.verticalLayout_5.addWidget(self.image_preview)

        self.console = QWidget(self.script_page)
        self.console.setObjectName(u"console")
        self.console.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_4 = QVBoxLayout(self.console)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.console_log = QTextEdit(self.console)
        self.console_log.setObjectName(u"console_log")
        self.console_log.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.console_log)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.run_script = QPushButton(self.console)
        self.run_script.setObjectName(u"run_script")
        self.run_script.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"")
        self.run_script.setCheckable(False)
        self.run_script.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.run_script)

        self.stop_script = QPushButton(self.console)
        self.stop_script.setObjectName(u"stop_script")
        self.stop_script.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"")
        self.stop_script.setCheckable(True)
        self.stop_script.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.stop_script)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.console)


        self.verticalLayout_24.addLayout(self.verticalLayout_5)

        self.stackedWidget.addWidget(self.script_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.horizontalLayout_6 = QHBoxLayout(self.home_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tabWidget = QTabWidget(self.home_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.tab_overview = QWidget()
        self.tab_overview.setObjectName(u"tab_overview")
        self.verticalLayout_20 = QVBoxLayout(self.tab_overview)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.introduction = QTextEdit(self.tab_overview)
        self.introduction.setObjectName(u"introduction")
        self.introduction.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_20.addWidget(self.introduction)

        self.tabWidget.addTab(self.tab_overview, "")
        self.tab_config_doc = QWidget()
        self.tab_config_doc.setObjectName(u"tab_config_doc")
        self.verticalLayout_21 = QVBoxLayout(self.tab_config_doc)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.documentation = QTextEdit(self.tab_config_doc)
        self.documentation.setObjectName(u"documentation")

        self.verticalLayout_21.addWidget(self.documentation)

        self.tabWidget.addTab(self.tab_config_doc, "")
        self.tab_change_log = QWidget()
        self.tab_change_log.setObjectName(u"tab_change_log")
        self.verticalLayout_22 = QVBoxLayout(self.tab_change_log)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.update_log = QTextEdit(self.tab_change_log)
        self.update_log.setObjectName(u"update_log")

        self.verticalLayout_22.addWidget(self.update_log)

        self.tabWidget.addTab(self.tab_change_log, "")
        self.tab_about = QWidget()
        self.tab_about.setObjectName(u"tab_about")
        self.verticalLayout_23 = QVBoxLayout(self.tab_about)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.about = QTextEdit(self.tab_about)
        self.about.setObjectName(u"about")

        self.verticalLayout_23.addWidget(self.about)

        self.tabWidget.addTab(self.tab_about, "")

        self.horizontalLayout_6.addWidget(self.tabWidget)

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
        self.browse_img.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

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

        self.download_img = QPushButton(self.upper_image_page)
        self.download_img.setObjectName(u"download_img")
        self.download_img.setMinimumSize(QSize(0, 30))
        self.download_img.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.download_img)


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
        self.prev_img.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.prev_img)

        self.next_img = QPushButton(self.lower_image_page)
        self.next_img.setObjectName(u"next_img")
        self.next_img.setMinimumSize(QSize(0, 30))
        self.next_img.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.next_img)


        self.verticalLayout_12.addWidget(self.lower_image_page)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.stackedWidget.addWidget(self.images_page)
        self.videos_page = QWidget()
        self.videos_page.setObjectName(u"videos_page")
        self.verticalLayout_19 = QVBoxLayout(self.videos_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.upper_video_page = QWidget(self.videos_page)
        self.upper_video_page.setObjectName(u"upper_video_page")
        self.upper_video_page.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_8 = QHBoxLayout(self.upper_video_page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.browse_vid = QPushButton(self.upper_video_page)
        self.browse_vid.setObjectName(u"browse_vid")
        self.browse_vid.setMinimumSize(QSize(0, 30))
        self.browse_vid.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.browse_vid)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.video_view_status = QLabel(self.upper_video_page)
        self.video_view_status.setObjectName(u"video_view_status")
        self.video_view_status.setMinimumSize(QSize(100, 0))
        self.video_view_status.setMaximumSize(QSize(500, 16777215))
        self.video_view_status.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.video_view_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.video_view_status, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.download_vid = QPushButton(self.upper_video_page)
        self.download_vid.setObjectName(u"download_vid")
        self.download_vid.setMinimumSize(QSize(0, 30))
        self.download_vid.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.download_vid)


        self.verticalLayout_18.addWidget(self.upper_video_page)

        self.video_screen = QVideoWidget(self.videos_page)
        self.video_screen.setObjectName(u"video_screen")

        self.verticalLayout_18.addWidget(self.video_screen)

        self.pause_resume = QPushButton(self.videos_page)
        self.pause_resume.setObjectName(u"pause_resume")
        self.pause_resume.setMinimumSize(QSize(0, 30))
        self.pause_resume.setMaximumSize(QSize(100, 16777215))
        self.pause_resume.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_18.addWidget(self.pause_resume, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lower_video_page = QWidget(self.videos_page)
        self.lower_video_page.setObjectName(u"lower_video_page")
        self.lower_video_page.setMinimumSize(QSize(0, 100))
        self.lower_video_page.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_17 = QVBoxLayout(self.lower_video_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.vid_slider = QSlider(self.lower_video_page)
        self.vid_slider.setObjectName(u"vid_slider")
        self.vid_slider.setStyleSheet(u"color: rgb(94, 92, 100);")
        self.vid_slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_17.addWidget(self.vid_slider)

        self.volume_slider = QSlider(self.lower_video_page)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMaximumSize(QSize(150, 16777215))
        self.volume_slider.setStyleSheet(u"color: rgb(94, 92, 100);\n"
"")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(100)
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)
        self.volume_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.volume_slider.setTickInterval(10)

        self.verticalLayout_17.addWidget(self.volume_slider)


        self.verticalLayout_18.addWidget(self.lower_video_page)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)

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
        self.save_button.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.save_button)

        self.save_new_profile = QPushButton(self.configs_page)
        self.save_new_profile.setObjectName(u"save_new_profile")
        self.save_new_profile.setMinimumSize(QSize(0, 30))
        self.save_new_profile.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.save_new_profile)

        self.update_profile = QPushButton(self.configs_page)
        self.update_profile.setObjectName(u"update_profile")
        self.update_profile.setMinimumSize(QSize(0, 30))
        self.update_profile.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.update_profile)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.stackedWidget.addWidget(self.configs_page)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(70, 70))
        self.icon_only_widget.setMaximumSize(QSize(70, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(94, 92, 100);\n"
"}\n"
"\n"
"QPushButton {\n"
"\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	height:30px;\n"
"	border:none;\n"
"}\n"
"QPushButton::checked {\n"
"	\n"
"	color: rgb(94, 92, 100);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_28 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSpacer_3 = QSpacerItem(18, 94, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_27.addItem(self.verticalSpacer_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_1 = QPushButton(self.icon_only_widget)
        self.home_1.setObjectName(u"home_1")
        self.home_1.setStyleSheet(u"")
        self.home_1.setCheckable(True)
        self.home_1.setChecked(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1)

        self.script_1 = QPushButton(self.icon_only_widget)
        self.script_1.setObjectName(u"script_1")
        self.script_1.setStyleSheet(u"")
        self.script_1.setCheckable(True)
        self.script_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.script_1)

        self.config_1 = QPushButton(self.icon_only_widget)
        self.config_1.setObjectName(u"config_1")
        self.config_1.setStyleSheet(u"")
        self.config_1.setCheckable(True)
        self.config_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.config_1)

        self.images_1 = QPushButton(self.icon_only_widget)
        self.images_1.setObjectName(u"images_1")
        self.images_1.setStyleSheet(u"")
        self.images_1.setCheckable(True)
        self.images_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.images_1)

        self.videos_1 = QPushButton(self.icon_only_widget)
        self.videos_1.setObjectName(u"videos_1")
        self.videos_1.setStyleSheet(u"")
        self.videos_1.setCheckable(True)
        self.videos_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.videos_1)


        self.verticalLayout_27.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(18, 448, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer)

        self.exit_1 = QPushButton(self.icon_only_widget)
        self.exit_1.setObjectName(u"exit_1")
        self.exit_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"height:30px;")
        self.exit_1.setCheckable(True)
        self.exit_1.setAutoExclusive(True)

        self.verticalLayout_27.addWidget(self.exit_1)


        self.verticalLayout_28.addLayout(self.verticalLayout_27)


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
        self.tabWidget.setCurrentIndex(0)


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
        self.toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle SideBar", None))
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.server_status.setText(QCoreApplication.translate("MainWindow", u"Server: Disconnected", None))
        self.elapsed_timer.setText(QCoreApplication.translate("MainWindow", u"Elapsed Time: 00:00:00", None))
        self.image_preview.setText("")
        self.console_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">make sure to fill the config first</p></body></html>", None))
        self.run_script.setText(QCoreApplication.translate("MainWindow", u"Run Script", None))
        self.stop_script.setText(QCoreApplication.translate("MainWindow", u"Force Stop", None))
        self.introduction.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:700; color:#000000;\">WELCOME</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Introduction</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This is an UI designed for the rebox algorithm (label and bounding box correction). The algorithm generates a new directory of corrected labels, boxes them and generates a video from the boxed images. Go to the Documentation tab to see how the configs work. Check out the Updates tab to see what has been updated for both the underlying algorithm and the UI. See the more detailed explanation of the algorithm in the About tab.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; text-decoration: underline;\">NOTE:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Project folder must consist of both images and labels subfolder (Must be called images and labels)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- classes.txt is optional in labels folder</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- When running script, it may take more than a few seconds for the first output to be shown. Still looking for a way to show output with 0 buffer after making the algorithm run in a screen.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Although the resolutions of the image is automatically found in the algorithm, you still need to fill them in the configs (subject to change)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Documentation may not be up to date</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; text-decoration: underline;\">Usage:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Understand e"
                        "ach config, (Go to the documentation tab)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Go to the Configs page, fill the configs, choose a project folder, name the generated video (ok to leave the video name empty, now generates default names)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- Go to the Script page, run the script and see real-time console logs of the process</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">- After the script finished running, go to the Images and Videos page to view the results</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:"
                        "12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p s"
                        "tyle=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_overview), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.documentation.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">Documentation of configs:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-size:18pt; text-decoration: underline;\">Resolution section</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Provide the resolutions of the project images to be processed, also the video fps preferred</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#9141ac;\">resolution_x</span><span style=\" font-size:12pt;\">: the width of the images (Default: 1920)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0"
                        "px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#9141ac;\">resolution_y</span><span style=\" font-size:12pt;\">: the height of the images (Default: 1080)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#9141ac;\">video_fps</span><span style=\" font-size:12pt;\">: the frames per second for the video (Default: 10)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; text-decoration: underline;\">Effectiveness section</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This part controls the effectiveness and also the speed of the algorithm. Typically, the higher the numbers given to these configs, the better the outcomes are, but the speed of the algorithm will also be heavily reduced. Carefully tweak these configs according to your preferences.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                        " -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#9141ac;\">no_photo_match</span><span style=\" font-size:12pt;\">: how many images next to the current image will be used to correct labels. The higher this number is, the more consistent the box sizes would be (Cannot guarantee significant improvement, but its still better to have this number higher than 1) (Default: 3)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#9141ac;\">nfeature_obj</span><span style=\" font-size:12pt;\">: the amount of featur"
                        "es extracted from each object labelled in the original labels. Naturally, the higher this number is, the more consistent the box sizes will be. However, this config along with nfeature_detect_zone are the major bottlenecks of this algorithm. (Don't set either of these 2 value over 300000 or the program will either freeze or crash) (Default: 10000)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#9141ac;\">nfeature_detect_zone</span><span style=\" font-size:12pt;\">: the amount of features extracted from the detection zone. Instead of comparing an object to the entire image, only a portion of the image is used (configured in the offset section). Smaller values may be better if you want to detect "
                        "moving objects from a static background. Higher values to prevent boxes from shrinking fast. (Default: 10000)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; text-decoration: underline;\">Offsets section</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This part determines the detection zone. The x, y offsets determine how many x, y units away from the original object's top left coordinates. The width and height offs"
                        "ets determine how big the detection zone is. This design allows more accurate matchings when the camera is clearly going to a certain direction. As these offset settings allow the user to focus on a zone in a biased way. For example, the x,y offsets are high but the width offset is smaller than the x offset means the left part of the image is more focused on, which is good when the camera travels to the right such that the objects move to the left. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Note that the width of the detection zone = original width of ob"
                        "ject + width_offset</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Same logic applies to the height of the detection zone</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9141ac;\">x_offset_for_detection</span><span style=\" font-size:12pt;\">: determines how many pixels away from top left x-coord of object (Default: 200 for 1920 pixel wide image)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9141ac;\">y_offset_for_detection</span><span style=\" font-size:12pt;\">: determines how many pixels away from top left y-coord of object (Default: 200  for 1080 pixel tall image)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9141ac;\">width_offset</span><span style=\" font-size:12pt;\">: determines the extra width of the detection zone (Default: 200), width offset should be at least the x-offset if camera is not moving in a clear direction</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\""
                        "><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9141ac;\">height_offset</span><span style=\" font-size:12pt;\">: determines how tall the detection zone is (Default 200), height offset should be at least the y-offset if camera is not moving in a clear direction</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9141ac;\">min_x_offset_same_cls</span><span style=\" font-size:12pt;\">: determines how close can new generated bounding box be for the same class using the CENTER COORDINATES of the new box, these configs are set to prevent multiple same bounding boxes being generated on the same obje"
                        "ct/ very close to the same object (Default: 30)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9141ac;\">min_y_offset_same_cls</span><span style=\" font-size:12pt;\">: determines how close can new generated bounding box be for the same class using the CENTER COORDINATES of the new box. (Default: 30)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; text-decoration: underline;\">Confidence section</span></p>\n"
"<p style=\"-"
                        "qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">This part determines the generation of bounding boxes. More new boxes will be generated if the confidence threshold is lower but accuracy cannot be guaranteed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9141ac;\">ratio_threshold</span><span style=\" font-size:12pt;\">: the lower this value is, the more harsh the threshold is. Higher values are sometimes better for amb"
                        "iguous objects. Value ranges from 0 to 1. (Default: 0.5)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9141ac;\">min_matches</span><span style=\" font-size:12pt;\">: The number of minimum feature matches required to accept a new generated box. Setting this value low can help eliminate lingering boxes that may not be relevant after a few images</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#9141ac;\">max_size_acce"
                        "ptable</span><span style=\" font-size:12pt;\">: The maximum size acceptable for a new box to be generated. Sometimes a new box can be few times larger than the original due to loose confidence setting. This setting prevents box with width or height being a certain times larger or more from being accepted.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config_doc), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.update_log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">16/7 Additions</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Implemented screen algorithm running, user can leave the"
                        " app when the algorithm is running without terminating it. Latest output will be shown once the app is opened again. (Output is slower compared to before)</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User cannot save config when script is running</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Implemented image preview in script tab, user can now see the latest generated image while the algorithm runs.</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Relabelled, boxed folder and video file share the same name now</li></ul>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"12-7-additions\"></a>"
                        "<span style=\" font-size:12pt; font-weight:700;\">1</span><span style=\" font-size:12pt; font-weight:700;\">5/7 Additions</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">finished documentation</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Added tab view in home page</li></ul>\n"
"<p style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"12-7-additions\"></a><span style=\" font-size:12pt; font-weight:700;\">1</span><span style=\" font-size:12pt; font-weight:700;\">2/7 Additions</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-in"
                        "dent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Fully implemented video player</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Added download &amp; delete functions for image viewer and video player</li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"10-7-additions\"></a><span style=\" font-size:large; font-weight:700;\">1</span><span style=\" font-size:large; font-weight:700;\">0/7 Additions</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Added "
                        "default video name </span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Added config profile </li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Changed up the plot_label, (no longer hard coding classes and colors)</li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"9-7-additions\"></a><span style=\" font-size:large; font-weight:700;\">9</span><span style=\" font-size:large; font-weight:700;\">/7 Additions</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Implemented I"
                        "mage viewing tab, user can choose which image folder to view and view with next/prev button</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Added refresh button to refresh when server up again</li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"8-7-additions\"></a><span style=\" font-size:large; font-weight:700;\">8</span><span style=\" font-size:large; font-weight:700;\">/7 Additions</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">plot_labels and image_to_video now automatically create or locate folder</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fixed the output problem in script tab</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Implemented server side config storing</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sped up real time output</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Implemented timer to keep track of algorithm running time</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Users can now see the current configs</li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"5-7-additions\"></a><span style=\" font-size:large; font-weight:700;\">5</span><span style=\" font-size:large; font-weight:700;\">/7 Additions</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Script, config tab completed</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">flask server set up to run script on server and listdir on server</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">user can choose dir in project folder in server</li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left"
                        ":0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"4-7-additions\"></a><span style=\" font-size:large; font-weight:700;\">4</span><span style=\" font-size:large; font-weight:700;\">/7 Additions</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Made an UI with side bars (home, script, config tab)</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">implemented local script running and config saving</li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"28-6-additions\"></a><span style=\" font-size:large; font-weight:700;\">2</span><span style=\" font-size:l"
                        "arge; font-weight:700;\">8/6 Additions</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Fixed multiprocessing not working</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">added prevention of same class boxes cloning themselves just because the center is slightly out of the original box (still need work)</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fixed overwriting original labels</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Probably fixed th"
                        "e label txt bug</li></ul>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"27-6-additions\"></a><span style=\" font-size:large; font-weight:700;\">2</span><span style=\" font-size:large; font-weight:700;\">7/6 Additions</span></h3>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Instead of matching with the whole image 2, only a relevant range of image 2 is used for matching, this means more features end up in a relevant part</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1 image is used to match with the next 3 images (DOESNT WORK)</li>\n"
"<li style=\" font-size:12pt;\" style=\" margi"
                        "n-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">allow boxes with larger size to replace those with smaller size IF SAME CLASS AND CENTER IN BOX, however new box cannot be more than 1.3 times larger to prevent extremely big box</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nfeature for obj and background upped to 50000 and 100000 (from 3000 and 100000)</li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Older updates not logged</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_change_log), QCoreApplication.translate("MainWindow", u"Page", None))
        self.about.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">About this app</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WIP </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_about), QCoreApplication.translate("MainWindow", u"Page", None))
        self.browse_img.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.image_view_status.setText(QCoreApplication.translate("MainWindow", u"Choose an image folder", None))
        self.download_img.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.image_box.setText("")
        self.prev_img.setText(QCoreApplication.translate("MainWindow", u"Previous Image", None))
        self.next_img.setText(QCoreApplication.translate("MainWindow", u"Next Image", None))
        self.browse_vid.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.video_view_status.setText(QCoreApplication.translate("MainWindow", u"Choose a video", None))
        self.download_vid.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.pause_resume.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
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

