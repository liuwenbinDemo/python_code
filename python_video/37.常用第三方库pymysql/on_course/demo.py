from . import get_conn

def test_demo():
    # 1. 打开连接
    conn = get_conn()
    # 2. 获取游标
    cursor = conn.cursor()
    # 3. 执行SQL
    cursor.execute("SELECT VERSION();")
    # 4. 获取结果
    version = cursor.fetchone()
    print(version)
    # 5. 关闭连接
    conn.close()