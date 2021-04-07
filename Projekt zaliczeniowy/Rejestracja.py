#####################################################################
#
# Autorzy: Weronika Miksa i Lukasz Bińkowski
#
# Data: 29.11.2020
# Data ostatniej poprawki: 07.12.2020
#
# Opis ogólny: Prosty interface sklepu połączonego z bazą danych
# wykonany na zaliczenie programowania wieloplatformowego w Qt
#
# Opis szczegółowy: Klasa realizujaca rejestracje wraz z
# raficznym przedstawieniem, dane uzytkownika trafiaja do bazy danych
#
######################################################################


import mysql.connector
import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QVBoxLayout


class Ui_Form(object):
    def Rejestracja(self):
        mydb2 = mysql.connector.connect\
        (
            host="localhost",
            user="root",
            password="",
            database="sklep"
        )

        self.mycursor = mydb2.cursor()

        haslo2 = self.haslo_edit.text()
        powtorzhaslo2 = self.powtorzhaslo_edit.text()
        nazwa2 = self.login_edit.toPlainText()

        if  haslo2!="" and nazwa2!="":
            if haslo2 == powtorzhaslo2:
                if self.checkBox.isChecked():
                    hash_object = hashlib.md5(haslo2.encode())
                    sql = "INSERT INTO uzytkownicy VALUES (%s, %s)"
                    val = (nazwa2,hash_object.hexdigest())
                    self.mycursor.execute(sql, val)
                    mydb2.commit()

                    self.widget.close()
                    self.ostrzezenie_label.setText("")
                    self.widget22.setGeometry(QtCore.QRect(150, 280, 681, 141))

                    layout = QVBoxLayout()

                    self.labelek = QtWidgets.QLabel(self.widget22)
                    self.labelek.setEnabled(True)
                    self.labelek.setGeometry(QtCore.QRect(10, 80, 361, 91))
                    self.labelek.setMinimumSize(QtCore.QSize(200, 30))

                    self.checkBox.hide()
                    self.Zaloguj_button.hide()
                    self.labelek.setStyleSheet(" font-size: 20px; qproperty-alignment: AlignJustify; font-family: Unispace;")
                    self.labelek.setText("     Rejestracja przebiegla pomyslnie!\nMozna zamknac okno i przejsc do logowania\n  ")

                    layout.addWidget(self.labelek)
                    self.widget22.setLayout(layout)

                else:
                    self.ostrzezenie_label.setText("Prosze zaakceptowac regulamin!")
            else:
                self.ostrzezenie_label.setText("Podane hasla sa rozne!")
        else:
            self.ostrzezenie_label.setText("Pola nie moga byc puste!")
        mydb2.close()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.widget22 = QtWidgets.QWidget(Form)
        self.widget22.setGeometry(QtCore.QRect(-20, 180, 681, 141))
        self.Witamy_txt = QtWidgets.QLabel(Form)
        self.Witamy_txt.setGeometry(QtCore.QRect(220, 50, 361, 91))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Witamy_txt.setFont(font)
        self.Witamy_txt.setObjectName("Witamy_txt")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-20, 180, 681, 141))
        self.widget.setObjectName("widget")
        self.haslo_edit = QtWidgets.QLineEdit(self.widget)
        self.haslo_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.haslo_edit.setGeometry(QtCore.QRect(280, 50, 300, 30))
        self.haslo_edit.setObjectName("haslo_edit")
        self.login_edit = QtWidgets.QTextEdit(self.widget)
        self.login_edit.setGeometry(QtCore.QRect(280, 10, 300, 30))
        self.login_edit.setObjectName("login_edit")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(120, 50, 200, 30))
        self.label_4.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(120, 10, 200, 31))
        self.label_5.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 200, 30))
        self.label_3.setMinimumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.powtorzhaslo_edit =QtWidgets.QLineEdit(self.widget)
        self.powtorzhaslo_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.powtorzhaslo_edit.setGeometry(QtCore.QRect(280, 90, 300, 30))
        self.powtorzhaslo_edit.setObjectName("powtorzhaslo_edit")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(180, 360, 461, 20))
        self.checkBox.setObjectName("checkBox")
        self.Zaloguj_button = QtWidgets.QPushButton(Form)
        self.Zaloguj_button.setGeometry(QtCore.QRect(270, 410, 269, 70))
        self.Zaloguj_button.setMinimumSize(QtCore.QSize(200, 70))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Zaloguj_button.setFont(font)
        self.Zaloguj_button.setObjectName("Zaloguj_button")
        self.ostrzezenie_label = QtWidgets.QLabel(Form)
        self.ostrzezenie_label.setGeometry(QtCore.QRect(260, 309, 301, 31))
        self.ostrzezenie_label.setText("")
        self.ostrzezenie_label.setObjectName("ostrzezenie_label")

        self.Zaloguj_button.clicked.connect(self.Rejestracja)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Witamy_txt.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#148098;\">WszystkoPOL</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">hasło</p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p align=\"center\">login</p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">powtórz hasło</p></body></html>"))
        self.checkBox.setText(_translate("Form", "oświdczam, że zapoznałem się z regulaminem i akceptuje jego warunki"))
        self.Zaloguj_button.setText(_translate("Form", "Zarejestruj się"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
