# -*- coding: utf-8 -*-
import qtawesome
from PyQt5.QtGui import QPixmap, QImage
from pages.mainWindow.QSS import set_style
import pages.player.player as player
import pages.mainWindow.logic as logic
import pages.statistics.error_log.error_log as error_log
import pages.statistics.communication_error_log.error_log as communication_error_log
import pages.user_center.ui as user_center
import pages.contact_us.ui as contact_us

from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QStackedWidget, QWidget, QMessageBox, QPushButton, QScrollBar, QScrollArea, QListWidget, \
    QLabel, QVBoxLayout, QHBoxLayout



class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QStackedWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列

        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        # self.left_close.clicked.connect(self.close1)  # 关闭窗口
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        # self.left_visit.clicked.connect(self.back)  # 关闭窗口
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        # self.left_mini.clicked.connect(self.showMinimized)  # 最小化窗口

        self.left_label_1 = QtWidgets.QPushButton("视频监控")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("信息反馈")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("帮助与用户")
        self.left_label_3.setObjectName('left_label')

        self.video_list = QListWidget(self)
        self.video_list.setMaximumHeight(200)
        logic.get_local_videos(self)
        print(logic.files)
        for i in range(1, len(logic.files) + 1):
            self.video_list.addItem(f'视频{i}')

        self.player_widget = player.Player()

        def currentItemChanged():
            self.player_widget.on_path_change(logic.files[self.video_list.currentRow()],
                                              self.video_list.currentRow() + 1)
            if self.right_widget.currentIndex() != 0:
                self.right_widget.setCurrentIndex(0)

        self.video_list.currentItemChanged.connect(currentItemChanged)

        self.error_log = error_log.ErrorLog()
        self.communication_error_log = communication_error_log.CommunicationErrorLog()
        self.user_center=user_center.MyWidget()
        self.contact_us=contact_us.MyWidget()

        self.right_widget.addWidget(self.player_widget)
        self.right_widget.addWidget(self.communication_error_log)
        self.right_widget.addWidget(self.error_log)
        self.right_widget.addWidget(self.user_center)
        self.right_widget.addWidget(self.contact_us)

        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.line-chart', color='white'), "网络异常统计")
        self.left_button_5.setObjectName('left_button')
        self.left_button_5.clicked.connect(lambda: self.right_widget.setCurrentIndex(1))
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.bar-chart', color='white'), "监控异常统计")
        self.left_button_6.setObjectName('left_button')
        self.left_button_6.clicked.connect(lambda: self.right_widget.setCurrentIndex(2))
        self.user_center_button = QtWidgets.QPushButton(qtawesome.icon('fa.user-o', color='white'), "个人中心")
        self.user_center_button.setObjectName('left_button')
        self.user_center_button.clicked.connect(lambda: self.right_widget.setCurrentIndex(3))
        self.contact_us_button = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.contact_us_button.setObjectName('left_button')
        self.contact_us_button.clicked.connect(lambda: self.right_widget.setCurrentIndex(4))

        self.left_xxx = QtWidgets.QPushButton(" ")
        self.left_layout.addWidget(self.left_mini, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.video_list, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 3, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 6, 0, 1, 3)
        self.left_layout.addWidget(self.user_center_button, 7, 0, 1, 3)
        self.left_layout.addWidget(self.contact_us_button, 8, 0, 1, 3)

        set_style(self)

