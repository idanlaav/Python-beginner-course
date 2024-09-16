# lesson 4
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
# import csv_db as db
import db
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi('../ui/welcomescreen.ui', self)
        self.create.clicked.connect(self.go_to_create)
        self.login.clicked.connect(self.go_to_login)

    def go_to_create(self):
        create = CreateScreen()
        widget.addWidget(create)
        widget.setCurrentWidget(create)

    def go_to_login(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentWidget(login)

class CreateScreen(QDialog):
    def __init__(self):
        super(CreateScreen, self).__init__()
        loadUi('../ui/createacc.ui', self)
        self.btnSingup.clicked.connect(self.create_user)

    def create_user(self):
        username = self.txtUserName.text()
        password = self.txtPassword.text()
        confirmpassword = self.txtConfirmPassword.text()
        if username == "":
            self.error.setText("You mast enter username")
        elif password == "":
            self.error.setText("You mast enter password")
        elif password != confirmpassword:
            self.error.setText("Password does not match")
        else:
            id = db.create_user(username,password)
            if id > 0:
                # self.error.setText("Successfully create user")
                self.go_to_fill_profile(id)
            else:
                self.error.setText("Error while create user")

    def go_to_fill_profile(self, id):
        fill = FillProfile(id)
        widget.addWidget(fill)
        widget.setCurrentWidget(fill)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('../ui/login.ui', self)
        self.btnLogin.clicked.connect(self.login)
    def login(self):
        username = self.txtUserName.text()
        password = self.txtPassword.text()
        if username == "":
            self.error.setText("You mast enter username")
        elif password == "":
            self.error.setText("You mast enter password")
        else:
            if db.login(username, password):
                # self.error.setText("Successfully login")
                self.go_to_fill_profile()
            else:
                self.error.setText("Username or password are incorrect")

    def go_to_fill_profile(self):
        fill = FillProfile()
        widget.addWidget(fill)
        widget.setCurrentWidget(fill)

class FillProfile(QDialog):
    def __init__(self, id):
        super(FillProfile, self).__init__()
        loadUi('../ui/fillprofile.ui', self)
        self.lblUsername.setText(str(id))



app = QApplication([])
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
app.exec()
