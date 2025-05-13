from PySide6.QtWidgets import  QLabel, QLineEdit, QPushButton
from PySide6.QtGui import QFont


class CreateAccountPage:
    def __init__(self, box, login_page):
        self.box = box
        self.login_page = login_page

        self.list_objs_ca_screen_function = [        
            self.create_account_txtt,
            self.name_txtt,
            self.display_namee,
            self.password_txtt,
            self.display_passwordd,
            self.email_txtt,        
            self.display_emaill,
            self.login_buttonn,
            self.create_buttonn
        ]

        for obj in self.list_objs_ca_screen_function:
            obj().show()

        self.list_objs_ca_screen_atributes = [        
            self.create_account_txt,
            self.name_txt,
            self.display_name,
            self.password_txt,
            self.display_password,
            self.email_txt,        
            self.display_email,
            self.login_button,
            self.create_button
        ]
        

    def create_account_txtt(self):
        self.create_account_txt = QLabel('Create Account', self.box)
        self.create_account_txt.setFont(QFont("Arial", 20, QFont.Bold))
        self.create_account_txt.setStyleSheet('color: white')
        self.create_account_txt.move(100, 120)
        return self.create_account_txt

    def name_txtt(self):
        self.name_txt = QLabel('Name', self.box)
        self.name_txt.setFont(QFont("Arial", 16, QFont.Bold))
        self.name_txt.setStyleSheet('color: white')
        self.name_txt.move(60, 170)
        return self.name_txt

    def display_namee(self):
        self.display_name = QLineEdit(self.box)
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
        self.display_password = QLineEdit(self.box)
        self.display_password.resize(240, 40)
        self.display_password.setFont(QFont("Arial", 14, QFont.Bold))
        self.display_password.setStyleSheet('''QLineEdit{
                                background-color: white;
                                border: 1px solid #ccc;
                                border-radius: 10px;
                                }''') 
        self.display_password.move(60, 280)
        return self.display_password
    
    def email_txtt(self):
        self.email_txt = QLabel('Email', self.box)
        self.email_txt.setFont(QFont("Arial", 16, QFont.Bold))
        self.email_txt.setStyleSheet('color: white')
        self.email_txt.move(60, 330)
        return self.email_txt

    def display_emaill(self):
        self.display_email = QLineEdit(self.box)
        self.display_email.resize(240, 40)
        self.display_email.setFont(QFont("Arial", 14, QFont.Bold))
        self.display_email.setStyleSheet('''QLineEdit{
                                background-color: white;
                                border: 1px solid #ccc;
                                border-radius: 10px;
                                }''') 
        self.display_email.move(60, 360)
        return self.display_email

    def login_buttonn(self):
        self.login_button = QPushButton('Login', self.box)
        self.login_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.login_button.setStyleSheet('color: white')
        def show_login_page():
            self.close()
            self.login_page.show_page()

        self.login_button.clicked.connect(show_login_page)
        self.login_button.move(230, 410)
        return self.login_button
    
    def create_buttonn(self):
        self.create_button = QPushButton('Create', self.box)
        self.create_button.setFont(QFont("Arial", 22, QFont.Bold))
        self.create_button.setStyleSheet('color: white; background-color: #8d9db6; border-radius: 10px; padding: 5 30 5 30px')
        self.create_button.move(120, 480)
        return self.create_button    
    
    def close(self):
        for obj in self.list_objs_ca_screen_atributes:
            obj.close()