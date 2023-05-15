from PyQt5.QtGui import QPixmap, QFont, QIcon, QPalette, QBrush
from PyQt5.QtWidgets import QDesktopWidget, QLineEdit, QLabel, QFormLayout, QHBoxLayout, QWidget, QPushButton, \
    QGridLayout, QCheckBox, QMessageBox, QTextBrowser
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtNetwork import QUdpSocket, QHostAddress, QTcpServer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self, ):
        super().__init__()
        self.resize(400, 400)

        # 1
        self.browser = QTextBrowser(self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.browser)
        self.setLayout(self.v_layout)

        # 2
        self.server = QTcpServer(self)
        if not self.server.listen(QHostAddress.LocalHost, 6666):
            self.browser.append(self.server.errorString())

        self.server.newConnection.connect(self.new_socket_slot)

        self.on_start = None
        self.on_stop = None
        print('on_stop')

    def set_on_start(self, f):
        self.on_start = f

    def set_on_stop(self, f):
        self.on_stop = f

    def new_socket_slot(self):
        sock = self.server.nextPendingConnection()

        peer_address = sock.peerAddress().toString()
        peer_port = sock.peerPort()
        news = 'Connected with address {}, port {}'.format(peer_address, str(peer_port))
        self.browser.append(news)

        sock.readyRead.connect(lambda: self.read_data_slot(sock))
        sock.disconnected.connect(lambda: self.disconnected_slot(sock))

    def read_data_slot(self, sock):
        while sock.bytesAvailable():
            datagram = sock.read(sock.bytesAvailable())
            message = datagram.decode()
            answer = 'ok'
            new_datagram = answer.encode()
            sock.write(new_datagram)
            if message == 'start':
                print('on_start')
                self.on_start()
            if message == 'stop':
                self.on_stop()
                print('on_stop')

    def disconnected_slot(self, sock):
        peer_address = sock.peerAddress().toString()
        peer_port = sock.peerPort()
        news = 'Disconnected with address {}, port {}'.format(peer_address, str(peer_port))
        self.browser.append(news)
        sock.close()
