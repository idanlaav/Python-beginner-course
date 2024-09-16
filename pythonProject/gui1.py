# lesson 4
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
class WelcomeScreen(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('ui/welcomescreen-personal.ui', self)
        self.login.clicked.connect(self.clickme)
    def clickme(self):
        print("click")

app = QApplication([])
welcome = WelcomeScreen()
widgets = QtWidgets.QStackedWidget()
widgets.addWidget(welcome)
widgets.setFixedHeight(800)
widgets.setFixedWidth(1200)
widgets.show()
app.exec()
