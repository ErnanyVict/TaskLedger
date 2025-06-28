import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from View.PackagePage import PackagePage
from Controller.makePackage import MakePackage
from PySide6.QtWidgets import QScrollArea, QLabel, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class MainPage:
    def __init__(self, box):
        self.box = box
        self.list_objs: list[QWidget] = []
        self.user = None
        

    def create_label(self, package):
        self.package_button = QPushButton()
        self.package_button.setFixedSize(300, 120)
        self.labelname = QLabel(package.name, self.package_button)
        self.labelname.setFont(QFont("Arial", 18, QFont.Bold))
        self.labelname.move(45, 10)
        self.labeldescription = QLabel(package.description, self.package_button)        
        self.labeldescription.setFont(QFont("Arial", 10))
        self.labeldescription.move(10, 40)
        self.package_button.setStyleSheet('background-color: #8d9db6; border-radius: 10px; border: 0px 10px 2px 0px')
        def showPackage():
            for obj in self.list_objs:
                obj.close()
            self.package_page = PackagePage(package.package_id, self.box, self)
        self.package_button.clicked.connect(showPackage)
        self.list_objs.append(self.package_button)
        
        return self.package_button
    
    def create_scroll(self):
        container = QWidget()
        container.setStyleSheet("padding-right: 1px;")
        layout = QVBoxLayout(container)
        self.scroll = QScrollArea(self.box)
        self.scroll.setStyleSheet('''
                                  
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical{
            height: 0;
        }
        QScrollBar::handle:vertical{
            border-radius: 10px;
            min-height: 20px;
            background-color: white;
        }
    
        QScrollBar:vertical {
            background: transparent;
            width: 8px;
        }

        QScrollBar::groove:vertical {
            background: transparent;
            border: none;
        }

        QScrollBar::handle:vertical {
            background-color: white;
            border-radius: 10px;
            min-height: 20px;
        }
        ''')
        
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedSize(350, 300)
        self.scroll.move(30, 230)
        self.scroll.setViewportMargins(0, 0, 12, 0)
        print(self.user)
        self.packages_list = MakePackage(self.user.user_id).get_packages()
        for package in self.packages_list:
            print(package)
            layout.addWidget(self.create_label(package))
        

        self.scroll.setWidget(container)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_objs.append(self.scroll)
        return self.scroll
    
    def show(self, user):
        self.user = user
        self.create_scroll()
        for obj in self.list_objs:
            obj.show()