import sqlite3

import qtawesome
from PyQt5.QtWidgets import QWidget, QMessageBox
from qtpy import QtWidgets, QtCore
import pages.statistics.error_log.error_log_table as error_log_table


class ErrorLog(QWidget):
    def __init__(self):
        super().__init__()

        self.formLayout2 = QtWidgets.QGridLayout()

        # 2.1 信息提示对话框
        self.right_message_Alter = QMessageBox();
        self.right_message_Alter.setObjectName("right_message_Alter");
        self.right_message_Alter.setWindowOpacity(0.9)  # 设置窗口透明度
        self.right_message_Alter.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        # 2.2 文件选择框及按钮
        self.right_bar_widget1 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout1 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget1.setLayout(self.right_bar_layout1)

        self.mm5 = QtWidgets.QLabel('监控错误日志')
        self.mm5.setFont(qtawesome.font('fa', 35))
        self.right_folder_button = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "")
        self.right_folder_button.setObjectName('right_search_button')
        self.right_folder_button.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button.setFont(qtawesome.font('fa', 20))
        self.right_folder_button.setFixedSize(30, 30)  # 设置按钮大小

        self.right_folder_button1 = QtWidgets.QPushButton(qtawesome.icon('fa.user-circle', color='balck'), "查询")
        self.right_folder_button1.setObjectName('right_search_button')
        self.right_folder_button1.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button1.setFont(qtawesome.font('fa', 20))
        # self.right_folder_button1.clicked.connect(self.view_data111)
        self.right_folder_button1.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button1.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button3 = QtWidgets.QPushButton(qtawesome.icon('fa.trash', color='balck'), "清空")
        self.right_folder_button3.setObjectName('right_search_button')
        self.right_folder_button3.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button3.setFont(qtawesome.font('fa', 20))
        # self.right_folder_button3.clicked.connect(self.view_data2)
        self.right_folder_button3.setFixedSize(110, 30)  # 设置按钮大小
        self.right_folder_button3.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")
        self.right_folder_button2 = QtWidgets.QPushButton(qtawesome.icon('fa.address-book-o', color='balck'),
                                                          "查询全部信息")
        self.right_folder_button2.setObjectName('right_search_button')
        self.right_folder_button2.setStyleSheet('''QPushButton{border:none;color:black;}''')
        self.right_folder_button2.setFont(qtawesome.font('fa', 20))
        # self.right_folder_button2.clicked.connect(self.view_data)
        self.right_folder_button2.setFixedSize(200, 30)  # 设置按钮大小
        self.right_folder_button2.setStyleSheet(
            "QPushButton{color:highlight}"
            "QPushButton:hover{color:white}"
            "QPushButton{background-color:rgb(0,191,255)}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:5px 6px}"
            "QPushButton{font-size:14pt}")

        self.right_bar_widget_folder_input88 = QtWidgets.QLineEdit()
        self.right_bar_widget_folder_input88.setPlaceholderText("请输入学号/姓名")
        self.right_bar_widget_folder_input88.setObjectName("right_input_item");
        self.right_bar_widget_folder_input88.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:10px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')
        self.right_bar_layout1.addWidget(self.mm5, 0, 0, 1, 5)
        # self.right_bar_layout1.addWidget(self.right_folder_button, 1, 0, 1, 1)
        # self.right_bar_layout1.addWidget(self.right_folder_button1, 1, 21, 1, 5)
        # self.right_bar_layout1.addWidget(self.right_folder_button2, 1, 27, 1, 5)
        # self.right_bar_layout1.addWidget(self.right_folder_button3, 1, 33, 1, 5)
        # self.right_bar_layout1.addWidget(self.right_bar_widget_folder_input88, 1, 1, 1, 20)
        self.formLayout2.addWidget(self.right_bar_widget1, 0, 0, 1, 0)

        # 2.4 输出结果
        self.right_bar_widget3 = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout3 = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget3.setLayout(self.right_bar_layout3)

        # 结果输出
        self.right_batch_result_lable = QtWidgets.QLabel('结果:')
        self.right_batch_result_lable.setFont(qtawesome.font('fa', 16))

        self.right_batch_result_listView = error_log_table.ErrorLogTable()

        self.right_bar_layout3.addWidget(self.right_batch_result_lable, 0, 0, 1, 9)
        self.right_bar_layout3.addWidget(self.right_batch_result_listView, 1, 0, 1, 9)
        self.formLayout2.addWidget(self.right_bar_widget3, 2, 0, 1, 9)
        # 消息框美化
        self.right_message_Alter.setStyleSheet('''
                                                       QMessageBox{
                                                           background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0,stop: 0 rgba(255, 255, 255, 100%),
                                                           stop: 1 rgba(70, 130, 180, 100%));
                                                           border-top:1px solid black;
                                                           border-bottom:1px solid black;
                                                           border-left:1px solid black;
                                                           border-right:1px solid black;
                                                           border-radius:10px;
                                                           padding:2px 4px;
                                                       }   
                                                   ''')
        self.right_batch_result_listView.setStyleSheet('''
                                QListView {
                                    alternate-background-color: yellow; 
                                    padding:2px 4px;
                                }
                                QListView {
                                show-decoration-selected: 1; /* make the selection span the entire width of the view */
                                }
                                /* 此处QListView::item:alternate覆盖会alternate-background-color: yellow属性*/
                                QListView::item:alternate {
                                    background: #EEEEEE; /* item交替变换颜色，如图中灰色 */
                                }
                                QListView::item:selected {
                                border: 1px solid #6a6ea9;
                                }
                                QListView::item:selected:!active {
                                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                             stop: 0 #ABAFE5, 
                                                             stop: 1 #8588B2);
                                }
                                QListView::item:selected:active {
                                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                             stop: 0 #6a6ea9, 
                                                             stop: 1 #888dd9);
                                }
                                QListView::item:hover {
                                    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                             stop: 0 #FAFBFE, 
                                                             stop: 1 #DCDEF1);
                            ''')
        self.setLayout(self.formLayout2)

    def indexChanged(self):
        self.right_batch_result_listView = error_log_table.ErrorLogTable()
        print('on_focus')
