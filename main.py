import sys

import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy, QMainWindow, QAction, QLabel, QButtonGroup, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, uic

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 731, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 351, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 0, 361, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Изменить запись"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить новую"))


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 171, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 161, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 10, 141, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 201, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 210, 231, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 40, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 40, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 40, 161, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(490, 40, 141, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 240, 211, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(250, 240, 231, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 270, 391, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Сорт"))
        self.label_2.setText(_translate("MainWindow", "Степень прожарки"))
        self.label_3.setText(_translate("MainWindow", "Гранулы / Зерна"))
        self.label_4.setText(_translate("MainWindow", "Вкус"))
        self.label_5.setText(_translate("MainWindow", "Цена Р"))
        self.label_6.setText(_translate("MainWindow", "Вес Г"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.db")
        cur = self.con.cursor()
        result = cur.execute("SELECT * from coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(["ИД", "Сорт",
                                                    "Степень прожарки", "Гранулы/Зерна", "Вкус", "Цена Р", "Вес Г"])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.pushButton.clicked.connect(self.book1)
        self.pushButton_2.clicked.connect(self.book2)

    def book1(self):
        global row
        row = int(list(set([i.row() for i in self.tableWidget.selectedItems()]))[0]) + 1
        self.book = BOOK()
        self.book.show()

    def book2(self):
        self.book3 = BOOK1()
        self.book3.show()

    def restart(self):
        self.con = sqlite3.connect("data/coffee.db")
        cur = self.con.cursor()
        result = cur.execute("SELECT * from coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(["ИД", "Сорт",
                                                    "Степень прожарки", "Гранулы/Зерна", "Вкус", "Цена Р", "Вес Г"])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.pushButton.clicked.connect(self.book1)


class BOOK(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.set)

    def set(self):
        global row
        self.con = sqlite3.connect("data/coffee.db")
        cur = self.con.cursor()
        cur.execute("UPDATE coffee SET name = ? WHERE id = ?", (self.lineEdit.text(), row,))
        cur.execute("UPDATE coffee SET `doneness degree` = ? WHERE id = ?", (self.lineEdit_2.text(), row,))
        cur.execute("UPDATE coffee SET `ground / grains` = ? WHERE id = ?", (self.lineEdit_3.text(), row,))
        cur.execute("UPDATE coffee SET taste = ? WHERE id = ?", (self.lineEdit_4.text(), row,))
        cur.execute("UPDATE coffee SET price = ? WHERE id = ?", (self.lineEdit_5.text(), row,))
        cur.execute("UPDATE coffee SET size = ? WHERE id = ?", (self.lineEdit_6.text(), row,))
        self.con.commit()
        self.con.close()
        self.close()
        wnd.restart()


class BOOK1(QMainWindow, Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.set)

    def set(self):
        self.con = sqlite3.connect("data/coffee.db")
        cur = self.con.cursor()
        cur.execute("INSERT INTO coffee(name,"
                    " `doneness degree`, `ground / grains`, taste, price, size) VALUES(?, ?, ?, ?, ?, ?)",
                    (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()
                     , self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text()))
        self.con.commit()
        self.con.close()
        self.close()
        wnd.restart()


row = 0


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
