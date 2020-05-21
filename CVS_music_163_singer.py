# python操作数据库创建数据表
import pymysql
# try:
#     # 获取数据库连接。注意：如果是utf-8类型，需要定制数据库
#     # 代开数据库连接
#     """
#     host='192.168.1.145', 数据库服务器地址
#     user='root', 登陆数据库用户
#     passwd='root', 用户密码
#     db='text', 所链接的数据库名
#     port=3306 数据库端口号，mysql默认3306
#     """
#     db = pymysql.connect(host='192.168.1.145', user='root', passwd='root', db='text', port=3306)
#     # print(db)
#     # 创建游标，对数据进程操作，使用cursor()方法
#     cursor = db.cursor()
#     # 使用execute()执行sql语句
#     cursor.execute('DROP TABLES IF EXISTS PYTHONX')
#     # 使用预处理语句创建表
#     sql = """create table PYTHONX(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT)
#     """
#     cursor.execute(sql)
#     db.close()
# except:
#     print("创建失败")

# # 数据库插入操作
# db = pymysql.connect(host='192.168.1.145', user='root', passwd='root', db='text', port=3306)
# cursor = db.cursor()
# # sql = """insert into PYTHONX(FIRST_NAME,LAST_NAME,AGE,SEX,
# # SEX,INCOME)VALUES("liu","dana",18,"M",1000000),
# # ("huang","laoban",19,"M",99999)"""
# sql = """insert into PYTHONX(FIRST_NAME,LAST_NAME,AGE,SEX,
# INCOME)VALUES("%s","%s",%d,"%c",%s)"""%("liu", "dana", 18, "M", "1000000")
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交执行
#     db.commit()
#     print('执行成功')
# except:
#     # 发生意外,数据库回滚
#     db.rollback()
#     print('执行失败')
# db.close()

# 数据库插入操作
# db = pymysql.connect(host='192.168.1.145', user='root', passwd='root', db='text', port=3306)
# cursor = db.cursor()
# # sql = """insert into PYTHONX(FIRST_NAME,LAST_NAME,AGE,SEX,
# # SEX,INCOME)VALUES("liu","dana",18,"M",1000000),
# # ("huang","laoban",19,"M",99999)"""
# sql = """insert into PYTHONX(FIRST_NAME,LAST_NAME,AGE,SEX,
# INCOME)VALUES("%s","%s",%d,"%c","%s")""" % ("huang", "laoban", 19, "M", "99999")
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交执行
#     db.commit()
#     print('执行成功')
# except:
#     # 发生意外,数据库回滚
#     db.rollback()
#     print('执行失败')
# db.close()

# 数据库查询操作
db = pymysql.connect(host='192.168.1.145', user='root', passwd='root', db='text', port=3306)
cursor = db.cursor()
sql = """
select * from PYTHONX
"""
try:
    # 执行sql语句
    cursor.execute(sql)
    """
    fetchall() 接收全部返回结果
    fetchone():获取下一个查询结果集
    rowcount:只读属性，返回执行语句影响的行数
    """
    # datas为一个元组
    datas = cursor.fetchall()
    # datas = cursor.fetchone()
    # datas = cursor.rowcount
    print(datas)
    for data in datas:
        print(data)
    print('执行成功')
    cursor.close()
    db.close()
except Exception as e:
    print('查询失败')
    print(e)


