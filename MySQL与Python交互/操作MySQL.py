from pymysql import *
import os
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
# Connection 对象
# 用于建立与数据库的连接
#
# 创建对象：调用connect()方法
#
# conn=connect(参数列表)
# 参数host：连接的mysql主机，如果本机是'localhost'
# 参数port：连接的mysql主机的端口，默认是3306
# 参数database：数据库的名称
# 参数user：连接的用户名
# 参数password：连接的密码
# 参数charset：通信采用的编码方式，推荐使用utf8
def main():
    from Settings import mysql_config

    conn=connect(host=mysql_config['host'],port=mysql_config['port'],database=mysql_config['database'],
                 user=mysql_config['user'],password=mysql_config['password'],charset=mysql_config['charset'])

    # 获取Cursor对象：调用Connection对象的cursor()方法
    cs1=conn.cursor()
    # 执行insert语句，并返回受影响的行数：添加一条数据
    # 增加
    count=cs1.execute('insert into goods_cates(name) values("硬盘")')
    print("count",count)
    count1=cs1.execute('insert into goods_cates(name) values("光盘")')
    print("count1",count1)
    # # 更新
    # count = cs1.execute('update goods_cates set name="机械硬盘" where name="硬盘"')
    # # 删除
    # count = cs1.execute('delete from goods_cates where id=6')

    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    conn.commit()

    # 关闭Cursor对象
    cs1.close()
    # 关闭Connection对象
    conn.close()

if __name__ == '__main__':
    main()
