import configparser

import pymysql


def implement(sql, *args):
    """
    执行sql语句
    :param sql:预编译sql
    :param args:预编译sql中的占位符对应参数
    :return: 两个参数分别为受影响行数和执行结果
    """
    #读取数据库配置文件
    cf = configparser.ConfigParser()
    cf.read('db.conf', encoding='utf-8')
    # 获取数据库连接
    db = pymysql.connect(
        host=cf.get('mysql', 'DB_HOST'),
        user=cf.get('mysql', 'DB_USER'),
        passwd=cf.get('mysql', 'DB_PWD'),
        db=cf.get('mysql', 'DB_NAME'),
        port=cf.getint('mysql', 'DB_PORT'),
        charset=cf.get("mysql", 'CHARSET'),
    )
    # 获取连接游标
    cursor = db.cursor()
    result, row = None, None
    try:
        row = cursor.execute(sql, args)  # 执行sql语句
        result = cursor.fetchall()  # 获取结果集
        db.commit()  # 提交事务
    except Exception as e:
        print(f"{e},操作失败！！！")
        db.rollback()  # 回滚事务
    finally:
        cursor.close()  # 关闭游标
        db.close()  # 关闭连接
        return row, result