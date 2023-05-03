import sys

from PyQt5.QtGui import QIcon

import pages.login.ui as login
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from database_init import database_init
from qt_material import apply_stylesheet, QtStyleTools, density
from PyQt5.QtCore import QLocale
import time

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = login.Login()

    # apply_stylesheet(app, theme='dark_teal.xml')
    # logo = QIcon("qt_material:/logo/logo.svg")
    database_init()
    sys.exit(app.exec_())
