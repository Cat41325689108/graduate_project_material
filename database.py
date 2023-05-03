import hashlib
import sqlite3
import time

conn = sqlite3.connect('datas.db')


# 检查数据库文件是否存在
def check_appdatas():
    # conn = sqlite3.connect('datas.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE users
                   (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
                   name TEXT NOT NULL,
                   password TEXT NOT NULL);''')
        c.execute('''CREATE TABLE login_info
                           (id CHAR(10) PRIMARY KEY NOT NULL ,
                           value TEXT  NOT NULL);''')
        conn.commit()
        print("新建表单")
    except Exception as e:
        print(e)


def new_account(username, password):
    c = conn.cursor()
    t = time.time()
    password = f'{password}{t}'
    # 创建MD5对象，可以直接传入要加密的数据
    m = hashlib.md5(password.encode(encoding='utf-8'))
    password = m.hexdigest()  # 转化为16进制打印md5值

    try:
        res = c.execute('''
             INSERT INTO users (name,password,timestamp) values (?,?);
             ''', [username, password, t])
        conn.commit()
        print("新建表单")
    except Exception as e:
        print(e)


def check_password(username, password):
    c = conn.cursor()
    try:
        res = c.execute('''
        SELECT count() FROM users WHERE name=? and password=?
        ''', [username, password])
        if res.fetchone()[0] == 0:
            return False
        else:
            return True
    except Exception as e:
        print(e)


def save_login_info(username, password):
    c = conn.cursor()
    try:
        res = c.execute('''
        SELECT count() FROM USERS WHERE NAME=? and PASSWARD=?
        ''', [username, password])
        if res.fetchone()[0] == 0:
            return False
        else:
            return True
    except Exception as e:
        print(e)
