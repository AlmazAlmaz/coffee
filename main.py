import sys

import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QSizePolicy, QMainWindow, QAction, QLabel, QButtonGroup, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.db")
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
        self.con = sqlite3.connect("coffee.db")
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


class BOOK(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.set)

    def set(self):
        global row
        self.con = sqlite3.connect("coffee.db")
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


class BOOK1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.pushButton.clicked.connect(self.set)

    def set(self):
        self.con = sqlite3.connect("coffee.db")
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
