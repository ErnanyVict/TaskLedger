from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel)
from PySide6.QtGui import QFont

class Screen(QMainWindow):
    def __init__(self, app: QApplication, *args, **kwargs,):
        super().__init__(*args, **kwargs)
        self.app = app
        self.setFixedSize(470, 610)
        self.setStyleSheet('background-color: #464e63')
        self.create_box()
        self.create_title()

    def create_box(self):
        self.box = QLabel(self)
        self.box.setGeometry(30, 30, 420, 560)
        self.box.setStyleSheet('background-color: #667292; border-radius: 20px')
        return self.box
        
    def create_title(self):
        self.title = QLabel('TaskLedger', self.box)
        self.title.setFont(QFont("Arial", 20, QFont.Bold))
        self.title.setStyleSheet('color: white')
        self.title.move(120, 30)
        return self.title

    def run(self):
        self.show()
        self.app.exec()