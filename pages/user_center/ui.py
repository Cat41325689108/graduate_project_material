# -*- coding: utf-8 -*-
import qtawesome

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer, QSettings

from PyQt5.QtGui import QPixmap, QFont, QIcon, QPalette, QBrush
from PyQt5.QtWidgets import QDesktopWidget, QLineEdit, QLabel, QFormLayout, QHBoxLayout, QWidget, QPushButton, \
    QGridLayout, QCheckBox, QMessageBox


class MyWidget(QWidget):
    def __init__(self, mode=0):
        super().__init__()
        self.formLayout2 = QtWidgets.QGridLayout()

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox()
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)
        self.a = QPushButton(qtawesome.icon('fa.user', color="black"), ":")  #个人账号
        self.a.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a1 = QPushButton(qtawesome.icon('fa.mars', color="black"), ":")  # 个人账号
        self.a1.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a2 = QPushButton(qtawesome.icon('fa.university', color="black"), ":")  # 个人账号
        self.a2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a3 = QPushButton(qtawesome.icon('fa.birthday-cake', color="black"), ":")  # 个人账号
        self.a3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.a4 = QPushButton(qtawesome.icon('fa.child', color="black"), ":")  # 个人账号
        self.a4.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.user9 = QtWidgets.QLabel("个人资料")
        self.user9.setFont(qtawesome.font('fa', 31))
        self.right_bar_layout1.addWidget(self.user9, 0, 1, 2, 4)
        f = open("2.txt", 'r+')
        word = f.readline()
        self.user = QtWidgets.QLabel(word)
        self.user.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user, 3, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a, 3, 2, 2, 3)
        self.user1 = QtWidgets.QLabel("男")
        self.user1.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user1, 5, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a1, 5, 2, 2, 3)
        self.user4 = QtWidgets.QLabel("黄延滨")
        self.user4.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user4, 4, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a4, 4, 2, 2, 3)
        self.user2 = QtWidgets.QLabel("电子科技大学")
        self.user2.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user2, 6, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a2, 6, 2, 2, 3)
        self.user3 = QtWidgets.QLabel("2001.01.18")
        self.user3.setFont(qtawesome.font('fa', 22))
        self.right_bar_layout1.addWidget(self.user3, 7, 4, 2, 4)
        self.right_bar_layout1.addWidget(self.a3, 7, 2, 2, 3)
        self.a.setFont(qtawesome.font('fa', 22))
        self.a.setIconSize(QtCore.QSize(20, 20))
        self.user.setObjectName('right_search_button1')
        self.xiugai = QtWidgets.QPushButton(qtawesome.icon('fa.address-card', color='black'), "修改密码")
        self.xiugai.setObjectName('right_search_button2')
        self.xiugai.setFont(qtawesome.font('fa', 30))
        # self.xiugai.clicked.connect(self.right_folder_button_clicked)
        self.right_bar_layout1.addWidget(self.xiugai, 26, 4, 1, 3)
        self.xiugai.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.zhuxiao = QtWidgets.QPushButton(qtawesome.icon('fa.reply-all', color='black'),"注销账号")
        self.zhuxiao.setObjectName('right_search_button2')
        self.zhuxiao.setFont(qtawesome.font('fa', 16))
        # self.zhuxiao.clicked.connect(self.right_folder_button_clicked1)
        self.right_bar_layout1.addWidget(self.zhuxiao, 27, 4, 1, 3)
        self.zhuxiao.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.bianji = QtWidgets.QPushButton(qtawesome.icon('fa.pencil-square-o', color='black'), "编辑资料")
        self.bianji.setObjectName('right_search_button3')
        self.bianji.setFont(qtawesome.font('fa', 16))
        # self.bianji.clicked.connect(self.right_folder_button_clicked2)
        self.right_bar_layout1.addWidget(self.bianji, 25, 4, 1, 3)
        self.bianji.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_bar_widget2 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout2 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget2.setLayout(self.right_bar_layout2)
        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setIcon(QtGui.QIcon('./1.png'))
        self.recommend_button_1.setIconSize(QtCore.QSize(200, 200))
        self.right_bar_layout1.addWidget(self.recommend_button_1, 3, 1, 6, 1)
        self.recommend_button_1.setStyleSheet('''
                                         QToolButton{border:none;color:black;}
                                         QToolButton:hover{color:white}
                                          ''')

        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget2, 1, 0, 1, 9)

        self.setLayout(self.formLayout2)

