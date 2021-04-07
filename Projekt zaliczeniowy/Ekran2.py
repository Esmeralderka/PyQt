############################################################################
#
# Autorzy: Weronika Miksa i Lukasz Bińkowski
#
# Data: 29.11.2020
# Data ostatniej poprawki: 07.12.2020

# Opis ogólny: Prosty interface sklepu połączonego z bazą danych
# wykonany na zaliczenie programowania wieloplatformowego w Qt
#
# Opis szczegółowy: Klasa drugiego ekranu wraz z graficznym przedstawieniem
# zawierajaca liste produktow, koszyk oraz pole wyszukiwania obiektow
#
#############################################################################

import datetime
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 800)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 1251, 81))
        self.widget_2.setObjectName("widget_2")
        self.szukaj_button = QtWidgets.QPushButton(self.widget_2)
        self.szukaj_button.setGeometry(QtCore.QRect(1190, 10, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.szukaj_button.sizePolicy().hasHeightForWidth())
        self.szukaj_button.setSizePolicy(sizePolicy)
        self.szukaj_button.setMinimumSize(QtCore.QSize(20, 20))
        self.szukaj_button.setMaximumSize(QtCore.QSize(50, 50))
        self.szukaj_button.setSizeIncrement(QtCore.QSize(20, 20))
        self.szukaj_button.setBaseSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.szukaj_button.setFont(font)
        self.szukaj_button.setObjectName("szukaj_button")
        self.Witamy_txt_2 = QtWidgets.QLabel(self.widget_2)
        self.Witamy_txt_2.setGeometry(QtCore.QRect(0, 10, 250, 61))
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Witamy_txt_2.setFont(font)
        self.Witamy_txt_2.setObjectName("Witamy_txt_2")
        self.wyszukaj_textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.wyszukaj_textEdit.setEnabled(True)
        self.wyszukaj_textEdit.setGeometry(QtCore.QRect(260, 10, 911, 50))
        self.wyszukaj_textEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.wyszukaj_textEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.wyszukaj_textEdit.setSizeIncrement(QtCore.QSize(20, 20))
        self.wyszukaj_textEdit.setBaseSize(QtCore.QSize(50, 50))

        self.wyszukaj_textEdit.setLineWidth(0)
        self.wyszukaj_textEdit.setMidLineWidth(0)
        self.wyszukaj_textEdit.setObjectName("wyszukaj_textEdit")

        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(10, 90, 761, 701))
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 51))
        self.label.setObjectName("label")
        self.koszyk_button = QtWidgets.QPushButton(self.widget_3)
        self.koszyk_button.setGeometry(QtCore.QRect(510, 650, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.koszyk_button.setFont(font)
        self.koszyk_button.setObjectName("koszyk_button")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(0, 650, 121, 51))
        self.label_4.setObjectName("label_4")
        self.produkt_label = QtWidgets.QLabel(self.widget_3)
        self.produkt_label.setGeometry(QtCore.QRect(110, 650, 391, 51))
        self.produkt_label.setObjectName("produkt_label")
        self.produkty_list = QtWidgets.QListWidget(self.widget_3)
        self.produkty_list.setGeometry(QtCore.QRect(0, 50, 701, 591))
        self.produkty_list.setObjectName("produkty_list")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(730, 95, 551, 41))
        self.label_2.setObjectName("label_2")
        self.koszyk_tableWidget = QtWidgets.QTableWidget(Form)
        self.koszyk_tableWidget.setGeometry(QtCore.QRect(730, 140, 561, 591))
        self.koszyk_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.koszyk_tableWidget.setObjectName("koszyk_tableWidget")
        self.koszyk_tableWidget.setColumnCount(3)
        self.koszyk_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.koszyk_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.koszyk_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.koszyk_tableWidget.setHorizontalHeaderItem(2, item)
        self.koszyk_tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.koszyk_tableWidget.horizontalHeader().setHighlightSections(False)
        self.koszyk_tableWidget.horizontalHeader().setMinimumSectionSize(90)
        self.koszyk_tableWidget.verticalHeader().setDefaultSectionSize(65)
        self.koszyk_tableWidget.verticalHeader().setMinimumSectionSize(50)
        self.koszyk_tableWidget.setGridStyle(False)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(734, 740, 101, 51))
        self.label_3.setObjectName("label_3")
        self.suma_label = QtWidgets.QLabel(Form)
        self.suma_label.setGeometry(QtCore.QRect(844, 740, 231, 51))
        self.suma_label.setObjectName("suma_label")
        self.kup_button = QtWidgets.QPushButton(Form)
        self.kup_button.setGeometry(QtCore.QRect(1100, 740, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.kup_button.setFont(font)
        self.kup_button.setObjectName("kup_button")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.check=0
        self.tabgl=[]
        self.atab=[]
        self.robienie_Sklepu("")
        self.szukaj_button.clicked.connect(self.Wyszukiwanie)
        self.koszak()
        self.AA = 0
        self.kup_button.clicked.connect(self.clearev)
        self.produkty_list.itemClicked.connect(self.textshow)
        self.koszyk_button.clicked.connect(self.ladowaniekosza)
        self.aw=""

        self.textshop=""
        self.destiny_Itself=0


    def Wyszukiwanie(self):
        st = self.wyszukaj_textEdit.toPlainText()
        self.robienie_Sklepu(st)

    def robienie_Sklepu(self,text):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sklep"
        )

        mycursor = mydb.cursor()

        if self.check == 1:
            sql=f"SELECT * FROM produkty WHERE nazwa LIKE '%{str(text)}%' "
            mycursor.execute(str(sql))

        else:
            mycursor.execute(f"select * from produkty")

        self.produkty_list.clear()
        self.tabgl.clear()
        aa=0

        for x in mycursor:
            tab2 = []
            tab2.insert(0,x[0])
            tab2.insert(1,str(x[1]))
            tab2.insert(2,str(x[2]))
            self.tabgl.insert(aa,tab2)

            imageLabel = QtWidgets.QLabel()
            imageLabel.setScaledContents(True)

            qimg = QtGui.QImage.fromData(x[0])
            pixmap = QtGui.QPixmap.fromImage(qimg)
            item=QtWidgets.QListWidgetItem()
            lab=QtCore.QSize()
            lab.setHeight(200)
            lab.setWidth(160)

            icon=QtGui.QIcon()
            icon.addPixmap(pixmap)

            item.setIcon(icon)
            item.setText(f" -{x[1]} - {x[2]},00 zl")
            QQQ = QtGui.QFont("Times New Roman")
            QQQ.setPointSize(20)
            item.setFont(QQQ)
            self.produkty_list.setIconSize(lab)
            self.produkty_list.addItem(item)
            aa += 1

        self.check=1
        mycursor.close()
        mydb.close()

    def textshow(self):
        x = self.produkty_list.currentRow()
        self.produkt_label.setText(f" {self.tabgl[int(x)][1]} {self.tabgl[int(x)][2]},00 zl")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.produkt_label.setFont(font)


    def ladowaniekosza(self):
        x = self.produkty_list.currentRow()
        self.atab.insert(self.AA,self.tabgl[int(x)])
        self.AA+=1
        self.koszak()


    def koszak(self):
        self.koszyk_tableWidget.clear()
        aa=0
        self.destiny_Itself=0
        self.koszyk_tableWidget.setRowCount(len(self.atab))
        self.textshop=""
        for x in self.atab:
            imageLabel = QtWidgets.QLabel()
            imageLabel.setScaledContents(True)

            qimg = QtGui.QImage.fromData(x[0])
            pixmap = QtGui.QPixmap.fromImage(qimg)

            imageLabel.setPixmap(pixmap)
            self.koszyk_tableWidget.verticalHeader().setDefaultSectionSize(88)
            self.koszyk_tableWidget.setCellWidget(aa, 0, imageLabel)
            self.koszyk_tableWidget.setItem(aa, 1, QtWidgets.QTableWidgetItem(f"{x[1]}"))
            self.koszyk_tableWidget.setItem(aa, 2, QtWidgets.QTableWidgetItem(f"{x[2]},00 zl"))
            self.textshop=self.textshop+f"{x[1]} - {x[2]},00 \n"
            self.destiny_Itself+=int(x[2])
            aa+=1

        if self.destiny_Itself!=0:
            self.suma_label.setText(f"{self.destiny_Itself},00 zł")
            font = QtGui.QFont()
            font.setPointSize(15)
            self.suma_label.setFont(font)

    def getLogin(self):
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sklep"
        )
        mycursor = mydb2.cursor()
        mycursor.execute("select * from login")
        for x in mycursor:
            self.aw=x
        mycursor.execute("delete from login")
        mydb2.commit()
        mydb2.close()



    def clearev(self):
        self.getLogin()
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sklep"
        )
        if self.destiny_Itself !=0:
            now = datetime.datetime.now()

            now2=now.strftime("%Y-%m-%d %H:%M")
            mycursor=mydb2.cursor()
            sql = "INSERT INTO zamowienia VALUES (%s, %s,%s,%s)"
            val = (now2,self.textshop,str(self.aw),f"{str(self.destiny_Itself)},00")
            mycursor.execute(sql, val)
            mydb2.commit()

        self.koszyk_tableWidget.clear()
        self.koszyk_tableWidget.setRowCount(0)
        self.atab.clear()
        self.suma_label.clear()
        self.textshop=""
        self.destiny_Itself=0

        mydb2.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.szukaj_button.setText(_translate("Form", "🔎"))
        self.Witamy_txt_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" color:#148098;\">WszystkoPOL</span></p></body></html>"))
        self.wyszukaj_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body  style=\" font-family:\'MS Shell Dlg 2\'; font-size:15pt; font-weight:600; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt;\"></span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; font-weight:600; color:#000000;\">Produkty</span></p></body></html>"))
        self.koszyk_button.setText(_translate("Form", "DODAJ DO KOSZYKA"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Wybrano:</span></p></body></html>"))
        self.produkt_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\"/></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#000000;\">Koszyk</span></p></body></html>"))
        item = self.koszyk_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Zdjecie"))
        item = self.koszyk_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nazwa"))
        item = self.koszyk_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Cena"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Suma:</span></p></body></html>"))
        self.suma_label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:30pt;\"/></p></body></html>"))
        self.kup_button.setText(_translate("Form", "KUP TERAZ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())