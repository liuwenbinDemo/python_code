from . import get_conn


def test_delete():
    # 建立连接
    conn = get_conn()

    # 获取游标
    cursor = conn.cursor()

    # SQL语句
    sql = "delete from testcase where id=3;"

    # 执行事务
    try:
        cursor.execute(sql)  # 执行SQL
        conn.commit()  # 提交
    except:
        conn.rollback()  # 回滚
    finally:
        conn.close()  # 关闭连接
