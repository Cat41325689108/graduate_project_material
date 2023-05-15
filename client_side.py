import sys

import pages.login.ui as login
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from database_init import database_init
from qt_material import apply_stylesheet, QtStyleTools, density

if __name__ == '__main__':
    app = QApplication(sys.argv)

    apply_stylesheet(app, theme='default.xml')
    MainWindow = login.Login()

    database_init()
    sys.exit(app.exec_())
