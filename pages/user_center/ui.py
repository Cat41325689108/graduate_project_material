# -*- coding: utf-8 -*-
import qtawesome

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QSettings, QSize

from PyQt5.QtGui import QPixmap, QFont, QIcon, QPalette, QBrush, QImage
from PyQt5.QtWidgets import QDesktopWidget, QLineEdit, QLabel, QFormLayout, QHBoxLayout, QWidget, QPushButton, \
    QGridLayout, QCheckBox, QMessageBox


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.formLayout2 = QtWidgets.QGridLayout()
        self.setObjectName('mainWidget')

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox()
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QHBoxLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)
        self.a = QLabel()  #个人账号
        self.a1 = QLabel()  # 个人账号
        self.a2 = QLabel()  # 个人账号
        self.a3 = QLabel()  # 个人账号
        self.a4 = QLabel()  # 个人账号


        self.zhuxiao = QtWidgets.QPushButton("账号信息")
        self.zhuxiao.clicked.connect(self.right_folder_button_clicked3)
        self.zhuxiao.setMaximumWidth(400)
        self.zhuxiao.setObjectName('right_search_button2')
        self.zhuxiao.setFont(qtawesome.font('fa', 16))
        self.right_bar_layout1.addWidget(self.zhuxiao)


        self.right_bar_widget2 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout2 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget2.setLayout(self.right_bar_layout2)

        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 9)
        # self.formLayout2.addWidget(self.right_bar_widget2, 1, 0, 1, 9)

        self.setLayout(self.formLayout2)

    def right_folder_button_clicked3(self):
        self.right_message_Alter.information(self.right_message_Alter, "联系方式", self.tr(
            '''用户：admin
角色：管理员'''))
