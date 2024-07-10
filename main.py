import sys
import os
import natsort
import requests
import time
from PySide6.QtCore import QProcess, QIODevice, QUrl, QEventLoop, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6 import QtGui
from sidebar import Ui_MainWindow
from img_dialog import Ui_Dialog

class Dialogo(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.par = parent
        
        self.setupUi(self)
        self.ok.clicked.connect(self.accept)
        self.cancel.clicked.connect(self.reject)
        self.img_folder_listWidget.clear()

        # Get the list of directories inside the base directory
        try:
            directories = requests.get(self.par.url+"listdir/boxed").json()
            # directories = natsort.os_sorted([os.path.join(dir,d) for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))])

            # Add directories to the list widget
            self.img_folder_listWidget.addItems(directories)
        except requests.exceptions.ConnectionError:
            print("OFFLINE MODE")
            self.img_folder_listWidget.addItems(["OFFLINE"])

    def accept(self):
        if self.img_folder_listWidget.selectedItems():
            self.par.image_dir = self.img_folder_listWidget.selectedItems()[0].text()
            self.par.image_list = requests.get(self.par.url+f"listdir/boxed/{self.par.image_dir}").json()
            
            self.par.image_index = 0
            self.par.load_image()
            
            

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.url = "http://dev.alphaaitech.com:40030/"

        self.ui = Ui_MainWindow()
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(self)
        self.ui.setupUi(self)
        self.setWindowTitle("Rebox")

        self.ui.icon_name_widget.hide()

        self.ui.home_1.clicked.connect(self.switch_to_home_page)
        self.ui.home_2.clicked.connect(self.switch_to_home_page)

        self.ui.script_1.clicked.connect(self.switch_to_script_page)
        self.ui.script_2.clicked.connect(self.switch_to_script_page)

        self.ui.config_1.clicked.connect(self.switch_to_configs_page)
        self.ui.config_2.clicked.connect(self.switch_to_configs_page)

        self.ui.images_1.clicked.connect(self.switch_to_images_page)
        self.ui.images_2.clicked.connect(self.switch_to_images_page)

        self.ui.videos_1.clicked.connect(self.switch_to_videos_page)
        self.ui.videos_2.clicked.connect(self.switch_to_videos_page)

        self.ui.refresh_button.clicked.connect(self.refresh)

        self.ui.run_script.clicked.connect(self.run_script)
        self.ui.stop_script.clicked.connect(self.stop_script)

        self.ui.next_img.clicked.connect(self.next_img)
        self.ui.prev_img.clicked.connect(self.prev_img)
        self.ui.browse_img.clicked.connect(self.browse_img)
        self.ui.delete_img.clicked.connect(self.delete_img)

        self.ui.console_log.setReadOnly(True)
        self.ui.current_config.setReadOnly(True)
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
        self.ui.video_name_LineEdit.setPlaceholderText("Enter boxed video name")
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
        #       16         "video_name":"",
        #       17         "":""
        #                }
        
        self.projects_directory = "./projects"
        self.config_name = ["resolution_x","resolution_y","video_fps","no_photo_match","nfeature_obj","nfeature_detect_zone","x_offset_for_detection","y_offset_for_detection"
                            ,"width_offset","height_offset","min_x_offset_same_cls","min_y_offset_same_cls","ratio_threshold","min_matches","max_size_acceptable","project_folder","video_name"]
        self.config_list = [1920,1080,10,3,3000,100000,500,300,800,500,30,25,0.5,15,1.3, "", ""]    # default config list values
        self.config_type = ["int", "int", "int", "int", "int", "int", "int", "int", "int", "int", "float", "float","float","int","float","str","str"]
        
        self.program_running = False
        self.second = 0
        self.program_elapsed_timer = QTimer(self)
        self.program_elapsed_timer.setInterval(1000)
        self.program_elapsed_timer.timeout.connect(self.elapsed_time)
        
        self.check_server_status()
        self.server_status_timer = QTimer(self)
        self.server_status_timer.setInterval(10000)
        self.server_status_timer.timeout.connect(self.check_server_status)
        self.server_status_timer.start()

        self.image_dir = ""
        self.image_list = []
        self.image_index = 0
        # self.test_image = os.path.join("./images",self.image_dir[self.img_index])
        # self.ui.image_box.setScaledContents(True)
        # pixmap = QtGui.QPixmap(self.test_image)
        # self.ui.image_box.setPixmap(pixmap)
        # self.setCentralWidget(self.ui.image_box)

        
        try: 
            requests.put(self.url+"store-config", json=self.config_list)
        except requests.exceptions.ConnectionError:
            print("OFFLINE MODE")
        with open("config.txt", "w") as f:
            for i in self.config_list:
                f.write(f"{i}\n")
        
        self.populate_directory_list()
        self.enter_cur_config()

    def check_server_status(self):
        try:
            requests.get(self.url + "/check")
            self.ui.server_status.setStyleSheet(u"color: rgb(0, 204, 0);")
            self.ui.server_status.setText("Server: Connected")
        except requests.exceptions.ConnectionError:
            self.ui.server_status.setStyleSheet(u"color: rgb(204, 0, 0);")
            self.ui.server_status.setText("Server: Disconnected")

    def refresh(self):
        self.check_server_status()
        self.populate_directory_list()

    def switch_to_home_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def switch_to_script_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def switch_to_configs_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    
    def switch_to_images_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def switch_to_videos_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def elapsed_time(self):
        if self.program_running:
            self.second += 1
            second = "{0:02d}".format(self.second%60)
            minute = "{0:02d}".format(self.second//60%60)
            hour = "{0:02d}".format(self.second//3600)
            self.ui.elapsed_timer.setText(f"Elapsed Time: {hour}:{minute}:{second}")

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
        
        self.program_running = True
        self.program_elapsed_timer.start()
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
            self.program_elapsed_timer.stop()
            self.program_running = False
            self.second = 0
            
    def read_output(self):
        # output = self.process.readAllStandardOutput().data().decode()
        # self.ui.console_log.moveCursor(QtGui.QTextCursor.End)
        # self.ui.console_log.insertPlainText(output)
        
        # self.now_elapsed_time = time.time()
        # second = round(self.now_elapsed_time-self.program_elapsed_time) % 3600 
        # self.ui.elapsed_timer.setText(f"Elapsed Time: {second}s")
        
        while self.reply.canReadLine():
            output = self.reply.readLine().data().decode().strip()
            self.ui.console_log.moveCursor(QtGui.QTextCursor.End)
            self.ui.console_log.insertPlainText(output + '\n')
        
    def script_finished(self):
        self.ui.run_script.setEnabled(True)
        self.ui.stop_script.setEnabled(False)
        self.program_elapsed_timer.stop()
        self.program_running = False
        self.second = 0

    def check_numeric(x):
        if not isinstance(x, (int, float, complex)):
            msg_box = QMessageBox()
            msg_box.setText('Invalid Input: Input numbers only!')
            msg_box.setWindowTitle('Invalid')
            
            # Set stylesheet for message box buttons
            msg_box.setStyleSheet('QPushButton { color: black; }')
            # Show the message box
            msg_box.exec()

    def populate_directory_list(self):
        # Clear the list widget
        self.ui.project_listwidget.clear()

        # Get the list of directories inside the base directory
        try:
            directories = requests.get(self.url+"listdir/projects").json()
            # directories = natsort.os_sorted([os.path.join(dir,d) for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))])

            # Add directories to the list widget
            self.ui.project_listwidget.addItems(directories)
        except requests.exceptions.ConnectionError:
            print("OFFLINE MODE")
            self.ui.project_listwidget.addItems(["OFFLINE"])

    def enter_cur_config(self):
        self.ui.current_config.clear()
        with open("config.txt","r") as f:
            data = f.readlines()
            for i in range(len(data)):
                self.ui.current_config.moveCursor(QtGui.QTextCursor.End)
                self.ui.current_config.insertPlainText(f"{self.config_name[i]}: {data[i]}")

    def show_error_msg(self, config):
            msg_box = QMessageBox()
            msg_box.setText(f'Invalid Input: {config}')
            msg_box.setWindowTitle('Invalid')
            
            # Set stylesheet for message box buttons
            msg_box.setStyleSheet('QPushButton { color: black; }')
            # Show the message box
            msg_box.exec()
            return
    
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
        entries.append(self.ui.video_name_LineEdit.text())
        print(entries)
        

        for i in range(len(entries) - 2):
            
            if entries[i] == "":
                continue
            
            if self.config_type[i] == "int":
                try:
                    int(entries[i])
                except ValueError:
                    self.show_error_msg(self.config_name[i])
                    return
            
            elif self.config_type[i] == "float":
                try:
                    float(entries[i])
                except ValueError:
                    self.show_error_msg(self.config_name[i])
                    return
            
            
        if entries[15] == "":       # index 15 is project_folder
                msg_box = QMessageBox()
                msg_box.setText('Choose a project folder!')
                msg_box.setWindowTitle('Invalid')
                
                # Set stylesheet for message box buttons
                msg_box.setStyleSheet('QPushButton { color: black; }')
                # Show the message box
                msg_box.exec()
                return
        
        if entries[16] == "":      # index 16 is video_name
            counter = 1
            try:
                video_dir = requests.get(self.url+"listdir/videos").json()
                while True:
                    if f"{entries[15]}_video{counter}.mp4" in video_dir:
                        counter += 1
                    break
                entries[16] = f"{entries[15]}_video{counter}"
            except requests.exceptions.ConnectionError:
                pass
        
        with open("config.txt", "w") as f:
            for i in range(15):
                if entries[i] == "":
                    f.write(f"{self.config_list[i]}\n")
                else:
                    f.write(f"{entries[i]}\n")
            for i in range(15, len(entries)):
                f.write(f"{entries[i]}\n")
        
        with open("config.txt","r") as f:
            final = [i.replace("\n","") for i in f.readlines()]

        # print(final)
        requests.put(self.url+"store-config", json=final)
        self.enter_cur_config()
        msg_box = QMessageBox()
        msg_box.setText('Data has been saved successfully!')
        msg_box.setWindowTitle('Saved')
        
        
        # Set stylesheet for message box buttons
        msg_box.setStyleSheet('QPushButton { color: black; }')
        
        # Show the message box
        msg_box.exec()

    def load_image(self):
        response = requests.get(self.url+f"get-image/boxed/{self.image_dir}/{self.image_list[self.image_index]}")

        if response.status_code == 200:
            image = QtGui.QPixmap()
            image.loadFromData(response.content)

            self.ui.image_box.setPixmap(image)
  
            self.ui.image_view_status.setText(f"{self.image_index+1}/{len(self.image_list)}    {self.image_dir}/{self.image_list[self.image_index]}")
        else:
            self.ui.image_box.setText("Failed to retrieve image")

    def next_img(self):
        if self.image_index + 1 < len(self.image_list):
            self.image_index +=1
            self.load_image()
            self.ui.image_view_status.setText(f"{self.image_index+1}/{len(self.image_list)}    {self.image_dir}/{self.image_list[self.image_index]}")
        
    def prev_img(self):
        if self.image_index - 1 >= 0:
            self.image_index -= 1
            self.load_image()
            self.ui.image_view_status.setText(f"{self.image_index+1}/{len(self.image_list)}    {self.image_dir}/{self.image_list[self.image_index]}")

    def browse_img(self):
        # dialog = QDialog(self)
        # dialog.setWindowTitle("Choose an image folder")
        # dialog.resize(500,400)
        dialog = Dialogo(self)
        dialog.setWindowTitle("Choose an image folder")
        dialog.exec()
        
    def delete_img(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet('QLabel, QLineEdit, QTextEdit { color: black; }')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
