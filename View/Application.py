import sys
import os
from PySide6.QtWidgets import QApplication
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from View.Screen import Screen
from View.LoginPage import LoginPage
from View.MainPage import MainPage

app = QApplication()
app.setStyle("Fusion")
window = Screen(app)

mainpage = MainPage(window.box) 
login_page = LoginPage(window.box, mainpage)
create_account_page = login_page.account_page
user = login_page.user


window.run()