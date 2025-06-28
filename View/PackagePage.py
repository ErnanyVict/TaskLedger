
import sys
import os
from Model.Entities.Task import Task
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Controller.getTasks import get_tasks
from Controller import AddNewTask
from PySide6.QtWidgets import QLabel, QCheckBox, QPushButton, QMainWindow, QLineEdit
from PySide6.QtGui import QFont

class PackagePage:
    def __init__(self, package_id, box, main_page):
        self.box = box
        self.package_id = package_id
        self.list_task = get_tasks(package_id)
        self.main_page = main_page
        self.tasks = []
        self.y = 200

        self.create_tasks(self.list_task)
        self.add_task()
        self.last_page()
        for widget in self.tasks:
            widget.show()

        self.task_window = None
            
    def last_page(self):
        self.last_page_button = QPushButton("<=", self.box)
        self.last_page_button.setFixedSize(40, 20)
        self.last_page_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.last_page_button.move(50, 110)
        self.last_page_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 0px')
        
        def return_page():
            self.close()
            for widget in self.main_page.list_objs:
                widget.show()

        self.last_page_button.clicked.connect(return_page)
        self.tasks.append(self.last_page_button)


    def new_task_page(self):
        self.task_window = QMainWindow()
        self.task_window.setWindowTitle("Nova Tarefa")
        self.task_window.setStyleSheet('background-color: #667292')
        self.task_window.resize(350, 500)

        title = QLabel("New Task", self.task_window)
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setStyleSheet('color: white')
        title.setFixedWidth(200)
        title.move(120, 30)

        name_label = QLabel("Name", self.task_window)
        name_label.setFont(QFont("Arial", 14, QFont.Bold))
        name_label.setStyleSheet('color: white')
        name_label.move(60, 130)

        name_display = QLineEdit("", self.task_window) 
        name_display.setFont(QFont("Arial", 14, QFont.Bold))
        name_display.setStyleSheet('''QLineEdit{
                                background-color: white;
                                border: 1px solid #ccc;
                                border-radius: 10px;
                                }''')
        name_display.setFixedSize(200, 30)
        name_display.move(60, 160)



        description_label = QLabel("Description", self.task_window)
        description_label.setFont(QFont("Arial", 14, QFont.Bold))
        description_label.setStyleSheet('color: white')
        description_label.setFixedSize(200, 30)
        description_label.move(60, 230)

        description_display = QLineEdit("", self.task_window) 
        description_display.setFont(QFont("Arial", 14, QFont.Bold))
        description_display.setStyleSheet('''QLineEdit{
                                background-color: white;
                                border: 1px solid #ccc;
                                border-radius: 10px;
                                }''')
        description_display.setFixedSize(200, 30)
        description_display.move(60, 260)

        done_button = QPushButton("Add", self.task_window)
        done_button.setFixedSize(100, 50)
        done_button.setFont(QFont("Arial", 14, QFont.Bold))
        done_button.move(100, 320)
        done_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 0px')
        self.task_window.show()
        tsk_window = self.task_window
        pack_id = self.package_id
       
        def add_task_DB():
            
            AddNewTask.add_task_DB(name_display.text(), description_display.text(), pack_id)
            tsk_window.close()
            self.create_tasks([Task(None, name_display.text(), description_display.text(), "Incomplete", None)])
            for task in self.tasks:
                task.show()


        done_button.clicked.connect(add_task_DB)

    def add_task(self):
        self.add_task_button = QPushButton("New", self.box)
        self.add_task_button.setFixedSize(70, 40)
        self.add_task_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.add_task_button.move(300, 140)
        self.add_task_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 0px')
        self.tasks.append(self.add_task_button)
        self.add_task_button.clicked.connect(self.new_task_page)
        

    def create_tasks(self, tasks):

        for task in tasks:
            task_label = QLabel(self.box)
            task_label.move(70, self.y)
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
            checkbox.move(30, self.y)

            remove_task_button = QPushButton("X", self.box)
            remove_task_button.setFixedSize(20, 20)
            remove_task_button.setFont(QFont("Arial", 10, QFont.Bold))
            remove_task_button.move(30, self.y+35)
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

            self.y += 70

            self.tasks.append(task_label)
            self.tasks.append(checkbox)

    def close(self):
        for task in self.tasks:
            task.close()