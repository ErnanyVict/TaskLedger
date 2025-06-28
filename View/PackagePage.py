
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.Entities.Package import Package
from Controller.getTasks import get_tasks
from PySide6.QtWidgets import QLabel, QCheckBox, QPushButton, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class PackagePage:
    def __init__(self, package_id, box, main_page):
        self.box = box
        self.list_task = get_tasks(package_id)
        self.main_page = main_page
        self.tasks = []

        self.create_tasks()
        self.add_task()
        self.last_page()
        for widget in self.tasks:
            widget.show()
            
    def last_page(self):
        self.last_page_button = QPushButton("<=", self.box)
        self.last_page_button.setFixedSize(40, 20)
        self.last_page_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.last_page_button.move(50, 110)
        self.last_page_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 0px')
        print('oi')
        def return_page():
            self.close()
            for widget in self.main_page.list_objs:
                widget.show()

        self.last_page_button.clicked.connect(return_page)
        self.tasks.append(self.last_page_button)


    def add_task(self):
        self.add_task_button = QPushButton("New", self.box)
        self.add_task_button.setFixedSize(70, 40)
        self.add_task_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.add_task_button.move(300, 140)
        self.add_task_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 0px')
        self.tasks.append(self.add_task_button)

    def create_tasks(self):
        y = 200
        for task in self.list_task:
            task_label = QLabel(self.box)
            task_label.move(70, y)
            task_label.setFixedSize(300, 60)
            task_label.setStyleSheet('background-color: #8d9db6; border-radius: 10px; border: 0px 10px 2px 0px')
            
            labelname = QLabel(task.name, task_label)
            labelname.move(10, 5)
            labelname.setFont(QFont("Arial", 16, QFont.Bold))

            labeldescription = QLabel(task.description, task_label)        
            labeldescription.setFont(QFont("Arial", 14))
            labeldescription.move(10, 40)
            
            checkbox = QCheckBox(self.box)
            checkbox.setStyleSheet('''
            QCheckBox::indicator{
            height: 30px;
            width: 30px;                            
            }                    
            ''')
            if task.status == 'Completed':
                checkbox.setChecked(True)
            checkbox.move(30, y)
            
            remove_task_button = QPushButton("X", self.box)
            remove_task_button.setFixedSize(20, 20)
            remove_task_button.setFont(QFont("Arial", 10, QFont.Bold))
            remove_task_button.move(30, y+35)
            remove_task_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 0px')
            
            def remove(t_label, cb, btn):
                t_label.setParent(None)
                cb.setParent(None)
                btn.setParent(None)
                t_label.deleteLater()
                cb.deleteLater()
                btn.deleteLater()
                self.tasks.remove(t_label)
                self.tasks.remove(cb)
                self.tasks.remove(btn)
                for widget in self.tasks:
                    widget.show()
                

            remove_task_button.clicked.connect(
            lambda _, t_label=task_label, cb=checkbox, btn=remove_task_button: remove(t_label, cb, btn)
            )
            self.tasks.append(remove_task_button)        

            y += 70

            self.tasks.append(task_label)
            self.tasks.append(checkbox)

    def close(self):
        for task in self.tasks:
            task.close()