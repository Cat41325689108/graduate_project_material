from PyQt5.QtCore import QSettings, QTimer
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt5 import QtGui, QtCore

import database

from pages.mainWindow.ui import MainUi
from pages.signup.ui import Signup


# import database
# import pages.mainView.ui as MainView

def bind(self):
    database.check_appdatas()

    self.pushButton_enter.clicked.connect(lambda: on_pushButton_enter_clicked(self))
    self.pushButton_quit1.clicked.connect(lambda: on_pushButton_enter_clicked1(self))
    init_login_info(self)

    self.timer = QTimer(self)
    self.timer.timeout.connect(lambda: goto_autologin(self))
    self.timer.setSingleShot(True)
    self.timer.start(1000)
    # 自动登录


def goto_autologin(self):
    if self.checkBox_autologin.isChecked() == True and self.mode == 0:
        self.on_pushButton_enter_clicked()


def on_pushButton_enter_clicked(self):
    account_dict = {}
    f = open("1.txt", 'r+')
    for line in f:
        (keys, value) = line.strip().split()
        account_dict[keys] = value
    account1 = self.lineEdit_account.text()
    password1 = self.lineEdit_password.text()
    account_keys = list(account_dict.keys())
    f1 = "2.txt"
    with open(f1, "w") as file:  # 只需要将之前的”w"改为“a"即可，代表追加内
        file.write(account1)
    if account1 != "" and password1 != "":

        if account1 not in account_keys:
            reply1 = QMessageBox.information(self, '登录出错', '用户不存在', QMessageBox.Yes | QMessageBox.No,
                                             QMessageBox.Yes)
        elif password1 == account_dict[account1]:
            ####### 保存登录信息
            save_login_info(self)
            # 通过验证，关闭对话框并返回1
            self.close()
            save_login_info(self)
            self.mainWindow=MainUi()
            self.mainWindow.show()
        else:
            QMessageBox.information(self, '登录出错', '密码错误', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    else:
        QMessageBox.information(self, '错误', '输入不能为空！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


def on_pushButton_enter_clicked1(self):
    self.signup = Signup(self)
    self.signup.show()
    self.close()


# 保存登录信息
def save_login_info(self):
    settings = QSettings("config.ini", QSettings.IniFormat)
    settings.setValue("account", self.lineEdit_account.text())
    settings.setValue("password", self.lineEdit_password.text())
    settings.setValue("remeberpassword", self.checkBox_remeberpassword.isChecked())
    settings.setValue("autologin", self.checkBox_autologin.isChecked())


# 初始化登录信息
def init_login_info(self):
    settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
    the_account = settings.value("account")
    the_password = settings.value("password")
    the_remeberpassword = settings.value("remeberpassword")
    the_autologin = settings.value("autologin")
    ########
    self.lineEdit_account.setText(the_account)
    if the_remeberpassword == "true" or the_remeberpassword == True:
        self.checkBox_remeberpassword.setChecked(True)
        self.lineEdit_password.setText(the_password)

    if the_autologin == "true" or the_autologin == True:
        self.checkBox_autologin.setChecked(True)


regexp = QtCore.QRegExp('^[a-zA-Z0-9]*$')
validator = QtGui.QRegExpValidator(regexp)
