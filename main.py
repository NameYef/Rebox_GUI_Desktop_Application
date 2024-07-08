import sys
import os
import natsort
import requests
from PySide6.QtCore import QProcess, QIODevice, QUrl, QEventLoop
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6 import QtGui
from sidebar import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.url = "http://dev.alphaaitech.com:40030/"

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Rebox")

        self.ui.icon_name_widget.hide()

        self.ui.home_1.clicked.connect(self.switch_to_home_page)
        self.ui.home_2.clicked.connect(self.switch_to_home_page)

        self.ui.script_1.clicked.connect(self.switch_to_script_page)
        self.ui.script_2.clicked.connect(self.switch_to_script_page)

        self.ui.config_1.clicked.connect(self.switch_to_configs_page)
        self.ui.config_2.clicked.connect(self.switch_to_configs_page)

        self.ui.run_script.clicked.connect(self.run_script)
        self.ui.stop_script.clicked.connect(self.stop_script)

        self.ui.console_log.setReadOnly(True)
        # self.process = QProcess(self)
        # self.process.setProcessChannelMode(QProcess.MergedChannels)
        # self.process.readyReadStandardOutput.connect(self.read_output)
        # self.process.finished.connect(self.script_finished)

        self.ui.save_button.clicked.connect(self.save_config)

        self.ui.res_x_lineEdit.setPlaceholderText("default: 1920")
        self.ui.res_y_lineEdit.setPlaceholderText("default: 1080")
        self.ui.video_fps_lineEdit.setPlaceholderText("default: 10")
        self.ui.no_photo_match_lineEdit.setPlaceholderText("default: 3")
        self.ui.nfeature_obj_lineEdit.setPlaceholderText("default 3000")
        self.ui.nfeature_det_lineEdit.setPlaceholderText("default: 100000")
        self.ui.x_off_lineEdit.setPlaceholderText("default: 500")
        self.ui.y_off_lineEdit.setPlaceholderText("default: 300")
        self.ui.width_off_lineEdit.setPlaceholderText("default: 800")
        self.ui.height_off_lineEdit.setPlaceholderText("default: 500")
        self.ui.min_x_lineEdit.setPlaceholderText("default: 30")
        self.ui.min_y_lineEdit.setPlaceholderText("default: 25")
        self.ui.ratio_lineEdit.setPlaceholderText("default: 0.5")
        self.ui.min_match_lineEdit.setPlaceholderText("default: 15")
        self.ui.max_size_lineEdit.setPlaceholderText("default: 1.3")

        self.process = None
        self.manager = QNetworkAccessManager(self)
        #    Indexes         config_list
        #       0        {"resolution_x":"",              # resolutions
        #       1         "resolution_y":"",
        #       2         "video_fps":"",
        #       3         "no_photo_match":"",            # effectiveness
        #       4         "nfeature_obj":"",
        #       5         "nfeature_detect_zone":"",
        #       6         "x_offset_for_detection":"",    # offsets
        #       7         "y_offset_for_detection":"",
        #       8         "width_offset":"",
        #       9         "height_offset":"",
        #       10         "min_x_offset_same_cls":"",
        #       11         "min_y_offset_same_cls":"",
        #       12         "ratio_threshold":"",           # confidence
        #       13         "min_matches":"",
        #       14         "max_size_acceptable":"",
        #       15         "project_folder":""
        #       16         "boxed_folder_name":"",
        #       17         "video_name":"",
        #       18         "":""
        #                }
        
        self.projects_directory = "./projects"
        self.config_list = [1920,1080,10,3,3000,100000,500,300,800,500,30,25,0.5,15,1.3, ""]    # default config list values
        with open("config.txt", "w") as f:
            for i in self.config_list:
                f.write(f"{i}\n")
        
        self.populate_directory_list(self.projects_directory)

    def switch_to_home_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def switch_to_script_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def switch_to_configs_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def run_script(self):
        # self.ui.console_log.clear()
        # self.ui.run_script.setEnabled(False)
        # self.ui.stop_script.setEnabled(True)
        # self.process.start("python", ["script.py"])
        self.ui.console_log.clear()
        self.ui.run_script.setEnabled(False)
        self.ui.stop_script.setEnabled(True)

        url = QUrl(self.url+"run-script")
        request = QNetworkRequest(url)
        self.reply = self.manager.get(request)
        self.reply.readyRead.connect(self.read_output)
        self.reply.finished.connect(self.script_finished)

    def stop_script(self):
        # if self.process.state() == QProcess.Running:
        #     self.process.kill()
        #     self.ui.console_log.append("\nScript forcefully stopped.\n")
        #     self.script_finished()  # Handle UI changes when script is stopped
     # pass
        if self.reply.isRunning():
            self.reply.abort()
            self.ui.console_log.append("\nScript forcefully stopped.\n")
            self.script_finished()
    def read_output(self):
        # output = self.process.readAllStandardOutput().data().decode()
        # self.ui.console_log.moveCursor(QtGui.QTextCursor.End)
        # self.ui.console_log.insertPlainText(output)
        while self.reply.canReadLine():
            output = self.reply.readLine().data().decode().strip()
            self.ui.console_log.moveCursor(QtGui.QTextCursor.End)
            self.ui.console_log.insertPlainText(output + '\n')

    def script_finished(self):
        self.ui.run_script.setEnabled(True)
        self.ui.stop_script.setEnabled(False)

    def check_numeric(x):
        if not isinstance(x, (int, float, complex)):
            msg_box = QMessageBox()
            msg_box.setText('Invalid Input: Input numbers only!')
            msg_box.setWindowTitle('Invalid')
            
            # Set stylesheet for message box buttons
            msg_box.setStyleSheet('QPushButton { color: black; }')
            # Show the message box
            msg_box.exec()

    def populate_directory_list(self, dir):
        # Clear the list widget
        self.ui.project_listwidget.clear()

        # Get the list of directories inside the base directory
        directories = requests.get(self.url+"listdir").json()
        # directories = natsort.os_sorted([os.path.join(dir,d) for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))])

        # Add directories to the list widget
        self.ui.project_listwidget.addItems(directories)

    def save_config(self):
        entries = []
        entries.append(self.ui.res_x_lineEdit.text()) 
        entries.append(self.ui.res_y_lineEdit.text())
        entries.append(self.ui.video_fps_lineEdit.text())
        entries.append(self.ui.no_photo_match_lineEdit.text())
        entries.append(self.ui.nfeature_obj_lineEdit.text())
        entries.append(self.ui.nfeature_det_lineEdit.text())
        entries.append(self.ui.x_off_lineEdit.text())
        entries.append(self.ui.y_off_lineEdit.text())
        entries.append(self.ui.width_off_lineEdit.text())
        entries.append(self.ui.height_off_lineEdit.text())
        entries.append(self.ui.min_x_lineEdit.text())
        entries.append(self.ui.min_y_lineEdit.text())
        entries.append(self.ui.ratio_lineEdit.text())
        entries.append(self.ui.min_match_lineEdit.text())
        entries.append(self.ui.max_size_lineEdit.text())
        if self.ui.project_listwidget.selectedItems():
            entries.append(self.ui.project_listwidget.selectedItems()[0].text())
        else:
            entries.append("")

        for i in entries[:-1]:
            try:
                if i == "":
                    continue
                float(i)

            except ValueError:
                msg_box = QMessageBox()
                msg_box.setText('Invalid Input: Input numbers!')
                msg_box.setWindowTitle('Invalid')
                
                # Set stylesheet for message box buttons
                msg_box.setStyleSheet('QPushButton { color: black; }')
                # Show the message box
                msg_box.exec()
                return
            
        if entries[15] == "":
                msg_box = QMessageBox()
                msg_box.setText('Choose a project folder!')
                msg_box.setWindowTitle('Invalid')
                
                # Set stylesheet for message box buttons
                msg_box.setStyleSheet('QPushButton { color: black; }')
                # Show the message box
                msg_box.exec()
                return
        
        with open("config.txt", "w") as f:
            for i in range(len((entries))):
                if entries[i] == "":
                    f.write(f"{self.config_list[i]}\n")
                else:
                    f.write(f"{entries[i]}\n")

        msg_box = QMessageBox()
        msg_box.setText('Data has been saved successfully!')
        msg_box.setWindowTitle('Saved')
        
        # Set stylesheet for message box buttons
        msg_box.setStyleSheet('QPushButton { color: black; }')
        
        # Show the message box
        msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet('QLabel, QLineEdit, QTextEdit { color: black; }')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
