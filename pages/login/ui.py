import qtawesome

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QSettings

from PyQt5.QtGui import QPixmap, QFont, QIcon, QPalette, QBrush
from PyQt5.QtWidgets import QDesktopWidget, QLineEdit, QLabel, QFormLayout, QHBoxLayout, QWidget, QPushButton, \
    QGridLayout, QCheckBox, QMessageBox
import pages.login.logic as logic


class Login(QWidget):
    def __init__(self, mode=0):
        super().__init__()

        self.mode = mode
        self.setWindowTitle('登录界面')
        self.resize(800, 450)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./1.png")))
        self.setPalette(palette)
        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)

        self.a = QPushButton(qtawesome.icon('fa.user-circle', color='white'), ":")
        self.verticalLayout.addWidget(self.a, 2, 3, 1, 2)
        self.a.setStyleSheet('''
                           QPushButton{border:none;color:black;}
                           QPushButton:hover{color:white}
                            ''')
        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account, 2, 4, 1, 3)
        self.lineEdit_account.setStyleSheet(
            '''QLineEdit{
                        border:1px solid gray;
                        width:200px;
                        border-radius:10px;
                        padding:2px 4px;
                }''')

        self.a1 = QPushButton(qtawesome.icon('fa.lock', color='white'), ":")
        self.verticalLayout.addWidget(self.a1, 3, 3, 1, 2)
        self.a1.setStyleSheet('''
                                   QPushButton{border:none;color:black;}
                                   QPushButton:hover{color:white}
                                    ''')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password, 3, 4, 1, 3)
        self.lineEdit_password.setStyleSheet(
            '''QLineEdit{
                        border:1px solid gray;
                        width:200px;
                        border-radius:10px;
                        padding:2px 4px;
                }''')
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.checkBox_remeberpassword = QCheckBox()
        self.checkBox_remeberpassword.setText("记住密码")
        self.verticalLayout.addWidget(self.checkBox_remeberpassword, 4, 4, 1, 3)
        self.checkBox_remeberpassword.setStyleSheet(
            "QCheckBox { color : white; }; QCheckBox::indicator { color:black; }");

        self.checkBox_autologin = QtWidgets.QCheckBox()
        self.checkBox_autologin.setText("自动登录")
        self.verticalLayout.addWidget(self.checkBox_autologin, 4, 5, 1, 3)
        self.checkBox_autologin.setStyleSheet(
            "QCheckBox { color : white; }; QCheckBox::indicator { color:black; }");
        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("登录")
        self.verticalLayout.addWidget(self.pushButton_enter, 5, 4, 1, 3)
        self.pushButton_enter.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("注册")
        self.verticalLayout.addWidget(self.pushButton_quit1, 6, 4, 1, 3)
        self.pushButton_quit1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        logic.bind(self)
        self.show()

