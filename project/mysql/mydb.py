#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Project:   
@File:      
@Author:    
@Date:      2023/7/24
"""

"""
说明：
pymysql
mysql-connector-python
mysqlclient
"""



import MySQLdb
from mylog import MyLogger
from mycmd import MyCommand





# 数据库操作
class OperateSQL:
    def __init__(self, logger=print, host="localhost", 
                                user="root", 
                                passwd="123456", 
                                database="mytest", 
                                charset='utf8'):
        self.log  = logger
        self.host = host
        self.user = user
        self.passwd   = passwd
        self.database = database
        self.charset  = charset

    def logon_sql(self, host, user, pawd, db):
        self.log('logon sql:')
        try:
            db = MySQLdb.connect(host=host,  user=user, passwd=pawd, db=db,  charset='utf8')
            cursor = db.cursor()
            # 执行SQL语句
            cursor.execute("SELECT VERSION()")
            results = cursor.fetchone()
            # 使用 fetchone() 方法获取单条数据.
            self.log("Database version : %s " % results)
            # 关闭数据库连接
            cursor.close()
            db.close()
        except MySQLdb.Error as e:
            self.log(f"Error connecting to MySQL Platform: {e}")
    
    def open_sql(self, host=None, user=None, pawd=None, db=None):
        self.log('open sql:')
        try:
            if host:
                self.db = MySQLdb.connect(
                    host=host,  user=user, passwd=pawd, db=db,  charset='utf8')
            else:
                self.db = MySQLdb.connect(host=self.host, 
                                        user=self.user, 
                                        passwd=self.passwd, 
                                        db=self.database, charset='utf8')
        except MySQLdb.Error as e:
            self.log(f"Open MySQL error: {e}")

    def close_sql(self):
        self.log('close sql:')
        self.db.close()

    def execucte_sql(self, cmd:str):
        try:
            # 使用cursor()方法获取操作游标 
            cursor = self.db.cursor()
            cursor.execute(cmd)
            # 提交事务
            self.db.commit()
            print("Execucte_sql successfully")
        except Exception as e:
            # 发生错误时回滚
            self.db.rollback()
            print(f"Execucte_sql error: {e}")
        finally:
            # 关闭游标和连接
            cursor.close()

    def execucte_sel(self, cmd:str):
        results = None
        try:
            # 使用cursor()方法获取操作游标 
            cursor = self.db.cursor()
            cursor.execute(cmd)
            # 获取所有记录列表
            results = cursor.fetchall()
            #print("Execucte_sel successfully")
        except Exception as e:
            print(f"Execucte_sel error: {e}")
        finally:
            # 关闭游标和连接
            cursor.close()
        return results

    def create_table_sql(self, table:str, format:str):
        cmd_sql = f"CREATE TABLE {table} ( {format} )"
        self.execucte_sql(cmd_sql)

    def delect_table_sql(self, table:str):
        cmd_sql = f"DROP TABLE IF EXISTS {table}"
        self.execucte_sql(cmd_sql)

    def select_sql(self):
        self.log('update sql:')

    def delect_sql(self):
        self.log('update sql:')

    def insert_sql(self):
        self.log('add sql:')

    def update_sql(self):
        self.log('update sql:')


def test_1(mytest):
    mytest.connet_remote_cmd('ls')
    mytest.connet_remote_cmd('ls', '172.31.3.80', 22, 'liauto')
    mytest.change_init('172.31.3.80', 22, 'liauto')
    mytest.connet_remote_cmd('ls')
    mytest.change_init()
    mytest.connet_remote_cmd('ls')

def test_2(mytest):
    mytest.exe_subprocess_run('ls')
    mytest.exe_subprocess_run('lx')
    mytest.exe_subprocess_popenE('ls')
    mytest.exe_subprocess_popenE('lx')
    mytest.exe_subprocess_popen('ls')
    mytest.exe_subprocess_popen('lx')
    mytest.exe_os_system_cmd('ls')
    mytest.exe_os_system_cmd('lx')

def test_3(mytest):
    mytest.get_result_remote_cmd('ls', '172.31.3.80', 'liauto')
    mytest.get_result_local_cmd('ls')

def test_logon():
    sql = OperateSQL()
    sql.logon_sql("localhost", "root", "123456", "mytest")

# 创建数据表SQL语句
def test_create():
    sql = OperateSQL()
    sql.open_sql()
    sql_cmd ="""CREATE TABLE employee (
                name  CHAR(20) NOT NULL,
                age INT,  
                sex CHAR(1),
                income FLOAT )"""
    sql.execucte_sql(sql_cmd)
    sql.close_sql()

# 删除数据表SQL语句
def test_remove():
    sql = OperateSQL()
    sql.open_sql()
    sql_cmd ="DROP TABLE IF EXISTS employee"
    sql.execucte_sql(sql_cmd)
    sql.close_sql()

# 插入数据表SQL语句
def test_insert():
    sql = OperateSQL()
    sql.open_sql()
    sql_cmd = """INSERT INTO employee(id, 
         name, age, sex, income)
         VALUES (INT AUTO_INCREMENT PRIMARY KEY, 'Mohan', 20, 'M', 2000)"""
    sql_cmd1 = """INSERT INTO employee(
         name, age, sex, income)
         VALUES ('Mohan', 20, 'M', 2000)"""
    sql_cmd2 = """INSERT INTO employee(
         name)
         VALUES ('Mac')"""
    sql_cmd3 = """INSERT INTO employee(
         name, age)
         VALUES ('LiXiang', 19)"""
    sql.execucte_sql(sql_cmd1)
    sql.execucte_sql(sql_cmd2)
    sql.execucte_sql(sql_cmd3)
    sql.close_sql()

# 查询数据表SQL语句
def test_select():
    sql = OperateSQL()
    sql.open_sql()
    #sql_cmd ="SELECT * FROM employee WHERE income > %s" % (1000)
    sql_cmd = "SELECT * FROM employee"
    res = sql.execucte_sel(sql_cmd)
    sql.close_sql()
    for row in res:
        name = row[0]
        age  = row[1]
        sex  = row[2]
        income = row[3]
        # 打印结果
        print("name=%s,age=%s,sex=%s,income=%s" % (name, age, sex, income))

# 插入数据表SQL语句
def test_update():
    sql = OperateSQL()
    sql.open_sql()
    sql_cmd = "UPDATE employee SET age = age + 1 WHERE sex = '%c'" % ('M')
    sql.execucte_sql(sql_cmd)
    sql.close_sql()      

# 删除数据表SQL语句
def test_delect():
    sql = OperateSQL()
    sql.open_sql()
    sql_cmd = "DELETE FROM employee WHERE name = 'Mac'"
    sql.execucte_sql(sql_cmd)
    sql.close_sql()   

if __name__ == '__main__':
    myLog = MyLogger(write_to_file=True)
    myCmd = MyCommand()
    myXmd = MyCommand(myLog.info)
    test_logon()
    test_remove()
    test_create()
    test_insert()
    test_select()
    test_update()
    test_select()
    test_delect()
    test_select()
    


    

