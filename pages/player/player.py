import cv2 as cv
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
import pages.player.detection as detection
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
import sqlite3
import pages.player.communication as communication


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.camera_index = None
        self.detector = None
        self.cap = None
        self.fold_path = './occlusion_detection/datas/'
        self.player_button_widget = QWidget()
        self.video_status_bar_widget = QWidget()

        self.video_player = QLabel()

        self.video_status_bar_layout = QHBoxLayout()
        self.video_status = QLabel()
        self.communication_status = QLabel()

        self.video_status_bar_layout.addWidget(self.video_status)
        self.video_status_bar_layout.addWidget(self.communication_status)
        self.video_status_bar_widget.setLayout(self.video_status_bar_layout)

        self.video_status.setMinimumHeight(30)
        self.set_communication_status('ok')

        self.video_status_timer = QTimer()
        self.video_communication_timer = QTimer()
        self.timer = QTimer()

        def reset_video_status():
            self.video_status.setText('视频状态:正常')
            self.video_status.setStyleSheet(
                'border-width: 1px;border-style: solid;'
                'background-color: rgb(0, 249 , 26);')
            self.video_status_timer.stop()

        reset_video_status()

        self.video_status_timer.timeout.connect(reset_video_status)
        self.video_player.setObjectName('video_player')

        self.video_player_layout = QVBoxLayout()
        self.video_player_layout.addWidget(self.video_player)
        self.video_player_layout.addWidget(self.video_status_bar_widget)
        self.video_player_layout.addWidget(self.player_button_widget)
        self.video_player_layout.setStretchFactor(self.video_player, 20)
        self.video_player_layout.setStretchFactor(self.video_status, 1)
        self.video_player_layout.setStretchFactor(self.player_button_widget, 1)

        self.setLayout(self.video_player_layout)

        self.communication_widget = communication.MyWidget()
        self.communication_widget.set_on_start(self.start_video)
        self.communication_widget.set_on_stop(self.stop_video)
        self.stop_video()

    def stop_video(self):
        self.timer.stop()
        self.set_communication_status('lose')

    def start_video(self):
        self.timer.start(10)
        self.set_communication_status('ok')

    def on_path_change(self, name, camera_index):
        self.cap = cv.VideoCapture(self.fold_path + name)
        self.timer.stop()
        self.detector = detection.Detector(self.cap)
        self.update_frame()
        self.timer.timeout.connect(self.update_frame)
        self.camera_index = camera_index

    def set_communication_status(self, status):
        if status == 'ok':
            self.communication_status.setText('监控器通信状态:正常')
            self.communication_status.setStyleSheet(
                'border-width: 1px;border-style: solid;'
                'background-color: rgb(0, 249 , 26);')
        if status == 'lose':
            self.communication_status.setText('监控器通信状态:连接中断')
            self.communication_status.setStyleSheet(
                'border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);'
                'background-color: rgb(255, 251, 13);')
            self.take_communication_error('连接中断')

    def set_video_status(self, status):
        if status == 'occlusion':
            self.video_status.setText('视频状态：摄像头被遮挡，请检查摄像头')
            self.video_status.setStyleSheet(
                'border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);'
                'background-color: rgb(255, 251, 13);')
            if not self.video_status_timer.isActive():
                self.take_error_record('摄像头被遮挡')
            self.video_status_timer.start(5000)

        if status == 'motion':
            self.video_status.setText('视频状态：摄像头被移动，请检查摄像头')
            self.video_status.setStyleSheet(
                'border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);'
                'background-color: rgb(5, 50, 255);')
            if not self.video_status_timer.isActive():
                self.take_error_record('摄像头被移动')
            self.video_status_timer.start(5000)

        if status == 'shake':
            self.video_status.setText('视频状态：摄像头抖动，请检查摄像头')
            self.video_status.setStyleSheet(
                'border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);'
                'background-color: rgb(225, 41, 41);')
            if not self.video_status_timer.isActive():
                self.take_error_record('摄像头抖动')
            self.video_status_timer.start(5000)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret == False:
            self.stop_video()
            return
        self.set_video_status(self.detector.frame_in(frame))
        img = frame
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv.cvtColor(img, cv.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        QImg = QImg.scaled(self.video_player.width(), self.video_player.height())
        pixmap = QPixmap.fromImage(QImg)
        self.video_player.setPixmap(pixmap)

    def take_error_record(self, error_info):
        conn = sqlite3.connect('datas.db')
        c = conn.cursor()
        c.execute('''
                INSERT INTO error_logs (camera_index,error_info) VALUES (?,?)
                ''', [self.camera_index, error_info])
        conn.commit()
        conn.close()

    def take_communication_error(self, error_info):
        conn = sqlite3.connect('datas.db')
        c = conn.cursor()
        c.execute('''
                INSERT INTO communication_error_logs (camera_index,error_info) VALUES (?,?)
                ''', [self.camera_index, error_info])
        conn.commit()
        conn.close()
