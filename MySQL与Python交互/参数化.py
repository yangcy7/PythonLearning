from pymysql import *
def main():
    from Settings import mysql_config

    conn=connect(host=mysql_config['host'],port=mysql_config['port'],database=mysql_config['database'],
                 user=mysql_config['user'],password=mysql_config['password'],charset=mysql_config['charset'])
    find_name=input("请输入物品名称：")
    # 获取Cursor对象：调用Connection对象的cursor()方法
    cs1=conn.cursor()

    # # 非安全的方式 字符串拼接不安全 引号很容易被利用
    # # 输入 " or 1=1 or "   (双引号也要输入)
    # sql = 'select * from goods where name="%s"' % find_name
    # print("""sql===>%s<====""" % sql)
    ## 输入" or 1=1 or "后 变为select * from goods where name = "" or 1 = 1 or "" 等价为 where Ture
    # # 执行select语句，并返回受影响的行数：查询所有数据
    # count = cs1.execute(sql)


    # 安全的方式
    # 构造参数列表
    params = [find_name]
    print(params)
    # 执行select语句，并返回受影响的行数：查询所有数据
    count = cs1.execute('select * from goods where name=%s', params)
    # #不像第一种 此时，输入的参数作用于name而不会对where有影响
    # 注意：
    # 如果要是有多个参数，需要进行参数化
    # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可



    # 打印受影响的行数
    print(count)
    # 获取查询的结果
    # result = cs1.fetchone()
    result = cs1.fetchall()
    # 打印查询的结果
    print(result)

    # 关闭Cursor对象
    cs1.close()
    # 关闭Connection对象
    conn.close()

if __name__ == '__main__':
    main()
