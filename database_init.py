import sqlite3

def database_init():
    conn = sqlite3.connect('datas.db')
    c = conn.cursor()
    try:
        c.execute('''
        CREATE TABLE IF NOT EXISTS `error_logs`(
        `id` INTEGER PRIMARY KEY  NOT NULL, 
        `camera_index` INTEGER, 
        `error_info` varchar(255), 
        `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
        ''')
        c.execute('''
                CREATE TABLE IF NOT EXISTS `communication_error_logs`(
                `id` INTEGER PRIMARY KEY  NOT NULL, 
                `camera_index` INTEGER, 
                `error_info` varchar(255), 
                `create_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
                ''')
        print('database_init')
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

