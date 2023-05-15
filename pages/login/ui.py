import qtawesome

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QSettings

from PyQt5.QtGui import QPixmap, QFont, QIcon, QPalette, QBrush, QPainter
from PyQt5.QtWidgets import QDesktopWidget, QLineEdit, QLabel, QFormLayout, QHBoxLayout, QWidget, QPushButton, \
    QGridLayout, QCheckBox, QMessageBox, QMainWindow
import pages.login.logic as logic


class Login(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('登录界面')
        self.resize(800, 450)

        self.setObjectName("Login")

        self.setObjectName("Login")
        self.setStyleSheet("#Login{border-image:url(./resources/1.png)}")
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setObjectName("MyWidget")
        self.widget.setStyleSheet("#MyWidget{background-color: transparent;}")

        logo = QIcon("qt_material:/logo/logo.svg")
        self.setWindowIcon(logo)

        # 设置界面控件
        self.verticalLayout = QGridLayout(self.widget)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)

        self.a = QLabel("账号:")
        self.verticalLayout.addWidget(self.a, 2, 3, 1, 2)
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account, 2, 4, 1, 3)

        self.a1 = QLabel("密码:")
        self.verticalLayout.addWidget(self.a1, 3, 3, 1, 2)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password, 3, 4, 1, 3)

        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.checkBox_remeberpassword = QCheckBox()
        self.checkBox_remeberpassword.setText("记住密码")
        self.verticalLayout.addWidget(self.checkBox_remeberpassword, 4, 4, 1, 3)

        self.checkBox_autologin = QtWidgets.QCheckBox()
        self.checkBox_autologin.setText("自动登录")
        self.verticalLayout.addWidget(self.checkBox_autologin, 4, 5, 1, 3)

        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("登录")
        self.verticalLayout.addWidget(self.pushButton_enter, 5, 4, 1, 3)

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("注册")
        self.verticalLayout.addWidget(self.pushButton_quit1, 6, 4, 1, 3)

        logic.bind(self)
        self.show()
