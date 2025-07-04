import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Controller.DeletePackage import delete_package
from View.PackagePage import PackagePage
from Controller.makePackage import MakePackage
from PySide6.QtWidgets import (QScrollArea, QLabel, QWidget, QVBoxLayout,
QPushButton, QMainWindow, QLineEdit)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from Controller import AddNewPackage

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
        self.id_package = package.package_id    
        def showPackage():
            for obj in self.list_objs:
                obj.close()
            self.package_page = PackagePage(package.package_id, self.box, self)
        self.package_button.clicked.connect(showPackage)

        self.delete_button = QPushButton("X", self.package_button)
        self.delete_button.setFixedSize(20, 20)
        self.delete_button.setFont(QFont("Arial", 7, QFont.Bold))
        self.delete_button.move(5, 90)
        self.delete_button.setStyleSheet('color: white; background-color: #464e63; border-radius: 5px; padding: 0px')
        self.list_objs.append(self.package_button)
        
        def remove_package(package_button, id_package):
            package_button.setParent(None)
            self.list_objs.remove(package_button)
            self.close()
            for widget in self.list_objs:
                    widget.show()
            delete_package(id_package)

        self.delete_button.clicked.connect(lambda _, package_button=self.package_button,
        id_package=self.id_package: remove_package(package_button, id_package))

        return self.package_button
    
    def create_scroll(self):
        container = QWidget()
        container.setStyleSheet("padding-right: 1px;")
        self.layout = QVBoxLayout(container)
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

        self.packages_list = MakePackage(self.user.user_id).get_packages()
        for package in self.packages_list:
            print(package)
            self.layout.addWidget(self.create_label(package))
        

        self.scroll.setWidget(container)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_objs.append(self.scroll)
        return self.scroll
    
    def new_package_page(self):
        self.package_window = QMainWindow()
        self.package_window.setWindowTitle("New Package")
        self.package_window.setStyleSheet('background-color: #667292')
        self.package_window.resize(350, 500)

        title = QLabel("New Package", self.package_window)
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet('color: white')
        title.setFixedWidth(200)
        title.move(120, 30)

        name_label = QLabel("Name", self.package_window)
        name_label.setFont(QFont("Arial", 14, QFont.Bold))
        name_label.setStyleSheet('color: white')
        name_label.move(60, 130)

        name_display = QLineEdit("", self.package_window) 
        name_display.setFont(QFont("Arial", 14, QFont.Bold))
        name_display.setStyleSheet('''QLineEdit{
                                background-color: white;
                                border: 1px solid #ccc;
                                border-radius: 10px;
                                }''')
        name_display.setFixedSize(200, 30)
        name_display.move(60, 160)



        description_label = QLabel("Description", self.package_window)
        description_label.setFont(QFont("Arial", 14, QFont.Bold))
        description_label.setStyleSheet('color: white')
        description_label.setFixedSize(200, 30)
        description_label.move(60, 230)

        description_display = QLineEdit("", self.package_window) 
        description_display.setFont(QFont("Arial", 14, QFont.Bold))
        description_display.setStyleSheet('''QLineEdit{
                                background-color: white;
                                border: 1px solid #ccc;
                                border-radius: 10px;
                                }''')
        description_display.setFixedSize(200, 30)
        description_display.move(60, 260)

        done_button = QPushButton("Add", self.package_window)
        done_button.setFixedSize(100, 50)
        done_button.setFont(QFont("Arial", 14, QFont.Bold))
        done_button.move(100, 320)
        done_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 0px')
        self.package_window.show()
        pck_window = self.package_window
        user_id = self.user.user_id
       
        def add_task_DB():
            
            AddNewPackage.add_package_DB(name_display.text(), description_display.text(), user_id)
            pck_window.close()
            self.layout.addWidget(self.create_label(MakePackage(self.user.user_id).get_packages()[-1]))
            self.list_objs[-1].show()

        done_button.clicked.connect(add_task_DB)

    def add_package(self):
        self.add_package_button = QPushButton("New", self.box)
        self.add_package_button.setFixedSize(70, 40)
        self.add_package_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.add_package_button.move(40, 100)
        self.add_package_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 0px')
        self.list_objs.append(self.add_package_button)

        self.add_package_button.clicked.connect(self.new_package_page)    

    def show(self, user):
        self.user = user
        self.create_scroll()
        self.add_package()
        for obj in self.list_objs:
            obj.show()

    def close(self):
        for widget in self.list_objs:
            widget.close()