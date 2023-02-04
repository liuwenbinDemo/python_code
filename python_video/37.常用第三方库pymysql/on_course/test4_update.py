from . import get_conn


def test_update():
    # 建立连接
    conn = get_conn()

    # 获取游标
    cursor = conn.cursor()

    # SQL语句
    sql = "update testcase set owner='hogwarts' where id=2";

    # 执行事务
    try:
        cursor.execute(sql)  # 执行SQL
        conn.commit()  # 提交
    except:
        conn.rollback()  # 回滚
    finally:
        conn.close()  # 关闭连接
