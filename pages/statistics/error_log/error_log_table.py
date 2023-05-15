import sqlite3

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QHeaderView, QTableView, QWidget, QVBoxLayout


class ErrorLogTable(QTableView):
    def __init__(self):
        super().__init__()

        # 4行3列
        self.model = QStandardItemModel(4, 3)

        # 设置表头
        self.model.setHorizontalHeaderLabels(['监视器id', '错误信息', '错误时间'])

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setModel(self.model)

        # 添加数据
        rows = self.read_database()
        for i in range(len(rows)):
            print(rows[i])
            item1 = QStandardItem(str(rows[i][0]))
            item2 = QStandardItem(rows[i][1])
            item3 = QStandardItem(rows[i][2])
            self.model.setItem(i, 0, item1)
            self.model.setItem(i, 1, item2)
            self.model.setItem(i, 2, item3)

    def read_database(self):
        conn = sqlite3.connect('datas.db')
        c = conn.cursor()
        try:
            res = c.execute('''
               SELECT camera_index,error_info,create_time FROM error_logs;
               ''')
            rows = res.fetchall()
            conn.close()
        except Exception as e:
            print(e)
        return rows
