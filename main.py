import sys

import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QMainWindow, QAction, QLabel, QButtonGroup, QTableWidgetItem
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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
