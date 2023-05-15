from PyQt5.QtGui import QPixmap, QFont, QIcon, QPalette, QBrush
from PyQt5.QtWidgets import QDesktopWidget, QLineEdit, QLabel, QFormLayout, QHBoxLayout, QWidget, QPushButton, \
    QGridLayout, QCheckBox, QMessageBox, QMainWindow
import pages.signup.logic as logic

class Signup(QMainWindow):
    def __init__(self, parent, mode=0):
        super().__init__()
        self.parent=parent
        self.mode = mode
        self.setWindowTitle('注册账号')
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

        ###### 设置界面控件
        self.verticalLayout = QGridLayout(self.widget)
        self.H = QLabel(" ")
        self.verticalLayout.addWidget(self.H, 0, 0, 9, 0)
        self.a = QLabel( "")
        self.verticalLayout.addWidget(self.a, 2, 3, 1, 2)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account, 2, 4, 1, 3)




        self.a1 = QLabel('')
        self.verticalLayout.addWidget(self.a1, 3, 3, 1, 2)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password, 3, 4, 1, 3)

        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.a1 = QLabel('')
        self.verticalLayout.addWidget(self.a1, 4, 3, 1, 2)

        self.lineEdit_password1 = QLineEdit()
        self.lineEdit_password1.setPlaceholderText("请再次输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password1, 4, 4, 1, 3)

        self.lineEdit_password1.setEchoMode(QLineEdit.Password)

        self.pushButton_quit1 = QPushButton()
        self.pushButton_quit1.setText("注册")
        self.verticalLayout.addWidget(self.pushButton_quit1, 5, 4, 1, 3)

        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("返回")
        self.verticalLayout.addWidget(self.pushButton_quit, 6, 4, 1, 3)

        logic.bind(self)

        ###### 绑定按钮事件
        # self.pushButton_quit1.clicked.connect(self.on_pushButton_enter_clicked1)
        self.pushButton_quit.clicked.connect(self.back)


    def back(self):
        self.close()
        self.parent.show()
