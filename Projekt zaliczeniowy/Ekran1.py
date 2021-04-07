#####################################################################
#
# Autorzy: Weronika Miksa i Lukasz Bińkowski
#
# Data: 29.11.2020
# Data ostatniej poprawki: 07.12.2020

# Opis ogólny: Prosty interface sklepu połączonego z bazą danych
# wykonany na zaliczenie programowania wieloplatformowego w Qt
#
# Opis szczegółowy: Klasa ekranu startowego wraz z jego graficznym
# przedstawieniem zawierajaca logowanie oraz przycisk realizujacy
# przejscie do ekranu rejestracji
#
######################################################################

import mysql.connector
import Ekran2
import Rejestracja
from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib


class Ui_MainWindow(object):
    def Sprawdz(self):
        mydb2 = mysql.connector.connect \
                (
                host="localhost",
                user="root",
                password="",
                database="sklep"
            )

        self.mycursor = mydb2.cursor()
        self.mycursor.execute("SELECT * FROM `uzytkownicy` ")

        for x in self.mycursor:
            haslo2 = self.haslo_edit.text()
            hash_object = hashlib.md5(haslo2.encode())
            nazwa2 = self.login_edit.toPlainText()
            if ((nazwa2 == x[0]) and (hash_object.hexdigest() == x[1])):
                self.label_3.setText("")
                self.openWindowA()
            else:
                self.label_3.setText("                        Wprowadzone dane są nie poprawne!")

        self.mycursor.execute("DELETE FROM login")
        mydb2.commit()
        sql = "INSERT INTO login VALUES (%s)"
        val = str(self.login_edit.toPlainText())
        self.mycursor.execute(f"INSERT INTO login VALUES ('{val}')")
        mydb2.commit()
        mydb2.close()


    def openWindowA(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ekran2.Ui_Form()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def openWindowB(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Rejestracja.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Witamy_txt = QtWidgets.QLabel(self.centralwidget)
        self.Witamy_txt.setGeometry(QtCore.QRect(250, 80, 821, 161))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Witamy_txt.setFont(font)
        self.Witamy_txt.setObjectName("Witamy_txt")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(250, 330, 681, 111))
        font = QtGui.QFont()
        font.setKerning(False)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.haslo_edit = QtWidgets.QLineEdit(self.widget)
        self.haslo_edit.setGeometry(QtCore.QRect(280, 50, 300, 30))
        self.haslo_edit.setObjectName("haslo_edit")
        self.haslo_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_edit = QtWidgets.QTextEdit(self.widget)
        self.login_edit.setGeometry(QtCore.QRect(280, 10, 300, 30))
        self.login_edit.setObjectName("login_edit")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(120, 50, 200, 30))
        self.label_2.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(120, 10, 200, 31))
        self.label.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.Zaloguj_button = QtWidgets.QPushButton(self.centralwidget)
        self.Zaloguj_button.setGeometry(QtCore.QRect(510, 500, 270, 70))
        self.Zaloguj_button.setMinimumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Zaloguj_button.setFont(font)
        self.Zaloguj_button.setObjectName("Zaloguj_button")

        self.Zaloguj_button.clicked.connect(self.Sprawdz)

        self.Zaloguj_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Zaloguj_button_2.setGeometry(QtCore.QRect(510, 580, 270, 70))
        self.Zaloguj_button_2.setMinimumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Zaloguj_button_2.setFont(font)
        self.Zaloguj_button_2.setObjectName("Zaloguj_button_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 430, 391, 41))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Zaloguj_button_2.clicked.connect(self.openWindowB)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Witamy_txt.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; color:#148098;\">WszystkoPOL</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">hasło</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">login</p></body></html>"))
        self.Zaloguj_button.setText(_translate("MainWindow", "Zaloguj "))
        self.Zaloguj_button_2.setText(_translate("MainWindow", "Zarejestruj"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
