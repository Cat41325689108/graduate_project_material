import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QLocale

import camera_side


if __name__ == '__main__':
    app = QApplication(sys.argv)
    camera_size = camera_side.MyWidget()
    camera_size.show()

    # client_side=client_side.MyWidget()
    # client_side.show()

    sys.exit(app.exec_())
