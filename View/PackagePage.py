
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.Entities.Package import Package
from Controller.getTasks import get_tasks
from PySide6.QtWidgets import QLabel, QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
class PackagePage:
    def __init__(self, package_id, box):
        self.list_task = get_tasks(package_id)
        self.tasks = []
        self.create_tasks(box)
        for task in self.tasks:
            task.show()
    
    def create_tasks(self, box):
        y = 120
        for task in self.list_task:
            self.task_label = QLabel(box)
            self.task_label.move(70, y)
            self.task_label.setFixedSize(300, 60)
            self.task_label.setStyleSheet('background-color: #8d9db6; border-radius: 10px; border: 0px 10px 2px 0px')
            
            self.labelname = QLabel(task.name, self.task_label)
            self.labelname.move(10, 5)
            self.labelname.setFont(QFont("Arial", 16, QFont.Bold))

            self.labeldescription = QLabel(task.description, self.task_label)        
            self.labeldescription.setFont(QFont("Arial", 14))
            self.labeldescription.move(10, 40)
            
            self.checkbox = QCheckBox(box)
            self.checkbox.setStyleSheet('''
            QCheckBox::indicator{
            height: 30px;
            width: 30px;                            
            }                    
            ''')
            if task.status == 'Completed':
                self.checkbox.setChecked(True)
            self.checkbox.move(30, y)
            
            y += 30

            self.tasks.append(self.checkbox)
            self.tasks.append(self.task_label)