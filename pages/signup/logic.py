from PyQt5.QtCore import QSettings, QTimer
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt5 import QtGui, QtCore

import database

import pages.login.ui as login


def bind(self):
    self.pushButton_quit1.clicked.connect(lambda: on_pushButton_enter_clicked(self))


def on_pushButton_enter_clicked(self):
    f = open("1.txt", 'a')

    # 账号判断
    account1 = self.lineEdit_account.text()
    password1 = self.lineEdit_password.text()

    f.write(f'{account1} {password1}\n')

    self.mainWindow = login.Login()
    self.close()
    self.mainWindow.show()
