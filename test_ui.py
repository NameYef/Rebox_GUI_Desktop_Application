import sys
from PySide6.QtCore import QProcess, QIODevice
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtGui
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.run_script)
        self.ui.pushButtonStop.clicked.connect(self.stop_script)

        self.process = QProcess(self)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.read_output)
        self.process.finished.connect(self.script_finished)

    def run_script(self):
        self.ui.textEdit.clear()
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButtonStop.setEnabled(True)
        self.process.start("python", ["script.py"])

    def stop_script(self):
        if self.process.state() == QProcess.Running:
            self.process.kill()
            self.ui.textEdit.append("\nScript forcefully stopped.\n")
            self.script_finished()  # Handle UI changes when script is stopped

    def read_output(self):
        output = self.process.readAllStandardOutput().data().decode()
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.ui.textEdit.insertPlainText(output)

    def script_finished(self):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButtonStop.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
