import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QMediaContent
from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QImage, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Video Viewer")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # QGraphicsView and QGraphicsScene for video display
        self.graphics_view = QGraphicsView