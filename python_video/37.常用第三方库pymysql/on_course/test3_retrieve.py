import sys

from . import get_conn

def test_retrieve():

    # 建立连接
    conn = get_conn()

    # 获取游标
    cursor = conn.cursor()

    # SQL语句
    sql = "select * from testcase;"

    # 捕获异常，不需要执行事务
    try:
        cursor.execute(sql)  # 执行SQL
        records = cursor.fetchone()  # 查询单条
        records = cursor.fetchmany(2)  # 查询多条
        records = cursor.fetchall()  # 查询所有
        print(records)
    except Exception as e:
        print(sys.exc_info())  # 打印执行信息
    finally:
        conn.close()  # 关闭连接
        print("Close")