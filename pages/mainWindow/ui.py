# -*- coding: utf-8 -*-
import os

import qtawesome
from PyQt5.QtGui import QPixmap, QImage, QIcon
from qt_material import QtStyleTools, apply_stylesheet

# from pages.mainWindow.QSS import set_style
import pages.player.player as player
import pages.mainWindow.logic as logic
import pages.statistics.error_log.error_log as error_log
import pages.statistics.communication_error_log.error_log as communication_error_log
import pages.user_center.ui as user_center
import pages.contact_us.ui as contact_us

from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QStackedWidget, QWidget, QMessageBox, QPushButton, QScrollBar, QScrollArea, QListWidget, \
    QLabel, QVBoxLayout, QHBoxLayout, QMainWindow, QToolBar, QAction, QActionGroup, QMenuBar


class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def setRightWidget(self):
        self.right_widget = QStackedWidget()
        self.right_widget.setObjectName('right_widget')

        self.setCentralWidget(self.right_widget)

        self.right_widget.addWidget(self.player_widget)
        self.right_widget.addWidget(self.communication_error_log)
        self.right_widget.addWidget(self.error_log)
        self.right_widget.addWidget(self.user_center)
        self.right_widget.addWidget(self.contact_us)

        def set_background(i):
            if i == 3 or i == 4:
                print(i)
                widget = self.right_widget.currentWidget()
                widget.setStyleSheet(".QWidget{border-image:url(./resources/1.png)}")

        self.right_widget.currentChanged.connect(set_background)

    def setNavigationBar(self):
        self.navigation_bar = QToolBar(self)

        self.navigation_bar.setAllowedAreas(Qt.LeftToolBarArea | Qt.RightToolBarArea)
        self.navigation_bar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.navigation_bar.setOrientation(Qt.Vertical)
        self.navigation_bar.setFloatable(False)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.navigation_bar)

        # 创建一个动作组
        self.action_group = QActionGroup(self)
        # 设置动作组只能有一个动作被选中
        self.action_group.setExclusive(True)

        self.surveillance_label = QAction("视频监控", self)
        self.error_log_label = QAction(self)
        self.error_log_label.setText('异常记录')
        self.video_list.setMinimumWidth(1)
        self.video_list.setMaximumWidth(120)
        self.camera_error_button = QAction('网络异常记录', self)
        def error1():
            self.right_widget.setCurrentIndex(1)
            self.right_widget.currentWidget().indexChanged()
        self.camera_error_button.triggered.connect(error1)
        self.camera_error_button.setCheckable(True)
        self.communication_error_button = QAction('画面异常记录', self)
        self.communication_error_button.setCheckable(True)
        def error2():
            self.right_widget.setCurrentIndex(2)
            self.right_widget.currentWidget().indexChanged()
        self.communication_error_button.triggered.connect(error2)

        self.help_label = QAction('用户和帮助', self)
        self.user_info_button = QAction('账号', self)
        self.user_info_button.setCheckable(True)

        self.user_info_button.triggered.connect(lambda: self.right_widget.setCurrentIndex(3))  # 假设账号对应的是第2个组件
        self.help_center_button = QAction('帮助', self)

        self.help_center_button.setCheckable(True)
        self.help_center_button.triggered.connect(lambda: self.right_widget.setCurrentIndex(4))  # 假设帮助对应的是第3个组件

        self.navigation_bar.addAction(self.surveillance_label)
        self.navigation_bar.addWidget(self.video_list)
        self.navigation_bar.addSeparator()
        self.navigation_bar.addAction(self.error_log_label)
        self.navigation_bar.addAction(self.camera_error_button)
        self.navigation_bar.addAction(self.communication_error_button)
        self.navigation_bar.addSeparator()
        self.navigation_bar.addAction(self.help_label)
        self.navigation_bar.addAction(self.user_info_button)
        self.navigation_bar.addAction(self.help_center_button)

        # 将所有的标签添加到动作组和工具栏
        for action in [self.surveillance_label, self.error_log_label, self.camera_error_button,
                       self.communication_error_button, self.help_label, self.user_info_button,
                       self.help_center_button]:
            self.action_group.addAction(action)

    def setMenu(self):
        # self.custom_styles()
        self.menu=QMenuBar()
        self.menuStyles=self.menu.addMenu('主题')
        # apply_stylesheet(self, theme='default.xml')
        self.add_menu_theme(self, self.menuStyles)
        self.setMenuBar(self.menu)

    def update_theme_event(self, parent):
        """"""
        try:
            theme = [
                action.text()
                for action in self.menu_theme_.actions()
                if action.isChecked()
            ][0]
        except:
            theme = [
                action.text
                for action in self.menu_theme_.actions()
                if action.checked
            ][0]

        apply_stylesheet(
            parent,
            theme=theme,
            invert_secondary=theme.startswith('light'),
        )

    def add_menu_theme(self, parent, menu):
        def list_themes():
            """"""
            themes = os.listdir(
                os.path.join('./themes')
            )
            themes = filter(lambda a: a.endswith('xml'), themes)
            return sorted(list(themes))


        self.menu_theme_ = menu
        action_group = QActionGroup(menu)
        try:
            action_group.setExclusive(True)
        except:
            action_group.exclusive = True

        for i, theme in enumerate(['default'] + list_themes()):
            action = QAction(parent)
            # action.triggered.connect(self._wrapper(parent, theme, self.extra_values, self.update_buttons))
            action.triggered.connect(lambda: self.update_theme_event(parent))
            try:
                action.setText(theme)
                action.setCheckable(True)
                action.setChecked(not bool(i))
                action.setActionGroup(action_group)
                menu.addAction(action)
                action_group.addAction(action)
            except:  # snake_case, true_property
                action.text = theme
                action.checkable = True
                action.checked = not bool(i)
                action.action_group = action_group
                menu.add_action(action)
                action_group.add_action(action)

    def setVideoList(self):
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

    def init_ui(self):
        self.resize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        logo = QIcon("qt_material:/logo/logo.svg")
        self.setWindowIcon(logo)
        self.setWindowTitle('监控运维管理')

        self.error_log = error_log.ErrorLog()
        self.communication_error_log = communication_error_log.CommunicationErrorLog()
        self.user_center = user_center.MyWidget()
        self.contact_us = contact_us.MyWidget()

        self.setVideoList()
        self.setRightWidget()
        self.setNavigationBar()
        self.setMenu()
