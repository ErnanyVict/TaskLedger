from PySide6.QtWidgets import  QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QFont
from CreateAccountPage import CreateAccountPage

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Model.Entities.User import User
from Controller.EnterAccount import EnterAccount

class LoginPage:
    
    def __init__(self, box, mainpage):
        self.box = box
        self.mainpage = mainpage
        self.user = None
          
        self.login_txtt()
        self.name_txtt()
        self.display_namee()
        self.password_txtt()
        self.display_passwordd()     
        self.enter_buttonn()
        self.create_account_buttonn()
        
        self.list_objs = [
            self.login_txt,
            self.name_txt,
            self.display_name,
            self.password_txt,
            self.display_password,  
            self.enter_button,
            self.create_account_button
        ]

        


    def login_txtt(self):
        self.login_txt = QLabel('Login', self.box)
        self.login_txt.setFont(QFont("Arial", 20, QFont.Bold))
        self.login_txt.setStyleSheet('color: white')
        self.login_txt.move(150, 120)
        return self.login_txt

    def name_txtt(self):
        self.name_txt = QLabel('Name', self.box)
        self.name_txt.setFont(QFont("Arial", 16, QFont.Bold))
        self.name_txt.setStyleSheet('color: white')
        self.name_txt.move(60, 170)
        return self.name_txt

    def display_namee(self):
        self.display_name = QLineEdit('Ernany Victor', self.box)
        self.display_name.resize(240, 40)
        self.display_name.setFont(QFont("Arial", 14, QFont.Bold))
        self.display_name.setStyleSheet('''QLineEdit{
                                background-color: white;
                                border: 1px solid #ccc;
                                border-radius: 10px;
                                }''') 
        self.display_name.move(60, 200)
        return self.display_name
    
    def password_txtt(self):
        self.password_txt = QLabel('Password', self.box)
        self.password_txt.setFont(QFont("Arial", 16, QFont.Bold))
        self.password_txt.setStyleSheet('color: white')
        self.password_txt.move(60, 250)
        return self.password_txt

    def display_passwordd(self):
        self.display_password = QLineEdit('4321', self.box)
        self.display_password.resize(240, 40)
        self.display_password.setFont(QFont("Arial", 14, QFont.Bold))
        self.display_password.setStyleSheet('''QLineEdit{
                                background-color: white;
                                border: 1px solid #ccc;
                                border-radius: 10px;
                                }''') 
        self.display_password.move(60, 280)
        return self.display_password

    def create_account_buttonn(self) ->CreateAccountPage:
        self.create_account_button = QPushButton('New account', self.box)
        self.create_account_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.create_account_button.setStyleSheet('color: white')
        self.create_account_button.move(180, 330)
        self.account_page = None
        def Create_Account_Page_lambda():
            self.close_page()
            self.account_page = CreateAccountPage(self.box, self)
            

        self.create_account_button.clicked.connect(Create_Account_Page_lambda)
        return self.account_page
    
    def enter_buttonn(self):
        self.enter_button = QPushButton('Enter', self.box)
        self.enter_button.setFont(QFont("Arial", 22, QFont.Bold))
        self.enter_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 5 30 5 30px')

        def enter():
            name_txt = self.display_name.text()
            password_txt = self.display_password.text() 
            enter = EnterAccount(name_txt, password_txt)
            self.user = enter.enter()
            if self.user != None:
                self.close_page()
                self.mainpage.show(self.user)
        self.enter_button.clicked.connect(enter)
        self.enter_button.move(120, 400)
        return self.enter_button
    


    def close_page(self):
        for obj in self.list_objs:
            obj.close()

    def show_page(self):
        for obj in self.list_objs:
            obj.show()