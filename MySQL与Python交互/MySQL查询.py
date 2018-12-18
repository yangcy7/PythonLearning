import copy

from pymysql import *

def one():
    from Settings import mysql_config
    conn = connect(host=mysql_config['host'], port=mysql_config['port'], database=mysql_config['database'],
                   user=mysql_config['user'], password=mysql_config['password'], charset=mysql_config['charset'])

    # 获取Cursor对象：调用Connection对象的cursor()方法
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count=cs1.execute('select id,name from goods where id>=4')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)
    for i in range(count):
        # 获取查询的结果
        result=cs1.fetchone()
        # 打印查询的结果
        print(result)
        # 获取查询的结果

        # 关闭Cursor对象
    cs1.close()
    conn.close()
def all():
    from Settings import mysql_config
    conn = connect(host=mysql_config['host'], port=mysql_config['port'], database=mysql_config['database'],
                   user=mysql_config['user'], password=mysql_config['password'], charset=mysql_config['charset'])

    # 获取Cursor对象：调用Connection对象的cursor()方法
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count=cs1.execute('select id,name from goods where id>=4')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)
    # for i in range(count):
    #     # 获取查询的结果
    #     result=cs1.fetchone()
    #     # 打印查询的结果
    #     print(result)
    #     # 获取查询的结果
    # result=cs1.fetchall()
    # print(result)
    # 获取结果后,cs1就清空了,就不能同时用fetchmany和fetchall
    many_data=cs1.fetchmany(10)
    print(many_data)
        # 关闭Cursor对象
    cs1.close()
    conn.close()
def UseCopy():
    from Settings import mysql_config
    conn = connect(host=mysql_config['host'], port=mysql_config['port'], database=mysql_config['database'],
                   user=mysql_config['user'], password=mysql_config['password'], charset=mysql_config['charset'])

    # 获取Cursor对象：调用Connection对象的cursor()方法
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count=cs1.execute('select id,name from goods where id>=4')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)
    # for i in range(count):
    #     # 获取查询的结果
    #     result=cs1.fetchone()
    #     # 打印查询的结果
    #     print(result)
    #     # 获取查询的结果

    cs2=copy.copy(cs1)
    result=cs1.fetchall()
    print(result)
    many_data=cs2.fetchmany(10)
    print(many_data)
        # 关闭Cursor对象
    cs1.close()
    conn.close()


if __name__ == '__main__':
    # one()
    # all()
    UseCopy()