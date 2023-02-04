from . import get_conn


def test_insert():
    # 建立连接
    conn = get_conn()

    # 获取游标
    cursor = conn.cursor()

    # SQL语句
    sql = "insert into testcase (id, title, expect, owner) " \
          "values (5, 'S11全球总决赛', '冠军', 'EDG');"

    # 执行事务
    try:
        cursor.execute(sql)  # 执行SQL语句
        conn.commit()  # 提交
        print("Success")
    except:
        conn.rollback()  # 回滚
        print("Rollback")
    finally:
        conn.close()  # 关闭连接
        print("Close")
