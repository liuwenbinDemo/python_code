import pymysql


# 返回数据库连接对象
def get_conn():
    conn = pymysql.connect(
        host="服务器地址",
        user="用户名",
        password="密码",
        database="数据库名",
        charset="utf8mb4"
    )

    return conn
